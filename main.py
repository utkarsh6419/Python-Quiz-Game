"""A short multiple-choice quiz."""

QUESTIONS = [
    ("What is the capital of France?", {"a": "Paris", "b": "Rome", "c": "Madrid"}, "a"),
    ("How many continents are there?", {"a": "5", "b": "7", "c": "9"}, "b"),
    ("Which planet is known as the Red Planet?", {"a": "Mars", "b": "Venus", "c": "Jupiter"}, "a"),
    ("Which language runs this program?", {"a": "Python", "b": "HTML", "c": "SQL"}, "a"),
    ("What is 9 × 8?", {"a": "63", "b": "72", "c": "81"}, "b"),
]


def main():
    score = 0
    for question, answers, correct in QUESTIONS:
        print("\n" + question)
        for key, answer in answers.items():
            print(f"  {key}) {answer}")
        if input("Answer: ").strip().lower() == correct:
            score += 1
            print("Correct!")
        else:
            print(f"The correct answer was {correct}.")
    print(f"\nFinal score: {score}/{len(QUESTIONS)}")


if __name__ == "__main__":
    main()
