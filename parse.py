# --

import os, sys
import json
from parse_database import make_db

# --


selected_fields = ['id', 'oracle_id', 'layout', 'released_at', 'image_uris', 'mana_cost', 'cmc', 'colors', 'color_identity', 'name', 'type_line', 'oracle_text', 'power', 'toughness', 'legalities', 'set', 'set_name', 'reprint', 'artist', 'rarity', 'lang']

all_fields = ['id', 'multiverse_ids', 'tcgplayer_id', 'uri' , 'scryfall_uri' , 'highres_image', 'games', 'reserved', 'foil', 'nonfoil', 'oversized', 'promo', 'set_uri', 'set_search_uri', 'scryfall_set_uri', 'rulings_uri', 'prints_search_uri', 'collector_number', 'digital', 'illustration_id', 'border_color', 'frame', 'frame_effect', 'full_art', 'story_spotlight', 'related_uris']

# --


# loop through the jsonFile, pulling all lines that have a 
# name matching one in the deckFile.
def load_json_obj(jsonFile, jsonObj):
  """
  load the json file into a provided list, so that we can 
  turn it into a DB.
  """

  jsonObj = {}

  # open the json file
  with open(jsonFile, 'r') as jsonItem:

    # load the file into the json parser.
    jsonLoadedItem = json.load(jsonItem)

    # add all of the lines in the jsonObj.
    for jsonLine in jsonLoadedItem:
      
      # add the card to the jsonObj with the key being its 
      # name
      if (jsonLine['reprint']):
        jsonObj[jsonLine['name']] = jsonLine

      # load the json cards, print their names
      # inCard = json.loads(jsonLine)
      # print(jsonLine)

      # for key in jsonLine:
        # if key not in selected_fields:
          # print(key, ', ', end='')
          # print(key, '\n\t', jsonLine[key], '\n')
        
      # print()
      # for key in all_fields:
        # if key not in selected_fields:
          # print(key, end=', ')

      # print()
      # for key in selected_fields:
        # print(key, end=', ')
        # print(key, ' =\t\t', jsonLine[key])
      # print()

    for key in jsonObj:
      print(key)

  print('json item lines: {}'.format(len(jsonObj)))

# --


# loop through the jsonFile, pulling all lines that have a 
# name matching one in the deckFile.
def load_deck_obj(deckFile, deckObj):
  """
  reset the deckObj, and load in the lines from deckFile.
  """

  deckObj = []

  # open up the deck file, and start adding lines to the deckObj
  with open(deckFile, 'r') as deckItem:
    for deckLine in deckItem:
      # print([deckLine])
      deckObj += [deckLine]

    # print the first 4 card names in the deck.
    # for card in deckObj[:4]:
      # print(card)

    # print the length of the json cards, and the deck's lines
    # print('deck item lines: {}'.format(len(deckObj)))
    
    return 


# --


# main function
if (__name__ == '__main__'):
  """
  """

  # start a list of the deck and json lines.
  deckObj = []
  jsonObj = []

  if (len(sys.argv) != 3):
    print("\nError 1:\npython3 parse.py deck scry-list")

  # figure out if we need to make a new database
  if True:
    make_db('asdf', ['asdf'])

  # if we have a source file that is newer than the DB or
  # a no DB file, we need to generate one.
  if (False): 
    load_json_obj(sys.argv[2], jsonObj)

  # load the deck lines.
  if (False):
    load_deck_obj(sys.argv[1], deckObj)


# --