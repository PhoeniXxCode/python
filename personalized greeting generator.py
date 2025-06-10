def greeting_card(name, occasion, relation, msg):
    print("\n------------")
    print("Hey %s!" % name)
    print("Hello %s!" % occasion)
    print("You are an amazing %s!" % relation)
    print("%s!" % msg)
    print("Have a fantastic day!")
    print("------------\n")

print("Personalised greeting card generator!\n")
name = input("Enter the name of the person: ")
occasion = input("Enter the occasion: ")
relation = input("Enter your relation with the person (e.g., friend, sister): ")
msg = input("Enter your custom message: ")

greeting_card(name, occasion, relation, msg)

