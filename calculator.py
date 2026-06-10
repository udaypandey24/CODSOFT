print("===== SMART CALCULATOR =====")

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "7":
        print("Calculator Closed.")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid Choice!")
        continue

    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    if choice == "1":
        result = first_number + second_number
        operation = "+"

    elif choice == "2":
        result = first_number - second_number
        operation = "-"

    elif choice == "3":
        result = first_number * second_number
        operation = "*"

    elif choice == "4":
        if second_number == 0:
            print("Division by zero is not allowed!")
            continue
        result = first_number / second_number
        operation = "/"

    elif choice == "5":
        result = first_number ** second_number
        operation = "^"

    elif choice == "6":
        result = first_number % second_number
        operation = "%"

    print(f"{first_number} {operation} {second_number} = {result}")
