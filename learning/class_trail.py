class Animal:
    def speak(self):
        print("animal", self)


class Dog(Animal):
    # 例子：重写父类中的方法，并且还使用了 super() 调用父类方法
    def speak(self):
        print("dog setup", self)
        super().speak()

dog = Dog()
dog.speak()

# 是同一个 self 实体！！super.() 的语法糖

# 输出结果：
# dog setup <__main__.Dog object at 0x7aa8d2ffefc0>
# animal < __main__.Dog object at 0x7aa8d2ffefc0>