# pattern 3 
# * * * * *
# * * * *
# * * *
# * *
# *

def pattern3():
    for i in range(6):
        for j in range(6-i):
            print("*",end = " ")
        print() 
pattern3()