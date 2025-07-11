# Python code for Grading System
def calculate_grade(score):
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score <= 69:
        return "B"
    elif 50 <= score <= 59:
        return "C"
    elif 45 <= score <= 49:
        return "D"
    elif 40 <= score <= 44:
        return "E"
    else:
        return "F"

def main():
    try:
        score = float(input("Enter your score (0-100): "))
        if 0 <= score <= 100:
            grade = calculate_grade(score)
            print(f"Your grade is: {grade}")
        else:
            print("Invalid score")
    except ValueError:
        print("Please enter a valid number")

if __name__ == "__main__":
    main()