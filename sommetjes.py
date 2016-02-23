from random import randint
import sys
import os

os.system('clear')

low = int(sys.argv[1])
high = int(sys.argv[2])
op_list = ['+', '-', '*', '/']

for i in range(5):
    som = "{0} {1} {2}".format(randint(low, high), op_list[randint(0, 1)], randint(low, high))
    answer = int(raw_input("Som {0}: {1} = ".format(i+1, som)))
    if eval(som) == answer:
        print "Goed!"
        print
    else:
        print "Ah, jammer. {0} = {1}".format(som, eval(som))
        print

input = raw_input("Nog een keer? (j/n):")

while True:
    if input == "j":
        os.system('python sommetjes.py 1 10')
        break
    elif input == "n":
        print "Ok, tot de volgende keer!"
        print
        break
    else:
        input = raw_input("Wil je nog een keer? \nDruk op 'j' of 'n':")
