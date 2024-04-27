'''
The terget game
'''
import random
def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',\
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    vowel_letters = ['a','e','i','o','u']
    output=[]
    result=[]
    count=0
    count_vowels=0
    while True:
        while count <3:
            for j in range (1,4):
                letters_remove=random.randint(0,len(letters)-j)
                output.append(letters[letters_remove])
                # letters.pop(letters_remove)
                if output[j-1] in vowel_letters:
                    count_vowels+=1
            result.append(output)
            count+=1
            output=[]
        if count_vowels<2:
            result,output,count=[],[],0
        else: break
    return result
def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    output=[]
    string=''
    try:
        while True:
            string=input()
            output.append(string)
            string=''
    except EOFError:
        return output
def get_words(fil: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words('1st_term/Python_tasks (4)-20240121T161209Z-001/Python_tasks (4)/lab6 (4)/en (4).txt',['e', 't', 'o', 'o', 'p', 'n','p', 'u', 'r'])
    ['epopt', 'erupt', 'netop', 'noop', 'nope', 'noup', 'nupe', 'open', 'opportune', 'outpop', \
'pent', 'peon', 'pepo', 'pern', 'pert', 'peru', 'perun', 'peto', 'poet', 'pone', 'pont', 'ponto', \
'poon', 'poop', 'poor', 'poot', 'pope', 'pore', 'port', 'porteno', 'porto', 'pote', 'poter', \
'pour', \
'pout', 'pouter', 'prep', 'prone', 'pronto', 'proo', \
'prop', 'propone', 'prote', 'proto', 'proton', \
'protone', 'prue', 'prune', 'prunt', 'prut', 'puno', \
'punt', 'punter', 'punto', 'pure', 'repot', 'repp', \
'rope', 'ropp', 'roup', 'roupet', 'tepor', 'terp', 'toop', \
'tope', 'topepo', 'toper', 'topo', 'topper', \
'toprope', 'toup', 'troop', 'trope', 'troupe', 'turp', \
'unpope', 'unpot', 'unprop', 'unrope', 'untop', 'upon', 'uppent', 'upper', 'uproot', 'uptorn']
    """
    with open(fil,'r',encoding="utf-8") as file:
        text_file=file.readlines()
    key_letter=letters[4]
    possible_words_key=[]
    letters_cut=letters[:]
    cut_the_letter=''
    check=True
    #check for a match in letters
    for i in text_file:
        i=i.replace('\n','')
        i=i.lower()
        check=True
        letters_cut=letters[:]
        if len(i)>3 and key_letter in list(i):
            for j in i:
                if j in letters_cut:
                    cut_the_letter=letters_cut.index(j)
                    letters_cut.pop(cut_the_letter)
                else:
                    check=False
                    break
            if check:
                possible_words_key.append(i)
    return possible_words_key
def convert_user_input(letters:list[list[str]]):
    '''
    Converts user input into the valid form

    '''
    user_letters=[]
    for i in letters:
        for j in range(3):
            user_letters.append(i[j])
    return user_letters
def get_pure_user_words(user_words: list[str], letters: list[str],\
 words_from_dict: list[str]) -> list[str]:
    """
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    >>> get_pure_user_words(['opto'],['e', 't', 'o', 'o', 'p', 'n','p', 'u', 'r'],\
['epopt', 'erupt', 'netop', 'noop', 'nope', 'noup', 'nupe', 'open', 'opportune', \
'outpop', 'pent', 'peon', 'pepo', 'pern', 'pert', 'peru', 'perun', 'peto', 'poet', \
'pone', 'pont', 'ponto', 'poon', 'poop', 'poor', 'poot', 'pope', 'pore', 'port', \
'porteno', 'porto', 'pote', 'poter', 'pour', 'pout', 'pouter', 'prep', 'prone', \
'pronto', 'proo', 'prop', 'propone', 'prote', 'proto', 'proton', 'protone', \
'prue', 'prune', 'prunt', 'prut', 'puno', 'punt', 'punter', 'punto', 'pure', \
'repot', 'repp', 'rope', 'ropp', 'roup', 'roupet', 'tepor', 'terp', 'toop', \
'tope', 'topepo', 'toper', 'topo', 'topper', 'toprope', 'toup', 'troop', \
'trope', 'troupe', 'turp', \
'unpope', 'unpot', 'unprop', 'unrope', 'untop', 'upon', 'uppent', 'upper', 'uproot', 'uptorn'])
    ['opto']
    """
    #check for validity
    output=[]
    result=[]
    key_letter=letters[4]
    for i in user_words:
        check=True
        letters_cut=letters[:]
        if len(i)>3 and key_letter in list(i):
            for j in i:
                if j in letters_cut:
                    cut_the_letter=letters_cut.index(j)
                    letters_cut.pop(cut_the_letter)
                else:
                    check=False
                    break
            if check:
                output.append(i)
    #form the result
    length=len(output)
    for i in range(length):
        if not output[i] in words_from_dict:
            result.append(output[i])
    return result

def main():
    """
    Lunches the program

    """
    #prints out the board to player

    game_board=generate_grid()
    output_board=[]
    result_board=[]
    for i in game_board:
        for j in i:
            output_board.append(j.capitalize())
        result_board.append(output_board)
        output_board=[]
    print(f'Your board is {result_board}')

    #word suggestions

    print('Please, suggest your word here:')
    user_words=get_user_words()
    possible_words=get_words(r'lab6\en.txt',game_board)
    right_user_words=[]
    for i in user_words:
        if i in possible_words:
            right_user_words.append(i)
    missed_words=[]
    for i in right_user_words:
        cut_words=possible_words.index(i)
        missed_words=possible_words.pop(cut_words)
    print(f'Number of the right words: {len(right_user_words)}')

    print('All possible words:')
    print(possible_words)
    print('You missed the following words:')
    print(missed_words)
    print(f"You suggest, but we don't have them in the dictionary: \
{get_pure_user_words(user_words,game_board,possible_words)}")


# if __name__ == "__main__":
#     main()
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
