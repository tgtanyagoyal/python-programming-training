day = input("Enter a day of the week: ").lower()

match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("It is a Weekday.")
    case "saturday" | "sunday":
        print("It is a Weekend.")
    case _:
        print("Invalid day entered.")
