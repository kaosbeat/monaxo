#! /usr/bin/env python

import time, random, threading, monome
import time
import rtmidi
from monome import Monome

# try to find a monome (you can skip this if you already know the host/port)
print "looking for a monome..."
host, port = monome.find_any_monome()
print "found!"
m = Monome((host, port))
m.start()


class Axo(object):
    def __init__(self):
    	#init the MIDI port
		midiout = rtmidi.MidiOut()
		available_ports = midiout.get_ports()
		print available_ports
		if available_ports:
		    midiout.open_port(1)
		else:
		    midiout.open_virtual_port("My virtual output")

    def note_on(self, channel, note, velocity):
    	print self.channel
    	self.msg = [channel, note, velocity]
    	# msg = [0x99, 60, 112]
    	print msg
        self.midiout.send_message(msg)

    def note_on(self, channel, note):
        self.midiout.send_message([channel, note, 0])

a = Axo()
# a.note_on(10, 60, 112)

def keypressed(x, y, s):
    m.led_set(x, y, s)
    if s == 1:
        a.note_on(60, 112)
    else:
        a.note_off(0x99, 60)



m.grid_key = keypressed

m.led_all(0)
try:
    while True:
        for i in range(8):
            time.sleep(1.0/20)
except KeyboardInterrupt:
    # r.panic()
    m.led_all(0)
    m.close()
