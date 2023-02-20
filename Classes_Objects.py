
class Person:
    res_list = [] #static variable
    kids = 300
    adult = 500
    record_count = 0
    countrow = 0

    def __init__(self, name, date, _time, x , y):
        self.name = name
        self.date = date
        self._time = _time
        self.x = x
        self.y = y

    # superclass's version of display()
    def display(self):
        return "NAME: " + self.name + "\t" + "Date: " + self.date + "\t" + "Time: " + self._time + "\t" + "No of Adults: " + str(self.x) + "\t\t" + "No of Children: " + str(self.y) + "\t" "Subtotal: " + str(self.getTotalAmt()) + "\n"

    def getTotalAmt(self):
        return ((int(self.x) * int(Person.adult))+(int(self.x) * int(Person.kids)))


    def setData(self):

        Person.res_list.append(self.name)
        Person.res_list.append(self.date)
        Person.res_list.append(self._time)
        Person.res_list.append(self.x)
        Person.res_list.append(self.y)

    def viewData(self):
        print("NAME: " + "\t\t" + "Date: " + "\t\t\t" + "Time: " + "\t\t" + "Adults: " + "Children: ")
        for row in Person.res_list:
                print(row, end="\t\t")
                Person.countrow += 1
                if Person.countrow >= 5:
                    print("\n")
                    Person.countrow = 0

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
            print("\n########################NOTHING FOLLOWS#################################")
            if count_record >= 1:
                print(str(count_record) + ' Record(s) Found.')
            else:
                print('No Record')
            fl.close()
            # print("File close")
            # ask save to textfile

    def viewtotal():
        #Total number of Adults: 6
        #Total number of Kids: 6
        #Grand Total: PHP 4800.00
        pass

    def display(self):
        print(super(Person,self).display())

    def deleteData(op_delete):
        lines = []
        try:
            # Open the file in read mode and read its contents
            with open('file.txt', 'r') as file:
                print("\n")
                lines = file.readlines()

            # Remove the third line (index 2)
            del lines[op_delete - 1]

            # Open the file in write mode and write the updated contents back to the file
            with open('file.txt', 'w') as file:
                file.writelines(lines)

            with open('file.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    print(line)

            while True:
                try:
                    x = input("\npress [D] to delete another reservation / [M] to go back to the menu: ").upper()
                    if x == 'D':
                        try:
                            with open("file.txt","r") as file:
                                lines = file.readlines()

                            for line in lines:
                                print(line)

                            op_delete = int(input("Select record to delete: "))
                            p1 = Customer.deleteData(op_delete)

                        except:
                            print("No record Found to be deleted")
                    elif x == 'M':
                        menu()
                except:
                        exit()
        except:
            print("File not found")

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

        while True:
            try:
                q1 = input("Would you like to try and reserve again? [Y/N]")

                if q1.upper() == 'Y':
                    menu()
                    break
                elif q1.upper() == 'N':
                    print("Thank you, Goodbye . . . .")
                    break
                else:
                    print("Invalid Input Try Again")

            except ValueError:
                print("Invalid input. Please try again...")

    if reserve.upper() == 'B':
        p1 = Person(input("Name: "),
                    input("Date-format(m-d-yyyy): "),
                    input("Time-format(h:m): "),
                    input("Number of Adult: "),
                    input("Number of Children: "))
        p1.setData()
        p1.viewData()
        print("\n")

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
                fl.write("NAME: " + p1.name + "\t" + "Date: " + p1.date + "\t" + "Time: " + p1._time + "\t" + "No of Adults: " + str(p1.x) + "\t" + "No of Children: " + str(p1.y) + "\t" "Subtotal: " + str(p1.getTotalAmt()) + "\n")
            finally:
                fl.close()
        elif q1.upper() == "N":  # reload to options
            print('back to options...')

        while True:
            _next = input("Would you like to view/make another reservation? Please type Y/N: ")
            if _next.upper() == 'Y':
                menu()
            elif _next.upper() == 'N':
                print("Thank you, Goodbye . . . .")
                break
            else:
                print("Invalid Input Try Again")

    if reserve.upper() == 'C':
        try:
            fl = open("file.txt", "r")
        except:
            print("File not found")
        else:
            Person.res_list = fl.readlines()
            count_record = 0
            for row in Person.res_list:
                count_record += 1
                #print(row)
            if count_record >= 1:
                #print(str(count_record) + ' Record(s) Found.')
                with open("file.txt","r") as file:
                    lines = file.readlines()
                for line in lines:
                    print(line)
                op_delete = int(input("Select record to delete: "))
                p1 = Customer.deleteData(op_delete)
            else:
                print('No record of Reservations found')
                print("\n")
                menu()

    if reserve.upper() == 'D':
        p1 = Customer.view_reservation()
        #p1 = Customer.view_total()

        while True:
            try:
                q1 = input("Would you like to try and reserve again? [Y/N]")

                if q1.upper() == 'Y':
                    menu()
                    break
                elif q1.upper() == 'N':
                    print("Thank you, Goodbye . . . .")
                    break
                else:
                    print("Invalid Input Try Again")

            except ValueError:
                print("Invalid input. Please try again...")

    if reserve.upper() == 'E':
        print("Thank you and come again!")
        exit()

menu()