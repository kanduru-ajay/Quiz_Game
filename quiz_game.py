questions = [
    {
        "question": "1. Which language is used for Python programming?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. Java"],
        "answer": "B"
    },
    {
        "question": "2. Which function is used to display output in Python?",
        "options": ["A. input()", "B. print()", "C. output()", "D. display()"],
        "answer": "B"
    },
    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "4. Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Float", "D. Boolean"],
        "answer": "D"
    },
    {
        "question": "5. Which loop is used to repeat code in Python?",
        "options": ["A. for", "B. switch", "C. case", "D. define"],
        "answer": "A"
    }
]

score = 0

print("================================")
print("       WELCOME TO QUIZ GAME     ")
print("================================")

for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    while True:
        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input! Please enter A, B, C, or D.")

    if user_answer == question["answer"]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")
        print("Correct answer:", question["answer"])

print("\n================================")
print("          QUIZ COMPLETED        ")
print("================================")

print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100

print("Percentage:", percentage, "%")

if percentage == 100:
    print("Excellent! Perfect Score!")
elif percentage >= 60:
    print("Good Job! Keep Learning!")
else:
    print("Keep Practicing! You Can Do Better!")

print("Thank you for playing!")
