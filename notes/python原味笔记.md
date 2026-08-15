# Python 暑期课程原味学习笔记

## Day 1：Python 入门 —— 输入输出、变量与条件判断

### 1.1 程序输出与 print 函数

```python
# 文件：1（print输出函数）.py
print(100,13.14,sep='*',end="=") #分隔符:单个内部 终止符 分隔符  \n换行
print("Hello XiaoDuo")
```

- 字面量（数据）的类型：数字（整数、浮点数、布尔值）、字符串、列表、元组
- print 输出函数：分隔方式（sep）、终止方式（end）
- 字符串 `""`、数字、变量、列表各有特殊规则

```python
# 文件：2（输出换行+变量赋值）.py
print(1234,5678,sep=" * ",end=" = ")
print(7006652)

print('1234 * 5678 =',1234*5678)
# 字面量分隔默认空格，内部自己加空格
# end换行可以采用 = 空格进行修改
```

赋值语句从右向左结合，复合算数赋值：`x += y` 等价于 `x = x + y`

```python
# 文件：5（pass）.py
a = 20
b = 12
print(a,b,"a*b =",a*b)
# 输出结果：20 12 a*b = 240
```

### 1.2 输入函数与变量

```python
# 文件：3（输入函数-输出变量）.py
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=(a+b)*c
print(d)
# 多个变量输入 确定输入个数
# 多个输入量的分离
# 输入量的数据类型转化

# 输入内容可以储存在变量中 这个变量已有字符串意义
name=input()
print(name)
print("name")
# 再次反映print输出变量背后被赋予的东西
```

```python
# 文件：6（输入提示引号）.py
a = input("请输入")
a = int(a)
type(a)
# 输入函数的提示内容必须加引号
```

### 1.3 多变量输入的几种写法

```python
# 文件：9（多个输入内容相加）.py
x,y,z=input().split()
x = int(x); y = int(y); z = int(z)
print(x+y+z)
# 输入内容为字符串类型，直接加则只表示合起来，先化成整数

x,y,z = map(int, input().split())
print(x+y+z)
# map函数 一次性完成
```

```python
# 文件：12（多变量输入）.py
x,y,z=input().split()
x=int(x); y=int(y); z=int(z)
ans=x*0.2+y*0.3+z*0.5
ans=int(ans)  #要求输出整数
print(ans)

x,y,z=map(int, input().split())
```

### 1.4 数位分离

```python
# 文件：14（数位分离）.py
# 输入一个数字转化为三位，数位分离采用带余除法
# 区分于初始时一次性输入三个数字分开，使用分离函数
a=int(input())  # 字符串先转化为数字才能求余
baiwei=a//100
shiwei=a//10%10
# 123十位数字的处理思路：先//10取整得12，再%10求余得2
gewei=a%10
print(gewei,shiwei,baiwei,sep="")
# 输出最后三个结果时默认有空格连接
```

```python
# 文件：7（表示数位）.py
a = input(); a = int(a)
g = a%10
s = a//10%10
b = a//100
ans = g*100+s*10+b*1
print(ans)
# 有没有不限制数位的统一数位分离模型？
```

```python
# 文件：13（数位调换）.py
a=int(input())
baiwei=a//100
shiwei=a//10%10
gewei=a%10
print(gewei,shiwei,baiwei,sep="")
```

### 1.5 格式化输出

```python
# 文件：15（输出格式化与数位控制）.py
a,b=input().split()
a=int(a); b=int(b)
c=a/b; c=float(c)
print("%.9f"%c)
# 利用%进行精度控制和格式化  %s %f %d占位
```

```python
# 文件：16（数位控制和变量展开）.py
# "%s %d %f"（内部%占位必须标清楚类型）          ------占位隐藏
# %5.2f宽度空格填充控制，小数点四舍五入控制        ------变量精度控制
# 多个%的处理方式(a,b,c) 内部是变量               ------变量展开
```

```python
# 文件：17.py —— format函数格式化
f=input(); f=float(f)
c=5*(f-32)/9
print("{:.5f}".format(c))
# 利用format函数进行精度控制和格式化
# 大括号表示占位部分
# 位置参数0，1，2 参数反复使用时 format内部编辑字符串 数字等
# 关键字占符
```

```python
# 文件：18（进阶之路-利用f-string函数）.py
name=input(); time=input(); num=input()
name=str(name); time=float(time); num=int(num)
print(f"我叫{name},今天用{time}小时,写了{num}个小程序,为\"自己点赞\"!")
# 利用f""控制格式化内容
```

```python
# 文件：26（格式化空格对齐）.py
a,b,c=input().split()
a=int(a); b=int(b); c=int(c)
print("{: >8d} {: >8d} {: >8d}".format(a,b,c))
```

三种格式化方式对比（作业 2.1）：

```python
# 文件：作业2.1.py
a=float(input())
if 0<=a<5:
    print("{:.3f}".format(-1*a+2.5))      # format方式
if 5<=a<10:
    b=2-1.5*(a-3)*(a-3)
    print(f"{b:.3f}")                      # f-string方式
if 10<=a<20:
    c=a/2-1.5
    print("%.3f"%c)                         # %占位方式
# 三种格式化方式 标程
```

format 和 f-string 对比（作业 1.2）：

```python
# 文件：作业1.2.py
print(f"{d:.4f} {c:.4f} {s:.4f}")
# print("{:.4f} {:.4f} {:.4f}".format(d,c,s))
# 在format函数中，需要在末尾加入占位符的具体展开
# 在f-string函数中，可以直接在占位括号内进行解释和限定
# 易错点：print内容中的空格需要自己打上
```

### 1.6 取整与四舍五入

```python
# 文件：10（打折四舍五入）.py / 11（去掉小数保留整数）.py
x,y=input().split()
x=int(x); y=float(y)
z=0.1*y        # 打折率的问题
ans=x*z
ans=int(ans)   # 去掉小数部分
ans=ans+5      # 解决进位问题
print(ans//10*10)  # 去掉个位部分
```

```python
# 文件：24（奇偶性的取整问题）.py
a=int(input())
if a%2==0:
    c=a/2; c=int(c); print(c)
if a%2==1:
    c=a+1; d=c/2; d=int(d); print(d)
# 奇偶性实际问题的整数取整
# 最后输出结果时运行出含小数数值 手动取整编码输出内容
```

### 1.7 带余除法与取整进阶

```python
# 文件：27（带余除法）.py
a,b=input().split()
a=int(a); b=int(b)
c=a//b; d=a%b
print(c,d,sep=" ")
```

```python
# 文件：34（简单计算器问题）（补充两种整数控制）.py
a=13; b=8
print("%d"%shang)    # 输出1 —— %d整数精度控制：保留整数部分
print("%.0f"%shang)  # 输出2 —— %0f整数精度控制，四舍五入保留整数
```

### 1.8 If 条件判断

```python
# 文件：19（If语句）.py
a=input(); a=int(a)
if a % 2 == 1:
    print("odd")
if a % 2 != 1:
    print("even")
```

```python
# 文件：21（最大数的输出）.py
a,b,c=map(int,input().split())
if a>b and a>c: print(a)
if b>a and b>c: print(b)
if c>a and c>b: print(c)
# ... 以及各种相等情况的处理
```

```python
# 文件：22（恰好一门课及格）.py
a,b=input().split()
a=int(a); b=int(b)
if a < 60 and b < 60: print(0)
if a <60 and b>=60: print(1)
if a >= 60 and b <60: print(1)
if a >=60 and b>=60: print(0)
```

```python
# 文件：25（实际问题的计算与值的取整）.py
n,x,y=input().split()
n=int(n); x=int(x); y=int(y)
if n-y/x<0:
    print(0)
if n-y/x>=0:
    c=n-y/x; c=int(c); print(c)
# 注意考虑问题的正负临界性
# 注意输出结果取整性
```

### Day 1 作业

```python
# 文件：作业1.1.py
a,b,c=input().split()
a=int(a); b=int(b); c=int(c)
s=a+b+c; s=int(s); print(s)
# 易错点：split函数忘记写() —— 输入多个变量的题首先检查
# 输入数据的类型设定 —— 只要有输入就要检查

# 文件：作业1.5.py
a,b,c=map(float,input().split())
d=max(a,b,c); print(d)
```

---

## Day 2：条件分支深入与循环入门

### 2.1 分类讨论与多分支

```python
# 文件：29（分类讨论问题）.py
a=int(input())
if a>=86: print("VERY GOOD")
if a>=60 and a<=85: print("GOOD")
if a<60: print("BAD")
```

```python
# 文件：30（多数整除类型）.py
a=int(input())
if a%105==0: print("3 5 7")
if a%15==0 and a%7!=0: print("3 5")
# ...各组合情况
# 另法：利用elif感觉并不好写
# 另法：if依次执行的特点，多分支从上到下依次执行将三个输出结果叠加
```

```python
# 文件：31（分类讨论问题）.py
d=int(input())
m=27+23+d/3; n=d/1.2
if m>n: print("Walk")
if m<n: print("Bike")
if m==n: print("All")
# 等号的表达方式
```

### 2.2 三数排序

```python
# 文件：32（三个数比大小排序问题）.py
# 交换法：通过交换把较小的移到后面，只需要设定如果较大则交换（从上到下）
# 最大值、最小值函数法：中间项 = a+b+c-max-min
a,b,c=map(int,input().split())
d=max(a,b,c); print(d)
# 最大值函数用法
```

### 2.3 回文数

```python
# 文件：33（回文数）.py
a,b=map(int,input().split())
sum1=a+b
print(sum1)
if 99>=sum1>=10:
    s=sum1//10; g=sum1%10
    huiwen=g*10+s
    if huiwen==sum1: print("Yes")
    else: print("No")
# 错误类型：split又漏掉  注意中英文括号（） ()
# 这些错误通过run可以直接提示
```

### 2.4 简单计算器

```python
# 文件：34（简单计算器问题）（补充两种整数控制）.py
a,b,c=input().split()
a=int(a); b=int(b); c=str(c)
if c=="+": print(a+b)
if c=="/":
    if b!=0:
        s=a/b; s=int(s); print(s)
    else:
        print("Divided by zero!")
if c!="+" and c!="-" and c!="/" and c!= "*":
    print("Invalid operator!")
# 多个if的多分支结构，最后一个else只对应最后一个if
# 注意输出结构的整数形式，//取整或者手动int来取整
```

### 2.5 while 循环

```python
# 文件：35（while控制输出次数）.py
n=input(); n=int(n)
i=1
while i<=n:
    print("I'm gonna WIN!")
    i=i+1
# 易错点：输入的变量没有进行类型规定
# 在while结构中控制
# 最好的办法是检验限定条件次数和最后输出次数到底相不相同
```

```python
# 文件：36（while记录并控制次数）.py
x=20; i=1; sum1=20
while sum1<500:
    i=i+1; x=x+5; sum1=sum1+x
print(i)
# 在while结构中控制结束和次数
# 保证执行while的次数对应总人数即可
```

### 2.6 枚举检索 —— while 递增

```python
# 文件：37（while循环-增大依次枚举检索因数）.py
x=int(input())
n=1
while n<x:
    if x%n==0:
        print(n)    # 标准程序，利用while依次增大检索
    n=n+1
# 思路：递增讨论检索符合条件的项
# 而且这个检索是递增检索
# n=n+1的迭代始终成立，不需要满足整除条件
```

- 倒序检索：只需把 `n=1` 改为 `n=x-1`，`n=n+1` 改为 `n=n-1`
- 质因数分解模型：保持目标数 n 不变，检索增大因数

### 2.7 角谷猜想与 while+if 复合

```python
# 文件：38（角谷猜想while+if复合结构）.py
n=int(input())
while n>1:
    if n%2==0:
        print("{:.0f}/2={:.0f}".format(n,n/2))
        n=n/2    # 这个赋值先后非常重要，否则下一步表达式中的值已经发生变化
    else:        # else后面直接接冒号
        print("{:.0f}*3+1={:.0f}".format(n,n*3+1))
        n=n*3+1
if n==1: print("End")
```

**关键发现 —— 双if 和 elif 区别**：
- 双if条件会依次执行，当第一个语句输出1时仍然会进行第二个语句，会导致反复出现 4 2 1 的死循环
- elif条件下，执行了if就不会执行else，而是重新进行while的大条件判定
- 巧妙修改：将偶数的if语句放在后面，这样就算出来1也立刻进行循环条件判定

### 2.8 奇偶项求和

```python
# 文件：39（奇偶项获取和求和修正）.py
n=int(input())
i=2; j=1
sumou=i; suji=j
while i<=n and i%2==0:
    sumou=sumou+i; i=i+2
while j<=n and j%2==1:
    suji=suji+j; j=j+2
print(sumou-2, suji-1)
# 对于while的理解：你想设置一个前提，但这个前提反复试探。相当于循环的if
# 并且多个while之间也是并列关系
# 注意到一开始就设定1、2，并且为了实现求和一开始就多加了一遍
```

### 2.9 for range 循环

```python
# 文件：40(for range函数格式).py
i=0
for i in range(10):
    print(i,end=" ")
# for函数知识点 —— 格式依然是冒号缩进（while、if、else、elif都是相同语法格式）
# range函数()括号内三个数位的含义：左闭、右开、递增的公差
# 字符串：遍历每个元素 G O O D ! 且为换行，需要手动添加空格print
# 数表：遍历表中的元素，此时字符串作为整体输出
```

```python
# 文件：41（for range函数记录循环次数）.py
sum1=0
for i in range(11):
    sum1=sum1+i
print(sum1)
# 易错点：另外引入一个诸如求和的变量时在循环开始前就要提前说明
```

### 2.10 持续输入求和

```python
# 文件：42（输入次数的持续输入求和）.py
n=int(input())
age=0
for x in range(n):
    x=int(input())
    age=x+age
ave=age/n
print("{:.2f}".format(ave))
# 这个题真的很难理解，两个输入内容：一个是循环次数，另一个持续输入
# x只是一个次数变量，并不需要提前说明，只需要表示他的range即可
# 输入的变量已经整型化了，所以可以直接放在range中
```

### 2.11 while 和 for 的转化

```python
# 文件：44（while和for循环的转化）.py
# for版本
a,b=map(int,input().split())
sum1=0
for i in range(a,b+1):
    if i%17==0:
        sum1=sum1+i
        i=i+1
    else:
        i=i+1
print(sum1)

# while版本
a,b=map(int,input().split())
sum1=0; n=a
while a<=n<=b:
    if n%17==0: sum1=sum1+n
    n=n+1
print(sum1)

# 对比：while函数的条件变量必须提前引入和解释，for i 不需要
```

### 2.12 斐波那契数列 —— 变量迭代

```python
# 文件：45（斐波那契数列-变量迭代求值）.py
n=int(input())
s1=1; s2=1
if n<=2: print(1)
else:
    for i in range(3,n+1):
        s3=s1+s2
        s1=s2    # 这里三个值的赋值顺序非常重要！先写前面的就会影响后面的进一步赋值
        s2=s3
    print(s3)
# i只是引入一个执行次数，也无需控制即可
# 第k个值和i的循环次数到底有什么关系？举个例子说明会更好理解
```

### 2.13 猜数字游戏 —— 循环终止

```python
# 文件：46（猜数字游戏-循环输入和输出）.py
a=int(input()); b=int(input())
while a!=b:
    if a>b: print("<"); b=int(input())
    if a<b: print(">"); b=int(input())
    if a==b: print("=")

# while True 版本
while True:
    if a>b: print("<"); b=int(input())
    if a<b: print(">"); b=int(input())
    if a==b: print("="); break

# 第二种非常好用！就是循环的if结构，只有达成最后条件才结束条件试探
```

```python
# 文件：47（循环结构持续输入）.py
a=int(input()); sum1=a
while True:
    if a!=0:
        a=int(input())
        sum1=a+sum1
    if a==0:
        print(sum1); break
# 一样是终止型循环结构，只有达到终止条件才停止循环试探，非常好用！！！
# 易错点：sum1需要提前说明，a值的说明就是持续输入
```

### Day 2 作业

```python
# 文件：作业2.3.py —— 统计数中3的个数
# 利用数位分离+逐个if判断

# 文件：作业2.4.py —— 水仙花数检索
a=100
while 100<=a<=999:
    s1=a//100; s2=a%100//10; s3=a%10
    k=s1**3+s2**3+s3**3
    if k==a: print(a)
    a=a+1

# 文件：作业2.5.py —— 最大公约数
# 文件：作业2.6.py —— 最小公倍数（利用while+break终止检索）
```

---

## Day 3：嵌套循环、列表入门

### 3.1 等比数列与 while

```python
# 文件：2（while循环计算等比数列）.py
h=int(input())
luodi=1; sum1=0
if luodi==1:
    sum1=h; luodi=luodi+1
while 2<=luodi<=10:
    h=h/2; sum1=sum1+h*2; luodi=luodi+1
print(f"{sum1:.2f}")
h=20*(1/2)**10; print(f"{h:.2f}")
# 落地距离分两类开始讨论，利用while循环计算等比数列
```

### 3.2 嵌套循环 —— 图形打印

```python
# 文件：5（嵌合循环矩形）.py
n=int(input())
for i in range(n):
    for i in range(n):
        print("*",end="")    # 单行内部的循环次数
    print("")                # 单行的换行处理
```

```python
# 文件：6（嵌合循环直角）.py
n=int(input()); m=0
for i in range(n):
    m=m+1
    for j in range(m):
        print("*",end="")    # 单行内部的循环次数
    print("")                # 执行一行之后的换行
# 利用新变量m来使每一行的循环次数增加
```

```python
# 文件：7（嵌合循环平行四边形）.py
n=int(input()); m=-1
for i in range(n):
    m=m+1                     # 单行的递增变量
    for i in range(m):
        print(" ",end="")     # 单行小内部的空格次数循环递增
    for i in range(n):
        print("*",end="")     # 单行小内部的*循环次数
    print("")                 # 单行的换行处理
```

### 3.3 阶乘与求和

```python
# 文件：8（阶乘求和）.py
n=int(input())
ans=0; sum1=1
for i in range(1,n+1):
    sum1=sum1*i
    ans=sum1+ans
print(int(ans))
# 阶乘的构造和理解：设立一个初始sum值，接着每次设置递增的i值
# 这个i可以自己遍历，while结构中才需要手动迭代
```

### 3.4 检索计数与求和

```python
# 文件：9（数位分离数字1的个数-检索计数）.py
# 方法一：四位数位分离+逐个if判断
# 方法二：while循环取余
j=1; ans=0
while j!=0:
    i=j
    if i%10==1: ans+=1
    i//=10    # 数位分离方式：一直看10的余数，除10取整就是减去末尾
    j=j+1
```

```python
# 文件：10（与7无关的数-检索求和）.py
n=int(input()); m=1; sum1=0
while m<=n:
    s1=m//10; s2=m%10; cnt=0
    if s1==7: cnt=cnt+1
    if s2==7: cnt=cnt+1
    if m%7!=0 and cnt==0: sum1=sum1+m*m
    m=m+1
print(sum1)
# 易错点：变量等号！！变量到底是哪一个进行运算
# 检索求和思路：依然是if语句，只是不加break，同样利用if
```

```python
# 文件：11（分解质因数-检索终止）.py
n=int(input()); m=2
while m<=n:
    if n%m==0:
        print(int(n/m)); break
    m=m+1
```

### 3.5 列表入门

```python
# 文件：12（三种表格生成方式）.py
# 方式一：map
a=list(map(int,input().split()))
# 方式二：循环append
list1=[]
for i in input().split():
    i=int(i); list1.append(i)
# 方式三：列表推导式
list1=[int(i) for i in input().split()]
# 三种列表的生成方式
```

```python
# 文件：14（输入内容放入列表-列表增加）.py
n=int(input())
list1=[]
for i in input().split():
    i=int(i); list1.append(i)
x=int(input()); y=int(input())
list1.insert(x-1,y)
print(*list1)
# 将输入的内容全部创建进列表组，记得需要将i进行类型转化
# 列表的增加：任意位置只能利用插入函数
```

```python
# 文件：13（访问列表-未知输入时用列表）.py
# 三种访问方式：while遍历、for range遍历、index索引
```

### 3.6 列表操作总结

```python
# 文件：18.py —— 列表操作大全
# 列表的添加：直接 for i in input 进行处理
# 列表所有元素个数的统计
# 列表的统计和计算：.count()某个元素的格式统计、最大值、最小值、求和
# 列表的增加：.append / .extend / .insert 三种函数
# 列表的删除：.remove（第一个访问的元素）、.pop（访问下标）、del（下标或切片）
# 切片删除（修改为空白列表）
# 列表修改：直接利用角标的索引修改；切片范围内加入多个元素（等数量替换）
# 列表差值
# 列表索引：返回第一个匹配到元素的下标
```

### Day 3 作业

```python
# 文件：作业3.3.py —— 利用 in 判断元素存在
flag=j in list1
```

---

## Day 4：列表进阶与二维列表

### 4.1 标记数组（重叠切片）

```python
# 文件：1（重叠切片-标记数字）.py
L,m=map(int,input().split())
list1=[]
for i in range(L+1):
    list1.append(1)
# list1=[1]*(L+1)
# list1=[1 for i in range(L+1)]
for i in range(m):
    a,b=map(int,input().split())
    list1[a:b+1]=[0]*(b-a+1)
print(int(list1.count(1)))
# 易错点：下标 0~L 等价于 1~L+1
# 易错点：列表的切片表示方式——冒号
# 数组的下标和range的下标：
#   数组中的角标位置——从0开始的位置索引
#   range的循环遍历次数——左开右闭区间
# 方法：标记数组——数字全部是1，只需要控制切片的数字即可
```

### 4.2 列表排序

```python
# 文件：2（列表排序）.py
n=int(input())
list1=[]
for i in input().split():
    i=int(i); list1.append(i)
for i in range(n):
    for j in range(i+1,n):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
print(*list1)
# 数组排序问题：先将输入的数字全部加入数组，然后执行擂台循环
# 每一轮只需要进行比较，如果有更小就进行换位（换位采用元组解包运算）
# 利用i和j的数字遍历来访问list中的元素，这样就可以实现条件比较
```

### 4.3 列表小综合

```python
# 文件：3（列表小综合）.py
# 查漏补缺：
# 1. list1的添加
# 2. list1的检索遍历
# 3. list的排序 .sort()
# 4. list的三种输出方式

# 文件：4（列表小综合）.py
# 列表数据的综合处理，排序函数的应用

# 文件：5（小鱼比可爱 列表大综合）.py
# 编程如绣花，大的思路完全没有任何问题，出错的点就在于几个小的细节
# 在for语句中sum1如果放for内部，会出现未定义变量
# 输出的次数也要特别注意，到底哪一步循环下需要进行输出
# 还是角标比较问题，真的非常细节，强烈建议带一个值进入比较
```

### 4.4 列表组成最小的数

```python
# 文件：6（列表组成最小的数）.py
n=int(input())
list1=[]
for i in input().split():
    i=int(i); list1.append(i)
list1.sort()
if not list1[0]:
    cnt=list1.count(0)
    list1[0],list1[cnt]=list1[cnt],list1[0]
print(*list1,sep="")
# 如果第一个是0，list1[0]=0所以会执行后面的语句
# 统计0的数量，随后进行交换
# 注意不能简单将0去掉，而是需要放在后面
```

### 4.5 二维列表

```python
# 文件：9（二维列表的生成和求和）.py
n,m=map(int,input().split())
arr1=[]
for i in range(n):
    arr1.append([])
    tmp=list(map(int,input().split()))
    for j in tmp:
        arr1[i].append(j)
# 同样利用推导式建立二维列表：
jz1=[[int(x) for x in input().split()] for i in range(n)]
```

```python
# 文件：14（行列式进行坐标排序）.py
n=int(input())
jz1=[]
for i in range(n):
    x,y=map(int,input().split())
    jz1.append([x,y])
jz1.sort(key=lambda x:(x[0],x[1]))
for i in jz1:
    print(*i)
# 二维列表的建立：利用一组一组元素进行添加
# 二维列表进行排序：利用lambda函数进行排序
# 遍历列表中的值：利用循环输出二维列表，最终输出结果就是每一行每一列
```

```python
# 文件：15（奖学金）.py
# 行列式中输入内容这里利用推导式就不是那么好，因为添加的元素不只是一组一组
# 当你利用两个嵌套循环添加输入内容时，其实也没有这么复杂
# 接着利用lambda函数进行排序，注意key的设置和reverse循环的设置
# 输出访问列表中的值，直接访问列表中的索引
```

### 4.6 删除重复数字

```python
# 文件：11（删除列表中的重复数字）.py
# 删除列表重复元素：不能利用remove函数进行处理，只能删除首个匹配
# 另外一种思路：删除这个首先检索到的数的后一个下标索引的数
# 利用count来判定，利用index来确定
```

### 4.7 列表值修改

```python
# 文件：16（列表更改 马里奥的银币3）.py
# 错误写法：
for i in list1:
    tmp=i
    if i==max1:
        tmp=tmp*2    # 错误原因：对原来列表中的值进行修改时，需要用到修改
    if i==min1:      # 对这个变量进行赋值没有用
        tmp=tmp+1

# 正确写法：通过索引修改
for i in range(n):
    if list1[i]==max1:
        list1[i]=2*list1[i]
    if list1[i]==min1:
        list1[i]=list1[i]+1
```

### Day 4 作业

```python
# 文件：作业4.1.py —— 矩阵循环嵌入的数字递增输入
# 每个数字的场宽设置，而不是单纯的空格问题，应该利用format函数补齐空格

# 文件：作业4.4（行列式每一行最大值）.py
# 矩阵的建立：利用推导式，结合循环嵌套，将输入内容全部放入行列式中
# 遍历行列式中每一行的最大值，并将每一行的值表示出来
```

---

## Day 5：字符串、元组与深层列表

### 5.1 元组

```python
# 文件：1.py
n=int(input())
tup=tuple(map(int,input().split()))
max1=max(tup); min1=min(tup)
countmax=tup.count(max1); countmin=tup.count(min1)

# 文件：2.py
# 从列表过渡到元组其实没有什么区别
# 核心的差异点：
#   1. 元组的建立和类型转化
#   2. 列表数据的统计和计算转化到元组中进行

# 文件：3.py
# 另一种思路：将两个元组进行zip处理，压缩成一个zip
# 然后遍历时分别赋值
# a,b = zip(tup1, tup2): sum1 = sum1 + a*b
```

### 5.2 元组解包与多组数据处理

```python
# 文件：6（多组数据 考了第k名的学生）.py
n,k=input().split()
list1=[]
for i in range(n):
    num,score=input().split()
    num=int(num); score=float(score)
    list1.append((num,score))
# 将二元数据编码进入一个二维行列式
# 二元数组利用二维行列式进行处理
#   输入创建：双循环（n循环+输入循环，两个变量的赋值）
#   排列：lambda函数 reverse双重控制
#   输出：双方框表示值，利用i循环
```

```python
# 文件：7（多组数据的行列式创建 排序 检索 输出）.py
# 列表综合的天花板了吧
# 要求和常用列表操作其实没有变化，只是把这些常用操作进行组合
# 列表向元组的过渡：将一组数据加入一个列表，其实就是二阶行列式
# 一组一组数据的处理：利用元组解包进行分别赋值，随后进行类型转化！
# 检索二阶行列式中的值：利用双角标即可！
# 行列式的输出：利用解包也行 print(*i)，或者表示列表中的单个元素 list1[i][j]
```

### 5.3 字符串基础

```python
# 文件：10.py —— replace替换
str1=input(); a,b=input().split()
str2=str1.replace(a,b); print(str2)

# 文件：14.py —— find查找子串
str1=input(); str2=input()
if str1.find(str2)!=-1: print(str2,"is substring of",str1)
elif str2.find(str1)!=-1: print(str1,"is substring of",str2)
else: print("No substring")

# 文件：19.py —— 回文判断（利用切片倒序）
str1=input()
restr1=str1[::-1]
if str1==restr1: print("yes")
else: print("no")
```

### 5.4 字符串分割与列表

```python
# 文件：作业5.3（最长的单词-利用分隔设置列表）.py
str1=input()
str2=str1.replace(".","")   # 字符串的修改，返回是一个新的字符串
str3=str2.split()           # 这一步输出的就是一个列表
list1=[]
for i in str3: list1.append(i)
list1.sort(key=len,reverse=True)
print(list1[0])
# 也可以利用max函数：max(list1, key=len)
```

```python
# 文件：作业5.4（单词的替换-利用分隔设置列表）.py
str1=input(); str2=" "+str1+" "
str3=" "+input()+" "; str4=" "+input()+" "
ans=str2.replace(str3,str4).strip()
print(ans)
# 在单词内部的内容并不属于字符串
# 将前后加入空格标记单词，或者直接分隔成列表
```

### Day 5 作业

```python
# 文件：作业5.1（列表多个最小值的索引输出）.py
# 前面索引值对于后面相同最小项的检索产生干扰？将这个值直接替换掉

# 文件：作业5.2（列表第一个最小值的索引输出）.py
```

---

## Day 6：字典、集合与函数初探

### 6.1 字典的两类创建模型

```python
# 文件：1（统计每个数的出现次数-两类字典的创建方式）.py
# 字典的用途：利用其算法特点，自动去除重复元素的干扰，便于统计出现次数

# 模型一：先创建空字典，利用update更新
dict1={}
for i in list1:
    dict1.update([(i,list1.count(i))])

# 模型二：利用if...else判断键是否存在
for i in list1:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1

# dict1[i]=list1.count(i) —— 前面的是key后面的是value
# 若存在可以表示获取这个dict1值，但前提是要有这个dict1值才能进行操作
# 因为当键不在字典中时，会报错 —— 是在对键值进行操作了

# 大总结：字典的两类创建模型
#   一类是数据出现次数进行利用
#       max1=max(dict1.values()) 利用这个来求最大键值
#   另一类是数据对的手动添加（或者也可以利用update），随后进行排序

# 字典的输出问题：item元组 *item=k,v，或者访问单独的键/值
```

```python
# 文件：2（有无重复学号）.py
# 利用字典来实现统计出现次数
for i in range(n):
    id=int(input())
    if id in dict1: dict1[id]+=1
    else: dict1[id]=1
    # 或者：dict1[id]=dict1.get(id,0)+1

# 判断有无重复：
if len(dict1)!=n: print(1)    # 计算字典长度
else: print(0)

# 访问字典：
for i in dict1.keys():    # 相当于利用键作为访问索引
    if dict1[i]>1:         # dict1[]来访问键对应的值
        ans=1
```

```python
# 文件：3（众数问题-统计列表和字典）.py
# 众数问题利用字典来处理比较方便，因为可以一次输出dict1的最大值
max1=max(dict1.values())
maxkey=[k for k,v in dict1.items() if v==max1]
ans=min(maxkey)
# 字典的次数问题 "数：出现次数"型的字典，还是经典的if语句
# 同时这个一定是if else结构，否则又会有干扰
```

### 6.2 成绩排序 —— 字典 vs 二维列表

```python
# 文件：4（成绩排序问题-二维列表和字典）.py
# 二维列表方式：
list1.sort(key=lambda x:(-x[1],x[0]))

# 字典方式：
for i in range(n):
    name,score=input().split()
    dict1[name]=int(score)
dict1=dict(sorted(dict1.items(),key=lambda x:(-x[1],x[0])))
# 对比：利用字典和二维列表来处理这个问题
# 字典中涉及到一个添加字典键值对的问题（区分对键值对进行处理才需要进行if判定）
# 字典排序问题：用 sorted 函数
```

### 6.3 字典综合 —— 两类模型结合

```python
# 文件：5（电讯商城的价格清单-字典的两类创建结合）.py
n=int(input())
dict1={}    # 注意字典的创建是大括号{}，做好区分！
# 否则提示list的indices(index)需要是整数，因为列表索引和利用字典的键进行索引不同
for i in range(n):
    name,price=input().split()
    price=float(price)
    if name not in dict1:
        dict1[name]=price*0.75
    else:    # 注意：又陷入了同样一个问题，两个if连续执行
        dict1[name]+=price
dict1=dict(sorted(dict1.items(),key=lambda x: x[0]))
for k,v in dict1.items():
    print(k,"{:.1f}".format(v))
# 字典的两类模型进行综合：
#   一类是字典出现次数的条件判定
#   另一类是字典二元数组的结合，直接利用dict1[]=float(price)来创建一个键值对
# 字典的输出：利用item进行访问，同时访问k,v但是输出v
```

### 6.4 集合

```python
# 文件：7（水果集合）.py
set1=set()
while True:
    fruit=input()
    if fruit=="q": break
    set1.add(fruit)    # 在if语句判定之后再进行添加，可以避免q的添加
print(sorted(set1))
# 水果集合，依据字典序进行排序
# 集合的输入、集合的输出
```

```python
# 文件：9（集合的创建和运算）.py
# 交：set1 & set2
# 并：set1 | set2
# 差：set1 - set2
```

```python
# 文件：10（列表和集合的综合使用）.py
# 列表和集合的综合使用：利用集合去掉重复的内容，然后进行集合排序
```

```python
# 文件：11（电梯运行时间-列表和集合的综合使用）.py
# 数学中的实际应用问题，列表和集合的综合问题
# 充分利用列表特性进行最大值、总人数等分析，利用集合进行去重
# 其实也可以利用列表和字典完成这些工作
```

### 6.5 函数定义初探

```python
# 文件：13（阶乘-函数定义和变量参数）.py
n=int(input())
def jc1(n):
    j=0; sum1=0    # local iterable的建立，局部变量在函数内部参与运算
    tmp=1           # 最后输出一个返回值就可以了，返回值最后在内部定义
    for i in range(n):
        j=j+1       # 全局变量可以参与函数内部的运算
        tmp=tmp*j
        sum1=sum1+tmp
    return sum1
ans=jc1(n)
print(ans)
# 如果利用定义函数：多次使用的将其弄成一个函数，再结合range(n)的循环累加
```

### Day 6 作业

```python
# 文件：作业6.2.py —— 统计字符串中字符出现次数，输出最多的
```

---

## Day 7：函数进阶与递推

### 7.1 因子之和函数

```python
# 文件：1（因子之和-函数的定义和使用）.py
n=int(input())
def sum_num(x):
    s=1
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            if i==x/i: s=s+i
            else: s=s+i+x/i
    return s
for i in range(2,n+1):
    if sum_num(i)==i: print(i)

# 第一次使用构造函数处理问题：
# 1. 从大的角度来说，是为了省一个循环来实现大的for循环嵌套
# 2. 遍历所有数时，只要满足条件就输出一个函数值
# 3. 构造函数找因数时可以简化——这一步是遍历因数
# 4. 构造函数时，传入一个形参即可，最后利用时利用括号调用即可
```

### 7.2 素数判断函数

```python
# 文件：5（哥德巴赫猜想（重要母题）-函数的定义和使用）.py
def sushu(n):
    flag=False; i=2; cnt=0
    while 2<=i<=n-1:
        if n%i==0: flag=False; break
        else: cnt=cnt+1
        i=i+1
    if cnt==n-2: flag=True
    return flag

def num_sum(n):
    for i in range(2,n):
        a=i; b=n-i
        if sushu(i) and sushu(b): break
    return a,b

# 需要在循环内部进行条件判断时，最好用i进行执行
# 如何设置检索所有情况后没有任何事情发生？
#   设置一个循环积累值，每一次不符合条件就累加
```

```python
# 文件：7（素数回文数-函数的定义和使用）.py
# 素数回文数：利用函数方便在外层循环中表示
# 否则在外层循环检索中会需要利用很长的代码来表示需要实现的条件
# 加入两个函数判断素数和回文数（利用flag），这样可以返回判定的条件

# 文件：8（合数-函数的定义和使用）.py
# 如果数字位数不确定，利用循环来依次判断每一位
# while i>0:
#     if not heshu(i%10): break
#     i=i//10
# 可以再添加以限定结束
```

### 7.3 Debug 技巧

```python
# 文件：4（pass-循环体中的debug技巧）.py
# 循环体的debug：利用print来显示每一步循环的检索值
# 错误点：最终结果输出错误，观察输出结果清单发现永远只利用了最后一次结果
# 猜测：原因在于sum1每次循环之后都得到了还原，需要在循环体的最外面设置累计值
# python中的复合运算不要大括号中括号
```

### 7.4 列表递推关系

```python
# 文件：11（求S的值-列表的递推关系）.py
list1=[0]*10000
sum1=1; list1[1]=1
for i in range(2,10000):
    list1[i]=list1[i-1]+i-1
    sum1=sum1+list1[i]
    if sum1>=5000: print(sum1); break
# 还是循环体的debug处理：找到每一个list项，还可以确定每一个sum1值的动态变化
# 递推：利用list1来确定每一项，可以通过0的空列表同时调整列表下标使全部错位
# 同时递推式必须要你提前写好前几个首项
```

```python
# 文件：13（pell数列-列表的递推和数据简化）.py
# 数列递推问题利用列表来解决：创建一个全是[0]的空值列表
# 具体递推关系利用列表中值的关系进行表示和更新
```

### 7.5 输入控制 —— EOF 处理

```python
# 文件：9（二轮复习-多种数据类型的输入方式）.py
# 输入问题的循环控制：
#   已知输入总数，当需要进行换行输入时，直接利用循环执行
#   已知输入总数，当需要进行同行输入时，直接利用 for i in input().split()
#   未知输入总数，含有一个无穷文档输入，利用后面的错误判定类型：
while True:
    try:
        n=int(input())
        print(score(n))
    except EOFError:
        break
# 利用 End of File 错误类型来跳出死循环
```

### Day 7 作业

```python
# 文件：作业7.4.py
# 在使用range函数时真的要注意范围问题
# 一开始利用长度做减法但是弄反方向
# 报错：索引越界
```

---

## Day 8：面向对象与异常处理

### 8.1 面向对象基础

```python
# 文件：1（面向对象：创建成员变量+成员方法+构造方法）.py
# 常规方式：先创建类，再逐个添加属性
class Student:
    name=None; age=None
stu1=Student()
tmp1=input().split()
stu1.name=tmp1[0]; stu1.age=int(tmp1[1])
# 但是类的设计时没有传入参数，所以没法在创建对象时直接把参数传入

# 利用构造方法创建类和对象
class Student:
    def __init__(self,name,age,chinese,math,english):
        self.name=name          # 成员变量
        self.age=age
        self.chinese=chinese
        self.math=math
        self.english=english
    def score(self):            # 成员方法
        return self.chinese+self.math+self.english

tmp1=input().split()
stu1=Student(tmp1[0],int(tmp1[1]),int(tmp1[2]),int(tmp1[3]),int(tmp1[4]))
# 基于类创建对象，利用stu1=Student()只是这里加入了参数进行赋值
# 好处就是不用写那么多行了，一次将参数全部传入

# 总结：
# 无论在哪种方式中，利用 . 来调用成员变量和传入参数
# 调用成员方法时，利用 .() 来调用成员方法和传入参数
```

### 8.2 魔术方法

```python
# 文件：4（相加和字符串的魔术方法）.py
class MyNumber:
    def __init__(self,num):
        self.num=num
    # 相加符号的魔术方法
    def __add__(self,other):
        return MyNumber(self.num+other.num)   # 返回内容的形式必须符合条件
    # 自身字符串的格式化
    def __str__(self):
        return f"{self.num}"

# 对于魔术方法的理解：
# 在"基于对象创建类中"还原出平时习以为常的python运算操作符等代码
# 例如写一个print(stu1>stu2)，系统提示typeerror:
#   ">" not supported between instances "student" and "student"
# 例如上面如果不写str格式化，系统会提示：
#   两个数字相加的结果为: <__main__.MyNumber object at 0x...>
# 因为add会返回一个MyNumber新的对象，直接打印结果并不是字符串

# 什么时候需要用到字符串魔术方法？通常是最终输出存在格式和形式的要求时
#   1. 直接打印对象时，需要str返回其一项属性值
#   2. 比如需要输出："我的名字是...，我的成绩是..."
#   3. 然后在print部分直接输出print(MyNumber)
```

```python
# 文件：5（sort与排序魔术方法）.py
class Student:
    def __init__(self,ID,C,M,E):
        self.C=C; self.M=M; self.E=E; self.ID=ID
    def score(self):
        return self.C+self.M+self.E
    # 比较大小排序的魔术方法
    def __lt__(self,other):
        if self.score()!=other.score():
            return self.score()>other.score()
        elif self.C!=other.C:
            return self.C>other.C
        else:
            return self.ID<other.ID
    # 相当于自定义一种比较排序的方法，包含三个维度

# 这个魔术方法指向的是sort函数：sort函数会默认利用less than(__lt__)实现排序
list1.sort()
```

### 8.3 继承与多态

```python
# 文件：6（鸭子类型：继承和多态）.py
class Animal:
    def __init__(self,name): self.name=name
    def speak(self): pass
    def description(self): return f"{self.name} 是一只 Animal。"

class Dog(Animal):
    def speak(self): return "Woof!"
    def description(self): return f"{self.name} 是一只 Dog。"
```

### 8.4 异常处理

```python
# 文件：7（整数相除反馈问题-异常的捕获和语法结构）.py
a=input(); b=input()
try:
    a=int(a); b=int(b)
    ans=a/b
except ValueError:
    print("错误：请输入有效的整数。")
except ZeroDivisionError:
    print("错误：除数不能为零。")
except Exception as e:
    print(f"发生了未预料的错误：{e}")
else:
    print(f"{ans:.1f}")
# 异常捕获的语法结构：
#   利用try来执行需要尝试的操作
#   注意int操作这一步也要放在try内部，因为需要考虑是否输入有效的数据类型
#   利用Exception as e这个语句，随后输出返回f的快速格式化语句
```

```python
# 文件：8（未知数据数量的输入-利用Eof错误类型跳出死循环）.py
while True:
    try:
        n=int(input())
        print(score(n))
    except EOFError:
        break
# 利用while建立死循环，用于读取多个测试点的多组测试数据
# 当输入内容终止时结束，可以用于未知数据数量的输入情形
```

```python
# 文件：9.py —— 主动引发异常
def checknum(n):
    if n>0: print("输入的数是正数")
    else: raise ValueError("错误：输入的数不是正数")
try:
    n=int(input()); checknum(n)
except ValueError as v: print(v)
except Exception as e: print(f"发生未知错误：{e}")
# 主动引发错误进行分析，except理解成当且仅当
# 设置valueerror的引发来输出一个自己想要的异常提示
```

```python
# 文件：10.py —— assert断言
def checknum():
    assert a==b, "错误：输入的两个整数不相等"
# 不知道为什么，最后必须去掉checknum前面的print
```

### 8.5 数学模块

```python
# 文件：12（引入数学模块）.py
import math
r=float(input())
a=math.pi; s=a*r*r
print(f"{s:.2f}")
```

### Day 8 综合应用：奖学金系统

```python
# 文件：3（西部奖学金申请-面向对象+字典+列表大综合的应用）.py
class Student:
    def __init__(self,name,scoret,scorec,offi,wes,thes):
        self.name=name
        self.scoret=scoret
        # ...
    def scholarship(self):
        sum1=0
        if self.scoret>80 and self.thes>=1: sum1=sum1+8000
        # ... 多项条件累加
        return sum1

n=int(input())
dict1={}; list2=[]
for i in range(n):
    tmp=input().split()
    stu=Student(tmp[0],int(tmp[1]),int(tmp[2]),tmp[3],tmp[4],int(tmp[5]))
    dict1.update({stu.name:stu.scholarship()})
    list2.append(stu.scholarship())
max1=max(list2)
```

---

## 附录：目录文件夹中的包结构

```
目录文件夹/my_package/
├── __init__.py
├── model.py
├── my_module.py
└── 主执行模块.py
```

---

*以上笔记整理自我2025年暑假Python课程的代码注释，保持了当初学习的原汁原味。回顾这些笔记，能看到自己从print都不会写，到能完成面向对象+异常处理的完整程序，每一步的困惑和顿悟都记录在案。*
