from random import choice
question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

class User:
    """
    Represents a user participating in a quiz game.

    Attributes:
        name (str): The name of the user.
        age (int): The age of the user.
        score (int): The user's current score in the quiz.
        playing (bool): A flag indicating whether the user is actively playing the game.
    """

    def __init__(self, name, age):
        """
        Initializes a new User object.

        Args:
            name (str): The name of the user.
            age (int): The age of the user.

        Prints:
            A welcome message including the user's name.
        """
        print(f"Welcome {name}")
        self.name = name
        self.age = age
        self.score = 0

    def ask_questions(self):
        """
        Asks the user a random True or False question from the question data.

        The method selects a random question, prompts the user for an answer,
        and updates the user's score based on correctness. If the answer is
        incorrect, the game ends by setting `self.playing` to False.

        Raises:
            KeyError: If the selected question does not contain 'text' or 'answer' keys.
        """
        question = choice(question_data)
        answer = input(f"{question['text']} True or False? ").capitalize()
        if answer == str(question['answer']):
            self.score += 1
            print(f"Correct!...your score is {self.score}")
        else:
            print(f"Wrong...Goodbye...your score is {self.score}")
            self.playing = False
    
    def playing(self):
        """
        Starts the game loop for the user.

        While the `playing` attribute is True, the user is repeatedly asked questions.
        The game stops when the `playing` attribute is set to False (e.g., after a wrong answer).
        """
        self.playing = True
        while self.playing:
            self.ask_questions()



user1 = User("joshua", 19)

user1.playing()