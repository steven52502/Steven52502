#importing the time module
import time
import random #importing the random module


#welcoming the user
name = raw_input("What is your name? ") #allow user to input their name

print "Hello, " + name, "Time to play hangman!" #greets user after name is inputted

print "" #print a word with an empty value

#wait for 1 second
time.sleep(1)

print "Start guessing..." #print "start guessing"
time.sleep(0.5) # wait for 0.5 seconds

#here we set the secretwords with the category of animals
word = ["gorilla",
    "turkey",
    "gopher",
    "dog",
    "cat",
    "fox",
    "walrus",
    "dinosaur",
    "rhino",
    "rabbit",
    "sasquatch",
    "reindeer",
    "rooster",
    "swordfish",
    "clownfish",
    "pufferfish",
    "shark",
    "rat",
    "dolphin",
    "kangaroo",
    "rudolph",
    "bamboon",
    "lion",
    "nemo",
    "giraffe",
    "zebra",
    "hippo",
    "chimpanzee",
    "snake",
    "liger",
    "llama",
    "lizard",
    "dragon",
    "deer",
    "whale",
    "pelican",
    "cow",
    "unicorn",
    "hyena",
    "vulture",
    "raven",
    "eagle",
    "stingray",
    "crocodile",
    "spider",
    "caterpillar",
    "chicken",
    "antelope",
    "panda",
    "coyote"]
secretword = random.choice(word) #make a random choice for the secretword

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secretword    
    for char in secretword:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # if the statement is true, print then out the character
            print char,    

        else:
    
        # if not found, print a dash
            print "_",     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # if statement true, print You Won
    if failed == 0:        
        print "You won"  

    # exit the script
        break              

    print

    # ask the user go guess a character
    guess = raw_input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in secretword:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print "Wrong"    
 
    # how many turns are left
        print "You have", + turns, 'more guesses' 
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Loose"
            print "You Loose"  