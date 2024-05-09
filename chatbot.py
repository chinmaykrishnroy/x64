import random
import re

# Define responses for the chatbot
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "hi": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm good, how about you?", "I'm great, thanks for asking!"],
    "what's your name": ["I'm just a chatbot!", "You can call me ChatBot.", "I don't have a name, but you can call me whatever you like!"],
    "what is your name": ["I'm just a chatbot!", "You can call me ChatBot.", "I don't have a name, but you can call me whatever you like!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"],
    "thank you": ["You're welcome!", "No problem!", "Anytime!"],
    "game": ["Let's play a game! Choose a number between 1 and 5.", "I'm up for a game! Pick a number between 1 and 5."],
    "1": ["You chose 1!", "Going with 1!"],
    "2": ["You chose 2!", "Picking 2!"],
    "3": ["You chose 3!", "Opting for 3!"],
    "4": ["You chose 4!", "Selecting 4!"],
    "5": ["You chose 5!", "Going with 5!"],
    "engineering": ["As a computer engineering student, you must be learning about algorithms, data structures, and more!", "Computer engineering is an exciting field that combines hardware and software aspects."],
    "year": ["In your third year, you might be studying advanced topics like operating systems, computer networks, and software engineering principles."],
    "hobbies": ["What are your hobbies? As a computer engineering student, you might enjoy programming, electronics tinkering, or even gaming!"],
    "projects": ["Have you worked on any interesting projects? Building projects is a great way to apply your skills and learn new things!"],
    "future": ["What are your plans after graduating? With a computer engineering degree, you'll have a wide range of career opportunities in areas like software development, hardware engineering, and more!"],
    "ai units": ["Chapter 1: AI - The Concept\nChapter 2: State Space Search\nChapter 3: Heuristic Search\nChapter 4: Adversarial Search and Games in AI\nChapter 5: Constraint Satisfaction\nChapter 6: Knowledge Representation Issues\nChapter 7: Logical Agents and Knowledge Representation using Propositional Logic\nChapter 8: First Order Logic - Predicate Logic\nChapter 9: Reasoning and inferencing using First Order Logic\nChapter 10: Knowledge Representation and Ontological Engineering\nChapter 11: AI Planning\nChapter 12: Programming in AI using Prolog"],
    "cloud computing units": ["Unit 1: Introduction to cloud computing\nUnit 2: Data storage and cloud computing\nUnit 3: Virtualization in Cloud Computing\nUnit 4: Cloud platform and cloud application\nUnit 5: Security in cloud computing\nUnit 6: Advanced techniques in cloud computing"],
    "another": ["Let's play a guessing game! I'm thinking of a number between 1 and 100. Try to guess it!"],
    "age": ["Sure, let me guess your age! Please enter remainders when dividing your age by 3, 5, and 7."]
}

# Regular expressions for identifying phone numbers, OTPs, email addresses, and website URLs
phone_number_pattern = re.compile(r'\b\d{10}\b')
otp_pattern = re.compile(r'\b\d{4,8}\b')
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
website_pattern = re.compile(r'\b(?:https?://|www\.)\S+\b')

# Function to handle user input and generate responses
def chat():
    print("Welcome to the ChatBot!")
    print("You can start chatting or type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()  # Convert user input to lowercase
        
        if (user_input == "bye" or user_input == "exit" or user_input == "quit"):
            print(random.choice(responses["bye"]))
            break  # Exit the loop if the user says 'bye'
        else:
            found_response = False
            
            for pattern, response_list in responses.items():
                if re.search(pattern, user_input):
                    if pattern == "another":
                        play_guessing_game()
                    elif pattern == "age":
                        calculate_age()
                    else:
                        print(random.choice(response_list))  # Respond with a random message from the responses
                    found_response = True
                    break
            
            if not found_response:
                if re.search(phone_number_pattern, user_input):
                    print("This looks like a phone number!")
                elif re.search(otp_pattern, user_input):
                    print("This looks like an OTP!")
                elif re.search(email_pattern, user_input):
                    print("This looks like an email address!")
                elif re.search(website_pattern, user_input):
                    print("This looks like a website URL!")
                else:
                    print("I'm not sure how to respond to that. Can you ask me something else?")

# Function to play a guessing game
def play_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100. Try to guess it!")
    
    while True:
        user_guess = int(input("Your guess: "))
        attempts += 1
        
        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
            break

# Function to calculate age based on remainders
def calculate_age():
    print("Sure, let me guess your age! Please enter remainders when dividing your age by 3, 5, and 7.")
    rem3 = int(input("Remainder when dividing by 3: "))
    rem5 = int(input("Remainder when dividing by 5: "))
    rem7 = int(input("Remainder when dividing by 7: "))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print(f"Your age is approximately {age} years!")

# Start the chat
chat()
