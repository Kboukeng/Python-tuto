

fav_color: str = input("Enter your favorate color: ")
print(fav_color)

match fav_color:
    case "blue":
        print("You like blue")
    case "red":
        print("You like red")
    case "black":
        print("You like black")
    case "white":
        print("You like white")
    case _:
        print(f"You like {fav_color}")