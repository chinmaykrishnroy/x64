# Import the necessary libraries
import random

# Define the knowledge base
knowledge_base = {
    "If the patient has a fever, then they may have a cold.": True,
    "If the patient has a cough, then they may have a cold.": True,
    "If the patient has a runny nose, then they may have a cold.": True,
}

# Define the rules
rules = [
    "If the patient has a fever and a cough, then they definitely have a cold.",
    "If the patient has a fever and a runny nose, then they probably have a cold.",
    "If the patient has a cough and a runny nose, then they might have a cold.",
]

# Define the function to find the diagnosis
def find_diagnosis(symptoms):
    # Check if the symptoms match any of the rules
    for rule in rules:
        # Split each rule into individual symptoms and check if all of them are present in the input symptoms
        if all(symptom in symptoms for symptom in rule.split(" ")):
            return rule  # Return the matched rule as the diagnosis

    # If no rules match, then return a random diagnosis from the knowledge base
    return random.choice(list(knowledge_base.keys()))

# Get the symptoms from the user
symptoms = input("What are your symptoms? ").split(" ")

# Find the diagnosis
diagnosis = find_diagnosis(symptoms)

# Print the diagnosis
print("The diagnosis is:", diagnosis)