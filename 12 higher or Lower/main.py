import art
import indian_data
import random

data_len = len(indian_data.data)-1
score = 0
is_right_answer = False

while not is_right_answer:

    print(art.logo)

    if score:
        print("You're right! Current score: ", score)

    first_idx = random.randint(0, data_len)
    print(f"Campare A: {indian_data.data[first_idx]["name"]}, {indian_data.data[first_idx]["description"]}, {indian_data.data[first_idx]["country"]}.")

    print(art.vs)

    second_idx = random.randint(0, data_len)

    while first_idx == second_idx:
        second_idx = random.randint(0, data_len)

    print(f"Against B: {indian_data.data[second_idx]["name"]}, {indian_data.data[second_idx]["description"]}, {indian_data.data[second_idx]["country"]}.")

    your_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    if your_answer == "A":
        if indian_data.data[first_idx]["follower_count"] > indian_data.data[second_idx]["follower_count"]:
            score += 1
        else:
            is_right_answer = not is_right_answer
    else:
        if indian_data.data[first_idx]["follower_count"] < indian_data.data[second_idx]["follower_count"]:
            score += 1
        else:
            is_right_answer = not is_right_answer

    for _ in range(100):
        print("\n")

    if is_right_answer:
        print(art.logo)
        print("Sorry, that's wrong. Final score: ", score)