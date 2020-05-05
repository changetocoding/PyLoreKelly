# DAVID: Nice fixed comments from last time
command = "Please enter an instruction "

phone_book = {"kelly": 4725692, "lore": 542652}

while True:
    print(command)
    user_prompt_text = input()
    new_list = user_prompt_text.split()

    # DAVID: Good spliting out into new better named variables (new_list[0] can be confusing later in the code)
    user_prompt_text = new_list[0] # Don't understand why you reused user_prompt_text rather than a new name: Can be confusing later
    name = new_list[1]

    if user_prompt_text == "add":
        # Good
        name = new_list[1] # DAVID: lol and you didnt use name: Dont need this line as already done this
        number = new_list[2]
        phone_book[name] = number
        print("This has been added \n")
    elif user_prompt_text == "query":
        name = ""         # David Why set this and one below
        number = 0

        # David: just need below 3 lines but good
        name = new_list[1]
        new_number = phone_book.get(name)
        print(name, new_number)

    # David: What is wrong with this if statement
    elif user_prompt_text == "query":
        name = ""
        number = 0
        number = new_list[2]
        phone_book[number] = name # this wont work
        print(name, number)