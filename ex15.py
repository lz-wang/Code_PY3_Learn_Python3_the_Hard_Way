from sys import argv

script, filename = argv

txt = open(filename) # open file

print(f"Here's your file {filename}:")
print(txt.read()) # read and print the file

print("Type the filename again:")
file_again = input("> ") # read another file

txt_again = open(file_again)

print(txt_again.read()) # read and print again
# warning: you should run this script like this(on windows):
#		python ex15.py ex15_sample.txt