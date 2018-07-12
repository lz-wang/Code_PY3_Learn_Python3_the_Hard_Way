def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after poping it off."""
	word = words.pop(0)
	print(word)

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print(word)

def sort_sentence(sentence):
	"""Take in full sentence and returns the sorted words"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""sorts the words then prints the first an last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

# ---------------C O M M A N D S------------------------------
# import ex25
# sentence = "All good thins come to those who wait."
# words = ex25.break_words(sentence)
# words
# sorted_words = ex25.sort_words(words)
# sorted_words
# ex25.print_first_word(words)
# ex25.print_last_word(words)
# words
# ex25.print_first_word(sorted_words)
# ex25.print_last_word(sorted_words)
# sorted_words = ex25.sort_sentence(sentence)
# sorted_words
# ex25.print_first_and_last(sentence)
# ex25.print_first_and_last_sorted(sentence)
# ---------------R E S U L T S------------------------------
# E:\Dropbox\Codes Backup\Sublime Text 3\Learn Python3 The Hard Way>python
# Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import ex25
# >>> sentence = "All good thins come to those who wait."
# >>> words = ex25.break_words(sentence)
# >>> words
# ['All', 'good', 'thins', 'come', 'to', 'those', 'who', 'wait.']
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words
# ['All', 'come', 'good', 'thins', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_word(words)
# All
# >>> ex25.print_last_word(words)
# wait.
# >>> words
# ['good', 'thins', 'come', 'to', 'those', 'who']
# >>> ex25.print_first_word(sorted_words)
# All
# >>> ex25.print_last_word(sorted_words)
# who
# >>> sorted_words = ex25.sort_sentence(sentence)
# >>> sorted_words
# ['All', 'come', 'good', 'thins', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_and_last(sentence)
# All
# wait.
# >>> ex25.print_first_and_last_sorted(sentence)
# All
# who
# >>>
