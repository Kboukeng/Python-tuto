# TRUTH TABLE
# AND:
# T and T = T 
# F and F = F 
# T and F = F 
# F and T = F 

# OR:
# T or T = T 
# F or F = F 
# T or F = T 
# F or T = T 



age: int = 20
country: str = "Cameroon"

if age < 20 and country == "Cameroon":
    print("You can't have a licence")
elif age >= 20 and country == "Cameroon":
    print("You can have a licence")
elif age < 20 and country == "france":
    print("You can apply for a french licence")