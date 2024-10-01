import os

# Function to create an MCQ-based quiz and save it to a file
def create_mcq_quiz(file_name):
    with open(file_name, 'w') as file:
        num_questions = int(input("Enter the number of questions: "))
        for i in range(1, num_questions + 1):
            question = input(f"Enter question {i}: ")
            print("Enter 4 options for this question:")
            option_a = input("Option A: ")
            option_b = input("Option B: ")
            option_c = input("Option C: ")
            option_d = input("Option D: ")
            correct_option = input("Enter the correct option (A/B/C/D): ").upper()
            
            # Writing question, options, and the correct answer in the file
            file.write(f"{question}?|{option_a}|{option_b}|{option_c}|{option_d}|{correct_option}\n")
        print(f"MCQ Quiz created successfully in {file_name}.")

# Function to take the MCQ quiz and calculate score
def take_mcq_quiz(file_name):
    if not os.path.exists(file_name):
        print(f"Quiz file {file_name} not found!")
        return
    
    score = 0
    total_questions = 0
    with open(file_name, 'r') as file:
        for line in file:
            total_questions += 1
            # Splitting the stored format: question?|option_a|option_b|option_c|option_d|correct_option
            data = line.strip().split('|')
            question = data[0]
            options = data[1:5]  # The 4 options
            correct_option = data[5]
            
            # Display the question and options
            print(f"\n{question}")
            print(f"A. {options[0]}")
            print(f"B. {options[1]}")
            print(f"C. {options[2]}")
            print(f"D. {options[3]}")
            
            # Get user's answer
            user_answer = input("Your answer (A/B/C/D): ").upper()
            if user_answer == correct_option:
                score += 1

    print(f"\nYou got {score}/{total_questions} correct!")
    record_score(score, total_questions)

# Function to record the user's score
def record_score(score, total):
    name = input("Enter your name: ")
    with open("scores.txt", 'a') as file:
        file.write(f"{name}: {score}/{total}\n")
    print("Your score has been recorded!")

# Main Program
def main():
    while True:
        print("\nQuiz System Menu:")
        print("1. Create a new MCQ quiz")
        print("2. Take the MCQ quiz")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            file_name = input("Enter the quiz file name (e.g., mcq_quiz.txt): ")
            create_mcq_quiz(file_name)
        elif choice == '2':
            file_name = input("Enter the quiz file name to take the quiz (e.g., mcq_quiz.txt): ")
            take_mcq_quiz(file_name)
        elif choice == '3':
            print("Exiting the quiz system. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
