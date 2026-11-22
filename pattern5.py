# pattern 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def pattern5():
    for i in range(5):
        for j in range(i+1):
            print(i+1,end = " ")
        print()
pattern5()