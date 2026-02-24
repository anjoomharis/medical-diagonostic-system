def diagnose():
    print("=== Medical Diagnosis System ===")
    print("Please answer the following questions with yes or no.\n")

    symptoms = {}

    questions = {
        "fever": "Do you have fever?",
        "cough": "Do you have cough?",
        "body_pain": "Do you have body pain?",
        "headache": "Do you have headache?",
        "sneezing": "Do you have sneezing?",
        "runny_nose": "Do you have runny nose?",
        "chills": "Do you have chills?",
        "sweating": "Do you have excessive sweating?",
        "loss_of_taste": "Do you have loss of taste or smell?",
        "fatigue": "Do you feel fatigue?"
    }

    for symptom, question in questions.items():
        answer = input(question + " (yes/no): ").strip().lower()
        symptoms[symptom] = True if answer == "yes" else False

    diseases = {
        "Flu": ["fever", "cough", "body_pain", "fatigue"],
        "Common Cold": ["cough", "sneezing", "runny_nose"],
        "Malaria": ["fever", "chills", "sweating", "headache"],
        "COVID-19": ["fever", "cough", "loss_of_taste", "fatigue"],
        "Migraine": ["headache", "fatigue"]
    }

    print("\n--- Diagnosis Result ---")

    best_match = None
    highest_score = 0

    for disease, disease_symptoms in diseases.items():
        match_count = 0
        for symptom in disease_symptoms:
            if symptoms.get(symptom):
                match_count += 1

        confidence = (match_count / len(disease_symptoms)) * 100

        if confidence > highest_score:
            highest_score = confidence
            best_match = disease

    if best_match and highest_score >= 40:
        print(f"Most likely condition: {best_match}")
        print(f"Confidence level: {highest_score:.2f}%")
    else:
        print("No strong match found. Please consult a medical professional.")

    print("\nNote: please consult a doctor if it is neccessary")

if __name__ == "__main__":
    diagnose()