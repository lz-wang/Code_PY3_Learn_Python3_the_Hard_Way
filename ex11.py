print("How old are you?", end = ' ') # end = ' '的作用在于不要让此行结束，以便接受input的参数
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weight?", end = '')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")