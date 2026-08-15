# Python 语法速查清单与练习

> 这份文档是一份循序渐进的 Python 复习手册。每个知识点都配有代码示例和练习题，题目大多来自你暑期课程的实际代码。无论你是想系统复习还是考前突击，跟着走一遍就稳了。

---

## 目录

1. [基础语法：变量、输入输出、数据类型](#1-基础语法变量输入输出数据类型)
2. [运算符与表达式](#2-运算符与表达式)
3. [条件判断](#3-条件判断)
4. [循环结构](#4-循环结构)
5. [字符串操作](#5-字符串操作)
6. [列表与元组](#6-列表与元组)
7. [字典与集合](#7-字典与集合)
8. [函数](#8-函数)
9. [文件操作](#9-文件操作)
10. [异常处理](#10-异常处理)
11. [面向对象](#11-面向对象)
12. [模块与包](#12-模块与包)
13. [测试与 pytest](#13-测试与-pytest)
14. [综合练习](#14-综合练习)

---

## 1. 基础语法：变量、输入输出、数据类型

### 1.1 print 输出

```python
# 基本输出
# 逗号分隔多个参数：字面量常量 literal（整数、浮点数、字符串） / 变量
print("Hello World")
message = "python"
print(100, 13.14 , 100 * 13.14 , message)   

# sep 分隔符（默认空格）
print(1234, 5678, sep=" * ")   # 1234 * 5678

# end 终止符（默认 \n 换行）
print("第一行", end=" → ")
print("接在后面")
```

区分 `cpp` 中 `endl`：

```cpp
cout << "Hello" << endl; 
```

---

### 1.2 input 输入

```python
# 单个输入
name = input()                   # 返回字符串
age = int(input())               # 转为整数
height = float(input())          # 转为浮点数

# 带提示的输入
name = input("请输入你的名字：")
```

---

### 1.3 多变量同行输入

```python
# 方法一：split() + 逐个转换（最基础，最本质，最好记）
x, y, z = input().split()
x = int(x); y = int(y); z = int(z)

# 方法二：map() 一次性转换（最常用）
x, y, z = map(int, input().split())

# 方法三：列表推导式
arr = [int(i) for i in input().split()]
```

> **常见错误**：忘记各种位置的括号 / 忘记把 `split()` 后的字符串结果用 `int()` 转换类型

---

### 1.4 变量与赋值

```python
# 普通赋值（从右向左结合）
a = 10
b = a           # b = 10，不是"链接"到 a
a = 11          # 变量的赋值可以被覆盖

# 交换两个变量的值（元组解包）
a, b = b, a
```

---

### 1.5 基本数据类型

| 类型 | 示例 | 说明 |
|------|------|------|
| **整型** `int` | `1000000000`, `100_000` | 可以无上限任意大，只有一种类型，可_标记数位 |
| **浮点数** `float` | `3.14`, `1.`，1e-3 | 只有一种类型，相当于C的 `double` |
| **字符串**`str` | `"hello"`，‘a’ | 没有`char` / 整数，相当于长度为1的字符串 |
| **布尔值**`bool` | `True`, `False` | 布尔值，输出也是 `True` 和 `False` |

没有常量类型限制标识，但是使用大写字母命名来指出 MAX_LISTNUM

---

### 📝 练习 1

**1.1** 从键盘输入两个整数 a 和 b，输出它们的和、差、积、商（保留两位小数）。

**1.2** 输入一个三位正整数，分别输出它的百位、十位、个位数字。

**1.3** 输入三个整数，输出它们的和。（注意：split 函数和类型转换）

<details>
<summary>参考答案</summary>

```python
# 1.1
a, b = map(int, input().split())
print(f"和：{a+b}, 差：{a-b}, 积：{a*b}, 商：{a/b:.2f}")

# 1.2
n = int(input())
print(n // 100, n // 10 % 10, n % 10)

# 1.3
a, b, c = map(int, input().split())
print(a + b + c)
```
</details>

---

## 2. 运算符与表达式

### 2.1 算术运算符

```python
a * b    # 乘法
a / b    # 除法（得到浮点数，即使能够整除！！）
a // b   # 整除（向下取整）
a % b    # 取余
a ** b   # 幂运算
```

### 2.2 取整与四舍五入

这是一个容易踩坑的点：

```python
# 三种取整方式对比
ans = 13 / 8       # 1.625

print(int(ans))    # 1 —— 直接去掉小数部分
print("%d" % ans)  # 1 —— 保留整数部分（不四舍五入）
print("%.0f" % ans) # 2 —— 四舍五入保留整数！

# 浮点精度格式化
print("{:.2f}".format(ans))   # 1.62
print(f"{ans:.2f}")            # 1.62
print("%.2f" % ans)            # 1.62
```

### 2.3 比较运算符

```python
>=    # 大于等于
<=    # 小于等于
```

### 2.4 逻辑运算符

```python
and    # 与：两边都为 True 才为 True
or     # 或：至少一边为 True 就是 True
not    # 非：取反

# 链式比较
if 60 <= score <= 85:    # 等价于 score >= 60 and score <= 85
```

---

### 📝 练习 2

**2.1** 一件商品原价 x 元，打 y 折后，四舍五入到整数，输出最终价格。（四舍五入技巧：先 +5 再用 `//10*10`）

**2.2** 输入两个整数 a 和 b，输出 `a // b`（整数商）和 `a % b`（余数）。

**2.3** 输入一个年份，判断是否为闰年。（能被4整除但不能被100整除，或能被400整除）

<details>
<summary>参考答案</summary>

```python
# 2.1
x, y = map(float, input().split())
ans = x * y * 0.1       # 注意区分 y 折和 y%
ans = int(ans) + 5
print(ans // 10 * 10)

# 2.2
a, b = map(int, input().split())
print(a // b, a % b)

# 2.3
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("闰年")
else:
    print("不是闰年")
```
</details>

---

## 3. 条件判断

### if / elif / else：注意冒号、缩进

冒号后面的内容可以写到同一行，不同行之间可以直接使用**分号**来分割

```python
score = int(input())
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else: print("需要努力") ; print("Hello World") 
```

---

## 4. 循环结构

### 4.1 while 循环

```python
# 基本格式
i = 1                           # 1. 初始化
while i <= 10:                   # 2. 条件判断
    print(i)
    i = i + 1                    # 3. 迭代更新

# while True + break（终止型循环，非常好用！）
sum = 0
while True:
    x = int(input())
    if x == 0:
        break                    # 达到终止条件，结束循环
    sum += x
print(sum)
```

### 4.2 for 循环与 range

```python
# range(5)：0 到 5-1
# list(range(5))   [0,1,2,3,4]
# 如果无意义变量 / 只用循环的次数，也可以直接用下划线 _ 来命名
for _ in range(5):          # 0, 1, 2, 3, 4  
    print(_)

# range(start, stop)：左闭右开，start 到 stop-1
for i in range(2, 6):       # 2, 3, 4, 5
    print(i)

# range(start, stop, step)：start 到 stop-1，步长 step
for i in range(1, 10, 2):   # 1, 3, 5, 7, 9
    print(i)

# 倒序
for i in range(10, 0, -1):  # 10, 9, 8, ..., 1
    print(i)
```

### 4.3 break 与 continue

```python
# break：结束整个循环
for i in range(100):
    if i == 5:
        break        # i=0,1,2,3,4 时正常循环，碰到5就退出

# continue：跳过本次循环，进入下一次
for i in range(10):
    if i % 2 == 0:
        continue     # 跳过偶数，只打印奇数
    print(i)
```

---

## 5. 字符串操作

### 5.1 字符串函数补充

```python
s = "Hello World"

len(s)           # 11 —— 长度
s[0]             # 'H' —— 索引访问
s[-1]            # 'd' —— 倒数第一个
s[0:5]           # 'Hello' —— 切片 [开始:结束]
s[::2]           # 'HloWrd' —— 每隔一个取
s[::-1]          # 'dlroW olleH' —— 反转字符串！

s.replace("World", "Python")   # 'Hello Python'
s.find("World")  # 6 —— 子串位置，找不到返回 -1
s.count("l")     # 3 —— 出现次数

# 字符串是不可变的！以上构造字符串 / 方法返回新字符串，原字符串不变
```

### 5.2 字符串分割与列表

```python
s = "apple banana cherry"

# split() 默认按空白分割，返回列表
words = s.split()          # ['apple', 'banana', 'cherry']

# 按指定字符分割
data = "2024,7,15".split(",")   # ['2024', '7', '15']

# join() 把**列表**拼回字符串
" | ".join(words)          # 'apple | banana | cherry'

# 无空格连接（常用于数字列表的输出）
nums = [1, 2, 3]
print("".join(map(str, nums)))  # '123'
```

---

### 📝 练习 5

**5.1** 输入一个字符串，判断它是否为回文串（正读反读一样）。忽略大小写和空格。

**5.2** 输入一段英文句子，找出最长的单词并输出。

**5.3** 输入一个字符串，将其中所有的数字 `"1"`、`"2"`、... `"9"` 替换为 `"one"`、`"two"`、... `"nine"`。

<details>
<summary>参考答案</summary>

```python
# 5.1
s = input().replace(" ", "").lower()
print("yes" if s == s[::-1] else "no")

# 5.2
words = input().rstrip(".").split()
longest = max(words, key=len)
print(longest)

# 5.3
digit_map = {"1": "one", "2": "two", "3": "three",
             "4": "four", "5": "five", "6": "six",
             "7": "seven", "8": "eight", "9": "nine"}
s = input()
for d, w in digit_map.items():
    s = s.replace(d, w)
print(s)
```
</details>

---

## 6. 列表与元组

### 6.1 列表创建

```python
# 三种等价方式创建列表
# 方式一：循环 append
arr = []

# 输入为同一行的情况
for x in input().split():
    array.append(int(x))

# 每个输入占一行，以Ctrl+D结束输入
while True:
    try: 
        array.append(int(input()))
    except EOFError: 
        break

# 方式二：map + list
arr = list(map(int, input().split()))

# 方式三：列表推导式（最 Pythonic）
arr = [int(x) for x in input().split()]

# 创建定长列表
zeros = [0] * 10              # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ones = [1 for _ in range(5)]  # [1, 1, 1, 1, 1]
```

### 6.2 列表常用操作

```python
arr = [3, 1, 4, 1, 5]
arr_str = ['colon','comma','period']

# 复制
arr_copy = arr[:]
arr_copy_failed = arr     # 会直接两个指针指向同一个列表，而不是复制一次内容

# 访问
arr[0]         # 3 —— 索引从 0 开始
arr[-1]        # 5 —— 倒数第一个
arr[1:3]       # [1, 4] —— 切片 [开始:结束)
arr[:3]        # [3,1,4]

# 添加
arr.append(9)             # 在末尾加一个
arr.insert(2, 100)        # 在索引 2 处插入 100
arr.extend([6, 7])        # 拼接另一个列表

# 删除
arr.remove(1)             # 删除第一个**值**为 1 的元素
popped = arr.pop()        # 删除并返回最后一个——需要使用
popped = arr.pop(0)       # 删除并返回索引 0 的元素
del arr[0]                # 删除**索引** 0 的元素
del arr[1:3]              # 删除切片范围内的元素

# 查找
arr.index(4)              # 4 的索引（第一个匹配）
arr.count(1)              # 1 出现的次数
3 in arr                  # True/False

# 求长
length = len(array)
```

### 6.3 列表排序

```python
arr = [3, 1, 4, 1, 5]

# 返回新列表（原列表不变）
sorted_arr = sorted(arr)
sorted_desc = sorted(arr, reverse=True)

# 原地排序（修改原列表）
arr.sort()
arr.sort(reverse=True)
arr.reverse()             						# 原地反转列表，不是按字母序，只是按排列序

# 自定义排序（按字符串长度）
words = ["apple", "kiwi", "banana"]
words.sort(key=len)                              # key 指定排序参照每一个元素的

# lambda 自定义排序
students = [("小明", 90), ("小红", 95), ("小刚", 85)]
students.sort(key=lambda x: x[1], reverse=True)   # 按成绩降序
students.sort(key=lambda x: (-x[1], x[0]))         # 成绩降序，姓名升序

# lambda = 一次性函数 lambda x,y: x + y
d = {'a': 3, 'b': 7, 'c': 1}
max(d, key=lambda k: d[k])  # 返回 'b'（值最大的key），max 函数在遍历 key，而 d[key] = value


d = {'apple': 5, 'banana': 2, 'cherry': 8}
sorted(d.items(), key=lambda x: x[1], reverse=True)   # 这里是对 items，每个键值对进行排序
# [('cherry', 8), ('apple', 5), ('banana', 2)]  


nums = [1, 2, 3, 4]
list(map(lambda x: x**2, nums))      # [1, 4, 9, 16]
list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]
```

### 6.4 列表遍历技巧

```python
# 遍历值 优雅
for item in items:
    print(item)

# 难点总结：py中没有类型声明，C中是取内存。然后取别名；py中本质都是指针，直接拿来关联使用。
# 类型取决于 函数 / 方法的参数类型定义，for循环是一种迭代取对象，贴标签

# 可迭代对象：重点是往外吐东西，不是数据类型、实体内存
# for i in range(5):
# for i in list(range(5)):
# for i in input().split():
# for i in "hello world":
   
# 遍历索引和值
for i, val in enumerate(arr):         # enumerate 函数，把索引和列表中原来的值打包成一个元组
    print(f"索引{i}的值是{val}")

# 列表解包输出
print(*arr)                    # 空格分隔
print(*arr, sep="/")           # slash 正斜杠分隔

# 列表统计
len(arr)        # 长度
sum(arr)        # 求和
max(arr)        # 最大值

tuple_array = [('Samy',98),('Michale',67),('Wincy',92)]
print(max(tuple_array,key = len))
# 对于列表而言，max 作用的对象是每一个元素，len 则是元组的长度，所以返回遇到的第一个

# tuple_array = ['Smlie','Nancy','JJhony']
print(max(tuple_array,key = lambda x: len(x[0])))  × 没有意义了
如果要用名字的长度   len(x)
如果要用字符串的首字母 x[0] 
```

### 6.5 二维列表

```python
# 创建 n 行 m 列的二维列表
matrix = [[int(x) for x in input().split()] for _ in range(n)]

# 遍历二维列表
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

# 二维列表排序（按每行的某个维度）
points = [(1, 3), (2, 1), (1, 2)]
points.sort(key=lambda p: (p[0], p[1]))   # 先按 x 再按 y
```

### 6.6 元组

```python
# 元组：不可变的列表
dimension_tup = (256, 256, 3)
dimension_tup = tuple(map(int, input().split()))   # 从输入创建
dimension_tup[0] = 1024    # 不可修改
# 要修改，可以重新定义整个元组 dimension_tup = (1024,1024,3)

# 元组解包
x, y, z = tup     # 一次性赋值
a, b = b, a       # 利用元组解包交换变量
```

> 元组 vs 列表：元组不可修改、更轻量、可作为字典的键。

---

### 📝 练习 6

**6.1** 输入一个列表，将奇数和偶数分开：奇数在前（降序排列），偶数在后（升序排列）。

**6.3** 输入 n 个人的坐标 (x, y)，按照 x 升序、y 升序排序，输出排序结果。

**6.4** 输入一个矩阵（二维列表），求每一行的最大值。

<details>
<summary>参考答案</summary>

```python
# 6.1
arr = [int(x) for x in input().split()]
odds = sorted([x for x in arr if x % 2 == 1], reverse=True)
evens = sorted([x for x in arr if x % 2 == 0])
print(*(odds + evens))

# 6.3
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
points.sort(key=lambda p: (p[0], p[1]))
for x, y in points:
    print(x, y)

# 6.4
n, m = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
for row in matrix:
    print(max(row))
```
</details>

---

## 7. 字典与集合

### 7.1 字典创建

字典的核心价值：**按"键"快速查找"值"**，且键是唯一的。

```python
# 创建空字典
d = {}
d = dict()

# 字面量创建
student = {"name": "小明", "age": 20, "score": 95}
# 键值对的数据类型灵活定义的，甚至每一组都可以不相同

mul_row_dict = {
    "apple": 20,
    "banana": 20,
    "cherry": 20,
    "date": 40,
    "elderberry": 50
}
# 分行方式创建字典和列表

# 从键值对**元组列表**创建
tuple_list = [("apple", 1), ("banana", 2), ("cherry", 3)]
dict_1 = dict(tuple_list)
print(dict_1)
# {'apple': 1, 'banana': 2, 'cherry': 3}
```

### 7.2 字典的两类创建模型

**模型一：统计出现次数**

```python
arr = [1, 2, 2, 3, 3, 3]
d = {}

# d[x] 表示键为 x 的元素的值，如 2:3

# 方式 a：if 判断
for x in arr:
    if x not in d:					  # not in 判断列表元素存在性
        d[x] = 1
    else:
        d[x] += 1

# 方式 b：get() 方法（更优雅）
for x in arr:
    d[x] = d.get(x, 0) + 1             # 前一个是寻找参数，后一个是默认返回值

# 方式 c：直接 count（效率低）
for x in arr:
    d[x] = arr.count(x)
```

**模型二：数据对的存储**

```python
n = int(input())
d = {}
for _ in range(n):
    name, score = input().split()
    d[name] = int(score)          # 直接赋值创建键值对
```

**注意区别**：统计型需要 if 判断键是否存在；数据对型可以直接赋值。

### 7.3 字典常用操作

```python
d = {"a": 1, "b": 2, "c": 3}

# 访问
d["a"]                  # 1（键不存在会报错）
d.get("z", 0)           # 0（键不存在返回默认值 0）

# 修改与添加
d["a"] = 100            # 修改已有键的值
d["d"] = 4              # 添加新键值对
d.update({"e": 5})      # 批量更新

# 删除
del d["b"]              # 删除键值对
val = d.pop("c")        # 删除并返回值

# 遍历
for k, v in d.items():  # 同时遍历键和值
    print(k, v)

for k in d.keys():      # 遍历键
    print(k)

for v in d.values():    # 遍历值
    print(v)

# 排序
sorted(d.items())                               # 按键排序
sorted(d.items(), key=lambda x: x[1])           # 按值排序
sorted(d.items(), key=lambda x: (-x[1], x[0]))  # 值降序，键升序
# {'elderberry': 50, 'date': 40, 'apple': 20, 'banana': 20, 'cherry': 20}

# 统计
len(d)                  # 键的数量
max(d.values())         # 最大值的值
```

### 7.4 集合

```python
# 创建
s = set()                     # 空集合（注意：{} 是空字典！）
s = {1, 2, 3}                 # 字面量创建，集合！而不是字典
s = set([1, 2, 2, 3, 3])     # {1, 2, 3} —— 自动去重

# 添加/删除
s.add(4)
s.remove(4)                   # 不存在会报错
s.discard(4)                  # 不存在不报错

# 集合运算
a & b     # 交集
a | b     # 并集
a - b     # 差集
a ^ b     # 对称差

# 判断
3 in s    # True / False
```

---

### 📝 练习 7

**7.1** 输入 n 个整数，统计每个数出现的次数（按数字升序输出）。

**7.2** 输入 n 个整数，找出出现次数最多的数（众数）。如果有多个，输出最小的那个。

**7.3** 输入 n 个整数，去重后按降序输出。

**7.4** 名片管理系统：反复输入命令 `add name phone`、`find name`、`quit`，实现添加和查找功能。

<details>
<summary>参考答案</summary>

```python
# 7.1
arr = [int(x) for x in input().split()]
d = {}
for x in arr:
    d[x] = d.get(x, 0) + 1
for k, v in sorted(d.items()):
    print(k, v)

# 7.2
arr = [int(x) for x in input().split()]
d = {}
for x in arr:
    d[x] = d.get(x, 0) + 1
max_val = max(d.values())
candidates = [k for k, v in d.items() if v == max_val]
print(min(candidates))

# 7.3
arr = [int(x) for x in input().split()]
print(*sorted(set(arr), reverse=True))

# 7.4
phonebook = {}
while True:
    cmd = input().split()
    if cmd[0] == "quit":
        break
    elif cmd[0] == "add":
        phonebook[cmd[1]] = cmd[2]
        print("添加成功")
    elif cmd[0] == "find":
        print(phonebook.get(cmd[1], "未找到"))
```
</details>

---

## 8. 函数

### 8.1 函数定义

```python
def 函数名(参数1, 参数2):
    """文档字符串：说明函数做什么"""
    # 函数体
    return 结果    # 可选
```

```python
# 判断素数的函数（来自你的代码）
def is_prime(n):
    """判断 n 是否为素数，返回 True/False"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 使用
for i in range(2, 100):
    if is_prime(i):
        print(i, end=" ")
```

### 8.2 参数与返回值

```python
# 默认参数
def greet(name, greeting="你好"):
    print(f"{greeting}，{name}！")

greet("小明")            # 你好，小明！
greet("小红", "早上好")  # 早上好，小红！

# 多返回值（实际返回元组）
def divide(a, b):
    return a // b, a % b

quotient, remainder = divide(13, 5)   # 2, 3

# 局部变量与全局变量
x = 10            # 全局变量

def func():
    x = 20        # 局部变量（不影响全局 x）
    print(x)

func()            # 20
print(x)          # 10（全局变量没变）
```

### 8.3 期中复习：Debug 循环体

```python
# 循环体 debug 技巧：加 print 观察每一步的值
def sum_factors(n):
    total = 1          # ⚠️ 累加变量要在循环外面定义！
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i + n // i
            # print(f"i={i}, total={total}")  # debug 用
    return total
```

---

### 📝 练习 8

**8.1** 编写函数 `digit_sum(n)`，返回整数 n 的各位数字之和。

**8.2** 编写函数 `is_palindrome(n)`，判断整数 n 是否为回文数（如 121）。

**8.3** 编写函数 `gcd(a, b)`，返回 a 和 b 的最大公约数。

**8.4** 哥德巴赫猜想验证：输入一个偶数 n（≥4），将其分解为两个素数之和并输出。

**8.5** 遍历 100~999 之间所有素数回文数（既是素数又是回文数）。

<details>
<summary>参考答案</summary>

```python
# 8.1
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# 8.2
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# 8.3
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 8.4
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

n = int(input())
for i in range(2, n):
    if is_prime(i) and is_prime(n - i):
        print(f"{n} = {i} + {n - i}")
        break

# 8.5
for i in range(100, 1000):
    if is_prime(i) and str(i) == str(i)[::-1]:
        print(i)
```
</details>

---

## 9. 文件操作

### 9.1 打开与关闭文件

```python
# 推荐方式：with 语句（自动关闭文件）
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 传统方式（需要手动关闭）
f = open("data.txt", "r", encoding="utf-8")
content = f.read()
f.close()
```

| 模式 | 含义 |
|------|------|
| `"r"` | 只读（文件必须存在） |
| `"w"` | 只写（覆盖已有内容，文件不存在则创建） |
| `"a"` | 追加（在文件末尾添加） |
| `"r+"` | 读写 |

### 9.2 读取文件

```python
with open("data.txt", "r", encoding="utf-8") as f:
    # 一次性读取全部
    content = f.read()

    # 读取一行
    line = f.readline()

    # 读取所有行，返回列表
    lines = f.readlines()

    # 逐行迭代（推荐，内存友好）
    for line in f:
        print(line.strip())
```

### 9.3 写入文件

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello World\n")
    f.write("第二行\n")
    f.writelines(["行1\n", "行2\n", "行3\n"])
```

### 9.4 处理 CSV 文件

```python
import csv

# 读取 CSV
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)       # 跳过表头
    for row in reader:
        print(row)              # row 是列表

# 写入 CSV
with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "分数"])
    writer.writerow(["小明", 95])
```

---

### 📝 练习 9

**9.1** 编写程序，读取一个文本文件 `input.txt`（每行一个数字），计算所有数字的平均值并写入 `result.txt`。

**9.2** 写一个函数 `copy_file(src, dst)`，实现文件复制功能。

**9.3** 读取一个 CSV 文件，包含两列"姓名"和"成绩"，找出最高分的同学姓名并打印。

<details>
<summary>参考答案</summary>

```python
# 9.1
with open("input.txt", "r", encoding="utf-8") as f:
    nums = [int(line.strip()) for line in f if line.strip()]
avg = sum(nums) / len(nums)
with open("result.txt", "w", encoding="utf-8") as f:
    f.write(f"平均值：{avg:.2f}\n")

# 9.2
def copy_file(src, dst):
    with open(src, "rb") as f_src:
        with open(dst, "wb") as f_dst:
            f_dst.write(f_src.read())

# 9.3
import csv
max_score = -1; top_student = ""
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for name, score in reader:
        if int(score) > max_score:
            max_score = int(score)
            top_student = name
print(f"最高分：{top_student}，{max_score}分")
```
</details>

---

## 10. 异常处理

### 10.1 try/except/else/finally

```python
try:
    a = int(input("输入被除数："))
    b = int(input("输入除数："))
    result = a / b
except ValueError:
    print("错误：请输入有效的整数。")
except ZeroDivisionError:
    print("错误：除数不能为零。")
except Exception as e:
    print(f"发生了未预料的错误：{e}")
else:
    # try 成功执行后运行（无异常时）
    print(f"结果：{result:.1f}")
finally:
    # 无论是否异常都会执行（常用于清理资源）
    print("计算结束。")
```

### 10.2 常见异常类型

| 异常类型 | 触发条件 |
|----------|----------|
| `ValueError` | 类型转换失败（如 `int("abc")`） |
| `ZeroDivisionError` | 除以零 |
| `TypeError` | 类型不匹配（如 `"a" + 1`） |
| `IndexError` | 列表索引越界 |
| `KeyError` | 字典键不存在 |
| `FileNotFoundError` | 文件不存在 |
| `EOFError` | 输入流结束 |

### 10.3 raise：主动抛出异常

```python
def check_positive(n):
    if n <= 0:
        raise ValueError("错误：输入的数不是正数")
    return True

try:
    n = int(input())
    check_positive(n)
except ValueError as e:
    print(e)
```

### 10.4 assert：断言（debug 利器）

```python
def divide(a, b):
    assert b != 0, "错误：除数不能为零"
    return a / b

# assert 默认在生产环境会被禁用（python -O）
# 所以不要用 assert 做业务逻辑验证
```

### 10.5 实用模式：处理未知数量的输入

```python
# 经典模式：读取多组测试数据直到 EOF
while True:
    try:
        n = int(input())
        # 处理 n
        print(f"处理结果：{n * 2}")
    except EOFError:
        break
```

---

### 📝 练习 10

**10.1** 编写一个安全除法函数 `safe_divide(a, b)`，处理除零和类型错误，始终返回一个有意义的结果或错误信息。

**10.2** 读取一个文件 `scores.txt`（每行一个分数），如果分数不是合法的整数则跳过并统计跳过的行数。输出有效分数的平均值和跳过的行数。

**10.3** 实现一个简单的银行取款函数 `withdraw(balance, amount)`：
- 如果 amount > balance，抛出 `ValueError("余额不足")`
- 如果 amount <= 0，抛出 `ValueError("取款金额必须为正数")`
- 否则返回 balance - amount

<details>
<summary>参考答案</summary>

```python
# 10.1
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "错误：除数不能为零"
    except TypeError:
        return "错误：请输入数字"
    except Exception as e:
        return f"未知错误：{e}"

# 10.2
valid, skipped = [], 0
try:
    with open("scores.txt", "r", encoding="utf-8") as f:
        for line in f:
            try:
                valid.append(int(line.strip()))
            except ValueError:
                skipped += 1
except FileNotFoundError:
    print("文件不存在")
    exit()
if valid:
    print(f"有效平均分：{sum(valid)/len(valid):.1f}")
print(f"跳过行数：{skipped}")

# 10.3
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("取款金额必须为正数")
    if amount > balance:
        raise ValueError("余额不足")
    return balance - amount
```
</details>

---

## 11. 面向对象

### 11.1 类与对象

```python
class Student:
    # 构造方法（创建对象时自动调用）
    def __init__(self, name, age):
        self.name = name          # 成员变量（实例属性）
        self.age = age
        self.scores = []          # 默认值

    # 成员方法
    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    # 字符串表示（print 时自动调用）
    def __str__(self):
        return f"学生(name={self.name}, age={self.age})"

# 使用
stu1 = Student("小明", 18)        # 调用 __init__
stu1.add_score(95)                 # 调用成员方法
print(stu1.average())              # 调用成员方法
print(stu1)                        # 调用 __str__
```

### 11.2 魔术方法

```python
class MyNumber:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):      # + 运算符
        return MyNumber(self.num + other.num)

    def __lt__(self, other):       # < 运算符（sort 会用到）
        return self.num < other.num

    def __eq__(self, other):       # == 运算符
        return self.num == other.num

    def __str__(self):            # print() 输出
        return f"MyNumber({self.num})"

    def __repr__(self):           # 调试输出（列表里会用）
        return f"MyNumber({self.num})"

a = MyNumber(10)
b = MyNumber(20)
c = a + b          # 调用 __add__
print(a < b)       # 调用 __lt__
print(c)           # 调用 __str__
```

### 11.3 继承与多态

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # 子类覆写

    def describe(self):
        return f"{self.name} 是一只{self.__class__.__name__}。"

class Dog(Animal):
    def speak(self):
        return "汪汪！"

class Cat(Animal):
    def speak(self):
        return "喵喵～"

# 多态：同一个接口，不同的行为
pets = [Dog("旺财"), Cat("咪咪"), Dog("大黄")]
for pet in pets:
    print(f"{pet.name}: {pet.speak()}")     # 各自调用各自的 speak
```

---

### 📝 练习 11

**11.1** 设计一个 `Rectangle` 类，包含属性 `width` 和 `height`，包含方法 `area()` 和 `perimeter()`。

**11.2** 为 `Rectangle` 类添加 `__lt__` 魔术方法，使得两个矩形可以按面积比较大小。

**11.3** 设计一个 `BankAccount` 类，包含 `deposit(amount)`、`withdraw(amount)` 方法和一个 `balance` 属性。取款时余额不足应抛出异常。

<details>
<summary>参考答案</summary>

```python
# 11.1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

# 11.2
class Rectangle:
    # ... 同上的 __init__, area, perimeter

    def __lt__(self, other):
        return self.area() < other.area()

# 11.3
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("存款金额必须为正数")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("取款金额必须为正数")
        if amount > self.balance:
            raise ValueError("余额不足")
        self.balance -= amount

    def __str__(self):
        return f"账户({self.owner})：余额 {self.balance} 元"
```
</details>

---

## 12. 模块与包

### 12.1 导入模块

```python
# 导入整个模块
import math
print(math.pi)
print(math.sqrt(16))

# 导入特定函数
from math import sqrt, pi
print(sqrt(16))

# 导入并起别名
import math as m
print(m.cos(0))

# 导入所有（不推荐 —— 会污染命名空间）
from math import *
```

### 12.2 常用标准库

```python
# 数学
import math
math.pi, math.e, math.sqrt(), math.sin(), math.ceil(), math.floor()

# 随机
import random
random.randint(1, 10)      # [1, 10] 随机整数
random.random()             # [0, 1) 随机浮点数
random.choice([1,2,3])      # 随机选一个
random.shuffle(arr)         # 原地打乱

# 时间
import time
time.time()                 # 当前时间戳
time.sleep(1)               # 暂停 1 秒

# 日期
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
```

### 12.3 创建自己的模块

```
my_package/
├── __init__.py          # 空文件，声明这是一个包
├── my_module.py         # 你的模块
└── main.py              # 主程序
```

```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

# main.py
from my_module import greet
print(greet("World"))
```

---

### 📝 练习 12

**12.1** 使用 `math` 模块计算圆的面积和周长（输入半径 r）。

**12.2** 使用 `random` 模块实现一个掷骰子程序：模拟掷两个骰子 n 次，统计每个点数（2~12）出现的次数。

<details>
<summary>参考答案</summary>

```python
# 12.1
import math
r = float(input())
print(f"面积：{math.pi * r**2:.2f}")
print(f"周长：{2 * math.pi * r:.2f}")

# 12.2
import random
n = int(input("掷多少次？"))
counts = {i: 0 for i in range(2, 13)}
for _ in range(n):
    total = random.randint(1, 6) + random.randint(1, 6)
    counts[total] += 1
for k, v in counts.items():
    print(f"点数{k}：{v}次 ({v/n*100:.1f}%)")
```
</details>

---

## 13. 测试与 pytest

### 13.1 安装 pytest

```bash
pip install pytest --break-system-packages
```

### 13.2 编写测试

测试文件命名：`test_*.py` 或 `*_test.py`

```python
# test_math_utils.py
import pytest
from math_utils import is_prime, factorial, gcd

# 测试 is_prime
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(1) == False
    assert is_prime(17) == True

# 测试 factorial
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

# 测试异常
def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

# 参数化测试（一次测试多种输入）
@pytest.mark.parametrize("a,b,expected", [
    (12, 8, 4),
    (7, 13, 1),
    (100, 25, 25),
    (17, 17, 17),
])
def test_gcd(a, b, expected):
    assert gcd(a, b) == expected
```

### 13.3 运行测试

```bash
# 运行所有测试
pytest

# 运行指定文件
pytest test_math_utils.py

# 显示详细信息
pytest -v

# 显示 print 输出
pytest -s

# 只运行含有关键字的测试
pytest -k "prime"
```

### 13.4 Fixture（测试夹具）

```python
# conftest.py 或测试文件内
import pytest

@pytest.fixture
def sample_student():
    """创建一个学生对象供测试使用"""
    from student import Student
    stu = Student("测试生", 20)
    stu.add_score(90)
    stu.add_score(80)
    return stu

def test_average(sample_student):
    assert sample_student.average() == 85.0

def test_add_score(sample_student):
    sample_student.add_score(100)
    assert len(sample_student.scores) == 3
```

---

### 📝 练习 13

**13.1** 为你在练习 8 中编写的 `is_prime` 和 `gcd` 函数编写 pytest 测试代码。

**13.2** 为练习 11 中的 `BankAccount` 类编写测试：测试存款、取款、余额不足异常。

<details>
<summary>参考答案</summary>

```python
# test_practice.py
import pytest

# 假设这些函数定义在 practice.py 中
from practice import is_prime, gcd, BankAccount

class TestIsPrime:
    def test_small_numbers(self):
        assert not is_prime(1)
        assert is_prime(2)
        assert is_prime(3)
        assert not is_prime(4)

    def test_larger_numbers(self):
        assert is_prime(17)
        assert is_prime(97)
        assert not is_prime(100)

class TestGcd:
    @pytest.mark.parametrize("a,b,expected", [
        (12, 8, 4), (7, 13, 1), (100, 25, 25)
    ])
    def test_gcd(self, a, b, expected):
        assert gcd(a, b) == expected

class TestBankAccount:
    def test_deposit(self):
        acc = BankAccount("测试", 100)
        acc.deposit(50)
        assert acc.balance == 150

    def test_withdraw(self):
        acc = BankAccount("测试", 100)
        acc.withdraw(30)
        assert acc.balance == 70

    def test_withdraw_insufficient(self):
        acc = BankAccount("测试", 100)
        with pytest.raises(ValueError, match="余额不足"):
            acc.withdraw(200)
```
</details>

---

## 14. 综合练习

以下练习综合运用了前面多个章节的知识。

### 14.1 学生成绩管理系统

```
功能需求：
1. 从文件 scores.csv 读取学生数据（姓名, 语文, 数学, 英语）
2. 计算每个学生的总分和平均分
3. 按总分降序排序，总分相同按语文成绩降序
4. 输出排名前 5 的学生信息
5. 统计各科平均分
6. 将结果写入 result.txt

异常处理：
- 文件不存在时给出提示
- 分数格式错误时跳过该行
```

### 14.2 单词频率统计

```
功能需求：
1. 读取文本文件 article.txt
2. 忽略大小写，按空格和标点符号分词
3. 统计每个单词出现的次数
4. 输出出现次数最多的 10 个单词

提示：使用字典、集合、字符串操作
```

### 14.3 奖学金评定系统（来自 Day8 练习）

```
某学校奖学金评定规则：
- 期末平均成绩 > 80 且发表论文 ≥ 1 篇：院士奖学金 8000 元
- 期末平均成绩 > 85 且班级评议成绩 > 80：五四奖学金 4000 元
- 期末平均成绩 > 90：成绩优秀奖 2000 元
- 期末平均成绩 > 85 且是西部省份学生：西部奖学金 1000 元
- 班级评议成绩 > 80 且是学生干部：班级贡献奖 850 元

输入：第 1 行是学生人数 n，接下来 n 行每行是：
    姓名 期末平均成绩 班级评议成绩 是否学生干部 是否西部省份 论文数
输出：总奖学金最高的学生姓名、金额，以及所有学生奖学金总和
```

<details>
<summary>参考答案</summary>

```python
# 14.3 奖学金评定系统
class Student:
    def __init__(self, name, score_t, score_c, is_official, is_west, papers):
        self.name = name
        self.score_t = int(score_t)
        self.score_c = int(score_c)
        self.is_official = is_official
        self.is_west = is_west
        self.papers = int(papers)

    def scholarship(self):
        total = 0
        if self.score_t > 80 and self.papers >= 1:
            total += 8000
        if self.score_t > 85 and self.score_c > 80:
            total += 4000
        if self.score_t > 90:
            total += 2000
        if self.score_t > 85 and self.is_west == "Y":
            total += 1000
        if self.score_c > 80 and self.is_official == "Y":
            total += 850
        return total

n = int(input())
students = []
total_scholarship = 0
for _ in range(n):
    name, st, sc, off, west, pap = input().split()
    stu = Student(name, st, sc, off, west, pap)
    students.append(stu)
    total_scholarship += stu.scholarship()

best = max(students, key=lambda s: s.scholarship())
print(best.name)
print(best.scholarship())
print(total_scholarship)
```
</details>

---

## 附录 A：常见错误速查

| 错误 | 原因 | 解法 |
|------|------|------|
| `split()` 忘记括号 | 写成 `input.split` | `input().split()` |
| 中英文括号混用 | 输入法问题 | 检查 `()`、`""` |
| 变量未定义 | 在循环内定义了累加变量 | 移到循环外 |
| `list indices must be integers` | 把列表当字典用了 | 检查是否该用 `[]` 还是 `{}` |
| `if` 连续执行 | 该用 `elif` 的地方用了 `if` | 互斥条件用 `elif` |
| 修改 `for` 循环变量无效 | `for x in arr: x = ...` | 通过索引修改 `arr[i] = ...` |
| range 范围错误 | 忘了左闭右开 | `range(n)` 是 0~n-1 |
| NoneType 错误 | 函数忘了 return | 检查函数是否有 return |

## 附录 B：常用字符串格式化速查

```python
# 整数
f"{42:5d}"      # '   42' —— 右对齐宽度5
f"{42:05d}"     # '00042' —— 补零

# 浮点数
f"{3.14159:.2f}" # '3.14' —— 保留两位小数
f"{3.14159:.0f}" # '3' —— 四舍五入到整数

# 字符串
f"{'hi':>10}"   # '        hi' —— 右对齐宽度10
f"{'hi':<10}"   # 'hi        ' —— 左对齐宽度10

# format 等价写法
"{:.2f}".format(3.14159)      # f-string 的前身
```

---

*这份清单覆盖了从入门 print 到面向对象、pytest 测试的完整 Python 语法。每个知识点旁边标注了易错点，练习题的参考答案都给了出来。建议每天刷一个章节，配合你原来的代码笔记一起看效果最好。加油！*
