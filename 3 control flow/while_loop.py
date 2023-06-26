

C_guess: bool = False
guess: str = ""
country: str = "cameroon"


# ALTERNATIVE 1:

# Initiating a while loop with a condition
# while C_guess is not True:
    
#     # Asking the user to guess a country then storing it in guess we declared above
#     guess = input("Guess my country:  ")
#     print(f"You entered {guess}")
    
#     # Check if the country entered by the user is the one we declared above  
#     if guess == country:
#         print("correct")
#         print("")
#         C_guess = True
#     else:
#         print("wrong, try again.")
#         print("-----------------")
#         print("")
        
        

# ALTERNATIVE 2:
# Initiating a while loop with a condition
while True:
    
    # Asking the user to guess a country then storing it in guess we declared above
    guess = input("Guess my country:  ")
    print(f"You entered {guess}")
    
    # Check if the country entered by the user is the one we declared above  
    if guess == country:
        print("correct")
        print("")
        break
    else:
        print("wrong, try again.")
        print("-----------------")
        print("")
        
        
        
        
        
        
        

i=1
while i < 100:
    i = i + 2
    i2 = i + 1
    print(12)