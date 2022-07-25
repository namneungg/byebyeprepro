"""araiwa"""
def main():
    """araiwa"""
    grade = float(input())
    grade2 = float(4-grade)
    if grade < 1.00:
        print("I'm so sad.")
    elif grade < 2.00 and grade >= 1.00:
        print("%.2f" %grade2)
    elif grade <= 4 and grade >= 2:
        print("I'm so happy.")
main()
