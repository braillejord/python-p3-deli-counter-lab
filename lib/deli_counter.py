katz_deli = []


def line(katz_deli):
    if katz_deli == []:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        for index, customer in enumerate(katz_deli):
            message += " " f"{index + 1}. {customer}"
        print(message)


def take_a_number():
    pass


def now_serving():
    pass
