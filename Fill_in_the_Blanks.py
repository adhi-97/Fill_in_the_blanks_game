#Stage 2 IPND Project

#Easy Level Answers
easy_solution=[["(1)","python"],["(2)","programming"],["(3)","syntax"],["(4)","code"],["(5)","programs"]]

#Easy Level Paragraph
easy_para=""" (1) is a widely used high-level, general-purpose,
interpreted, dynamic (2) language.Its design philosophy
emphasizes code readability, and its (3) allows programmers to express
concepts in fewer lines of (4) than possible in languages such as C++ or
Java.The language provides constructs intended to enable writing clear
(5) on both a small and large scale."""

#Medium Level Answers
medium_solution=[["(1)","functional"],["(2)","procedural"],["(3)","dynamic"],["(4)","memory"],["(5)","library"]]


#Medium Level Paragraph
medium_para="""Python supports multiple programming paradigms, including
object-oriented, imperative, (1) programming, and (2) styles.
It features a (3) type system and automatic (4) management and has a
large and comprehensive standard (5)."""

#Hard Level Answers
hard_solution=[["(1)","interpreters"],["(2)","operating"],["(3)","implementation"],["(4)","development"],["(5)","implementations"]]

#Hard Level Paragraph
hard_para="""Python (1) are available for many (2) systems,
allowing Python code to run on a wide variety of systems. CPython, the
reference (3) of Python, is open source software and has a
community-based (4) model, as do nearly all of its variant
(5). CPython is managed by the non-profit Python Software
Foundation."""

def no_of_attempts():
    #Reads max no. of attempts
    max_attempts=raw_input("Enter no. of attempts you like to have (1-5):")
    if max_attempts not in "12345":
        print "Enter a valid input"
        max_attempts=no_of_attempts()
    else:
        enter_level(max_attempts)
    
def enter_level(max_attempts):
    #Reads difficulty level from user
    list=["easy","medium","hard"]
    difficulty_level = raw_input("Choose your difficulty level : easy medium hard: ")
    if difficulty_level not in list:
        print "Enter a valid input"
        difficulty_level=enter_level(max_attempts)
    else:
        out_data(max_attempts,difficulty_level)
    

def fill_in_the_blanks(difficulty_para,solutions,max_attempts):
    #Reads answers from user and calls the check function 
    replaced_para=difficulty_para
    for blank,solution in solutions:
        replaced_para=check_solution(blank,solution,replaced_para,max_attempts)
    print "Well Played!!! Thank you playing :)"
    
def check_solution(blank,solution,replaced_para,max_attempts):
    #checks the user input with actual answer
    max_attempts=int(max_attempts)
    attempt=1
    while attempt<=max_attempts:
        user_answer=raw_input("What should be substituted for"+blank+": ")
        if solution==user_answer:
            print "NICE PLAY!!! Keep Going"
            replaced_para=replaced_para.replace(blank,solution)
            print "Replaced paragraph"+replaced_para
            return replaced_para
        else:
            if attempt<max_attempts:
                print "Wrong answer try again"
                print "You have "+str(max_attempts-attempt)+" attempts left"
            else:
               print "You have finished your chances"
               print "Thank you playing :)"
               exit()
        attempt+=1

def out_data(max_attempts,level):
    #Outputs details of user inputs and question
    print "You chose " + level + " level with " + str(max_attempts)+" attempts. ALL THE BEST!!!"
    print
    print "Your question for the difficulty level chosen is"
    print
    difficulty_para=eval(level +"_para")
    answers=eval(level+"_solution")
    print difficulty_para
    fill_in_the_blanks(difficulty_para,answers,max_attempts)
    
def start_game():
    #Starts the game and calls the function to read maxno. of attempts from user
    no_of_attempts()

#Main program    
print "Let's PLAY!!!"
start_game()



    




