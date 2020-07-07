import tracker.console.consoleUI as console

if __name__ == "__main__":
    console.start_up()

    should_continue = True
    while should_continue:
        should_continue = console.get_user_input()