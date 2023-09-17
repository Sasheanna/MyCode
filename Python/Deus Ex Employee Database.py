

import time
import sys

'''
WELCOME TO THE UNATCO DATA BASE
'''



class employee:

    def __init__(self, name, age, position, status, yearStarted, location):

        self.name = name
        self.age = age
        self.position = position
        self.status = status
        self.yearStarted = yearStarted
        self.location = location
        self.killSwitch = "DEACTIVATED"

    def info(self):

        return f"Name: {self.name}\nAge: {self.age}\nPosition: {self.position}\nCurrent Status: {self.status}\nFirst Year of Employment at UNATCO: {self.yearStarted}\nLocation: {self.location}\nKillswitch: {self.killSwitch}"

    def activate_killSwitch(self):

        self.killSwitch = "ACTIVATED"
        return "Killswitch activated.  Countdown: 12 hours remaining."

    def deactivate_killSwitch(self):

        self.killSwitch = "DEACTIVATED"
        return "Killswitch deactivated."


# Employees
em1 = employee("JC Denton", 27, "Agent", "On a mission", 2052, "New York City")
em2 = employee("Paul Denton", 33, "Agent", "ROGUE", 2045, "New York City")
em3 = employee("Anna Navarre", 30, "Agent", "CONFIDENTIAL", 2050, "New York City")
em4 = employee("Alex Jacobson", 28, "Hacker", "Watching Agent JC Denton's infolink", 2046, "UNATCO Headquarters")
em5 = employee("Sam Carter", 56, "Quartermaster", "Unloading supplies", 2024, "UNATCO Headquarters")


# The user interface
def searchEmployeeInfo():

    while True:

        print()
        search = input("Which employee's information would you like to retrieve? (type 'exit' to leave) ")

        if search == em1.name:
        
            print("\n"*2)
            print(em1.info())
            print("\n"*2)
        
        elif search == em2.name:
        
            print("\n"*2)
            print(em2.info())
            print("\n"*2)
        
        elif search == em3.name:
        
            print("\n"*2)
            print(em3.info())
            print("\n"*2)

        elif search == em4.name:

            print("\n"*2)
            print(em4.info())
            print("\n"*2)

        elif search == em5.name:

            print("\n"*2)
            print(em5.info())
            print("\n"*2)

        elif search == "exit":

            print("Returning to main menu...")
            break
        
        else:
            print("Sorry, that is not a valid input.  Please try again.")

def editInfo(employee):

    while True:

        print()
        toEdit = input("What attribute of that employee's data would you like to edit?  Type 'exit' to return to the previous page.\n\nName\nAge\nPosition\nCurrent status (type 'Status')\nFirst year of employment at UNATCO (type 'Employment')\nLocation\n\n")

        if toEdit == "Name":
            
            employee.name = input("Please enter the new first and last name for this employee: ")
            print("Edit successful.")
            
        elif toEdit == "Age":

            while True:

                try:
                    
                    employee.age = int(input("Please enter the new value for this employee's age (must be a number): "))
                    break

                except:

                    print("ERROR, not a valid input.  Please try again.")

            print("Edit successful.")
            
        elif toEdit == "Position":

            employee.position = input("Please enter the position of this employee: ")
            print("Edit successful.")
            
        elif toEdit == "Status":

            employee.status = input("Please enter the updated status of this employee: ")
            print("Edit successful.")
            
        elif toEdit == "Employment":

            while True:

                try:
                    
                    employee.yearStarted = input("Please enter the new value for the year this employee started working for UNATCO: ")
                    break

                except:

                    print("ERROR, not a valid input.  Please try again.")

        
        elif toEdit == "Location":

            employee.location = input("Please enter the updated location of this employee: ")
            print("Edit successful.")
            
        elif toEdit == "exit":
            print("Returning to previous menu...")
            print()
            break
        else:
            print("I'm sorry, that is not a valid entry.  Please try again.")
    

def changeKillSwitchState(employeeName, whatChange):

    if employeeName == em1.name:

        if whatChange == 'ACTIVATE':

            print(em1.activate_killSwitch())

        elif whatChange == 'DEACTIVATE':

            print(em1.deactivate_killSwitch())

    elif employeeName == em2.name:

        if whatChange == "ACTIVATE":

            print(em2.activate_killSwitch())

        elif whatChange == "DEACTIVATE":

            print(em2.deactivate_killSwitch())

    elif employeeName == em3.name:
        
        if whatChange == "ACTIVATE":

            print(em3.activate_killSwitch())

        elif whatChange == "DEACTIVATE":

            print(em3.deactivate_killSwitch())

    elif employeeName == em4.name:
        
        if whatChange == "ACTIVATE":

            print(em4.activate_killSwitch())

        elif whatChange == "DEACTIVATE":

            print(em4.deactivate_killSwitch())

    elif employeeName == em5.name:

        if whatChange == "ACTIVATE":

            print(em5.activate_killSwitch())

        elif whatChange == "DEACTIVATE":

            print(em5.deactivate_killSwitch())


        


#Usernames and passwords

#add someone who has a password 'ambrosia'
userpass = {
    "JCD": "IceBreaker",
    "WaltonSimons": "IOwnThisPlace",
    "PaulDenton": "GoneRogue",
    "Daedalus": "MASTERKEY"
    }

securityBreach = 0
secureSecurityBreach = 0
#Login

while True:

    try:

        username = input("USERNAME: ")

        password = input("PASSWORD: ")


        if userpass[username] == password:

            print()
            print("Logging in...")
            time.sleep(2)
            print()
            
            #Special personalized message if you own the company
            if username == "WaltonSimons":

                print("Welcome, Mr. Simons.")
                time.sleep(1)

            print("\n"*4)
                
            break

        else:
            securtiyBreach += 1
            print()
            print("NOT A VALID PASSWORD")
            print()
            
            if securityBreach >= 4:
                print("Unauthorized access attempted several times.  Calling security...")
                print()
                time.sleep(2)
                print("SHUTTING DOWN")
                sys.exit()

    except KeyError:

        securityBreach += 1
        print()
        print("NOT A VALID ID")
        print()

        if securityBreach >= 4:
            print("Unauthorized access attempted several times.  Calling security...")
            print()
            time.sleep(2)
            print("SHUTTING DOWN")
            sys.exit()


#Actual running of the program
while True:

    print("WELCOME TO THE UNATCO EMPLOYEE DATA ARCHIVES.")
    print()
    print(f"Employees currently in the system:\n\n{em1.name}\n{em2.name}\n{em3.name}\n{em4.name}\n{em5.name}")
    print()


    print()
    options = input("What would you like to do: SEARCH for an existing employee's information or EDIT an existing employee's information? Type 'logout' to quit. ")

    if options == "SEARCH":

        searchEmployeeInfo()

    elif options == "EDIT":

        while True:
            whichEmployee = input("Which employee's information would you like to edit? (type 'exit' to return to the main menu) ")

            if whichEmployee == "JC Denton":

                editInfo(em1)

            elif whichEmployee == "Paul Denton":

                editInfo(em2)

            elif whichEmployee == "Anna Navarre":

                editInfo(em3)

            elif whichEmployee == "Alex Jacobson":

                editInfo(em4)

            elif whichEmployee == "Sam Carter":

                editInfo(em5)

            elif whichEmployee == "exit":

                print("Returning to main menu...")
                break

            else:
                print("I'm sorry, that was not a valid input.  Please try again.")

#Confidential information and access.  Try to think of a better password, since this one is SMUGGLER'S, and that doesn't really work well
    elif options == 'bloodshot':

        print("Accessing confidential information...")
        print()

        while True:

            eliteOptions = input("Would you like to FIND or CHANGE the current state of an employee's killswitch?  Type 'exit' to return to the main menu. ")

#---------------------------------------------------------------------------- Finding killSwitch state
            if eliteOptions == "FIND":

                while True:
                    whichEm = input("Which employee would you like to search for? Note: only agents have killSwitches installed. (type 'exit' to return to the previous menu) ")
                    if whichEm == em1.name:

                        print(f"KillSwitch of {whichEm} is currently:")
                        print(em1.killSwitch)
                        print()
                        break

                    elif whichEm == em2.name:
                        
                        print(f"KillSwitch of {whichEm} is currently:")
                        print(em2.killSwitch)
                        print()
                        break

                    elif whichEm == em3.name:

                        print(f"KillSwitch of {whichEm} is currently:")
                        print(em3.killSwitch)
                        print()
                        break

                    elif whichEm == em4.name:

                        print(f"KillSwitch of {whichEm} is currently:")
                        print(em4.killSwitch)
                        print()
                        break

                    elif whichEm == em5.name:

                        print(f"KillSwitch of {whichEm} is currently:")
                        print(em5.killSwitch)
                        print()
                        break

                    elif whichEm == 'exit':
                        print("Returning to previous menu...")
                        break
                    else:

                        print("That is not an employee currently in the system.")
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------Changing killswitch state
            elif eliteOptions == "CHANGE":


                print("WARNING\nDeactivating a killswitch will reset it's countdown, and activating a killswitch will result in employee termination.")
                
                while True:
                    print()


                    changeKS = input("Which employee's killSwitch would you like to activate or deactivate? ")

                        
                    if changeKS == em1.name or changeKS == em2.name or changeKS == em3.name or changeKS == em4.name or changeKS == em5.name:

                        doubleSure = input("ARE YOU SURE YOU WANT TO DO THIS?  CHANGING A KILLSWITCH STATE CAN HAVE IRREVOCABLE CONSEQUENCES.  PROCEED? (Type 'Yes' or 'No') ")

                        if doubleSure == "Yes":

                            print("\n"*2)
                            print("As an extra security measure, please enter the password:")

                            while True:
                                extraSecurity = input("PASSWORD: ")

#the password is 'Majestic-12'
                            
                                if extraSecurity == 'Majestic-12':

                                    while True:

                                        print()
                                        AorD = input(f"ACTIVATE or DEACTIVATE {changeKS}'s killswitch? ")

                                        if AorD != 'ACTIVATE' and AorD != 'DEACTIVATE':

                                            print("Invalid entry, please try again.")

                                        else:
                                            changeKillSwitchState(changeKS, AorD)
                                            print()
                                            print("Type 'exit' to leave each following menu.")
                                            break
                                        
                                elif extraSecurity == 'exit':
                                    print("Returning to previous menu.")
                                    break
                                
                                else:
                                    secureSecurityBreach += 1
                                    print()
                                    print("INVALID PASSWORD")
                                    print()

                                    if secureSecurityBreach == 3:
                                        print("\n"*3)
                                        print("THREE ATTEMPTS FAILED")
                                        print()
                                        time.sleep(.75)
                                        print("Calling security...")
                                        print()
                                        time.sleep(.75)
                                        print("SHUTTING DOWN")
                                        sys.exit()
                                    
                            
                        elif doubleSure == "No":
                            print("KillSwitch change aborted.\nReturning to previous menu.")
                            print()
                            
                        else:

                            print("For safety and security, any answer that is not 'Yes' is interpreted as an abort action.\nReturning to previous menu.")

                    elif changeKS == 'exit':
                        print("Returning to previous menu...")
                        break

                    else: print("That is not an employee currently in the system.")
                    
                
            elif eliteOptions == 'exit':

                print("Returning to main menu...")
                time.sleep(1)
                print("\n"*8)
                break
            else:
                
                print("That is not a valid option.")
                    

    elif options == 'logout':

        print()
        print("Logging out...")
        time.sleep(2)
        break

    else:
        print("I'm sorry, that is not a valid option.  Please try again.  Try typing 'SEARCH' or 'EDIT'.")

