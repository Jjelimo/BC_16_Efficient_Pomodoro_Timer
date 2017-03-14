from cli_pomodoro import pomodoro_timer

def main():
	""" Pomodoro APP """

	print ("\n\n")
	print("******************************************")
	print("WELCOME TO YOUR AWESOME POMODORO TIMER!!!")
	print("*****************************************\n\n")
	print("***This will help you in Time Management***")


	settings = pomodoroTimer()

	while True:

		print("1.Start Pomodoro Timer\n  2.Allocate the period time\n 3.Allocate your shortbreak time\n 4.Allocate your long break time\n 5.Alarm Turn ON/OFF\n 6.STOP\n 7.view all tasks\n 8.Exit\n")

		action=input("please enter your preferred choice: ")

		if action == "1":
            
            settings.start_timer

		elif action=="2":
			period=input(" The default time is 25, but you can enter your preferred period time: ")
			if period == None:
				period=25
				settings.start_timer(int(period)
            else:
                try:
                    settings.start_timer(int(period))
                except ValueError:
            		print("Invalid choice: Please select again")

        elif action=="3":
        	shortbreak=input("The default time is 5, but you can enter your preferred period time: ")
            if shortbreak=="":
             	shortbreak=5
             	settings.config_short_break(int(shortbreak))

            elif shortbreak:
            	try:
            		settings.config_short_break(int(shortbreak))
            	except ValueError:
            		print("Invalid choice: Please select again")

            elif action=="4":
            	longbreak=input("The default time is 15, but you can enter your preferred period time: ")
            	if longbreak=="":
            		longbreak=15
            		settings.config_long_break(int(longbreak))

            	elif longbreak:
            		try:
            			settings.config_long_break(int(long_break))
            		except ValueError:
            			print("Invalid choice: Please select again")





if __name__ == '__main__': main()











