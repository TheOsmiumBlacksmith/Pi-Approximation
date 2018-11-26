#pylint:disable=W0612

'''
This code approximates pi by geneeating co-ordinates (x,y) such that x,y are in [-1,1]. Then the ratio of a circle to the square is pi/4.
'''

from random import uniform

def approx_pi(n):
	# number of times point lands within circle
    inside = 0
    # itterate co-ordinate choice n times
    for i in range(n):
    	# pick the co-ordinates as a tuple
        (x,y) = (
        uniform(-1,1),
        uniform(-1,1)
        )
        # point lands in circle?
        if (x**2)+(y**2)<1:
            inside += 1
    # area of circle = pi
    # area of square = 4
    # ratio = pi/4
    return 4*(float(inside)/n)

def main():
	# choose how many itterations to run
    a = approx_pi(
    int(input("n= "))
    )
    # print the resulting approximation
    print (a)

main()
