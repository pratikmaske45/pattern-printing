# pattern 12
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *

def pattern12():

    
    for i in range(5):
        for j in range(i+1):
            print("*", end=" ")

        for k in range(8-2*i):
            print(" ", end=" ")

        for l in range(i+1):
            print("*", end=" ")

        print()

    
    for i in range(3, -1, -1):
        for j in range(i+1):
            print("*", end=" ")

        for k in range(8-2*i):
            print(" ", end=" ")

        for l in range(i+1):
            print("*", end=" ")

        print()
pattern12()
