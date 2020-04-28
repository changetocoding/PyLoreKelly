
# start with creating class and dictionary

# Good start. Next step would be making it repetitive so I can add multiple users and query multiple people. How do that?

# DAVID: x is a bad name: this should be something more meaniful like command_text, or user_prompt_text
# DAVID:  secondly as file size gets bigger try searching for x lol
x = ">command: "

# DAVID:  Good data structure choice
phone_book = {"kelly": 4725692, "lore": 542652}

# DAVID:  you should define this within the if statement where they are used
name = ""
number = 0




while True:
    print(x)
    y = input()
    new_list = y.split()
    command = new_list[0]
    if command == "add":
        name = new_list[1]
        number = new_list[2]
        phone_book[name] = number
        print("this has been added \n", x)
    elif command == "query":
        name = new_list[1]
        number = phone_book[name]
        print(number)
