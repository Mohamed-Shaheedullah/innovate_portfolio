
from random import randint


# a while loop to present quotes from the user and ask whiuch film it is from
# quotes from Ghostbusters 1

quotes_1 =["Janine Melnitz: Do you believe in UFOs, astral projections, mental telepathy, ESP, clairvoyance, spirit photography, telekinetic movement, full trance mediums, the Loch Ness monster and the theory of Atlantis?  Winston Zeddemore: Ah, if there's a steady paycheck in it, I'll believe anything you say.",
"Dr. Raymond Stantz: Personally, I liked the university. They gave us money and facilities, we didn't have to produce anything! You've never been out of college! You don't know what it's like out there! I've WORKED in the private sector. They expect *results*.",
"Dr. Egon Spengler: I feel like the floor of a taxi cab.",
"Dr. Raymond Stantz: Hey... Where these stairs go?  Dr. Peter Venkman: They go up!"]

# quotes from Ghostbusters 2
quotes_2=["Janosz: Soon, the city will be mine and Vigo's... mainly Vigo's.",
"Peter Venkman: Dana, you just never got it. I'm a man, I need to feel loved. I need to be desired!  Dana: When you started introducing me as the old ball and chain, that's when I left.",
"Peter Venkman: Next week on 'World of the Psychic'. Hairless cats... weird.",
"Peter Venkman: Suck in the guts, guys, we're the Ghostbusters."]

# quotes from Ghostbusters 3 (2016)
quotes_3 = ["Jillian Holtzmann: [eating Pringles chips from the can] Just try saying no to these salty parabolas!",
"Kevin: You know, an aquarium is a submarine for fish.",
"Abby Yates: I'm just looking for a reasonable ratio of wontons to soup, this is madness!",
"Patty Tolan: It smells like burnt baloney and regrets down here."]

# quotes from Ghostbusters 4 (Afterlife)

quotes_4 = ["Winston Zeddemore: [Powering up his Proton Gun] I love that sound.",
"Trevor: Hey, remember that summer when we all died under a table?",
"Peter Venkman: [about to blast Gozer] Okay, on the count of three, go on two. One! Two!  [the Ghostbusters blast Gozer]",
"Callie: Pheebs, be a dear and break into your grandfather's house."]



def chooseQuote():
    # generate a quote from random numbers 
    which_film = randint(1, 4)
    which_quote = randint(1, 4)

    # if else clause selects film, index selcts quote from film
    print("")
    print("Quote")
    if which_film == 1:
        print(quotes_1[which_quote-1])
    elif which_film == 2:
        print(quotes_2[which_quote-1])
    elif which_film == 3:
        print(quotes_3[which_quote-1])
    else:
        print(quotes_4[which_quote-1])
    print("")
    quiz(which_film)


def check_answer(ans, chosen_film):
    # global which_film
    if ans == chosen_film:
        print("You are correct!")
    else:
        print("You are wrong!")

def message1():
    print ("1 for the original Ghostbusters")
    print ("2 for Ghostbusters 2")
    print ("3 for Ghostbusters 2016")
    print ("4 for Ghostbusters:Afterlife")



entered = False

def quiz(chosen_film):
    global entered

    valid_entry =['1' ,'2' ,'3' ,'4']
    try:
        while not entered:
            message1()
            my_var = input("type a number between 1 and 4 to choose a Ghostbusters film    >" )
            if my_var == "" or my_var not in valid_entry:
                print("Please try again")
                quiz(chosen_film)
            else :
                entered = True
                my_var = int(my_var)
                # print(my_var)
                check_answer(my_var, chosen_film)

    except:
        print("Error***********************")

# call first function
chooseQuote()



