#! /usr/bin/env python

import time, random, threading, monome, sched
import rtmidi
from monome import Monome

# try to find a monome (you can skip this if you already know the host/port)
print "looking for a monome..."
host, port = monome.find_any_monome()
print "found!"
m = Monome((host, port))
m.start()

#init the MIDI port
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
print available_ports
if available_ports:
	midiout.open_port(1)
else:
	midiout.open_virtual_port("My virtual output")

#setup the clock
class Clock:
	bpm = 120
	s = sched.scheduler(time.time, time.sleep)
	print 'clockeventinit'


	def runclockedstuff(self):
		self.s.enter(500, 1, runclockedstuff, ())
		return 'clockevent'


clock = Clock()


#config
#row1 = 'seq16'
monomeRowConfig =  ['seq16', 'loop16', 'toggle16','seq16', 'loop16', 'toggle16','seq16', 'loop16']

monomeState = [

				]

def note_on(channel, note, velocity):
	print channel
	msg = [channel, note, velocity]
	# msg = [0x99, 60, 112]
	print msg
	midiout.send_message(msg)

def note_off(channel, note):
	midiout.send_message([channel, note, 0])


def keypressed(x, y, s):

	rowType = monomeRowConfig[y]
	if s == 1:
		if rowType == 'seq16':
			if  m.get_led(x,y) == 1:
				m.led_set(x, y, 1 )
			else:
				m.led_set(x, y, 0 )
		if rowType == 'loop16':
			note_on(0x99,60, 112)
			m.led_row(x,y,0xff, 0xff)


	else:
		# if rowType == 'seq16':

		if rowType == '`loop16':
			note_off(0x99, 60)
			m.led_row(x,y,0x00, 0x00)

print(clock.runclockedstuff)

m.grid_key = keypressed


#repaint monome
m.led_all(0)


try:
	while True:
		for i in range(8):
			time.sleep(1.0/20)
except KeyboardInterrupt:
	# r.panic()
	m.led_all(0)
	m.close()
