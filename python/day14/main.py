# Day 14: Higher or lower game project

from random import choice



people = [
    {"name": "Charli D'Amelio", "followers": 150_000_000, "platform": "TikTok"},
    {"name": "MrBeast", "followers": 100_000_000, "platform": "YouTube"},
    {"name": "Addison Rae", "followers": 88_000_000, "platform": "TikTok"},
    {"name": "Khaby Lame", "followers": 160_000_000, "platform": "TikTok"},
    {"name": "LeBron James", "followers": 140_000_000, "platform": "Instagram"},
    {"name": "Neymar Jr.", "followers": 210_000_000, "platform": "Instagram"},
    {"name": "Emma Chamberlain", "followers": 16_000_000, "platform": "Instagram"},
    {"name": "Zendaya", "followers": 180_000_000, "platform": "Instagram"},
    {"name": "James Charles", "followers": 22_000_000, "platform": "YouTube"},
    {"name": "Logan Paul", "followers": 25_000_000, "platform": "Instagram"},
    {"name": "Kylie Jenner", "followers": 380_000_000, "platform": "Instagram"},
    {"name": "Dwayne 'The Rock' Johnson", "followers": 370_000_000, "platform": "Instagram"},
    {"name": "Ariana Grande", "followers": 370_000_000, "platform": "Instagram"},
    {"name": "Selena Gomez", "followers": 430_000_000, "platform": "Instagram"},
    {"name": "Kim Kardashian", "followers": 350_000_000, "platform": "Instagram"},
    {"name": "Taylor Swift", "followers": 270_000_000, "platform": "Instagram"},
    {"name": "Shakira", "followers": 100_000_000, "platform": "Instagram"},
    {"name": "Cristiano Ronaldo", "followers": 610_000_000, "platform": "Instagram"},
    {"name": "Lionel Messi", "followers": 480_000_000, "platform": "Instagram"},
    {"name": "Billie Eilish", "followers": 110_000_000, "platform": "Instagram"},
    {"name": "Drake", "followers": 140_000_000, "platform": "Instagram"},
    {"name": "Bad Bunny", "followers": 60_000_000, "platform": "Instagram"},
    {"name": "Doja Cat", "followers": 30_000_000, "platform": "Instagram"},
    {"name": "Cardi B", "followers": 150_000_000, "platform": "Instagram"},
    {"name": "Beyoncé", "followers": 320_000_000, "platform": "Instagram"},
    {"name": "Kendall Jenner", "followers": 290_000_000, "platform": "Instagram"},
    {"name": "Post Malone", "followers": 26_000_000, "platform": "YouTube"},
    {"name": "Jackie Chan", "followers": 20_000_000, "platform": "Instagram"},
    {"name": "Chris Hemsworth", "followers": 60_000_000, "platform": "Instagram"},
    {"name": "Will Smith", "followers": 65_000_000, "platform": "Instagram"},
    {"name": "Virat Kohli", "followers": 260_000_000, "platform": "Instagram"}
]

from random import choice

def higher_or_lower(list_of_dict):
    """
    A game where the player guesses who has more followers between two people.

    The game uses a list of dictionaries, where each dictionary represents a person
    with their name, follower count, and platform. The player is presented with two people
    (randomly selected from the list) and must guess which one has a higher follower count.
    The game continues until the player makes an incorrect guess or chooses to stop playing.

    Parameters:
    ----------
    list_of_dict : list
        A list of dictionaries containing people's data in the format:
        {"name": str, "followers": int, "platform": str}

    Gameplay:
    --------
    - The player is prompted to start the game.
    - Two people are selected randomly from the list.
    - The player guesses who has more followers ('A' or 'B').
    - If the guess is correct, the score increases, and the game continues with a new comparison.
    - If the guess is incorrect, the game ends, and the final score is displayed.

    Example Dictionary:
    -------------------
    people = [
        {"name": "Charli D'Amelio", "followers": 150_000_000, "platform": "TikTok"},
        {"name": "MrBeast", "followers": 100_000_000, "platform": "YouTube"}
    ]

    Example Usage:
    --------------
    higher_or_lower(people)

    Notes:
    ------
    - This game requires the `random.choice` function to work.
    - Handles user input errors (e.g., invalid guess or quit command).

    Returns:
    -------
    None
    """
    playing = True
    score = 0
    first_person = choice(list_of_dict)
    wanna_play = input("\nWanna Play? 'yes' or 'no' ").lower()
    while playing:
        if wanna_play == 'yes':
            second_person = choice(list_of_dict)
            while second_person == first_person:
                second_person = choice(list_of_dict)
            print(f"\nFirst person: {first_person['name']} is being compared against Second person: {second_person['name']}\n")
            guess = input(f"By followers, Who's more popular A: {first_person['name']} or B: {second_person['name']}: ").upper()
            if (guess == 'A' and first_person['followers'] > second_person['followers']) or (guess == 'B' and first_person['followers'] < second_person['followers']):
                print("Correct!!")
                score += 1
                first_person = second_person if first_person["followers"] < second_person["followers"] else first_person
            else:
                print(f"Wrong pick!!\nYour Score is {score}")
                break
            print(f"Your Score is {score}")
        elif wanna_play == 'no':
            playing = False
            print("Goodbye!!!")
        else:
            print("Wrong Input!!!")
            
higher_or_lower(people)
