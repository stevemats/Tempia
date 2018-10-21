#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-

def menu():
	print("\n1. Celsius to Fahrenheit")
	print("2. Fahrenheit to Celsius")
	print("3. Terminate")
	choice = int(input("Chose conversion method: "))
	return choice

def toCelsius(f):
	return int((f - 32) / 1.8)

def toFahrenheit(c):
	return int(c * 1.8 + 32)

def main():
	choice = menu()
	while choice != 3:
		if choice == 1:
			c = eval(input("Enter Celsius degrees: "))
			print(str(c) + "C = " + str(toFahrenheit(c)) + "F")
		elif choice == 2:
			f = eval(input("Enter Fahrenheit degrees: "))
			print(str(f) + "F = " + str(toCelsius(f)) + "C")
		else:
			print("Invalid choice try again.")
		choice = menu()

main()
