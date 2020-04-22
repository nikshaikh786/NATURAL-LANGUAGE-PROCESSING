' personalized appointment agent'


import nltk
from nltk.chat.util import Chat, reflections

pairs=[["What is your name",["My name is bot - your personalized appointment agent"]],
	["I want to book an appointment",["okay the next available dates are 28,29,30 march"]],
	["select 29 march",["the available doctors are Dr. bill, Dr. mark, Dr. elon select any one of those"]],
	["select 28 march",["the available doctors are Dr. ajay, Dr. shahrukh, Dr. amir select any one of those"]],
	["select 30 march",["the available doctors are Dr. kangana, Dr. garima, Dr. divya select any one of those"]],
	["select Dr. elon",["okay! available slots are 4pm and 8pm"]],
	["select Dr. mark",["okay! available slots are 3pm and 7pm"]],
	["select Dr. bill",["okay! available slots are 2pm and 6pm"]],
	["select Dr. ajay",["okay! available slots are 1pm and 5pm"]],
	["select Dr. shahrukh",["okay! available slots are 10am and 10pm"]],
	["select Dr. amir",["okay! available slots are 11am and 11pm"]],
	["select Dr. kangana",["okay! available slots are 12pm and 9pm"]],
	["select Dr. garima",["okay! available slots are 9am"]],
	["select Dr. divya",["okay! available slots are 8am"]],
	["4pm",["okay! appointment successful. Thankyou!"]],
	["8pm",["okay! appointment successful. Thankyou!"]],
	["3pm",["okay! appointment successful. Thankyou!"]],
	["7pm",["okay! appointment successful. Thankyou!"]],
	["2pm",["okay! appointment successful. Thankyou!"]],
	["6pm",["okay! appointment successful. Thankyou!"]],
	["1pm",["okay! appointment successful. Thankyou!"]],
	["5pm",["okay! appointment successful. Thankyou!"]],
	["10am",["okay! appointment successful. Thankyou!"]],
	["10pm",["okay! appointment successful. Thankyou!"]],
	["11am",["okay! appointment successful. Thankyou!"]],
	["11pm",["okay! appointment successful. Thankyou!"]],
	["12pm",["okay! appointment successful. Thankyou!"]],
	["9pm",["okay! appointment successful. Thankyou!"]],
	["9am",["okay! appointment successful. Thankyou!"]],
	["8am",["okay! appointment successful. Thankyou!"]],
	
	]

def nikhat_chat():
	print("Hi, i am your personalized appointment agent.")
	chat=Chat(pairs, reflections)
	chat.converse()

nikhat_chat()