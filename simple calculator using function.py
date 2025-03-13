def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def display_operations():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

def main():
    display_operations()
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice not in ('1', '2', '3', '4'):
        print("Invalid input! Please select a valid operation.")
        return
    
    try:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return
    
    if choice == '1':
        print(f"{n1} + {n2} = {add(n1, n2)}")
    elif choice == '2':
        print(f"{n1} - {n2} = {sub(n1, n2)}")
    elif choice == '3':
        print(f"{n1} * {n2} = {mul(n1, n2)}")
    elif choice == '4':
        print(f"{n1} / {n2} = {div(n1, n2)}")

if __name__ == "__main__":
    main()
