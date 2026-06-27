print("=== Muhammad Saleem Information Chatbot ===")
print("Hello! Ask me about Muhammad Saleem.")
print("Type 'help' to see available questions.")
print("Type 'exit' to quit.")

while True:
    question = input("\nYour Question: ").lower()

    if question == "exit":
        print("Goodbye!")
        break

    elif question == "help":
        print("\nYou can ask:")
        print("- What is his name?")
        print("- What is his date of birth?")
        print("- Where is he from?")
        print("- Where did he complete Matric?")
        print("- Where did he complete Intermediate?")
        print("- Where did he graduate?")
        print("- What is his job?")
        print("- Is he a social worker?")
        print("- What promotion did he get?")

    elif "name" in question:
        print("His name is Muhammad Saleem.")

    elif "date of birth" in question or "birth" in question or "dob" in question:
        print("His date of birth is 1985.")

    elif "matric" in question:
        print("He completed Matric from Govt MS High School Rasheed Abad, Multan.")

    elif "intermediate" in question or "college" in question:
        print("He completed Intermediate from Govt Civil Lines College, Multan.")

    elif "graduate" in question or "graduation" in question:
        print("He graduated from Govt Civil Lines College, Multan.")

    elif "work" in question or "job" in question or "profession" in question:
        print("He worked as a Teacher.")

    elif "social worker" in question or "social" in question:
        print("Yes, he also worked as a Social Worker.")

    elif "city" in question or "where" in question:
        print("He is from Multan, Pakistan.")

    elif "promotion" in question:
        print("He was promoted from Junior Teacher to Senior Teacher.")

    else:
        print("Sorry, I don't know the answer.")
