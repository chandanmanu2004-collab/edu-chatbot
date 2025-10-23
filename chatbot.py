# Simple Edu Chatbot

definitions = {
    "photosynthesis": "Photosynthesis is the process by which green plants use sunlight to make food from carbon dioxide and water.",
    "atom": "An atom is the smallest unit of matter that retains the properties of an element.",
    "gravity": "Gravity is the force that attracts objects toward the center of the Earth or any other physical body having mass.",
}

def chatbot():
    print("Hello! I am your Edu Chatbot. Ask me any definition question.")
    while True:
 question = input("Student: ").lower()
        found = False
        for term in definitions:
            if term in question:
                print(f"Chatbot: {definitions[term]}")
                found = True
                break
        if not found:
            print("Chatbot: Sorry, I don't know the definition for that yet.")
        if question in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break

if _name_ == "_main_":
    chatbot()
