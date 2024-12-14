# """
# list belgisi []
# Tuple-ozgarmas toplam
# tuple belgisi ()
# Misol: (1,2,3)
# """
# s1 = (2, 4, 5, 4)
# s2 = (2, 5, 4, 4)
# print(s1 == s2)
#
# print(s1[:2])  # 2- indexgacha bolgan barcha elementlarni chiqaradi
# print(s1[2:])  # 2- indexdan oxirigacha bolgan barcha elementlarni chiqaradi
# print(s1[1:3])  # 1- indexdan 3 indexgacha bolgan barcha elementlarni chiqaradi
#
# index = s.index(4)
# count = s.count(4)
# print(index, count)
# print(s, type(s))
#
#
# def test(a, b):
#     c = a + b
#     d = a - b
#     return c, d
#
#
# response = test(15, 10)
#
# print(response, type(response))
#
# """
# set- Toplam
# set belgisi -  {}
# dict-belgisi - {}
# """
# s2 = {5, 4, 3, 2, 7, 8, 11}
# s1 = {1, 2, 3, 4, 5, 10, 16, 0}
#
# print(s1 - s2)
# print(s2 - s1)
# print(s2 ^ s1)
# print(s2 & s1)
# print(s2 | s1)
# print(s1.union(s2))
# s1.add(8)
# a = s1.pop()  # toplam ichidan oxirgi elementni yulib olish
# print(len(s1))
# print(s1)
# print(s2)
# s1.remove(5)# berilgan qiymatni toplam ichidan ochirib tashlaydi
# d = s1.difference(s2)
# d2 = s2.difference(s1)
# print(s1.intersection(s2))
# print(s2.intersection(s1))
#
# # print(d, d2)
#
# list2 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 10]
# print(list2, type(list2))
# list2 = set(list2)
# print(list2, type(list2))
# list2 = list(list2)
# print(list2, type(list2))
#
# # a = (1,) + (2,)
# # print(a, type(a))
#
# """
# dict -lugat key value
# dict belgisi {}
# """
#
# yillar = {}
# yillar["1"] = "2024"
# yillar["2"] = "2025"
# print(yillar, type(yillar))
#
# for i in range(10):
#     yillar.update({f"{i + 1}": f"202{i}"})
#
# print(yillar)
# print(eng_uzb.get("apple1"))
# print(eng_uzb["apple1"])
#
# for key, value in eng_uzb.items():
#     print(key, value)
#
# a = yillar.pop("2")
# print(a)
# key, val = yillar.popitem()  # oxirgi itemni yulib oladi
# print(key, val)
# yillar.clear()
# print(yillar)
#
#
# form = {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "hobbies": ["reading", "painting", "cooking"],
#     "images": {
#         "img1": "http://",
#         "img2": "http://",
#         "img3": "http://",
#     }
# }
# # ctrl+alt+shift+j
#
# print("salom dunyo")
# print("salom dunyo")
# print("salom dunyo")
# print("salom dunyo")
# print("salom dunyo")
# print("salom dunyo")
# print("salom dunyo")
# print("salom dunyo")
# print("salom dunyo")
# print("salom dunyo")
