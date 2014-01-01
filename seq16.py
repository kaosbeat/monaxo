class Seq16:
	"""
	defines a monome row to use as a 16 step sequencer and send to a defined midi channel

	"""
	def __init__(self, Monome, row, channel=0):
		Monome.monomeRowConfig[row] = 'seq16'
		self.m = Monome


	def dostuff(self,x,y,s):
		# if  self.m.get_led(x,y) == 1:
		# 	self.m.led_set(x, y, 1 )
		# else:
		# 	self.m.led_set(x, y, 0 )
		self.m.led_row(x,y,0xff, 0xff)
		print self.m