
def parse_as_expense(comma_string):
    split = comma_string.split(',')
    if len(split) != 3:
        raise ValueError('comma_string should be a comma seperated string with 3 parts. But was %s' % comma_string)

    # what we do here is catch the error raised by converting to float so we can raise a nicer exception message
    try:
        amount = float(split[1])  # This raises a value error if it fails
        return Expense(split[0], amount, split[2])
    except ValueError:
        raise ValueError('comma_string should be a comma separated string with the middle part as a float. But was %s' % comma_string)


class Expense:
    def __init__(self, name, amount, category):
        self.name = name.strip()
        self.category = category.strip()
        self.amount = amount

    def __str__(self):
        return '%s, %s, %s' % (self.name, self.amount, self.category)