## Day 14 - Beginner | Capstone Project: The Higher Lower Game
## 10.06.2023

from day14Utils import logo, vs, data
import random

is_continue = True
total_score = 0

def play_game(data):
    global is_continue, total_score, start_idx1, start_idx2

    print(f"Compare A: {data[start_idx1]['name']}, a/an {data[start_idx1]['description']}, "
          f"from {data[start_idx1]['country']}")
    print(vs)
    print(f"Against B: {data[start_idx2]['name']}, a/an {data[start_idx2]['description']}, "
          f"from {data[start_idx2]['country']}")
    guess_high_low = input("Who has more followers? Type 'A' or 'B': ")
    if (data[start_idx1]['follower_count'] > data[start_idx2]['follower_count']) and (guess_high_low.lower() == 'a'):
        print(f"CORRECT! When {data[start_idx2]['name']} has {data[start_idx2]['follower_count']}, "
              f"{data[start_idx1]['name']} has {data[start_idx1]['follower_count']}\n")
        start_idx2 = random.choice(range(len(data)))
        while start_idx1 == start_idx2:
            start_idx2 = random.choice(range(len(data)))
        total_score += 1
        play_game(data)
    elif (data[start_idx1]['follower_count'] < data[start_idx2]['follower_count']) and (guess_high_low.lower() == 'b'):
        print(f"CORRECT! When {data[start_idx2]['name']} has {data[start_idx2]['follower_count']}, "
              f"{data[start_idx1]['name']} has {data[start_idx1]['follower_count']}\n")
        start_idx1 = random.choice(range(len(data)))
        while start_idx1 == start_idx2:
            start_idx1 = random.choice(range(len(data)))
        old_start_idx2 = start_idx2
        start_idx2 = start_idx1
        start_idx1 = old_start_idx2
        total_score += 1
        play_game(data)
    else:
        print(f"When {data[start_idx2]['name']} has {data[start_idx2]['follower_count']}, "
              f"{data[start_idx1]['name']} has {data[start_idx1]['follower_count']}\nYou lose :(")
        print(f"\nYour total score is: {total_score}")
        is_continue = False


print(logo)
print('Welcome to Higher or Lower Game!')
start_idx1 = random.choice(range(len(data)))
start_idx2 = random.choice(range(len(data)))
while start_idx1 == start_idx2:
    start_idx2 = random.choice(range(len(data)))

while is_continue == True:
    play_game(data)