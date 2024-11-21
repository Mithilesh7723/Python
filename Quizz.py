class User:
    def __init__(self, username, password):  
        self.username = username
        self.password = password


class Question:
    def __init__(self, question, options, correct_answer): 
        self.question = question
        self.options = options
        self.correct_answer = correct_answer


class Quiz:
    def __init__(self, questions):  
        self.questions = questions
        self.score = 0

    def present_question(self, question):
        print(question.question)
        for i, option in enumerate(question.options):
            print(f"{i + 1}. {option}")

    def get_user_answer(self, question):
        while True:
            try:
                user_answer = int(input("Enter the number of your answer: "))
                if 1 <= user_answer <= len(question.options):  
                    return user_answer
                else:
                    print("Invalid input. Please choose a valid option number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_answer(self, question, user_answer):
        if question.options[user_answer - 1] == question.correct_answer:
            self.score += 1
            print("Correct answer!")
        else:
            print(f"Sorry, the correct answer is {question.correct_answer}.")

    def run_quiz(self):
        for question in self.questions:
            self.present_question(question)
            user_answer = self.get_user_answer(question) 
            self.check_answer(question, user_answer)
        print(f"Quiz finished! Your final score is {self.score} out of {len(self.questions)}.")


users = []


def register(username, password):
    new_user = User(username, password)
    users.append(new_user)
    print(f"User '{username}' registered successfully!")


def login(username, password):
    for user in users:
        if user.username == username and user.password == password:
            print(f"User '{username}' logged in successfully!")
            return True
    print("Login failed. Please check your username and password.")
    return False


questions = [
    Question("Which element has the chemical symbol 'O'?", ["Oxygen", "Osmium", "Oganesson", "Oxide"], "Oxygen"),
    Question("What is the smallest prime number?", ["1", "2", "3", "5"], "2"),
    Question("What is the square root of 64?", ["6", "7", "8", "9"], "8"),
    Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], "Mars"),
    Question("Who wrote 'Hamlet'?", ["William Shakespeare", "Charles Dickens", "J.K. Rowling", "Jane Austen"], "William Shakespeare"),
    Question("What is the boiling point of water at sea level in Celsius?", ["90", "100", "110", "120"], "100"),
    Question("Who discovered penicillin?", ["Alexander Fleming", "Marie Curie", "Louis Pasteur", "Isaac Newton"], "Alexander Fleming"),
    Question("What is the longest river in the world?", ["Amazon", "Nile", "Yangtze", "Mississippi"], "Nile"),
    Question("Which country is known as the Land of the Rising Sun?", ["Japan", "China", "South Korea", "Thailand"], "Japan"),
    Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "Blue Whale"),
]

def main():
    while True:
        print("\nWelcome!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login(username, password):
                quiz = Quiz(questions)
                quiz.run_quiz()
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

