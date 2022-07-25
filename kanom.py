"""hiwwwww"""
def main():
    """snack"""
    money = int(input())
    water = int(input())
    snack_1 = int(input())
    snack_2 = int(input())
    snack_3 = int(input())
    cost = 0
    num1 = (money-water)%3
    if num1 == 0:
        kanom = 10
    elif num1 == 1:
        kanom = 15
    elif num1 == 2:
        kanom = 20
    money2 = (money-water)-kanom
    num2 = money2%3
    if num2 == 0:
        kanom2 = 12
    elif num2 == 1:
        kanom2 = 15
    elif num2 == 2:
        kanom2 = 18
    money3 = money2-kanom2
    num3 = money3%3
    if num3 == 0:
        kanom3 = 5
    elif num3 == 1:
        kano3 = 7
    elif num3 == 2:
        kanom3 = 9

main()
