class Animal:
    def speak(self):
        print("animal", self)


class Dog(Animal):
    # 例子：重写父类中的方法，并且还使用了 super() 调用父类方法
    def speak(self):
        print("dog setup", self)
        super().speak()

dog = Dog()
dog.speak()  # dog.speak() 语法糖 = Dog.speak(self)
# super.speak() 语法糖 = Animal.speak(self)  是同一个 self 实体！！！

# 输出结果：
# dog setup <__main__.Dog object at 0x7aa8d2ffefc0>
# animal < __main__.Dog object at 0x7aa8d2ffefc0>

# 这是一个关于 --amend 的测试：在已经 commit 并且 push 到远端仓库之后
# 如果继续使用 --amend，这个 --amend 的 commit 会在本地 push 之前的 commit 上产生分支，造成本地与远程仓库的分支差异