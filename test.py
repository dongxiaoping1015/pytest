#coding:utf8
# s = 'abcdefghijklmn'
#
# for(index,char) in enumerate(s):
#     print index
#     print char

# ta = [1,2,3]
# tb = [9,8,7]
# # tc = ['a','b','c']
# # for (a,b,c) in zip(ta,tb,tc):
# #     print(a,b,c)
#
# zipped = zip(ta,tb)
# print(zipped)
#
# na, nb = zip(*zipped)
# print(na,nb)
#
# for line in open('test.txt'):
#     print line

# def gen():
#     a = 100
#     yield a
#     a = a * 8
#     yield a
#     yield 1000
#
# for i in gen():
#     print i

# def gen():
#     for i in range(4):
#         yield i

# g = (x for x in range(4))
#
# for i in g:
#     print i

# l = []
# for x in range(10):
#     l.append(x**2)

# l = [x**2 for x in range(10)]
#
# print l

# func = lambda x,y: x + y
# print func(3,4)
#
# def test(f, a, b):
#     print 'test'
#     print f(a,b)
#
# test(func,3,5)
#
# test((lambda x,y:x**2 + y), 6,9)

# re = map((lambda x: x+3),[1,3,5,6])
# re = map((lambda x,y:x + y),[1,2,3],[6,7,8])
# print re

# def func(a):
#     if a > 100:
#         return True
#     else:
#         return False
#
# print filter(func,[10,56,101,500])

# print reduce((lambda x,y: x+y),[1,2,3,4,5])

# re = iter(range(5))
# try:
#     for i in range(100):
#         print re.next()
# except StopIteration:
#     print 'here is end',i
# print 'hahahaha'

# L1 = [1,2,3]
# L2 = L1
# L1 = 1
#
# print L1
# print L2

# def f(x):
#     x = 100
#     print x
#
# a = 1
# f(a)
# print a

# def f(x):
#     x[0] = 100
#     print x
#
# a = [1,2,3]
# f(a)
# print a

# class SampleMore(object):
#     def __call__(self, a):
#         return  a + 5
#
# add = SampleMore()
# print(add(2))
# a = map(add, [2,4,5])
# print (a)

# f = open("new.txt", 'w')
# print(f.closed)
# f.write('ni hao')
# f.close()
# print(f.closed)

# with open("new.txt", 'w') as f:
#     print(f.closed)
#     f.write('nihaoma')
# print(f.closed)

#自定义上下文管理器
# class VOW(object):
#     def __init__(self, text):
#         self.text = text
#     def __enter__(self):
#         self.text = "I say:" + self.text
#         return  self
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         self.text = self.text + '!'
#
# with VOW("I'm fine") as myvow:
#     print(myvow.text)
#
# print(myvow.text)

#对象的属性
#属性的__dict__系统
# class bird(object):
#     feather = True
# class chicken(bird):
#     fly = False
#     def __init__(self, age):
#         self.age = age
# summer = chicken(2)
# print(bird.__dict__)
# print(chicken.__dict__)
# print(summer.__dict__)
# #两种属性修改方法
# summer.__dict__['age'] = 3
# print(summer.__dict__['age'])
# summer.age = 5
# print(summer.age)

#特性  使用内置函数property()来创建 property()最多可以加载四个参数。前三个参数为函数，分别用于处理查询特性、修改特性、删除特性。最后一个参数为特性的文档，可以为一个字符串，起说明作用。
# class bird(object):
#     feather = True
# class chicken(bird):
#     fly = False
#     def __init__(self, age):
#         self.age = age
#     def getAdult(self):
#         if self.age > 1.0: return True
#         else:return  False
#     adult = property(getAdult)
#
# summer = chicken(2)
# print(summer.adult)
# summer.age = 0.5
# print(summer.adult)

# class num(object):
#     def __init__(self, value):
#         self.value = value
#     def getNeg(self):
#         return -self.value
#     def setNeg(self, value):
#         self.value = -value
#     def delNeg(self):
#         print('value also deleted')
#         del self.value
#     neg = property(getNeg, setNeg, delNeg, "I'm negative")
#
# x = num(1.1)
# print(x.neg)
# x.neg = -22
# print(x.value)
# print(num.neg.__doc__)
# del x.neg
"""property()最多可以加载四个参数。
前三个参数为函数，分别用于处理查询特性、修改特性、删除特性。
最后一个参数为特性的文档，可以为一个字符串，起说明作用。"""

#闭包
# def line_conf():
#     def line(x):
#         return 2*x+1
#     return  line
# my_line = line_conf()
# print(my_line(5))
"""
一个函数和它的环境变量合在一起，
就构成了一个闭包(closure)。
在Python中，所谓的闭包是一个包含有环境变量取值的函数对象。
环境变量取值被保存在函数对象的__closure__属性中。
比如下面的代码"""
# def line_conf():
#     b = 15
#     def line(x):
#         return 2*x+b
#     return  line
# b = 5
# my_line = line_conf()
# # print(my_line(5))
# print(my_line.__closure__)
# print(my_line.__closure__[0].cell_contents)
"""d__closure__里包含了一个元组(tuple)。
这个元组中的每个元素是cell类型的对象。
我们看到第一个cell包含的就是整数15，
也就是我们创建闭包时的环境变量b的取值。"""

# def line_conf(a, b):
#     def line(x):
#         return a*x + b
#     return line
# line1 = line_conf(1, 1)
# line2 = line_conf(4, 5)
# print(line1(5), line2(5))
"""这个例子中，函数line与环境变量a,b构成闭包。
在创建闭包的时候，我们通过line_conf 的参数a,b说明了这两个环境变量的取值，
这样，我们就确定了函数的最终形式(y = x + 1和y = 4x + 5)。
我们只需要变换参数a,b，就可以获得不同的直线表达函数。
由此，我们可以看到，闭包也具有提高代码可复用性的作用。

如果没有闭包，我们需要每次创建直线函数的时候同时说明a,b,x。
这样，我们就需要更多的参数传递，也减少了代码的可移植性。
利用闭包，我们实际上创建了泛函。line函数定义一种广泛意义的函数。
这个函数的一些方面已经确定(必须是直线)，但另一些方面(比如a和b参数待定)。
随后，我们根据line_conf传递来的参数，通过闭包的形式，将最终函数确定下来。"""

#装饰器   装饰器(decorator)是一种高级Python语法。装饰器可以对一个函数、方法或者类进行加工。

#装饰函数和方法

# def square_sum(a, b):
#     return a**2 + b**2
# def square_diff(a, b):
#     return a**2 - b**2
# print(square_sum(3, 4))
# print(square_diff(3, 4))

#改写上面例子，增加其他功能，例如打印输入
# def square_sum(a, b):
#     print("input:", a, b)
#     return a**2 + b**2
# def square_diff(a, b):
#     print("input:", a, b)
#     return a**2 - b**2
# print(square_sum(3, 4))
# print(square_diff(3, 4))
#下面用装饰器实现上述修改
# def decorator(F):
#     def new_F(a, b):
#         print("input", a, b)
#         return F(a, b)
#     return new_F
#
# @decorator
# def square_sum(a, b):
#     return a**2 + b**2
#
# @decorator
# def square_diff(a, b):
#     return a**2 - b**2
#
# print(square_sum(3, 4))
# print(square_diff(3, 4))
"""定义好装饰器后，我们就可以通过@语法使用了。
在函数square_sum和square_diff定义之前调用@decorator，
我们实际上将square_sum或square_diff传递给decorator，
并将decorator返回的新的可调用对象赋给原来的函数名(square_sum或square_diff)。
所以，当我们调用square_sum(3, 4)的时候，就相当于：
square_sum = decorator(square_sum)
square_sum(3, 4)"""

"""从本质上，装饰器起到的就是这样一个
重新指向变量名的作用(name binding)，
让同一个变量名指向一个新返回的可调用对象，
从而达到修改可调用对象的目的。"""

#含参的装饰器

"""在上面的装饰器调用中，比如@decorator，
该装饰器默认它后面的函数是唯一的参数。
装饰器的语法允许我们调用decorator时，
提供其它参数，比如@decorator(a)。
这样，就为装饰器的编写和使用提供了更大的灵活性。"""

# def pre_str(pre=''):
#     def decorator(F):
#         def new_F(a, b):
#             print(pre + "input", a, b)
#             return F(a, b)
#         return  new_F
#     return decorator
#
# @pre_str('^_^')
# def square_sum(a, b):
#     return a**2 + b**2
#
# @pre_str('T_T')
# def square_diff(a, b):
#     return a**2 - b**2
#
# print(square_sum(3, 4))
# print(square_diff(3, 4))
"""上面的pre_str是允许参数的装饰器。
它实际上是对原有装饰器的一个函数封装，
并返回一个装饰器。我们可以将它理解为一个含有环境参量的闭包。
当我们使用@pre_str('^_^')调用的时候，Python能够发现这一层的封装，
并把参数传递到装饰器的环境中。该调用相当于:
square_sum = pre_str('^_^') (square_sum)"""

#装饰类
#  一个装饰器可以接收一个类，并返回一个类，从而起到加工类的效果

# def decorator(aClass):
#     class newClass:
#         def __init__(self, age):
#             self.total_display = 0
#             self.wrapped = aClass(age)
#         def display(self):
#             self.total_display += 1
#             print("total display", self.total_display)
#             self.wrapped.display()
#     return newClass
#
# @decorator
# class Bird:
#     def __init__(self, age):
#         self.age = age
#     def display(self):
#         print("My age is",self.age)
#
# eagleLord = Bird(5)
# for i in range(3):
#     eagleLord.display()
"""装饰器的核心作用是name binding。
这种语法是Python多编程范式的又一个体现。"""

#内存管理

#1.对象的内存使用
#赋值语句 a = 1 ： 整数1为一个对象，而a是一个引用。利用赋值语句，应用a指向对象1，对象与引用分离。

# a = 1
# b = 1          # python会缓存整数和短字符串 故 a b 均指向对象1 内存地址相同
# print(id(a))   #内值函数id()  返回对象的身份(identity),即内存地址

# a = 1
# b = 1
# print(a is b) #True
#
# a = "good"
# b = "good"
# print(a is b) #True

# a = "very good morning aaaaaa bbbbbb cccccc dddddd ffffff eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
# b = "very good morning aaaaaa bbbbbb cccccc dddddd ffffff eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
# print(a is b)  #True 教程上说是False 难道这个字符串还不够长吗-.-
#
# a = []
# b = []
# print(a is b) #False
"""长的字符串和其它对象可以有多个相同的对象，
可以使用赋值语句创建出新的对象。"""

#对象引用对象
"""Python的一个容器对象(container)，比如表、词典等，可以包含多个对象。
实际上，容器对象中包含的并不是元素对象本身，是指向各个元素对象的引用。"""

# class from_obj(object):
#     def __init__(self, to_obj):
#         self.to_obj = to_obj
#
# b = [1,2,3]
# a = from_obj(b)
# print(id(a.to_obj))
# print((id(b)))
"""可以看到，a引用了对象b。
对象引用对象，是Python最基本的构成方式。"""

# import TestLib
# print(TestLib.lib_func(120))

# import sys
# print(sys.path)

# print(all([True, 0, "hello!"]))

# print(globals())

# a = "I'm %s. I'm %d year old" % ('Vamei', 99)
# print(a)

# print("I'm %(name)s. I'm %(age)d year old" % {'name':'Vamei', 'age':99})

#格式符

# %s    字符串 (采用str()的显示)
# %r    字符串 (采用repr()的显示)
# %c    单个字符
# %b    二进制整数
# %d    十进制整数
# %i    十进制整数
# %o    八进制整数
# %x    十六进制整数
# %e    指数 (基底写为e)
# %E    指数 (基底写为E)
# %f    浮点数
# %F    浮点数，与上相同
# %g    指数(e)或浮点数 (根据显示长度)
# %G    指数(E)或浮点数 (根据显示长度)
#
# %%    字符"%"

# %[(name)][flags][width].[precision]typecode
#
# (name)为命名

# flags可以有+,-,' '或0。+表示右对齐。-表示左对齐。' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。
#
# width表示显示宽度
#
# precision表示小数点后精度
#
# 比如：
#
# print("%+10x" % 10)
# print("%04d" % 5)
# print("%6.3f" % 2.3)
# 上面的width, precision为两个整数。我们可以利用*，来动态代入这两个量。比如：
#
# print("%.*f" % (4, 1.2))
# Python实际上用4来替换*。所以实际的模板为"%.4f"。

#python标准库

#1.正则表达式re包

# import re
# m = re.search('[0-9]','abcd4ef')
# print(m.group(0))

#2.时间与日期(time, datetime包)
#2.1 time包
# import time
# print(time.time())
# print(time.clock())
# print('start')
# time.sleep(10)
# print('wake up')
# st = time.gmtime()
# print(st)
# st = time.localtime()
# print(st)
# s = time.mktime(st)
# print(s)

#2.2 datetime包

# import datetime
# t = datetime.datetime(2012,9,3,21,30)
# print(t)

# t      = datetime.datetime(2012,9,3,21,30)
# t_next = datetime.datetime(2012,9,5,23,30)
# delta1 = datetime.timedelta(seconds = 600)
# delta2 = datetime.timedelta(weeks = 3)
# print(t + delta1)
# print(t + delta2)
# print(t_next - t)

# print(t > t_next)

# from datetime import datetime
# format = "output-%Y-%m-%d-%H%M%S.txt"
# str    = "output-1997-12-23-030000.txt"
# t      = datetime.strptime(str, format)
#
# print(t)

# print(t_next.strftime(format))

#3.路径与文件(os.path包, glob包)
#3.1 os.path包
'''os.path包主要是处理路径字符串，
比如说'/home/vamei/doc/file.txt'，
提取出有用信息。'''

import os.path
# path = '/home/vamei/doc/file.txt'
#
# print(os.path.basename(path)) # 查询路径中包含的文件名
# print(os.path.dirname(path))  # 查询路径中包含的目录
#
# info = os.path.split(path)    #将路径分割成文件名和目录两个部分， 放在一个表中返回
# print(info)
# path2 = os.path.join('/', 'home', 'vamei', 'doc', 'file1.txt') # 使用目录名和文件名构成一个路径字符串
# print(path2)
# p_list = [path, path2]
# print(p_list)
# print(os.path.commonprefix(p_list)) #查询多个路径的共同部分
#
# path = '/home/vamei/../.'
# newpath = os.path.normpath(path)   # 去除路径path中的冗余。比如'/home/vamei/../.'被转化为'/home'
# print(newpath)

# os.path还可以查询文件的相关信息(metadata)
# path = '/home/dong/PycharmProjects/test/pytest/test.py'
#
# print(os.path.exists(path))    # 查询文件是否存在
#
# print(os.path.getsize(path))   # 查询文件大小
# print(os.path.getatime(path))  # 查询文件上一次读取的时间
# print(os.path.getmtime(path))  # 查询文件上一次修改的时间
#
# print(os.path.isfile(path))    # 路径是否指向常规文件
# print(os.path.isdir(path))     # 路径是否指向目录文件

#3.2 glob包
'''glob包最常用的方法只有一个, glob.glob()。
该方法的功能与Linux中的ls相似，
接受一个Linux式的文件名格式表达式(filename pattern expression)，
列出所有符合该表达式的文件（与正则表达式类似），
将所有文件名放在一个表中返回。
所以glob.glob()是一个查询目录下文件的好方法。'''
# import glob
# print(glob.glob('/home/dong/PycharmProjects/test/pytest/*'))

#4.文件管理(部分os包, shutil包)
#4.1 os包

# os包包括各种各样的函数，以实现操作系统的许多功能。这个包非常庞杂。os包的一些命令就是用于文件管理。我们这里列出最常用的:
#
# mkdir(path) 创建新目录，path为一个字符串，表示新目录的路径。相当于$mkdir命令
#
# rmdir(path) 删除空的目录，path为一个字符串，表示想要删除的目录的路径。相当于$rmdir命令
#
# listdir(path) 返回目录中所有文件。相当于$ls命令。
#
# remove(path) 删除 path指向的文件。
#
# rename(src, dst) 重命名文件，src和dst为两个路径，分别表示重命名之前和之后的路径。
#
# chmod(path, mode) 改变path指向的文件的权限。相当于$chmod命令。
#
# chown(path, uid, gid) 改变path所指向文件的拥有者和拥有组。相当于$chown命令。
#
# stat(path) 查看path所指向文件的附加信息，相当于$ls -l命令。
#
# symlink(src, dst) 为文件dst创建软链接，src为软链接文件的路径。相当于$ln -s命令。
#
# getcwd() 查询当前工作路径 (cwd, current working directory)，相当于$pwd命令。
#
# 比如说我们要新建目录new：
#
# import os
# os.mkdir('/home/vamei/new')

# 4.2 shutil包
# copy(src, dst) 复制文件，从src到dst。相当于$cp命令。
#
# move(src, dst) 移动文件，从src到dst。相当于$mv命令。
#
# 比如我们想复制文件a.txt:
#
# import shutil
# shutil.copy('a.txt', 'b.txt')

#5.存储对象 (pickle包，cPickle包)

# 将内存中的对象转换成为文本流：
#
# import pickle
#
# # define class
# class Bird(object):
#     have_feather = True
#     way_of_reproduction  = 'egg'
#
# summer       = Bird()                 # construct an object
# picklestring = pickle.dumps(summer)   # serialize object
# 使用pickle.dumps()方法可以将对象summer转换成了字符串 picklestring(也就是文本流)。随后我们可以用普通文本的存储方法来将该字符串储存在文件(文本文件的输入输出)。
#
# 当然，我们也可以使用pickle.dump()的方法，将上面两部合二为一:
#
# import pickle
#
# # define class
# class Bird(object):
#     have_feather = True
#     way_of_reproduction  = 'egg'
#
# summer       = Bird()                        # construct an object
# fn           = 'a.pkl'
# with open(fn, 'w') as f:                     # open file with write-mode
#     picklestring = pickle.dump(summer, f)   # serialize and save object
# 对象summer存储在文件a.pkl

#6.子进程 (subprocess包)
#7.信号 (signal包)  signal包主要是针对UNIX平台(比如Linux, MAC OS)
#8.多线程与同步 (threading包)

#8.1多线程售票以及同步
'''使用Python来实现Linux多线程与同步文中的售票程序。
我们使用mutex (也就是Python中的Lock类对象)
来实现线程的同步:'''

# A program to simulate selling tickets in multi-thread way
# Written by Vamei

# import threading
# import time
# import os
#
# # This function could be any function to do other chores.
# def doChore():
#     time.sleep(0.5)
#
# # Function for each thread
# def booth(tid):
#     global i
#     global lock
#     while True:
#         lock.acquire()                # Lock; or wait if other thread is holding the lock
#         if i != 0:
#             i = i - 1                 # Sell tickets
#             print(tid,':now left:',i) # Tickets left
#             doChore()                 # Other critical operations
#         else:
#             print("Thread_id",tid," No more tickets")
#             os._exit(0)              # Exit the whole process immediately
#         lock.release()               # Unblock
#         doChore()                    # Non-critical operations
#
# # Start of the main function
# i    = 100                           # Available ticket number
# lock = threading.Lock()              # Lock (i.e., mutex)
#
# # Start 10 threads
# for k in range(10):
#     new_thread = threading.Thread(target=booth,args=(k,))   # Set up thread; target: the callable (function) to be run, args: the argument for the callable
#     new_thread.start()                                      # run the thread

#8.2   OOP创建线程
'''下面介绍如何通过面向对象
(OOP， object-oriented programming) 的方法实现多线程，
其核心是继承threading.Thread类。
我们上面的for循环中已经利用了threading.Thread()
的方法来创建一个Thread对象，并将函数booth()以及其参数传递给改对象，
并调用start()方法来运行线程。OOP的话，
通过修改Thread类的run()方法来定义线程所要执行的命令。'''

# A program to simulate selling tickets in multi-thread way
# Written by Vamei

# import threading
# import time
# import os
#
# # This function could be any function to do other chores.
# def doChore():
#     time.sleep(0.5)
#
# # Function for each thread
# class BoothThread(threading.Thread):
#     def __init__(self, tid, monitor):
#         self.tid          = tid
#         self.monitor = monitor
#         threading.Thread.__init__(self)
#     def run(self):
#         while True:
#             monitor['lock'].acquire()                          # Lock; or wait if other thread is holding the lock
#             if monitor['tick'] != 0:
#                 monitor['tick'] = monitor['tick'] - 1          # Sell tickets
#                 print(self.tid,':now left:',monitor['tick'])   # Tickets left
#                 doChore()                                      # Other critical operations
#             else:
#                 print("Thread_id",self.tid," No more tickets")
#                 os._exit(0)                                    # Exit the whole process immediately
#             monitor['lock'].release()                          # Unblock
#             doChore()                                          # Non-critical operations
#
# # Start of the main function
# monitor = {'tick':100, 'lock':threading.Lock()}
#
# # Start 10 threads
# for k in range(10):
#     new_thread = BoothThread(k, monitor)
#     new_thread.start()

#9. 进程信息 (部分os包)
'''Python的os包中有查询和修改进程信息的函数。'''
#10. 多进程初步 (multiprocessing包)
#11.多进程探索 (multiprocessing包)
#12. 数学与随机数 (math包，random包)
#13. 循环器 (itertools)

# for i in iter([2, 4, 5, 6]):
#     print(i)
# from itertools import *

# 13.1 无穷循环器
# count(5, 2)     #从5开始的整数循环器，每次增加2，即5, 7, 9, 11, 13, 15 ...
# cycle('abc')    #重复序列的元素，既a, b, c, a, b, c ...
# repeat(1.2)     #重复1.2，构成无穷循环器，即1.2, 1.2, 1.2, ...

# repeat(10, 5)   #重复10，共重复5次

# 13.2 函数式工具

# from itertools import *
#
# rlt = imap(pow, [1, 2, 3], [1, 2, 3])
#
# for num in rlt:
#     print(num)
#
#     tarmap(pow, [(1, 1), (2, 2), (3, 3)])  # pow将依次作用于表的每个tuple。
#     ifilter函数与filter()
#     函数类似，只是返回的是一个循环器。
#
#     ifilter(lambda x: x > 5, [2, 3, 5, 6, 7])  # 将lambda函数依次作用于每个元素，如果函数返回True，则收集原来的元素。6, 7。
#     此外：
#
#     ifilterfalse(lambda x: x > 5, [2, 3, 5, 6, 7])  # 与上面类似，但收集返回False的元素。2, 3, 5
#     takewhile(lambda x: x < 5, [1, 3, 6, 7, 1])  # 当函数返回True时，收集元素到循环器。一旦函数返回False，则停止。1, 3
#     dropwhile(lambda x: x < 5, [1, 3, 6, 7, 1])  # 当函数返回False时，跳过元素。一旦函数返回True，则开始收集剩下的所有元素到循环器。6, 7, 1

# 13.3 组合工具

'''通过组合原有循环器，来获得新的循环器。'''

# 13.4 groupby()
'''将key函数作用于原循环器的各个元素。
根据key函数结果，将拥有相同函数结果的元素分到一个新的循环器。
每个新的循环器以函数返回结果为标签。
'''

# from itertools import *
#
# def height_class(h):
#     if h > 180:
#         return "tall"
#     elif h < 160:
#         return "short"
#     else:
#         return "middle"
#
# friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]
#
# friends = sorted(friends, key = height_class)
# for m, n in groupby(friends, key = height_class):
#     print(m)
#     print(list(n))

# 13.5 其它工具

# compress('ABCD', [1, 1, 1, 0])  # 根据[1, 1, 1, 0]的真假值情况，选择第一个参数'ABCD'中的元素。A, B, C
# islice()                        # 类似于slice()函数，只是返回的是一个循环器
# izip()                          # 类似于zip()函数，只是返回的是一个循环器。

# 14. 数据库 (sqlite3)
# 14.1 创建数据库
# import  sqlite3
#
# conn = sqlite3.connect("test.db")
#
# c = conn.cursor()
#
# c.execute('''CREATE TABLE categoty
#         (id int primary key, sort int, name text)''')
#
# c.execute('''CREATE TABLE book
# (id int primary key,
# sort int,
# name text,
# price real,
# category int,
# FOREIGN KEY (category) REFERENCES category(id))''')
#
# conn.commit()
# conn.close()

# 14.2 插入数据

# import sqlite3
#
# conn = sqlite3.connect("test.db")
# c = conn.cursor()
#
# books = [(1,1,'Cook Recipe',3.12,1),
#          (2,3,'Python Intro',17.5,2),
#          (3,2,'OS Intro',13.6,2)]
#
# c.execute("INSERT INTO categoty VALUES (1,1, 'kitchen')")
#
# c.execute("INSERT INTO categoty VALUES (?,?,?)", (2,2,'computer'))
#
# c.execute('INSERT INTO book VALUES (?,?,?,?,?)', books)   #出现错误
#
# conn.commit()
# conn.close()

# 14.3 查询

# import sqlite3
#
# conn = sqlite3.connect('test.db')
# c = conn.cursor()
#
# c.execute('SELECT name FROM categoty ORDER BY sort')
# print(c.fetchone())
# print(c.fetchone())
#
# c.execute('SELECT * FROM book WHERE book.category=1')
# print(c.fetchall())
#
# for row in c.execute('SELECT name, price FROM book ORDER BY sort'):
#     print(row)

# 14.4 更新与删除

# conn = sqlite3.connect("test.db")
# c = conn.cursor()
#
# c.execute('UPDATE book SET price=? WHERE id=?',(1000,1))
# c.execute('DELETE FROM book WHERE id=2')
#
# conn.commit()
# conn.close()

# 15 原始Python服务器

# 15.1 TCP socket

'''首先是服务器端，我们使用bind()方法
来赋予socket以固定的地址和端口，
并使用listen()方法来被动的监听该端口。
当有客户尝试用connect()方法连接的时候，
服务器使用accept()接受连接，
从而建立一个连接的socket：'''

# import socket
#
# HOST = ''
# PORT = 8000
#
# reply = 'Yes'
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
# s.listen(3)
#
# conn, addr = s.accept()
# request = conn.recv(1024)
#
# print('request is: ',request)
# print('Connedted by',addr)
#
# conn.sendall(reply)

# conn.close()
'''首先是服务器端，
我们使用bind()方法来赋予socket以固定的地址和端口，
并使用listen()方法来被动的监听该端口。
当有客户尝试用connect()方法连接的时候
，服务器使用accept()接受连接，
从而建立一个连接的socket：'''

'''然后用另一台电脑作为客户，
我们主动使用connect()方法来搜索服务器端的IP地址
(在Linux中，你可以用$ifconfig来查询自己的IP地址)
和端口，以便客户可以找到服务器，并建立连接:'''

# import  socket
#
# HOST = '127.0.0.1'
# PORT = 8000
#
# request = 'can you hear me?'
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
# s.sendall(request)
# reply = s.recv(1024)
# print ('reply is: ',reply)
#
# s.close()