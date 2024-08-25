import re

def check_password_complexity(password):
    complexity_score = 0
    feedback = []

    if len(password) >= 8:
        complexity_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        complexity_score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        complexity_score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    if re.search(r"[0-9]", password):
        complexity_score += 1
    else:
        feedback.append("Add at least one digit (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        complexity_score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&*(), etc.).")

    return complexity_score, feedback

def main():
    password = input("Enter your password: ")
    score, feedback = check_password_complexity(password)

    if score == 5:
        print("Password is Very Strong")
    elif score == 4:
        print("Password is Strong")
    elif score == 3:
        print("Password is Moderate")
    elif score == 2:
        print("Password is Weak")
    elif score == 1:
        print("Password is Very Weak")
    else:
        print("Password must be at least 8 characters long")

    if feedback:
        print("\nFeedback on your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()
