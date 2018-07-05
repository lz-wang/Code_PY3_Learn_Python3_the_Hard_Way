from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w') # open file by 'write'

print("Truncating the file. Goodbye!")
target.truncate() # not necessary for this script

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ") # get strings
line2 = input("line 2: ") 
line3 = input("line 3: ") 

print("I'm going to write these to the file.")

target.write(line1) # write strings
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close() # close file
# warning: you should run this script like this(on windows):
#		python ex16.py test.txt