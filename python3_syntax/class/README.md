# class
## 1、类的继承
实现代码的复用

### 父类和子类的交互方式
* 子类上的动作完全等同于父类上的动作
* 子类上的动作完全覆盖了父类上的动作
* 子类上的动作部分替换了父类上的动作

### 隐式继承
子类使用父类的方法

#### code
```python
class Parent:
    def inplicit(self):
        print("PARENT implicit()");

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.inplicit()
son.inplicit()
```
#### 结果
```
PARENT implicit()
PARENT implicit()
```
### 显示覆盖
子类方法与父类方法有不同的行为

#### code
```python
class Parent:
    def overrideFunc(self):
        print("PARENT overrideFunc()")

class Child(Parent):
    def overrideFunc(self):
        print("CHILD overrideFunc()")

dad = Parent()
son = Child()

dad.overrideFunc()
son.overrideFunc()
```

#### 结果
```
PARENT overrideFunc()
CHILD overrideFunc()
```

### 成员变量的继承
#### 子类__init__方法空的情况
##### code
```python
class Parent:
    def __init__(self):
        self.member1 = 10
        self.member2 = "hello"

class Child(Parent):
    def __init__(self):
        pass

son = Child()
print(son.member1)
print(son.member2)
```

##### 结果
```
Traceback (most recent call last):
  File "C:/Users/zhangtianyu/PycharmProjects/learn_python_the_hard_way/member_inheritance.py", line 11, in <module>
    print(son.member1)
AttributeError: 'Child' object has no attribute 'member1'
```
#### 子类__init__方法中初始化父类的情况
##### code
```python
class Parent:
    def __init__(self):
        self.member1 = 10
        self.member2 = "hello"

class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()

son = Child()
print(son.member1)
print(son.member2)
```

##### 结果
```
10
hello
```
### super()
在子类中调用父类的方法,super有两个参数，第一个是子类，第二个参数是self

#### code
```python
class Parent:
    def __init__(self):
        self.member1 = 10
        self.member2 = "hello"

class Child(Parent):
    def __init__(self):
        super(Child, self).__init__()
```
### 多重继承
能避则避吧
