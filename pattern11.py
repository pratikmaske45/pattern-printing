# pattern 11 
# *
# * *
# *   *
# *     *
# * * * * *

def pattern11():
    for i in range(5):
        for j in range(5):
            if j == 0 or j == i or i == 4:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()
pattern11()