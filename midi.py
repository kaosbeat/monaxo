#! /usr/bin/env python

import time, random, threading, monome, sched
import rtmidi
import loop16
from seq16 import Seq16
from monome import Monome
from midiout import *

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
		print 'clockevent'


clock = Clock()


#config

m.monomeRowConfig =  ['none', 'none', 'none','none', 'loop16', 'toggle16','seq16', 'loop16']
m.r0 = Seq16(m,0,0)
m.r1 = Seq16(m,1,1)
m.r2 = Seq16(m,2,0)
m.r3 = Seq16(m,3,1)


# m.monomeState = [

# 				]


# if __name__ == '__main__':
# 	main()

def keypressed(x, y, s):
	if y == 0:
		m.r0.dostuff(x,y,s)
		m.r0.changestuff()
	if y == 1:
		m.r1.dostuff(x,y,s)
		print 'y = 1'
	if y == 2:
		m.r3.dostuff(x,y,s)
	if y == 3:
		m.r4.dostuff(x,y,s)

	# rowType = m.monomeRowConfig[y]
	# if s == 1:
	# 	if rowType == 'seq16':
	# 		if  m.get_led(x,y) == 1:
	# 			m.led_set(x, y, 1 )
	# 		else:
	# 			m.led_set(x, y, 0 )
	# 	if rowType == 'loop16':
	# 		note_on(0x99,60, 112)
	# 		m.led_row(x,y,0xff, 0xff)


	# else:
	# 	# if rowType == 'seq16':

	# 	if rowType == '`loop16':
	# 		note_off(0x99, 60)
	# 		m.led_row(x,y,0x00, 0x00)

print(clock.runclockedstuff)

m.grid_key = keypressed


# #repaint monome
# m.led_all(0)


try:
	while True:
		for i in range(8):
			time.sleep(1.0/20)
except KeyboardInterrupt:
	# r.panic()
	m.led_all(0)
	m.close()
