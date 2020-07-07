from tracker.core.budget import Budget
import tracker.core.expense # initially had this as budget.core.expense but conflicts with budget = Budget() below so renamed this to tracker.core.expense. Could have renamed budget = Budget() to budget_tracker = Budget() instead
import traceback
import tracker.input.csvReader as csvReader


budget = Budget()

def start_up():
    start_up_help()
    expenses = csvReader.read_csv()
    for expense in expenses:
        budget.add_expense(expense)


def start_up_help():
    print('Welcome to your budget')
    print('Accepted commands: ')
    print('Shortcode: -> Command(case insensitive): parameters -> Description')
    print('b -> Budget: Number                  -> Sets the budget for the month to 100"')
    print('e -> Expense: Name, Amount, Category -> Sets an expense')
    print('r -> Report                          -> Prints report')
    print('ml -> Money Left                     -> How much money do I have')
    print('p -> Penny Pound                     -> Did I spend more money on items less than £20 or items more than £20 ')
    print('a -> Average: Days                   -> Average spend over N days')
    print('x -> Expensive                       -> Most expensive item')
    print('Exit                                 -> Exits script')
    print('')


def get_user_input():
    try:
        user_input = input('Enter a command:\n')
        split = user_input.split(':')
        command = split[0].lower().strip()

        if command == 'budget' or command == 'b':
            budget.set_budget(float(split[1]))
            print('Your budget is now %.2f ' % budget.budget)

        elif command == 'expense' or command == 'e':
            expense = tracker.core.expense.parse_as_expense(split[1])
            budget.add_expense(expense)

        elif command == 'report' or command == 'r':
            report()

        elif command == 'money left' or command == 'ml':
            print('You have £%.2f left' % budget.budget_left())

        elif command == 'penny pound' or command == 'p':
            if budget.penny_foolish():
                print('You were penny foolish (spent more on items under £20)')
            else:
                print('You were pound foolish (spent more on items over £20)')

        elif command == 'average' or command == 'a':
            if len(split) != 2:
                raise ValueError('Expecting a number of days to work out the average over')

            average = budget.average_spend(int(split[1]))
            print('Your average spend per a day was £%.2f' % average)

        elif command == 'expensive' or command == 'x':
            expensive = budget.most_expensive()
            print('You spent a whopping £%.2f on %s' % (expensive.amount, expensive.name))

        elif command == 'exit':
            return False

        else:
            print('Unexpected command. Did you forget to put a : maybe?')
    except Exception as ex:
        print(ex)
        traceback.print_exc()

    return True


def report():
    report_dict = budget.report()
    print('Expenses by category:')
    for category, total in report_dict.items():
        print('%s : %.2f' % (category, total))


