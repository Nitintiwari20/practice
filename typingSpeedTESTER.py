import time

paragraph = """
Python is one of the most popular programming languages in the world.
It is easy to learn, powerful, and widely used in web development,
data science, artificial intelligence, and automation.
"""

print("=" * 60)
print("           TYPING SPEED TESTER")
print("=" * 60)

print("\nType the following paragraph exactly as shown:\n")
print(paragraph)

input("\nPress Enter when you're ready to start...")

start_time = time.time()

typed_text = input("\nStart typing:\n\n")

end_time = time.time()

time_taken = end_time - start_time

original_words = paragraph.split()
typed_words = typed_text.split()

correct_words = 0

for i in range(min(len(original_words), len(typed_words))):
    if original_words[i] == typed_words[i]:
        correct_words += 1

accuracy = (correct_words / len(original_words)) * 100

wpm = (len(typed_words) / time_taken) * 60

print("\n" + "=" * 60)
print("                 RESULTS")
print("=" * 60)

print(f"Time Taken : {time_taken:.2f} seconds")
print(f"Words Typed: {len(typed_words)}")
print(f"WPM        : {wpm:.2f}")
print(f"Accuracy   : {accuracy:.2f}%")

if wpm >= 60:
    print("Performance: Excellent 🚀")
elif wpm >= 40:
    print("Performance: Good 👍")
elif wpm >= 20:
    print("Performance: Average 🙂")
else:
    print("Performance: Needs Practice 💪")