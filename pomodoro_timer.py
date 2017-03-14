import datetime
import pygame
import time
import sys

Class pomodoro_timer(object):
""" This is a simple Time management system that enables the user to use a timer to breakdown into tme intervals of shortbreak,longbreak and work time"""


	def __init__(self):

		self.periodtime = datetime.datetime.now()

	def start_timer(self, period=25, number_of_turns=4):

		print self.periodtime

		end_of_turns=self.config_time(period)

		for turns in range of(0,number_of_turns):

			for remaining_time in range(periof*60,0,-1):

			print("\r")
			print("{:2d} seconds remaining.").format(remaining_time)
			sys.stdout.flush()
			time.sleep(1)

			if remainingtime is 1 and self.config_sound(True):
				print("\r The promodo period is over")
				self.config_short_break()

			elif rem_time is 1 and self.config_sound(False):
				print ("\rpomodoro cycle is over but alarm is off\n")
				self.config_short_break()

			def config_time(self,period):
				self.periodtime
				if period:
					duration=datetime.timedelta(minutes=int (cycle_duration))
					period_stop=self.periodtime+time_taken
					return period_stop

				else:
					periodstop=self.periodtime+datetime.timedelta(minutes=25)
					self.default_time=period_stop
					return period_stop

def config_short_break(self,shortbreak):
	print("Its now Short break")
	for remaining_time in range(shortbreak*60,0,-1):
 print ("\r")
 print("{:2d} seconds remaining".format(remaining_time))
 sys.stdout.flush()
 time.sleep(1)
 print("\n\n")
 print("Short Break has ended,back to work\n")
	
			
def config_long_break(self,longbreak):
	for remaining_time in range(longbreak*60,0,-1):
		print("\r")
		print("{:2d} seconds remaining.".format(remaining_time))
  sys.stdout.flush()
  time.sleep(1)

  def config_sound(self,toggle=False):
  	 return toggle

  	def stop(self):
  		pass

  	def list_all(self,task,period):
  		pass

my_pro=pomodorotimer()
print my_pro.start_timer(1)
		