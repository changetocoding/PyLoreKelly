# start with creating class and dictionary
command_start = ">command: "
phone_book = {"kelly": 4725692, "lore": 542652}

#print(new_list)

while True:
    print(command_start)
    input_user = input()
    input_list = input_user.split()
    command = input_list[0]
    if command == "add":
        name = "" # David Don't need this line. Why?
        number = 0 # David Don't need this line. Why?
        name = input_list[1]
        number = input_list[2]
        phone_book[name] = number  # David: There is a mistake here...
        print("The account for %s with number %011d has been added." % (name, int(number)))
    elif command == "query":
        name = ""
        number = 0
        number = input_list[1]


        if number.isdigit():
            name_for_no = ""
            list_numbers = phone_book.items()
            for new_number in list_numbers:  # David: new_number is a bad name
                if new_number[1] == int(number):
                    name_for_no = new_number[0]

                # David: how many times does this get printed
                print("The number %011d is linked to %s." % (int(number), name_for_no))

            if name_for_no == "":
                print("This number is not included in the phonebook. Please try again.")


        else:
            phone_book.get(name,"This name is not included in the phonebook"
            )
            name = input_list[1]
            number = phone_book[name]
            print("The number %011d is linked to %s." % (int(number), name))
    else:
        print("This account is not included in the phonebook, please try again.")

#print(phone_book)