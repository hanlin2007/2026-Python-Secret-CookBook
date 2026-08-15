import this

name = 'hEllo "wolf\'l\'"'
print(f"name.title()+\" Hello World\"")

a = 1.25
print(f"{a:.1f}")

b = a
def round_half_up(num,k):
    offset = 0.5 if num > 0 else -0.5
    # offset = (num > 0) ? 0.5 : -0.5 错误，在 py 中这不是合法的三目运算符，上面的 if / else 正确
    return int(offset + num * (10 ** k)) / (10 ** k)
print(round_half_up(a,1))


x = 3.1415926
x = int(x * 10000) / 10000
print(x)


my_string = "hello mystring"
print(f"{my_string:>20}saygoodbye")


print("Languages:\n\tPython\n\tJava\n\tKotlin")
message = "Languages:\n\tPython\n\tJava\n\tKotlin"
print(message.strip())   # 只能删除两侧的空白，中间的不行呀


# name = input("Enter your name: ")
# print(f"Hello {name.strip().title()}, would you like to learn some Python today?")