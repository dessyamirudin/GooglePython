#policespeed
import sys

def main():
	speed1=sys.argv[1]
	speed=int(speed1)
	mood='good'
	if speed >= 80:
		print ('License and registration please')
		
	if mood == 'terrible' or speed >= 100:
		print ('You have the right to remain silent.')
	elif mood == 'bad' or speed >= 90:
		print ("I'm going to have to write you a ticket.")
		#write_ticket()
	else:
		print ("Let's try to keep it under 80 ok?")
		
if __name__ == '__main__':
	main()