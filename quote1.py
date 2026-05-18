import random
import time

# Motivational quotes for developers
quotes = [
    "Code never lies, comments sometimes do.",
    "First, solve the problem. Then, write the code.",
    "Every expert was once a beginner.",
    "Push yourself, because no one else is going to do it for you.",
    "Small progress is still progress.",
    "Debugging is like being a detective in a crime movie."
]

# Fun developer tips
coding_tips = [
    "Use meaningful variable names.",
    "Practice coding every day.",
    "Read error messages carefully.",
    "Keep your GitHub active with small projects.",
    "Learn by building real projects."
]

print("\n🚀 Welcome to Dev Motivation Generator 🚀\n")
time.sleep(1)

while True:
    print("Choose an option:")
    print("1. Get a motivational quote")
    print("2. Get a coding tip")
    print("3. Exit")

    choice = input("\nEnter your choice (1-3): ")

    if choice == "1":
        print("\n💡 Quote:")
        print(random.choice(quotes))
        print()

    elif choice == "2":
        print("\n Coding Tip:")
        print(random.choice(coding_tips))
        print()

    elif choice == "3":
        print("\n👋 Keep coding!")
        break

    else:
        print("\n❌ Invalid choice. Please try again.\n")
