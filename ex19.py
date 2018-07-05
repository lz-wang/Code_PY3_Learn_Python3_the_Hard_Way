def cheese_and_crackers(cheese_count, boxs_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxs_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variable from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# 笔记：变量在函数中的应用可以有如下形式：
#       1. 引用函数时直接为变量赋值
#       2. 引用函数时将第三方变量导入原函数变量中
#       3. 引用函数时可以进行加减乘除等数学操作
#       4. 将第 2 和 3 步混合使用
