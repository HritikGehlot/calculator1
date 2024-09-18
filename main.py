
import os
import askii_art
print(askii_art.calc_photo)

def calculator(n1, n2, operation):
    if operation == "+":
        return n1 + n2
    elif operation == "-":
        return n1 - n2
    elif operation == "*":
        return n1 * n2
    elif operation == "/":
        return n1 / n2
    else:
        print("Invalid operation!")

calculation_history = []
should_continue = True

n1 = int(input("Enter the first number: "))

while should_continue:
    n2 = int(input("Enter the second number: "))
    operation = input("What calculation you want to do (+, -, *, /): ")

    result = calculator(n1, n2, operation)
    print(f"Result: {result}")

    
    calculation_history.append(f"{n1} {operation} {n2} = {result}")
    
    
    continue_choice = input("Do you want to continue with this result? (y to continue, n to start new): ").lower()

    if continue_choice == 'n':
        should_continue = False
        os.system('cls')
        print(f"Result: {result}\n")
        print("Calculation history:")
        for entry in calculation_history:
            print(entry)
        askii_art.thank_you()    

    elif continue_choice == 'y':
        
        n1 = result
    else:
        print("Invalid choice, exiting.")
        should_continue = False


        