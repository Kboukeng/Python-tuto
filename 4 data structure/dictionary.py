# Dictionary decleration
marks: dict[str, int] = {
    "maths": 15,
    "phy": 12,
    "chem": 9,
}


# Print the content of the dictionary
print("marks:", marks)


# Print the keys of the dictionary ie subjects
for subject in marks.keys():
    print(subject)


# Print the value of each key ie marks
for score in marks.values():
    print(score)


# Print out the key and value
for subject, score in marks.items():
    print(subject, ":", score, "/20")


# Cherck if he passed in his subjects
for subject, score in marks.items():
    if score >= 10:
        print(subject, ":", score, "/20", "pass")
    else:
        print(subject, ":", score, "/20", "failed")


# Updating a value in the dictionary
marks["chem"] = 14
print(f"Your chemistry mark is: {marks['chem']}")


# Creating new key and value in the dictionary
marks["bio"] = 15


for subject, score in marks.items():
    if score >= 10:
        print(subject, ":", score, "/20", "pass")
    else:
        print(subject, ":", score, "/20", "failed")



# Getting marks for a given subject:

# uption 1
phy_m = marks["phy"]
print(f"You scored {phy_m} in physics")

# Uption 2
bio_m = marks.get("bio")
print(f"You scored {bio_m} in biology")

# Uption 3
econs_m = marks.get("econs")
if econs_m is None:
    print(f"You do not study economics.")
else:
    print(f"You scored {econs_m} in economics.")


# delete a key and value from the dictionary
del marks["maths"]
print(marks)
