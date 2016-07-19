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