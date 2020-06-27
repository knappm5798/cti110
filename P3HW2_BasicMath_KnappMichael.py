# CTI-110
# P3HW2 - BasicMath
# Michael Knapp
# June 27th 2020
#
#Loop
loop='y'
while loop=='y':
#Display menu
    print('Please choose an option: ')
    print('1) Add Numbers')
    print('2) Multiply Numbers')
    print('3) Subtract Numbers')
    print('4) Exit')
    #Ask for selection
    select=int(input('Selection: '))
    #Conduct IF/ELSE statements
    if select==4: #Exit program
        print('Exiting...')
        break
    elif select==0 or select >= 5: #Invalid selection
        print('Invalid number presented')
        break
    else:
        #Ask for numbers
        number1=int(input('1st Number?: '))
        number2=int(input('2nd Number?: '))
        #Conduct Calculations and present solution
        if select== 1:
                print(number1 + number2)
        elif select==2:
                print(number1 * number2)
        elif select==3:
                print(number1 - number2)
        
