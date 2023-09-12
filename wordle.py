import random

def give_instructions():
    print('''\n Wordle is a word guessing game.
        You have 5 attempts to guess the word.
        ✔️ means the letter is in the word and in the correct position.
        ❌ means the letter is in the word but not in the correct position.
         _ means the letter is not in the word.
          
          Best of Luck''')



words =["five", "lake", "pink", "stew", "help", "crew", "cart"]
hidden_word = random.choice(words)


def check_word(guess):
    if hidden_word == guess:
        print("Congrats!! You did it.")
        return True
    else: 
        result = ""
        for i, j in zip(guess, hidden_word):
            if i == j:
                result = result + " ✔️ "
            elif i in hidden_word:
                result = result + " ❌ "
            else:
                result = result + " _ "
        print(result)
        return False


def main():
    attempt = 5
    give_instructions()
    while attempt > 0: 
        guess = input("Guess a four-letter word: ")
        if check_word(guess):
            break
        else:
            attempt -= 1
            print(f"You have {attempt} attemps left.")
    else:
        print("GAME OVER")

main()

