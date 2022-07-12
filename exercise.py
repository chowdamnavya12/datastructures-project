'''
import math as m
r=float(input("enter radius"))
a=m.pi*2*r
print(a)
fn= input("Enter Filename: ")
f = fn.split(".")
print ("Extension of the file is : " + f[-1])
