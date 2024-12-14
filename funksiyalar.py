# """
# metod va funksiya
# dry-dont repeat yourself
# def -funksiya kalit sozi
#
# def qoshish():
#     return 10+15
# """
#
# # def ayirish(a, b):
# #     return a - b
# # print(ayirish(10,8))
# # print(ayirish(15,8))
# # print(ayirish(20,8))
#
#
# # def test():
# #     text="salom dunyo"
# #     return text
# #
# #
# # print(test())
# import datetime
#
#
# def form(nomi, olcham, narx, sana=datetime.datetime.now()):
#     invoice = f"""Maxsulot nomi: {nomi},\n
#     Olchami yoki miqdori: {olcham},\n
#     Narx: {narx * olcham},\n
#     Sana: {sana},\n
#     Xaridingiz uchun raxmat!!!
#     """
#     return invoice
#
#
# while True:
#     nomi = input("Maxsulot nomini kiriting>>>")
#     miqdori = int(input("Maxsulot miqdorini kiriting>>>"))
#     narx = int(input("Maxsulot narxini kiriting>>>"))
#     print(form(nomi, miqdori, narx, sana=datetime.datetime.now()))
#
# #
# # ism, f, yosh = map(str, input().split(' '))
# # print(form(ism, f, yosh))
# # ism, f, yosh = map(str, input().split(' '))
# # print(form(ism, f, yosh))


# masala1
def masala1():
    a = int(input())
    b = int(input())
    c = a + b
    print(c)


def masala2():
    a = int(input())
    b = int(input())
    c = a * b
    return c


def masala3():
    a = int(input())
    b = int(input())
    c = a - b
    print(c)


# masala3()
# print(masala3())
# n = masala2()
# print(masala2())
# while True:
#     n = int(input('Masala raqamini kiriting>>>'))
#     match n:
#         case 1:
#             masala1()
#         case 2:
#             masala2()
#         case 3:
#             masala3()
#         case _:
#             print("Bunday masala yoq")
#
# # lambda


# add = lambda a, b: a + b
# check = lambda a: a > 0
# length = lambda s: len(s)
# d4 = lambda a: a ** 4
#
# print(add(10, 15))
# print(check(10))
# print(length("salom"))

# map(int, input().split(' '))

# a = list(map(lambda x: x ** 2, range(10)))
# b = list(map(lambda s: s.lower(), sozlar))
#
# print(a)
# print(b)

# a = list(filter(lambda x: x % 2 == 0, sonlar))
# a = list(filter(lambda x: x[-1].lower() == 'd', sozlar))
# print(a)

# S = list(map(int, input().split(' ')))
sozlar = ['Hello', 'wOrld', 'Hello', 'wOrld']


# from functools import reduce
#
# summa = reduce(lambda x, y: x + y, sonlar)
# max_element = reduce(lambda x, y: x if x > y else y, sonlar)
# print(summa)
# print(max_element)


# birikma = zip(sonlar, sozlar,range(len(sozlar)))
# print(list(birikma))
#
# def test(*args):
#     return sum(args)
#
#
# print(test(1, 2, 3, 4, 5, 6, 7, 8, 9))


# def test(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v)
#
#
# # print(test(1,2,3,4,5,6,7,8,9))
#
# test(a=1, b=2, c=3, d=4, e=5, f=6)
sonlar = [10, 2, 3, 4]
sonlar.sort()
print(sonlar)
print(max(sonlar))
print(min(sonlar))