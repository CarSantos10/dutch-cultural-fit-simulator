# Dutch Cultural Fit Simulator
# Created by: Carlos Santos

score = 0

print("Welcome to the Dutch Cultural Fit Simulator!")
print("Let's see how well your style fits Dutch work culture.\n")

# Question 1 - Directness
answer1 = input("Do you like to say what you think directly, even if it sounds harsh? (yes/no): ").lower().strip()

while answer1 != "yes" and answer1 != "no":
    print("Invalid answer. Please type only 'yes' or 'no'.")
    answer1 = input("Do you like to say what you think directly, even if it sounds harsh? (yes/no): ").lower().strip()

if answer1 == "yes":
    score = score + 1

# Question 2 - Lunch
answer2 = input("Do you prefer a quick, simple lunch over a long meal? (yes/no): ").lower().strip()

while answer2 != "yes" and answer2 != "no":
    print("Invalid answer. Please type only 'yes' or 'no'.")
    answer2 = input("Do you prefer a quick, simple lunch over a long meal? (yes/no): ").lower().strip()

if answer2 == "yes":
    score = score + 1

# Question 3 - Punctuality
answer3 = input("Do you value punctuality? (yes/no): ").lower().strip()

while answer3 != "yes" and answer3 != "no":
    print("Invalid answer. Please type only 'yes' or 'no'.")
    answer3 = input("Do you value punctuality? (yes/no): ").lower().strip()

if answer3 == "yes":
    score = score + 1

# Question 4 - Communication style
answer4 = input("Do you prefer direct or indirect communication? (direct/indirect): ").lower().strip()

while answer4 != "direct" and answer4 != "indirect":
    print("Invalid answer. Please type only 'direct' or 'indirect'.")
    answer4 = input("Do you prefer direct or indirect communication? (direct/indirect): ").lower().strip()

if answer4 == "direct":
    score = score + 1

# Question 5 - Leaving on time
answer5 = input("Do you prefer to leave work on time, even with pending tasks? (yes/no): ").lower().strip()

while answer5 != "yes" and answer5 != "no":
    print("Invalid answer. Please type only 'yes' or 'no'.")
    answer5 = input("Do you prefer to leave work on time, even with pending tasks? (yes/no): ").lower().strip()

if answer5 == "yes":
    score = score + 1

# Final result
print("\nYour final score was:", score)

if score >= 3:
    print("Congratulations! You have a great fit with Dutch work culture!")
else:
    print("You still have a bit to learn about Dutch culture, but you're on the right track!")