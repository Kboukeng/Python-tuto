friends: list[str] = ["fab", "bro", "sist", "cho"]
print(friends)
print()

for f in friends:
    print(f"Yo {f}")

print(f"friends lenth {len(friends)}")

# Remove an item from our list
remove = friends.pop()
print(f"removed {remove}")
print(friends)

# Add an item to our list
friends.append("karl")
print(f"friends: {friends}")

# Check item at given position
print(friends[2])

# Remove item from given position
remove = friends.pop(2)
print(f"removed {remove}")
print(friends)

# Insert an item at a given position
friends.insert(0, "luis")
print(friends)

# Check if an item is present in our list
if "luis" in friends:
    print("yes")
else:
    print("no")

friends.append("bob")
print(friends)

print(friends[4])


delete = friends.pop(3)
print("I removed", delete)


name = input("Enter the name:")
if name in friends:
    print("yes")
else:
    print("no")


friends.sort()
print(friends)

friends.reverse()
print(friends)
