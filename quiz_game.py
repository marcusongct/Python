def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------------------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)
def check_answer(answer, guess):

    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

def display_score(correct_guesses, guesses):
    print("------------------------------------------")
    print("Results")
    print("------------------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int(correct_guesses/len(questions) * 100)
    print("Your score is: " + str(score) + "%")

def play_again():

    response = input("Play again? (Yes/No): ").upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
    "1. Who is the richest man on earth?: ": "A",
    "2. What year did the twin towers fall?: ": "C",
    "3. What is the most expensive spice?: ": "C",
    "4. What is the largest e-sports event prize pool ever?: ": "B"
}

options = [
    ["A. Elon Musk", "B. Jeff Bezos", "C. Bernard Arnault", "D. Mark Zuckerberg"],
    ["A. 2000", "B. 2002", "C. 2001", "D. 1998"],
    ["A. Turmeric", "B. Sumac", "C. Saffron", "D. Tarragon"],
    ["A. $10M", "B. $40M", "C. $68M", "D. $19M"]
]
new_game()

while play_again():
    new_game()

print("Thanks for playing")
