
###
#START of Listing 3.19
###

from __future__ import print_function
# tag::bot_vs_bot[]
from dlgo import agent
from dlgo import goboard_slow as goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move
import time


def main():
    #Added a prompt for board size, comment out for 
    #The board size of 9
    #board_size = 9
    board_size = int(input("What size for the board? "))
    game = goboard.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: agent.naive.RandomBot(),
        gotypes.Player.white: agent.naive.RandomBot(),
    }
    while not game.is_over():
        #Changed the speed to make it quicker
        time.sleep(0.1)  # <1>

        print(chr(27) + "[2J")  # <2>
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        
        #Commented out the print_move since it made an unpleasant jiggering of printout 
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)


if __name__ == '__main__':
    main()

# <1> We set a sleep timer to 0.3 seconds so that bot moves aren't printed too fast to observe
# <2> Before each move we clear the screen. This way the board is always printed to the same position on the command line.
# end::bot_vs_bot[]

###
#END of Listing 3.19
###
