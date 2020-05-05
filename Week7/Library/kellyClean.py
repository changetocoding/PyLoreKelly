# DAVID: Nice fixed comments from last time
command = "Please enter an instruction "

phone_book = {"kelly": 1111, "lore": 542652}
no_dict = {1111 :"kelly", 542652: "lore" }

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
        number = int(new_list[2])
        phone_book[name] = number
        no_dict[number] = name
        print("This has been added \n")

    elif user_prompt_text == "query":
        if new_list[1].isdigit():
            number = int(new_list[1])
            name = no_dict.get(number)
            print(name, number)

        else:
            # David: just need below 3 lines but good
            name = new_list[1]
            new_number = phone_book.get(name)
            print(name, new_number)