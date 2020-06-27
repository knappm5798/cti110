# Area Of Rectangles
# June 27 2020
# CTI-110 P3T1 Area Of Rectangles
# Michael Knapp
#Input Length and Width of Rectangle 1
length1 = int(input('Enter the Length of Rectangle 1: '))
width1 = int(input('Enter the Width of Rectangle 1: '))
#Input Length and Width of Rectangle 2
length2 = int(input('Enter the Length of Rectangle 2: '))
width2 = int(input('Enter the Width of Rectangle 2: '))
#Calculate the areas of rectangle 1 and 2
area1 = length1 * width1
area2 = length2 * width2
#Determine whic rectangle is bigger
if area1 > area2:
    print("Rectangle 1 is bigger")
elif area2 > area1: 
    print("Rectangle 2 is bigger")
else:
    print("Both rectangles are the same size")