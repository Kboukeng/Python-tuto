from typing import Final

COOLBLACK_ATTACK_POWER: int = 200
COLASUCRE_ATTACK_POWER: int = 200
GRANDK_ATTACK_POWER: int = 150
JUSTICIERDEKOABAN_ATTACK_POWER: Final[int] = 250

lascar_life: int = 1200
choice = 0
attack_num: int = 0

WIN_MSG: Final[str] = "Congrt you saved Yaoundé"
LOOS_MSG: Final[str] = "You failed to save Yaoundé"

MESSAGE: str = """"
------------------------------------------------------------------------
Yaoundé is under attack by someone called Lascar, choose your heros to 
attack him

1) cool black and cola sucré
2) cola sucré and grand K
3) grand K and justicier de koaban
4) justicier de koaban and cool black
------------------------------------------------------------------------
"""
while True:
    print(MESSAGE)
    choice = int(input("Choose your players: "))
    match choice:
        case 1:
            print("cool black and cola sucré attack lascar.....")
            lascar_life = lascar_life - COOLBLACK_ATTACK_POWER - COLASUCRE_ATTACK_POWER
            attack_num = attack_num + 1
            print()
        case 2:
            print("cola sucré and grand K attack lascar.....")
            lascar_life = lascar_life - COLASUCRE_ATTACK_POWER - GRANDK_ATTACK_POWER
            attack_num = attack_num + 1
            print()
        case 3:
            print("grand K and justicier de koaban attack lascar.....")
            lascar_life = (
                lascar_life - GRANDK_ATTACK_POWER - JUSTICIERDEKOABAN_ATTACK_POWER
            )
            attack_num = attack_num + 1
            print()
        case 4:
            print("justicier de koaban and cool black attack lascar.....")
            lascar_life = (
                lascar_life - JUSTICIERDEKOABAN_ATTACK_POWER - COOLBLACK_ATTACK_POWER
            )
            attack_num = attack_num + 1
            print()

    if lascar_life <= 0 and attack_num <= 3:  # win
        print(WIN_MSG)
        break
    elif attack_num >= 3:  # loos
        print(LOOS_MSG)
        break
