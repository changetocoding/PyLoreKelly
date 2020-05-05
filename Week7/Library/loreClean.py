# start with creating class and dictionary
command_start = ">command: "
phone_book = {"kelly": 4725692, "lore": 542652}
no_dict = {4725692 :"kelly", 542652: "lore" }

#print(new_list)

while True:
    print(command_start)
    input_user = input()
    input_list = input_user.split()
    command = input_list[0]
    if command == "add":
        name = input_list[1]
        number = input_list[2]
        phone_book[name] = int(number)
        no_dict[int(number)] = name

        print("The account for %s with number %011d has been added." % (name, int(number)))
    elif command == "query":
        if input_list[1].isdigit():
            #number = input_list[1]
            #name_for_no = ""
            #list_numbers = phone_book.items()
            #for new_number in list_numbers:  # David: new_number is a bad name
            #    if new_number[1] == int(number):
            #        name_for_no = new_number[0]

            #if name_for_no == "":
            #    print("This number is not included in the phonebook. Please try again.")
            #else:
            #    print("The number %011d is linked to %s." % (int(number), name_for_no))
            number = int(input_list[1])
            name = no_dict[number]
            print("The number %011d is linked to %s." % (int(number), name))

        else:
            name = input_list[1]
            number = phone_book[name]
            print("The number %011d is linked to %s." % (int(number), name))
    else:
        print("This account is not included in the phonebook, please try again.")

#print(phone_book)