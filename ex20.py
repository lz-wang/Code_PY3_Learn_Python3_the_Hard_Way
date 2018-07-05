from sys import argv

script, input_file = argv

def print_all(f): # 打印出文件的全部内容
	print(f.read())

def rewind(f):
	f.seek(0) # 从文件开头开始寻找

def print_a_line(line_count, f): # 给定文件和行信息，打印
	print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1 # 当前为第一行
print_a_line(current_line, current_file) # 打印当前文件的当前行

current_line = current_line + 1 # 第二行
print_a_line(current_line, current_file)

current_line= current_line + 1 # 第三行
print_a_line(current_line, current_file)
# warning: you should run this script like this(on windows):
#		python ex20.py test.txt

# fileObject.seek(offset[, whence])
# 参数：
#   offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
#   whence：可选，默认值为 0
#         给offset参数一个定义，表示要从哪个位置开始偏移；
#           0代表从文件开头开始算起，
#           1代表从当前位置开始算起，
#           2代表从文件末尾算起。