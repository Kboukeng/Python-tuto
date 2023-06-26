subjects: tuple[str, str, str] = ("maths", "phy", "chem")
print(subjects)
print(len(subjects))


for sub in subjects:
    print("I do", sub)


print(subjects[1])


add_sub: tuple[str, str, str] = ("frech", "english", "bio")
T_sub = subjects + add_sub
print(T_sub)


course = input("Enter your course")
if course in T_sub:
    print("yes", course, "is in our list")
else:
    print("no", course, "is not in our list")
