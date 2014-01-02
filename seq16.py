from bitstring import BitArray, BitStream
import sys


class Seq16:
	rowState = BitArray('0x0f')
	print rowState.uint
	"""
	defines a monome row to use as a 16 step sequencer and send to a defined midi channel

	"""
	def __init__(self, Monome, row, channel=0):
		Monome.monomeRowConfig[row] = 'seq16'
		self.m = Monome
		# self.rowState = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		# print rowState.uint


	def dostuff(self,x,y,s):

		# if  self.m.get_led(x,y) == 1:
		# 	self.m.led_set(x, y, 1 )
		# else:
			# self.m.led_set(x, y, 0 )
		# print(self.m.led_row(x,y,self.rowState, 0xff))

		# self.m.led_row(x,y-1,0xff, 0xff)
		self.m.led_row(x,y,self.rowState.uint, 0xff)

		# self.m.led_row(x,y+1,0x00, 0x00)
		# print rowState

	def changestuff(self):
		self.rowState = BitArray('0xff')