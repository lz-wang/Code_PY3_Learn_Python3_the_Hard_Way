formatter = "{} {} {} {}" # 打印四个位置

print(formatter.format(1, 2, 3, 4)) # 四个数字
print(formatter.format("one", "two", "three", "four")) # 四个字符串
print(formatter.format(True, False, False, True)) # 四个布尔值，此处的 True 和 False 是关键词
print(formatter.format(formatter, formatter, formatter, formatter)) # 四个formatter空位置{}
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
	)) # 四个字符串，分行写开