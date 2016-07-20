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

#上下文管理器 一旦进入或离开适用范围，会有特殊操作被调用（如对象分配或释放内存）

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