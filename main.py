import random
from ciagi import Ciagi
# #zadanie 1
# A =[1 - x for x in range(1,11)]
# print(A)
#
# B =[4**x for x in range(0,8)]
# print(B)
#
# C = [x for x in B if x % 2 == 0]
# print(C)
#
# #zadanie 2
# lista1 = []
# for i in range(10):
#     j = random.randint(1, 10)
#     lista1.append(j)
# print(lista1)
# lista2 = [x for x in lista1 if x % 2 ==0]
# print(lista2)
#
# #zadanie 3
#
# lista_zakupow = {"pomidory": "kg", "jajka": "sztuki", "ciastka": "opakowania",
#                  "ogórki": "sztuki", "woda": "sztuki", "cukier": "kg", }
# list_zakup = [x for x in lista_zakupow if lista_zakupow[x] == "sztuki"]
# print(list_zakup)
#
# #zadanie 4
# def prostokatny(a,b,c):
#     if a**2 + b**2 == c**2:
#         print("trojkat jest prostokatny")
#     else:
#         print("trojkat nie jest prostokatny")
#
# prostokatny(3,4,5)
#
# #zadanie 5
#
# def pole_trapezu(a=5, b=6, h=7):
#     pole = (1/2) * (a + b) * h
#     print(pole)
# pole_trapezu(2,5,10)
# pole_trapezu()
#
# #zadanie 6
# def iloczyn_c(a=1, b=4, ile=10):
#
#     ciag = []
#     for i in range(a, ile+1):
#         i = i*b
#         ciag.append(i)
#     print(ciag)
#     iloczyn = 1
#     for x in ciag:
#         iloczyn = iloczyn * x
#     print(iloczyn)

#iloczyn_c()

#zadanie 7

 # zadanie 8
# def suma_zakupow(**lista):
#     return print(f'wszystkich produktow jest {len(lista)} za sume  {sum((lista.values()))}')
# suma_zakupow(pomidory = 10,ogorek = 5, bulki = 3,woda = 2)

#zadanie 9

ciag = Ciagi.arytmetyczny(1,2,3)
print(ciag)

# #zadanie 10
# liczby = [x for x in range(1,101) if x%4==0]
# with open('zadania.txt', 'a+') as plik:
#     plik.writelines(str(liczby))
#
# #zadanie 11
# with open("zadania.txt", 'r') as file:
#     a = file.readlines()
#     print(a)