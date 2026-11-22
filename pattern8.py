# pattern 8 
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

def pattern8():
    for i in range(5):
        for j in range(i):
            print(" ", end = " ")
        for k in range(9-2*i):
            print("*",end = " ")
        print()
pattern8()