"""There is 5 function in this file,
which are creating game Target with english words"""
import random
def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    list_prygol = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p",\
"q", "r", "s", "t", "v", "w", "x", "z"]
    list_golosnі = ["a", "e", "i", "o", "u" ,"y"]
    global sumar_elem
    global sumar_elem_2
    rnd_consonants = random.sample(list_prygol, 6)
    rnd_vowels = random.sample(list_golosnі, 3)
    rnd_lst0 = [*rnd_consonants[:2], rnd_vowels[0]]
    rnd_lst1 = [*rnd_consonants[2:4], rnd_vowels[1]]
    rnd_lst2 = [*rnd_consonants[4:], rnd_vowels[2]]
    sumar_elem=[]
    sumar_elem.append(rnd_lst0)
    sumar_elem.append(rnd_lst1)
    sumar_elem.append(rnd_lst2)
    sumar_elem_2=rnd_lst0+rnd_lst1+rnd_lst2
    return sumar_elem

def get_words(f: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    global sumar_elem_2
    maybe_word=[]
    with open(f,'r', encoding="utf-8") as file:
        for line in file:
            line=line.strip().lower()
            verifying_1=all((letter in letters) for letter in line)
            verifying_2=all(line.count(letter) <= letters.count(letter) for letter in letters)
            if len(line)>=4 and letters[4] in line and verifying_1 and verifying_2:
                maybe_word.append(line)
    return maybe_word


def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    user_input=[]
    try:
        while True: #точно?
            print("Please suggest your words here:")
            z=input()
            user_input.append(z)
    except EOFError:
        return user_input
def get_pure_user_words(user_words: list[str], letters: list[str], words_from_dict: list[str]) -> list[str]:
    """
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    response_a=[]
    response_b=[]
    resp_false=[]
    for elem in user_words:
        if elem not in words_from_dict and all(letters.count(letter) >= elem.count(letter) for letter in elem):
            response_a.append(elem)
        if elem in words_from_dict and all(letters.count(letter) >= elem.count(letter) for letter in elem):
            response_b.append(elem)
    else:
        resp_false.append(elem)
    return(resp_false)
