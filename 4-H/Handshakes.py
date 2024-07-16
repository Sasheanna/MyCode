
# handshake problem, first without using recursion, and then WITH recursion


# no recursion

"""

handshakes = 0

people = 0

test = input("How many people are in the room? ")


for a in range(int(test)):
    
    people = people + 1
    handshakes = handshakes + people - 1

print("The number of handshakes is: " + str(handshakes))

"""


# recursion

handshakes = 0

def meeting(people):

    handshakes = 0

    if people == 1:

         handshakes = 0

         return handshakes

    else:

        meeting(people - 1)

        handshakes = handshakes + people - 1

    print("There will be " + str(handshakes) + " handshakes.")

print("Test!!!")

meeting(10)


#print("There will be " + str(handshakes) + " handshakes.")

