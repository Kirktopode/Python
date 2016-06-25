record1 = {"Name":"Philip", "Phone":"303-422-5647", "Grade":3, "GPA":2.489, "Balance":5.32}
record2 = {"Name":"Sally", "Phone":"303-212-0901", "Grade":5, "GPA":3.0, "Balance":10.2}
record3 = {"Name":"Xenodorf", "Phone":"303-321-5455", "Grade":1, "GPA":0.01, "Balance":250.0}
records = [record1, record2, record3]
def UpdateGPA(student,record):
    print "\nGPA of " + str(student) + " is", record["GPA"]
    newGPA = raw_input("What would you like to update GPA to?")
    try:
        newGPA = float(newGPA)
        if newGPA >= 0 and newGPA <= 4:
            record["GPA"] = newGPA
            print "GPA updated to", record["GPA"]
        else:
            print "Invalid GPA."
    except:
        print "Invalid entry."
def UpdateGrade(student, record):
    print "\nGrade of " + str(student) + " is", record["Grade"]
    newGrade = raw_input("What would you like to update Grade to?")
    try:
        newGrade = float(newGrade)
        if newGrade >= 1 and newGrade <= 12 and newGrade%1 == 0:
            newGrade = int(newGrade)
            record["Grade"] = newGrade
            print "Grade updated to", record["Grade"]
        else:
            print "Invalid Grade."
    except:
        print "Invalid entry."
def UpdatePhone(student, record):
    print "\nPhone number of " + str(student) + " is", record["Phone"]
    newPhone = raw_input("What would you like to update phone number to? ")
    phone1 = newPhone[1:3]
    phone2 = newPhone[5:7]
    phone3 = newPhone[8:12]
    if newPhone.count("-") == 2 and phone1.isdigit() == True and phone2.isdigit() == True and phone3.isdigit() == True and len(newPhone) == 12:
        record["Phone"] = newPhone
        print "Phone number updated to", record["Phone"]
    else:
        print "Invalid phone number. Must be in format XXX-XXX-XXXX (digits only)."
def Deposit(student, record):
    print "\n" + str(student) + "'s current balance is", record["Balance"], "dollars."
    dep = raw_input("How much would you like to deposit? ")
    try:
        dep = float(dep)
        record["Balance"]+= dep
        print "Balance is now at", record["Balance"], "dollars."
    except:
        print "Invalid input."
def Withdraw(student, record):
    print "\n" + str(student) + "'s current balance is", record["Balance"], "dollars."
    wit = raw_input("How much would you like to withdraw? ")
    try:
        wit = float(wit)
        record["Balance"]-= wit
        print "Balance is now at", record["Balance"], "dollars."
    except:
        print "Invalid input."
def NegPrint():
    x = 0
    print "\n"
    for record in records:
        if record["Balance"] < 0:
            print record["Name"], "currently has a balance of", record["Balance"], "dollars."
            x += 1
    if x == 0:
        print "No accounts have a negative balance."
while True:
    print "\nStudent files:", record1["Name"] + ",", record2["Name"] + ",", record3["Name"]
    act = raw_input("What do you want to do?\n1. Update GPA.\n2. Update grade level\n3. Change phone number\n4. Deposit money to an account\n5. Withdraw money from an account\n6. Print a list of students who have a negative account balance. ")
    x = 0
    if act == "1":
        student = raw_input("\nWhich student would you like to update? ")
        for record in records:
            if record["Name"] == student:
                UpdateGPA(student,record)
                x += 1
        if x == 0:
            print "Invalid name."
    elif act == "2":
        student = raw_input("\nWhich student would you like to update? ")
        for record in records:
            if record["Name"] == student:
                UpdateGrade(student,record)
                x += 1
        if x == 0:
            print "Invalid name."
    elif act == "3":
        student = raw_input("\nWhich student would you like to update? ")
        for record in records:
            if record["Name"] == student:
                UpdatePhone(student, record)
                x += 1
        if x == 0:
            print "Invalid name."
    elif act == "4":
        student = raw_input("\nFor whom would you like to make a deposit? ")
        for record in records:
            if record["Name"] == student:
                Deposit(student, record)
                x += 1
        if x == 0:
            print "Invalid name."
    elif act == "5":
        student = raw_input("\nFor whom would you like to make a withdrawal? ")
        for record in records:
            if record["Name"] == student:
                Withdraw(student, record)
                x += 1
        if x == 0:
            print "Invalid name."
    elif act == "6":
        NegPrint()
    else:
        print "Invalid."
    
