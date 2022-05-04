#import libraries
import random


#  let the user select o or x

def create_user_char():
    user_char = input("select 'o' or 'x'")
    return user_char

def print_board():
    pass

my_spaces = [1,2,3,4,5,6,7,8,9]
player_spaces=[]
comp_spaces =[]
win_seq_1 = [1,2,3]
win_seq_2 = [4,5,6]
win_seq_3 = [7,8,9]
win_seq_4 = [1,4,7]
win_seq_5 = [2,5,8]
win_seq_6 = [3,6,9]
win_seq_7 = [1,5,9]
win_seq_8 = [3,5,7]



def player_choose():
    player_choice = input("enter a number between 1 and 9")
    player_spaces.append(player_choice)

def computer_choose():
    comp_choice = random.uniform(1,10)
    comp_spaces.append(comp_choice)

def check_board():
    #use if elif sequence, compare lists?
    # use returnMatches(list1, list2)
    if returnMatches(player_spaces, win_seq_1) == [1,2,3]:
        print("Player wins")
