import sys as system
import math

# # Zad1
# lista = ["pilka nozna", "siatkowka", "koszykowka", "skoki narciarskie"]
# lista.reverse()
# lista.extend(["F1", "rzut cegla", "szturchanie grubasow bagietka na silowni"])
# print(lista)
# del lista
#
# # Zad2
# slownik = {"ikr": "I know right", "idc": "I don't care", "smh": "shaking my head"}
# del slownik
#
# # Zad3
# slownik = {"csgo": "Counter Strike : Global Offensive", "lol": "League Of Legends", "ror2": "Risk of Rain 2"}
# print(len(slownik))
# del slownik

# # Zad4
# napis = input("Wprowadz zdanie\n")
# print(napis.count("a"))
# del napis

# # Zad5
#
# system.stdout.write("podaj a\n")
# a=int(system.stdin.readline())
# system.stdout.write("podaj b\n")
# b=int(system.stdin.readline())
# system.stdout.write("podaj c\n")
# c=int(system.stdin.readline())
#
#
# dzialanie = a**b+c
# print((dzialanie))

# # Zad6
# a = int(input("Podaj a"))
# b = int(input("Podaj b"))
# c = int(input("Podaj c"))
#
# if (a >= b) & (a >= c):
#     print(a)
# elif (b >= a) & (b >= c):
#     print(b)
# else:
#     print(c)

# # Zad7
# lista = [1, 3.14, 9, 2.50]
# for x in range (0, len(lista), 1):
#     lista[x] *= lista[x]
# print(lista)

# # Zad8
# lista=[]
# count = 0
# while count <=9:
#     a = int(input("Podaj liczbe"))
#     count+=1
#     if a % 2 == 0 :
#         lista.append(a)
# print(lista)

# # Zad9
# napis = ""
# lista = [1, 2, 3 ,4 ,5]
# for x in lista:
#     if x%2 == 0:
#         napis+="E\n"
#     else:
#         napis+="EEEEEE\n"
# print(napis)

# Zad10

x = (input("Podaj x aby obliczyc sqrt(x)"))

try:
        wynik = math.sqrt(int(x))
        print(wynik)
except ValueError:
        print("Podano ujemny x")
