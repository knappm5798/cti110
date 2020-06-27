# CTI-110
# P3HW1 - Color Mixer
# Michael Knapp
# June 27 2020
#
#Ask for a Primary Color
color1=input('Pick first primary Color: ')
color2=input('Pick second primary Color: ')
#Display Secondary color based on if, elif, and else statements
if color1 == 'red' and color2 == 'blue' or color1 == 'blue' and color2 == 'red':
    print('Your secondary color is Purple')
elif color1 == 'red' and color2== 'yellow' or color1 =='yellow' and color2=='red':
    print('Your Secondary color is Orange')
elif color1=='blue' and color2=='yellow' or color1=='yellow' and color2=='blue':
    print('Your Secondary color is Green')
else:
    print("You didn't enter a primary color. Try again!")