print("Match and Point!!!")
while True:
    animal = input("Enter an animal: ")
    if(animal=="exit"):
        break
    match animal:
        case "cat":
            print("You chose a cat!")
        case "dog":
            print("You chose a dog!")
        case "bird":
            print("You chose a bird!")
        case _:
            print("Unknown animal.")