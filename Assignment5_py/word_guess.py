import random

LEXICON_FILE = "Assignment5/Lexicon.txt"    # File to read word list from
#LEXICON_FILE = "Assignment5/TestLexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with

italics = '\033[3m'
plain = '\033[0m'

def replace_nth(s, index, c):
    chars = list(s)
    chars[index] = c
    res = "".join(chars)
    return res

def play_game(secret_word):

    #step 1.The word now looks like this: -----
    guess_word=''
    for i in range(len(secret_word)):
        guess_word = guess_word+"-"
    print("The word now looks like this:",guess_word)

    guess_cnt = INITIAL_GUESSES
    while guess_cnt>0:
        #step 2.You have x guesses left
        print("You have",guess_cnt,"guesses left")
        #step 3.input a letter
        letter=input("Type a single letter here, then press enter:"+italics)

        if len(letter) > 1:
            print(plain+"Guess should only be a single character.")
        else:
            correct_guess=0
            # print(plain+"")
            for i in range(len(secret_word)):
                #step 4.That guess is correct.
                if letter.upper()==secret_word[i].upper():
                    correct_guess=1
                    guess_word=replace_nth(guess_word,i,secret_word[i])

            if correct_guess==1:
                print(plain+"That guess is correct.")
                if guess_word.count('-') == 0:
                    print("Congratulations, the word is:",secret_word)
                    exit()
                else:
                    print("The word now looks like this:",guess_word)
            #step 4. that guess is incorrect
            else:
                print(plain+"There are no ",letter.upper(),"'s in the word",sep="")
                print("The word now looks like this:",guess_word)
                guess_cnt -= 1

    print("Sorry, you lost. The secret word was:",secret_word)


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    index = random.randrange(3)
    if index == 0:
        return 'HAPPY'
    elif index == 1:
        return 'PYTHON'
    else:
        return 'COMPUTER'


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    # part 1 - word from 3 word
    secret_word = get_word()
    play_game(secret_word)

    # part 2 - word from Lexicon
    file = open(LEXICON_FILE)
    word_list=[]
    for line in file:
        line = line.strip()
        word_list.append(line)

    ran_num = random.randrange(len(word_list))
    play_game(word_list[ran_num])


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()