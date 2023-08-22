katz_deli = []


def line(katz_deli):
    if katz_deli == []:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        for index, customer in enumerate(katz_deli):
            message += " " f"{index + 1}. {customer}"
        print(message)


def take_a_number(katz_deli, customer):
    # add new customer to line before creating/printing message
    katz_deli.append(customer)

    print(f"Welcome, {customer}. You are number {len(katz_deli)} in line.")


def now_serving(katz_deli):
    if katz_deli == []:
        print("There is nobody waiting to be served!")
    else:
        customer = katz_deli.pop(0)
        print(f"Currently serving {customer}.")
