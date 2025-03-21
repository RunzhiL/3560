#!/user/bin/env python3

first_num = float(input("What is the first num? "))
activity = input("What activity? (+ - * /)")
second_num = float(input("What is the second num? "))

if activity == "+":
    print(first_num + second_num)
if activity == "-":
    print(first_num - second_num)
if activity == "*":
    print(first_num * second_num)
if activity == "/":
    print(first_num / second_num)