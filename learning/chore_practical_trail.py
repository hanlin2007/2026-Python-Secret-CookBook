s = "Hello, World!"
print(s[::-1])

string = "Python"
for i in range(len(string)):
    print(string[i],end=(" " if (i + 1) != len(string) else "\n"))
# print()
# print("a",end = "a")

# 输入一个字符串
# mystring = input()

# # 字符串切片构造，利用是否相等来判断是否为回文
# if(mystring == mystring[::-1]):
#     print("是回文")
# else:
#     print("不是回文")



# 输入一段英文，找到最长英文单词并输出
mystring = input()
words = mystring.split()
longest_word = max(words, key=len)
print(longest_word)
