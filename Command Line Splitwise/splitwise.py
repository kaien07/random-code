# get list of expenses in list of dictionaries
expense_list = []
name_list = []
get_amt = True
while get_amt:
    name = input("Name (to end type 'end'): ")
    if name == "end":
        get_amt = False
        break
    amt = input("Amount paid: ")
    if amt.isdigit():
        amt = float("%.2f" % float(amt))
        if name not in name_list:
            expense_list.append({"amount": amt, "paid_by": name.capitalize()})
            name_list.append(name)
        else:
            index = name_list.index(name)
            amt += expense_list[index].get("amount")
            expense_list[index].update({"amount": amt})
    else:
        print("Input invalid.")

# calculate total expenses (sum of all expenses)
total_expense = 0
for elem in expense_list:
    total_expense += elem.get("amount")
print(f"Total Expense: ${total_expense:.2f}")

# calculate each persons share (total exp/ppl)
share = total_expense / len(name_list)
print(f"Each person's share: ${share:.2f}\n")

# transactions to settle up
print("Transactions to settle up:")

# find who paid less than their share
owe_list = []
for elem in expense_list:
    if elem.get("amount") < share:
        owe_list.append({"name": elem.get("paid_by"), "owe": (share - elem.get("amount"))})

# find who paid more than their share
owed_list = []
for elem in expense_list:
    if elem.get("amount") > share:
        owed_list.append({"name": elem.get("paid_by"), "owed": (elem.get("amount") - share)})

# subtract from both lists
while len(owe_list) != 0 and len(owed_list) != 0:
    person_owe = owe_list[0].get("name")
    amt_owe = owe_list[0].get("owe")
    person_owed = owed_list[0].get("name")
    amt_owed = owed_list[0].get("owed")
    if amt_owe >= amt_owed:
        owe_list[0].update({"owe": (amt_owe - amt_owed)})
        owed_list[0].update({"owed": 0})
        print(f"{person_owe} owes {person_owed}: ${amt_owed:.2f}")
    elif amt_owe < amt_owed: # amt owed is more than one person owes (someone has to be paid more than once)
        owe_list[0].update({"owe": 0})
        owed_list[0].update({"owed": (amt_owed - amt_owe)})
        print(f"{person_owe} owes {person_owed}: ${amt_owe:.2f}")
    if owe_list[0].get("owe") == 0 or owe_list[0].get("owe") == 0.0:
        owe_list.pop(0)
    if owed_list[0].get("owed") == 0 or owed_list[0].get("owed") == 0.0:
        owed_list.pop(0)
