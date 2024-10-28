
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Paris", "C) Madrid", "D) Rome"],
        "answer": "B"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A) William Shakespeare", "B) Charles Dickens", 
                    "C) Leo Tolstoy", "D) Mark Twain"],
        "answer": "A"
    },
    {
        "question": "What is the result of 3 + 2 * 2?",
        "options": ["A) 10", "B) 7", "C) 8", "D) 9"],
        "answer": "B"
    },
    {
        "question": "Who is CEO of Google?",
        "options": ["A) Bill Gates", "B) Mark Zukerberg", "C) Sundar Pichai", "D) Elon Musk"],
        "answer": "C"
    }
]
name=input(str("What is your name? "))
def run_quiz():
    print("Welcome to the Quiz",name,"! Please answer these easy 5 questions on General Knowlegde.\n")
    score = 0

    # Loop through each question
    for i, data in enumerate(quiz_data, start=1):
        print(f"Q{i}. {data['question']}")
        for option in data["options"]:
            print(option)

        # Get user input and validate it
        answer = input("Your answer (A, B, C, D): ").strip().upper()
        if answer == data["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {data['answer']}.\n")

    # Display the final score
    print(f"Your final score is {score} out of {len(quiz_data)}.")

if __name__ == "__main__":
    run_quiz()