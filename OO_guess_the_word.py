word_to_guess = "pog"
word_leng = len(word_to_guess)
win = False
guesses = 5


def guess_word(guesses,word,word_leng):
    if guesses == 5 :
        print("you have 5 guesses to guess the word")
    else:
        print("you have {} guesses left".format(guesses))
    if guesses == 4:
        print("the first letter is {}".format(word[0]))
    elif guesses == 1:
        print("the last letter is {}".format(word[word_leng - 1]))
    while True:
        guess = input("guess the word ").lower().strip()
        if guess.isdigit():
            print("<error> please enter a word not a number")
        else:
            break
    if guess == word:
        win = True
    else:
        guesses -= 1
        win = False

    output = [guesses,win]
    return output


print("the word to guess has {} letters".format(word_leng))

while win == False and guesses > 0:
    guess_output = guess_word(guesses,word_to_guess,word_leng)
    guesses = guess_output[0]
    win = guess_output[1]
    print("")

if win == True:
    print("Correct, you win!")
else:
    print("Incorrect, you lose")
