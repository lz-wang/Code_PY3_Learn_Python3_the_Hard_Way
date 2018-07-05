# this one is like your scripts with argv
# 定义的函数接收两个变量，但是在定义里只用了一个*arg代替，
# 也就是说，可以用*argv代替三个变量
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that * args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
	print("I got nothin'.")

print_two("Lz", "Wang")
print_two_again("Lz", "Wang")
print_one("First!")
print_none()
