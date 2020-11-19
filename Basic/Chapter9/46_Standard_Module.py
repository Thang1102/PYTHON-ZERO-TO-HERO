import random as ra
import datetime as dt
import os as o

print(ra.randint(1,10000))

x = list(range(25))
print(x)
ra.shuffle(x)
print(x)
################
t = dt.datetime.now()
print(t)

#######
print(o.getcwd()) #duowng dan file
print(o.getenv("PATH")) # bien moi truong