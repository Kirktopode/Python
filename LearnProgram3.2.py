accounts = {"Thomas" : 0, "Richard" : 0, "Harrison" : 0}
print "Accounts and balances:", accounts
x = 0
def deposit(holder):
    print "\n" + str(holder)+ "'s current balance is", str(accounts[holder]) + "."
    depnum = raw_input("How much would you like to deposit? ")
    try:
        depnum = int(depnum)
        accounts[holder] += depnum
        print str(holder)+ "'s new balance is", str(accounts[holder]) + ".\n"
    except:
        print "Invalid entry."
def withdraw(holder):
    print "\n" + str(holder)+ "'s current balance is", str(accounts[holder]) + "."
    witnum = raw_input("How much would you like to withdraw? ")
    try:
        witnum = int(witnum)
        accounts[holder] -= witnum
        print str(holder)+ "'s new balance is", str(accounts[holder]) + ".\n"
    except:
        print "Invalid entry."
def view(holder):
    print "\n" + str(holder) + "'s current balance is", str(accounts[holder]) + ".\n"
def negview():
    print "\n"
    count = 0
    for account in accounts:
        if accounts[account] < 0:
            count += 1
            print str(account) + "'s current balance is", accounts[account], "dollars."
    if count == 0:
        print "No account holders have a negative balance."
    print "\n"

while x == 0:
    act = raw_input("What would you like to do?\n1. Make a deposit for an account holder.\n2. Make a withdrawal for an account holder.\n3. Print the account balance of a given account holder.\n4. Print a list of all account holders who have negative balances. ")
    #try:
    act = int(act)
    if act == 1:
        holder = raw_input("For whom would you like to make a deposit? ")
        if holder in accounts:
            deposit(holder)
        else:
            print "Not a valid account holder."
    elif act == 2:
        holder = raw_input("For whom would you like to make a withdrawal? ")
        if holder in accounts:
            withdraw(holder)
        else:
            print "Not a valid account holder."
    elif act == 3:
        holder = raw_input("Whose account would you like to view? ")
        if holder in accounts:
            view(holder)
        else:
            print "Not a valid account holder."
    elif act == 4:
        negview()
    else:
        print "Invalid action."
    #except:
        #print "Invalid action."
