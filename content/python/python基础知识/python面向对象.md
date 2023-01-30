---
title: 类
date: 2022-12-6
lastmod: '2022-12-064T16:44:38+08:00'
summary: 类的介绍
weight: 56
toc: true
type: book
---

```python
class Circle:#类一般大写开头
    parents='two-dim' # 属于类的数据成员，公有成员
    __son='none'   # 属于类的数据成员，私有成员 
    
    def __init__(self,c,r,t): #构造方法，特殊方法，构造属于对象的数据成员，一般是在该函数中构造，也可以在其他方法中构造
        self.center=c       #self代表对象，通过 self.属性名 的形式来构建属性(属于对象的数据成员)并把参数的值赋给属性
        self.radius=r       #构造了两个属于对象的数据成员，并且都是公有的。
        self.__test=t       #t必须在创建对象时给出值，但是默认看不到这个属性，因为这是个私有成员，不能通过直接通过对象查看。
        Circle.parents='two-dim' #通过类名加成员名的方式访问类的数据成员
        
    def add_attr(self,dim=1):#通过调用这个实例方法可以实现为类添加对象成员但不可添加类成员
        self.__distance=sum([i**2 for i in self.center])**(1/2)#私有对象成员
        self.dimen=dim
        
    def __private_method(self):#私有方法，实例方法
        '''
        私有方法，不可使用对象直接调用，主要是供该对象类的其他方法使用
        '''
        return (self.__distance,Circle.__son)# 可以使用类和对象成员
    
    def public_method(self): # 公有方法，实例方法
        '''
        公有方法可以调用私有方法，也可以访问类成员和对象成员，公有方法可以被对象直接调用
        '''
        return self.__private_method()+(self.__distance,Circle.__son)
    
    @classmethod              #修饰器，声明类方法
    def classShowTotal(cls):  #类方法,一般以cls代表类，可以在调用时不传递cls参数
        print(cls.__son)

    @staticmethod             #修饰器，声明静态方法
    def staticShowTotal():    #静态方法,可以在调用时不传递参数
        print(Circle.__son)   
```

成员方法|适用成员|是否可调用
:-:|:-:|:-:
类的方法|                                            
类方法|类成员|可以通过类和对象调用，调用形式一样
静态方法|类成员|可以通过类和对象调用，调用形式一样
实例方法|
私有方法|类成员和对象成员|可以通过类利用特殊方法调用
公有方法|类成员和对象成员|可以通过类（A.method(object)）和对象调用，通过类时要显式传递self（对象）参数。
抽象方法|类成员和对象成员|可以通过类和对象调用，通过类时要显式传递self（对象）参数。
特殊方法|类成员和对象成员|可以通过类和对象调用，通过类时要显式传递self（对象）参数。

数据成员|是否可调用
:-:|:-:
公有成员|可以调用
\_xxx|受保护成员；
\_\_xxx\_\_|系统定义的特殊成员
\_\_xxx|私有成员，只有类对象自己能访问，子类对象不能直接访问到这个成员，但在对象外部可以通过“对象名.\_类名\_\_xxx”这样的特殊方式来访问。<br/>或者如果有公用方法中可以返回私有成员，从而可以通过调用该函数而获得私有成员。

注意：在python中并没有严格的私有成员

数据成员|调用形式
:-:|:-:
类成员|通过类或对象调用
对象成员|只能通过对象调用

私有和公有是能不能调用的问题，类和对象是通过谁调用的问题

实例方法和类方法是能够用类成员还是对象成员的问题。

## 类的简介

面向对象程序设计（Object Oriented Programming，OOP）的思想主要针对大型软件设计而提出，使得软件设计更加灵活，能够很好地支持代码复用和设计复用，代码具有更好的可读性和可扩展性，大幅度降低了软件开发的难度。

面向对象程序设计的一个关键性观念是将数据以及对数据的操作封装在一起，组成一个相互依存、不可分割的整体（对象），不同对象之间通过消息机制来通信或者同步。对于相同类型的对象（instance）进行分类、抽象后，得出共同的特征而形成了类（class），面向对象程序设计的关键就是如何合理地定义这些类并且组织多个类之间的关系。

Python是面向对象的解释型高级动态编程语言，完全支持面向对象的基本功能，如封装、继承、多态以及对基类方法的覆盖或重写。创建类时用变量形式表示对象特征的成员称为数据成员（attribute），用函数形式表示对象行为的成员称为成员方法（method），数据成员和成员方法统称为类的成员。

定义了类之后，就可以用来实例化对象，并通过“对象名.成员”的方式来访问其中的数据成员或成员方法。

在Python中，可以使用内置函数isinstance()来测试一个对象是否为某个类的实例，或者使用内置函数type()查看对象类型。

## 类的成员

创建类时用变量形式表示对象特征的成员称为数据成员（attribute），用函数形式表示对象行为的成员称为成员方法（method），数据成员和成员方法统称为类的成员。

### 数据成员

私有成员在类的外部不能直接访问，一般是在类的内部进行访问和操作，或者在类的外部通过调用对象的公有成员方法来访问，而公有成员是可以公开使用的，既可以在类的内部进行访问，也可以在外部程序中使用。

从形式上看，在定义类的成员时，如果成员名以两个下划线开头但是不以两个下划线结束则表示是私有成员，否则就不是私有成员。

Python并没有对私有成员提供严格的访问保护机制，通过一种特殊方式“对象名.\_类名\_\_xxx”也可以在外部程序中访问私有成员，但这会破坏类的封装性，不建议这样做。

数据成员可以大致分为两类：属于对象的数据成员和属于类的数据成员。属于对象的数据成员一般在构造方法\_\_init\_\_()中定义，当然也可以在其他成员方法中定义，在定义和在实例方法中访问数据成员时**以self作为前缀**，同一个类的不同对象（实例）的数据成员之间互不影响；**属于类的数据成员是该类所有对象共享的，不属于任何一个对象，在定义类时这类数据成员一般不在任何一个成员方法的定义中。**

在主程序中或类的外部，对象数据成员属于实例(对象)，只能通过对象名访问；而类数据成员属于类，可以通过类名或对象名访问。

### 成员方法

方法一般指与特定实例绑定的函数，通过对象调用方法时，**对象本身将被作为第一个参数自动传递过去**，普通函数并不具备这个特点。

Python类的成员方法大致可以分为公有方法、私有方法、静态方法、类方法和抽象方法这几种类型。

公有方法、私有方法和抽象方法一般是指属于对象的实例方法，私有方法的名字以两个开始，而抽象方法一般定义在抽象类中并且要求派生类必须重新实现。每个对象都有自己的公有方法和私有方法，在这两类方法中都可以访问属于类和对象的成员。公有方法通过对象名直接调用，私有方法不能通过对象名直接调用，只能在其他实例方法中通过前缀self进行调用或在外部通过特殊的形式来调用。

所有实例方法（包括公有方法、私有方法、抽象方法和某些特殊方法）都必须至少有一个名为self的参数，并且必须是方法的第一个形参（如果有多个形参的话），self参数代表当前对象。

在实例方法中访问实例成员时需要以self为前缀，但在外部通过对象名调用对象方法时并不需要传递这个参数。

如果在外部通过类名调用属于对象的公有方法，需要显式为该方法的self参数传递一个对象名，用来明确指定访问哪个对象的成员。

静态方法和类方法都可以通过类名和对象名调用，但不能直接访问属于对象的成员，只能访问属于类的成员。

静态方法和类方法不属于任何实例，不会绑定到任何实例，当然也不依赖于任何实例的状态，与实例方法相比能够减少很多开销。

类方法一般以cls作为类方法的第一个参数表示该类自身，在调用类方法时不需要为该参数传递值，静态方法则可以不接收任何参数

抽象方法一般在抽象类中定义，并且要求在派生类中必须重新实现，否则不允许派生类创建实例。

```python
## 利用类数据成员的共享性，可以实时获得该类的对象数量，并且可以控制该类可以创建的对象最大数量。例如：
class Demo(object):
    total = 0
    def __new__(cls, *args, **kwargs):           #该方法在__init__()之前被调用
        if cls.total >= 3:                       #最多允许创建3个对象
            raise Exception('最多只能创建3个对象')
        else:
            return object.__new__(cls)
    def __init__(self):
        Demo.total = Demo.total + 1
t1 = Demo()
t1
t2 = Demo()
t3 = Demo()
t4 = Demo()#不能创建第四个对象

```

    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    <ipython-input-40-ad753a930be3> in <module>
         13 t2 = Demo()
         14 t3 = Demo()
    ---> 15 t4 = Demo()

    <ipython-input-40-ad753a930be3> in __new__(cls, *args, **kwargs)
          4     def __new__(cls, *args, **kwargs):           #该方法在__init__()之前被调用
          5         if cls.total >= 3:                       #最多允许创建3个对象
    ----> 6             raise Exception('最多只能创建3个对象')
          7         else:
          8             return object.__new__(cls)

    Exception: 最多只能创建3个对象

```python
import abc

class Foo(metaclass=abc.ABCMeta):  #抽象类
    def f1(self):                  #普通实例方法
        print(123)

    def f2(self):                  #普通实例方法
        print(456)

    @abc.abstractmethod            #抽象方法
    def f3(self):
        raise Exception('You musr reimplement this method.')

class Bar(Foo):
    def f3(self):                  #必须重新实现基类中的抽象方法
        print(33333)

b = Bar()
b.f3()
```

    33333

```python
class Root:
    __total = 0
    def __init__(self, v):    #构造方法
        self.__value = v
        Root.__total += 1

    def show(self):           #普通实例方法
        print('self.__value:', self.__value)
        print('Root.__total:', Root.__total)

    @classmethod              #修饰器，声明类方法
    def classShowTotal(cls):  #类方法
        print(cls.__total)

    @staticmethod             #修饰器，声明静态方法
    def staticShowTotal():    #静态方法
        print(Root.__total)

```

## 属性

从外部来看函数的数据成员我们可以将其看成类的属性，对于这些属性，我们是否可以读取，是否可以修改，是否可以删除。这就涉及到property函数。如果没有这个函数，可以做任何操作，但是如果有，就可以对我们的操作产生某些限制。

```python
##可读
class Test:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):               #只读，无法修改和删除
        return self.__value

```

```python
## 可读可写
class Test:
    def __init__(self, value):
        self.__value = value	

    def __get(self):
        return self.__value

    def __set(self, v):
        self.__value = v
    value = property(__get, __set)

    def show(self):
        print(self.__value)

```

```python
## 可读、可修改、可删除的属性。
class Test:
    def __init__(self, value):
        self.__value = value

    def __get(self):
        return self.__value

    def __set(self, v):
        self.__value = v

    def __del(self):
        del self.__value

    value = property(__get, __set, __del)

    def show(self):
        print(self.__value)

```

## 类与对象的动态性、混入机制

在Python中比较特殊的是，可以动态地为自定义类和对象增加或删除成员，这一点是和很多面向对象程序设计语言不同的，也是Python动态类型特点的一种重要体现。

Python类型的动态性使得我们可以动态为自定义类及其对象增加新的属性和行为，俗称混入（mixin）机制，这在大型项目开发中会非常方便和实用。

例如系统中的所有用户分类非常复杂，不同用户组具有不同的行为和权限，并且可能会经常改变。这时候我们可以独立地定义一些行为，然后根据需要来为不同的用户设置相应的行为能力。

```python
class Car:
    price = 100000                     #定义类属性
    def __init__(self, c):
        self.color = c                 #定义实例属性

car1 = Car("Red")                      #实例化对象
car2 = Car("Blue")
print(car1.color, Car.price)           #查看实例属性和类属性的值
Car.price = 110000                     #修改类属性
Car.name = 'QQ'                        #动态增加类属性
car1.color = "Yellow"                  #修改实例属性
print(car2.color, Car.price, Car.name)
print(car1.color, Car.price, Car.name)

```

    Red 100000
    Blue 110000 QQ
    Yellow 110000 QQ

```python
import types#增加成员方法要用到

def setSpeed(self, s): 
    self.speed = s

car1.setSpeed = types.MethodType(setSpeed, car1) #动态增加成员方法，注意使用types.MethodType方法
car1.setSpeed(50)                                #调用成员方法
print(car1.speed)

```

    50

## python的封装，继承和多态

继承是用来实现代码复用和设计复用的机制，是面向对象程序设计的重要特性之一。设计一个新类时，如果可以继承一个已有的设计良好的类然后进行二次开发，无疑会大幅度减少开发工作量。

在继承关系中，已有的、设计好的类称为父类或基类，新设计的类称为子类或派生类。派生类可以继承父类的公有成员，但是不能继承其私有成员。如果需要在派生类中调用基类的方法，可以使用内置函数super()或者通过“基类名.方法名()”的方式来实现这一目的。

Python支持多继承，如果父类中有相同的方法名，而在子类中使用时没有指定父类名，则Python解释器将从左向右按顺序进行搜索。

```python
## -*- coding:utf-8 -*-
## Filename: AccessMembersOfBaseclass.py
## --------------------
## Function description:
## Show how to access method and data of parent class
## --------------------
## Author: 董付国
## Email: dongfuguo2005@126.com
##--------------------
## Date: 2014-11-27,Updated on 2017-4-4
## --------------------

class Person(object):
    def __init__(self, name = '', age = 20, sex = 'man'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)
        
    def setName(self, name):
        assert isinstance(name, str), 'name must be string.'
        self.__name = name
        
    def setAge(self, age):
        assert isinstance(age, int), 'age must be integer.'
        self.__age = age
        
    def setSex(self, sex):
        assert sex in ('man', 'woman'), 'sex must be "man" or "woman"'
        self.__sex = sex
        
    def show(self):
        print('Name:', self.__name)
        print('Age:', self.__age)
        print('Sex:', self.__sex)

class Teacher(Person):
    def __init__(self, name='', age = 30, sex = 'man', department = 'Computer'):
        super(Teacher, self).__init__(name, age, sex)
        # 也可以使用下面的形式对基类数据成员进行初始化
        #Person.__init__(self, name, age, sex)
        self.setDepartment(department)
        
    def setDepartment(self, department):        
        assert isinstance(department, str), 'department must be a string.'
        self.__department = department
        
    def show(self):
        super(Teacher, self).show()
        print('Department:', self.__department)

if __name__ =='__main__':
    print('='*30)
    zhangsan = Person('Zhang San', 19, 'man')
    zhangsan.show()

    print('='*30)
    lisi = Teacher('Li Si',32, 'man', 'Math')
    lisi.show()
    print('='*30)
    lisi.setAge(40)
    lisi.show()
```

    ==============================
    Name: Zhang San
    Age: 19
    Sex: man
    ==============================
    Name: Li Si
    Age: 32
    Sex: man
    Department: Math
    ==============================
    Name: Li Si
    Age: 40
    Sex: man
    Department: Math

所谓多态（polymorphism），是指基类的同一个方法在不同派生类对象中具有不同的表现和行为。派生类继承了基类行为和属性之后，还会增加某些特定的行为和属性，同时还可能会对继承来的某些行为进行一定的改变，这都是多态的表现形式。

Python大多数运算符可以作用于多种不同类型的操作数，并且对于不同类型的操作数往往有不同的表现，这本身就是多态，是通过特殊方法与运算符重载实现的。

```python
>>> class Animal(object):      #定义基类
    def show(self):
        print('I am an animal.')
>>> class Cat(Animal):         #派生类，覆盖了基类的show()方法
    def show(self):
        print('I am a cat.')
>>> class Dog(Animal):         #派生类
    def show(self):
        print('I am a dog.')
>>> class Tiger(Animal):       #派生类
    def show(self):
        print('I am a tiger.')
>>> class Test(Animal):        #派生类，没有覆盖基类的show()方法
    pass
>>> x = [item() for item in (Animal, Cat, Dog, Tiger, Test)]
>>> for item in x:        #遍历基类和派生类对象并调用show()方法
    item.show()

```

    I am an animal.
    I am a cat.
    I am a dog.
    I am a tiger.
    I am an animal.

### 特殊方法和运算符重载

Python类有大量的特殊方法，其中比较常见的是构造函数和析构函数，除此之外，Python还支持大量的特殊方法，运算符重载就是通过重写特殊方法实现的。

Python中类的构造函数是\_\_init\_\_()，一般用来为数据成员设置初值或进行其他必要的初始化工作，在创建对象时被自动调用和执行。如果用户没有设计构造函数，Python将提供一个默认的构造函数用来进行必要的初始化工作。

Python中类的析构函数是\_\_del\_\_()，一般用来释放对象占用的资源，在Python删除对象和收回对象空间时被自动调用和执行。如果用户没有编写析构函数，Python将提供一个默认的析构函数进行必要的清理工作。

方法|	功能说明
:-|:-
\_\_new\_\_()	|类的静态方法，用于确定是否要创建对象
\_\_init\_\_()	|构造方法，创建对象时自动调用
\_\_del\_\_()	|析构方法，释放对象时自动调用
\_\_add\_\_()	|+
\_\_sub\_\_()	|-
\_\_mul\_\_()	|\*
\_\_truediv\_\_()	|/
\_\_floordiv\_\_()	|//
\_\_mod\_\_()	|\%
\_\_pow\_\_()	|\*\*
\_\_eq\_\_()、 \_\_ne\_\_()、<br/>\_\_lt\_\_()、 \_\_le\_\_()、<br/>\_\_gt\_\_()、 \_\_ge\_\_()|	==、 \!=、<br/>\<、 \<=、<br/> \>、 \>=
\_\_lshift\_\_()、\_\_rshift\_\_()|	\<\<、\>\>
\_\_and\_\_()、\_\_or\_\_()、\_\_invert\_\_()、\_\_xor\_\_()|	\&、\|、\~、\^
\_\_iadd\_\_()、\_\_isub\_\_()|	+=、-=，很多其他运算符也有与之对应的复合赋值运算符
\_\_pos\_\_()	|一元运算符+，正号
\_\_neg\_\_()	|一元运算符-，负号
\_\_contains\_\_ ()	|与成员测试运算符in对应
\_\_radd\_\_()、\_\_rsub\_\_	|反射加法、反射减法，一般与普通加法和减法具有相同的功能，但操作数的位置或顺序相反，很多其他运算符也有与之对应的反射运算符
\_\_abs\_\_()	|与内置函数abs()对应
\_\_bool\_\_()	|与内置函数bool()对应，要求该方法必须返回True或False
\_\_bytes\_\_()	|与内置函数bytes()对应
\_\_complex\_\_()	|与内置函数complex()对应，要求该方法必须返回复数
\_\_dir\_\_()	|与内置函数dir()对应
\_\_divmod\_\_()	|与内置函数divmod()对应
\_\_float\_\_()	|与内置函数float()对应，要求该该方法必须返回实数
\_\_hash\_\_()	|与内置函数hash()对应
\_\_int\_\_()	|与内置函数int()对应，要求该方法必须返回整数
\_\_len\_\_()	|与内置函数len()对应
\_\_next\_\_()	|与内置函数next()对应
\_\_reduce\_\_()	|提供对reduce()函数的支持
\_\_reversed\_\_()	|与内置函数reversed()对应
\_\_round\_\_()	|对内置函数round()对应
\_\_str\_\_()	|与内置函数str()对应，要求该方法必须返回str类型的数据
\_\_repr\_\_()	|打印、转换，要求该方法必须返回str类型的数据
\_\_getitem\_\_()	|按照索引获取值
\_\_setitem\_\_()	|按照索引赋值
\_\_delattr\_\_()	|删除对象的指定属性
\_\_getattr\_\_()	|获取对象指定属性的值，对应成员访问运算符“.”
\_\_getattribute\_\_()	|获取对象指定属性的值，如果同时定义了该方法与\_\_getattr\_\_()，那么\_\_getattr\_\_()将不会被调用，除非\_\_getattribute\_\_()中显式调用\_\_getattr\_\_()或者抛出AttributeError异常
\_\_setattr\_\_()	|设置对象指定属性的值
\_\_base\_\_	|该类的基类
\_\_class\_\_	|返回对象所属的类
\_\_dict\_\_	|对象所包含的属性与值的字典
\_\_subclasses\_\_()	|返回该类的所有子类
\_\_call\_\_()	|包含该特殊方法的类的实例可以像函数一样调用
\_\_get\_\_()<br/>	\_\_set\_\_()<br/> \_\_delete\_\_()<br/>|定义了这三个特殊方法中任何一个的类称作描述符（descriptor），描述符对象一般作为其他类的属性来使用，这三个方法分别在获取属性、修改属性值或删除属性时被调用

```python
class myDeque:
    #构造方法，默认队列大小为10
    def __init__(self, iterable=None,maxlen = 10):
        if iterable==None:
            self._content = []
            self._current = 0
        else:
            self._content = list(iterable)
            self._current = len(iterable)
        self._size = maxlen
        if self._size < self._current:
            self._size = self._current

    #析构方法
    def __del__(self):
        del self._content

    #修改队列大小
    def setSize(self, size):
        if size < self._current:
            #如果缩小队列，需要同时删除后面的元素
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

    #在右侧入队
    def appendRight(self, v):
        if self._current < self._size:
            self._content.append(v)
            self._current = self._current + 1
        else:
            print('The queue is full')

    #在左侧入队
    def appendLeft(self, v):
        if self._current < self._size:
            self._content.insert(0, v)
            self._current = self._current + 1
        else:
            print('The queue is full')

    #在左侧出队
    def popLeft(self):
        if self._content:
            self._current = self._current - 1
            return self._content.pop(0)
        else:
            print('The queue is empty')

    #在右侧出队
    def popRight(self):
        if self._content:
            self._current = self._current - 1
            return self._content.pop()
        else:
            print('The queue is empty')

    #循环移位
    def rotate(self, k):
        if abs(k) > self._current:
            print('k must <= '+str(self._current))
            return
        self._content = self._content[-k:] + self._content[:-k]

    #元素翻转
    def reverse(self):
        self._content = self._content[::-1]

    #显示当前队列中元素个数
    def __len__(self):
        return self._current

    #使用print()打印对象时，显示当前队列中的元素
    def __str__(self):
        return 'myDeque(' + str(self._content) + ', maxlen='+ str(self._size) + ')'

    #直接对象名当做表达式时，显示当前队列中的元素
    __repr__ = __str__

    #队列置空
    def clear(self):
        self._content = []
        self._current = 0

    #测试队列是否为空
    def isEmpty(self):
        return not self._content

    #测试队列是否已满
    def isFull(self):
        return self._current == self._size

if __name__ == '__main__':
    print('Please use me as a module.')

```

    Please use me as a module.

```python
'''
Author: 董付国
部分成果：《Python程序设计基础》、《Python程序设计（第2版）》
          《Python可以这样学》
微信公众号：Python小屋，关注人数12000人，分享文章近500篇
email: dongfuguo2005@126.com
Date: 2014-11-10, Updated on 2017-12-8
'''

class Stack:
    def __init__(self, size = 10):
        '''创建栈对象并进行初始化，默认栈大小为10'''
        # 使用列表存放栈的元素
        self._content = []
        # 初始栈大小
        self._size = size
        # 栈中元素个数初始化为0
        self._current = 0
        
    def empty(self):
        '''清空栈'''
        self._content = []
        self._current = 0
        
    def isEmpty(self):
        '''测试栈是否为空'''
        return not self._content

    def setSize(self, size):
        '''调整栈的大小，可以增大或缩小栈空间'''
        # 如果缩小空间时指定的新大小，小于已有元素个数
        # 则删除指定大小之后的已有元素
        if size < self._current:
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size
    
    def isFull(self):
        '''测试栈是否已满'''
        return self._current == self._size
        
    def push(self, v):
        '''将新元素入栈'''
        # 模拟入栈，需要先测试栈是否已满
        if self._current < self._size:
            self._content.append(v)
            # 栈中元素个数加1
            self._current = self._current+1
        else:
            print('Stack Full!')

    def __str__(self):
        return str(self._content)

    __repr__ = __str__
            
    def pop(self):
        '''将栈顶元素出栈'''
        # 模拟出栈，需要先测试栈是否为空
        if self._content:
            # 栈中元素个数减1
            self._current = self._current-1
            return self._content.pop()
        else:
            print('Stack is empty!')
            
    def show(self):
        '''显示当前栈对象中的元素'''
        print(self._content)

    def showRemainderSpace(self):
        '''显示栈对象剩余空间大小'''
        print('Stack can still PUSH ', self._size-self._current, ' elements.')

if __name__ != '__main__':
    s = '''本模块由董付国编写，仅供学习和参考，
更多资源请关注微信公众号“Python小屋”
或参照《Python程序设计基础》、
      《Python程序设计（第2版）》、
      《Python可以这样学》、《Python程序设计开发宝典》系列图书
或与作者邮箱dongfuguo2005@126.com联系
使用方法：
        from stackDfg import Stack
        s = Stack()
        然后通过dir(s)命令查看详细用法
        并使用help(s.push)之类的命令查看具体用法'''
    print(s)
```

```python

```
