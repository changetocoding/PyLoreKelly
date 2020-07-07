from tracker.core.expense import Expense


class Budget:
    def __init__(self):
        self.budget = 0
        self.expenses = []

    def set_budget(self, amount):
        self.budget = amount

    def total_spent(self):
        return sum([expense.amount for expense in self.expenses]) # list comprehension

    def budget_left(self):
        return self.budget - self.total_spent()

    def add_expense(self, expense):
        self.expenses.append(expense)

    def report(self):
        rtn_dict = {}
        for expense in self.expenses:
            if expense.category in rtn_dict:
                rtn_dict[expense.category] += expense.amount
            else:
                rtn_dict[expense.category] = expense.amount

        return rtn_dict

    def penny_foolish(self):
        penny_total = 0.0
        pound_total = 0.0
        for expense in self.expenses:
            if expense.amount > 20:
                pound_total += expense.amount
            else:
                penny_total += expense.amount

        return penny_total > pound_total

    def average_spend(self, days):
        return self.total_spent() / days

    def most_expensive(self):
        expensive = Expense('None', 0.0, 'None')
        for expense in self.expenses:
            if expense.amount > expensive.amount:
                expensive = expense

        return expensive

