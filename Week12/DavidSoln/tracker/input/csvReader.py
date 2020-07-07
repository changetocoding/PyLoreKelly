from tracker.core.expense import parse_as_expense

def read_csv():
    lines = read_file()
    result = process_lines(lines)
    return result


def read_file():
    with open('BankStatement.csv', 'r') as reader:
        return [line.rstrip() for line in reader.readlines()]


def process_lines(lines):
    expenses = []
    for line in lines[1:]: # we skip first line as that is the header
        expense = parse_as_expense(line)
        expense.amount = expense.amount * -1 # we flip sign on expenses
        if expense.amount > 0:
            # only add to list if amount is > 0
            expenses.append(expense)
    return expenses
