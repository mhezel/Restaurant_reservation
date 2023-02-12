
class Person:
    res_list = [] #static variable
    kids = 300
    adult = 500
    record_count = 0

    def __init__(self, name, date, _time, x , y):
        self.name = name
        self.date = date
        self._time = _time
        self.x = x
        self.y = y

    # superclass's version of display()
    def display(self):
        return "NAME: " + self.name + "\t" + "Date: " + self.date + "\t" + "Time: " + self._time + "\t" + "No of Adults: " + str(self.x) + "\t" + "No of Children: " + str(self.y) + "\t" "Subtotal: " + str(self.getTotalAmt()) + "\n"

    def getTotalAmt(self):
        return ((int(self.x) * int(Person.adult))+(int(self.x) * int(Person.kids)))

class Customer(Person):

    def view_reservation():
        # Read File
        try:
            fl = open("file.txt", "r")
        except:
            print("File not found")
        else:
            Person.res_list = fl.readlines()
            count_record = 0
            for row in Person.res_list:
                count_record += 1
                print(row)
            if count_record >= 1:
                print(str(count_record) + ' Record(s) Found.')
            else:
                print('No Record')
            fl.close()
            # print("File close")
            # ask save to textfile

    def display(self):
        print(super(Person,self).display())

def menu():
    print("################### RESTAURANT RESERVATION PROGRAM #######################")
    print("################### A.View all Reservations ##############################")
    print("################### B. Make Reservations #################################")
    print("################### C. Delete Reservations ###############################")
    print("################### D. Generate Report ###################################")
    print("################### E. Exit ##############################################")

    reserve = input("What do you wish to do: ")

    if reserve.upper() == 'A':
        p1 = Customer.view_reservation()

    if reserve.upper() == 'B':
        p1 = Person(input("Name: "), input("Date: "), input("Time: "), input("Number of Adult: "),input("Number of Children: "))
        print(p1.display())

        while True:
            try:
                q1 = input("Do you like save these in textfile? [Y/N]")
                break
            except ValueError:
                print("Invalid input. Please try again...")
        if q1.upper() == "Y":  # run add
            # saveToTextFile()
            # reserve1 = Restaurant()
            try:
                fl = open("file.txt", "a")
            except:
                print("File not found")
            else:
                fl.write(
                    "NAME: " + p1.name + "\t" + "Date: " + p1.date + "\t" + "Time: " + p1._time + "\t" + "No of Adults: " + str(p1.x) + "\t" + "No of Children: " + str(p1.y) + "\t" "Subtotal: " + str(p1.getTotalAmt()) + "\n")
            finally:
                fl.close()
        elif q1.upper() == "N":  # reload to options
            print('back to options...')

        while True:
            _next = input("Would you like to view your reservation? Please type Y/N: ")
            if _next.upper() == 'Y':
                menu()
                break
            elif _next.upper() == 'N':
                print("Thank you, Goodbye . . . .")
            else:
                print("Invalid Input Try Again")
menu()
