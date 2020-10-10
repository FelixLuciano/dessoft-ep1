from system import *
from game import *
from utils import *

def init ():
  print_greetings()
  register_players()
  if len(players):
    print("Placar Inicial")
    print_stats(players)
    print("")

    print(colored("§B§rRODADA 1§0"))

    round_cards = draw_cards()

    print_cards(players, round_cards)

init()
