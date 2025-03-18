print("Welcome to the name and greet program!")
name = input("Please enter your name: ")
print(f"Hi {name}! How would you like to be greeted?")
print("1. Say hello")
print("2. Wave")
print("3. Smile")
choice = input("Enter your choice (1/2/3): ")
if choice == "1":
    print(f"Hello {name}, wishing you a pleasant day from here")
elif choice == "2":
    print(f"Nice to meet you {name}! Waves")
elif choice == "3":
    print(f"It's so nice to meet you with a smile {name}. The Lord is your strength")
else:
    print("Invalid choice. Please enter 1, 2 or 3.")
print("Thanks for using the name and greet program!")