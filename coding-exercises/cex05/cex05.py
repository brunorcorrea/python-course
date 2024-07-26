should_continue = True

while should_continue:
    user_input = input("Choose one option (q or p): ")
    if user_input == "p":
        print("Hello")
    elif user_input == "q":
        should_continue = False