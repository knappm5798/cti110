# Bug Collector with running total
# 20200704
# CTI-110 P4T2 - Bug Collector
# Michael Knapp
#
#Initialize Accumulator
total=0

#Loop for 5 days
for day in range(1,6):
    print('Enter number of bugs collected on day', day) 
    bugs=int(input()) #Input bugs collected
    total += bugs #Number added to total

print('Total collected a total of', total, 'bugs.') #Print total
