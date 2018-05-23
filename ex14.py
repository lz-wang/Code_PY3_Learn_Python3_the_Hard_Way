from sys import argv

script, user_name = argv # 'script' is the name of this python script file
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt) # display 'prompt' as '> ', then get your own input strings
					  # you can also use double-quotes for 'prompt' variable
print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
	Alright, so you said {likes} about liking me.
	You live in {lives}. Not sure where that is.
	And you have a {computer} computer. Nice.
	""")
# warning: you should run this script like this(on windows):
#		python ex14.py lzwang