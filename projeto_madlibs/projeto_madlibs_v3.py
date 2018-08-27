#Texts to fill the blanks
text_easy = '''___1___ is a widely used high-level, general-purpose, interpreted, dynamic ___2___ language.[22][23] Its design philosophy emphasizes code readability, and its ___3___ allows programmers to express concepts in ___4___ lines of code than would be possible in languages such as C++ or Java.[24][25] The language provides constructs intended to enable clear programs on both a small and large scale.[26] Source: Wikipedia'''
answer_easy = ["python", "programming", "syntax", "fewer"]
text_medium = '''Python supports multiple programming ___1___, including object-oriented, imperative and ___2___ programming or procedural styles. It features a dynamic type system and automatic ___3___ management and has a large and comprehensive standard ___4___.[27] Source: Wikipedia'''
answer_medium = ["paradigms", "functional", "memory", "library"]
text_hard = '''Python interpreters are available for installation on many operating systems, allowing Python code execution on a wide variety of systems. Using third-party tools, such as ___1___ or ___2___,[28] Python code can be ___3___ into stand-alone executable programs for some of the most popular operating systems, allowing the distribution of Python-based software for use on those environments without requiring the installation of a Python interpreter. ___4___, the reference implementation of Python, is free and open-source software and has a community-based development model, as do nearly all of its alternative implementations. Source: Wikipedia'''
answer_hard = ["py2exe", "pyinstaller", "packaged", "cpython"]

#Blank spaces
blank_space = ["___1___", "___2___","___3___","___4___" ]


def choose_level(user_level):
#Player will choose the level to play the Game
#input: level choosed by the user
#output: returns the text with blanks spaces and answers to each level

    if user_level == 'e':
        return text_easy, answer_easy
    if user_level == 'm':
        return text_medium, answer_medium
    if user_level == 'h':
        return text_hard, answer_hard

def check_answer(answer_list, index):
    #Ask the player an answer and check if the answer the player inputted it's right
    #input: answer_list with right answers according to level choosen, index to ask and check answer by player
    #output: return true if the player inputted the right answer or false if the player missed
        user_guess = raw_input('Type the right answer'+blank_space[index]+':')
        if user_guess == answer_list[index]:
            return True
        else:
            return False

def play_game(text_level, answer_list):
    #input: text from level wich user has choosed and the answers for each blank space in the text
    #output: return answer replaced if is right or give player other chance, but at max three chances
    user_try = 0
    for index, answer in enumerate(answer_list):
        print text_level
        right_answers = False
        while right_answers is not True:
            max_user_try = 3
            if user_try == max_user_try:
                return False
            right_answers = check_answer(answer_list, index)
            if right_answers != True: # TODO: alterar o nome da right_answers
                user_try += 1
                print user_try
            else:
                print 'Congrats!'
                text_level = text_level.replace(blank_space[index], answer)
    return True

def welcome_phrase():
#Print two welcome phrases and ask to the player choose a level to play, and if level choosed is valid, start the game, if not print 'invalid level' 
    print "Welcome to my madlib game."
    print "Please, choose a level and then complete the blank spaces in the phrases."
    while True:
        level = raw_input ("Type the letter that correspond the level you want to play - E (easy), M (medium), H (hard): ").lower()
        if level in ["e", "m", "h"]:
            text_level, answer_list = choose_level(level)
            if play_game(text_level, answer_list):
                print 'You win! \o/'
            else:
                print 'Game Over'
            break
        else:
            print 'Invalid level'
welcome_phrase()
