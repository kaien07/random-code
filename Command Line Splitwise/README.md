# Task
Write a Python script that:

1. Gets a list of expenses: Each expense is represented as a dictionary that includes the amount paid and the name of the person who paid it
2. Calculates total expenses and individual shares: Determine the total amount spent, how much each person has paid, and how much each person owes / is owed.
3. Prints a summary of transactions: Print the transactions needed for everyone to settle their debts, showing who owes whom and how much.

# Example Input
Your program should be able to process input like the following:
```
expenses = [
    {"amount": 120, "paid_by": "Alice"},
    {"amount": 140, "paid_by": "Bob"},
    {"amount": 190, "paid_by": "Charlie"},
    {"amount": 90, "paid_by": "Alice"},
]
```

# Example output
```
Total Expense: $540.00
Each person's share: $180.00

Transactions to settle up:
Bob owes Alice: $30.00
Bob owes Charlie: $10.00
```
