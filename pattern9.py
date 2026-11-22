# pattern 9
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

def pattern9():
    for i in range(5):
        for j in range(4-i):
            print(" ", end = " ")
        for k in range(2*i+1):
            print("*", end = " ")
        print()
    for l in range(4):
        for p in range(l+1):
            print(" ", end = " ")
        for m in range(7-2*l):
            print("*",end = " ")
        print()
pattern9()