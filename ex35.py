from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if '0' in choice or '1' in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you\'re not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")
