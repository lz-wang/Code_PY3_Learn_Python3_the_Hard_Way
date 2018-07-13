from sys import exit

def gold_room():
	print("This room is full of gold. How much do you take?")

	choice = input("> ")
	if "o" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print("Nice, you're not greedy, you win!")
		exit(0)
	else:
		dead("You greedy bastared!")


def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved = False

	while True:
		choice = input("> ")

		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print("The bear has moved from the door.")
			print("You can go through it now.")
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means.")


def cthulhu_room():
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")

	choice = input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()


def dead(why):
	print(why, "Good, job!")
	exit(0)

def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take?")

	choice = input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")


start()
# 错误信息 IndentationError: unindent does not match any outer indentation level 的排除：
#          检查缩进符号，是四个空格作为一个缩进还是一个TAB制表符做的缩进，
#          使得两者统一即可。
#    plus：sublime编辑器中，空格缩进表示为 ···· ，TAB缩进表示为 ———— 。
#          你需要全选才能显示编辑器中的所有字符（包含隐藏字符）。