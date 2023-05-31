def trivia():
    questions = [
        {
            'question': "What fast-food item was added to the McDonald's menu in 1968?",
            'options': ["Chicken McNuggets", "Big Mac"],
            'answer': 2
        },
        {
            'question': "Biggie fries were discontinued in 2006 by what fast-food chain?",
            'options': ["In-n-out", "Wendy's"],
            'answer': 2
        },
        {
            'question': "Who is the mascot for McDonald's?",
            'options': ["Ronald McDonald", "Ronald Burger"],
            'answer': 1
        },
        {
            'question': "What is the sister chain to the west-coast hamburger chain Carl's Jr.?",
            'options': ["Subway", "Hardees"],
            'answer': 2
        },
        {
            'question': "What famous fast-food company lost a lawsuit for intentionally making their coffee too hot?",
            'options': ["Sonic", "McDonalds"],
            'answer': 2
        }
    ]

    attempts = 0
    max_attempts = 3
    score = 0
    incorrect_answers = []

    while attempts < max_attempts:
        attempts += 1
        print(f"Fast Food trivia - Attempt {attempts}")
        print(" ")

        for i, question in enumerate(questions):
            print(f"Question {i + 1}: {question['question']}")
            for j, option in enumerate(question['options']):
                print(f"{j + 1}. {option}")

            answer = input("Your answer (enter the option number): ")
            try:
                answer = int(answer)
                if answer == question['answer']:
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect!")
                    incorrect_answers.append((question, answer))
            except ValueError:
                print("Invalid input. Skipping this question.")

            print()

        if attempts < max_attempts:
            retake_quiz = input("Do you want to retake the trivia? (yes/no): ")
            if retake_quiz.lower() != "yes":
                break

    print("Trivia completed!")
    print("You scored:", score)

    if len(incorrect_answers) > 0:
        print("\nQuestions answered incorrectly:")
        for i, (question, user_answer) in enumerate(incorrect_answers):
            print(f"\nQuestion {i + 1}: {question['question']}")
            print("Your answer:", question['options'][user_answer - 1])
            print("Correct answer:", question['options'][question['answer'] - 1])


trivia()
