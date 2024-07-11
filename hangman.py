from random_word import RandomWords
hangman_structure=[ """
                    -------------
                    |           |
                    |           |
                                |
                                |
                                |
                                |""",
                    """
                    -------------
                    |           |
                    |           |
                    O           |
                                |
                                |
                                |""",
                    """
                    -------------
                    |           |
                    |           |
                    O           | 
                    |           |
                                |
                                |
                                |""",
                    """
                    -------------
                    |           |
                    |           |
                    O           |
                   /|           |
                                |
                                |
                                |""",
                     """
                    -------------
                    |           |
                    |           |
                    O           |
                   /|\          |
                                |
                                |
                                |""",
                     """
                    -------------
                    |           |
                    |           |
                    O           |
                   /|\          |
                   /            |
                                |
                                |""",
                     """
                    -------------
                    |           |
                    |           |
                    O           |
                   /|\          |
                   / \          |
                                |
                                |"""
                    
                              
]

def choose_word():
    print("Welcome to hangman game!")
    list_of_words=RandomWords()
    word=list_of_words.get_random_word()
    return word
def word_space(word):
    word_space_area=[]
    for i in range(len(word)):
        word_space_area.append("_")
    print(word_space_area)
    return word_space_area
def get_guess():
    guess=input("Guess a letter:")
    return guess
def check_guess(guess,word,word_space_area,hangman_count):
    
    if guess in word:
        for i in range(len(word)):
            if guess==word[i]:
                word_space_area[i]=guess
        print("Congratulations!! Your Guess is correct")
        print(word_space_area)
    else:
        hangman_count+=1
        print(hangman_structure[hangman_count])
        print("Oops! Your guess is wrong.")
    return int(hangman_count),word_space_area


def main():
    word=choose_word()
    word_space_area=word_space(word)
    hangman_count = 0
    while hangman_count <6:
        guess=get_guess()
        hangman_count,word_space_area=check_guess(guess,word,word_space_area,hangman_count)
        if "_" not in word_space_area:
            print("Congrats")
    else:
        print("Game Over!!")
        print(hangman_structure[6])
        print("The word is",word)

main()