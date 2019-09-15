
# -- TESTING FUCNTIONS -------------------------------------
# ----------------------------------------------------------


# # -- IMPORTS ---------------------------------------------
# # --------------------------------------------------------

import os, sys, json
from parse_database import make_new_database
from global_variables import selected_fields, all_fields

# # --------------------------------------------------------
# # -- IMPORTS ---------------------------------------------


# # -- PRINT ALL KEYS --------------------------------------
# # --------------------------------------------------------

# name matching one in the deckFile.
def print_keys(jsonFile):
  """
  load the json file into a provided list, so that we can 
  turn it into a DB.
  """

  # open the json file
  with open(jsonFile, 'r') as jsonItem:

    # load the file into the json parser.
    jsonLoadedItem = json.load(jsonItem)

    keys = []

    # add all of the lines in the jsonObj.
    for jsonLine in jsonLoadedItem:

      for key in jsonLine:
        
        if key not in keys:
          keys += [key]

  print(keys)

  return

# # --------------------------------------------------------
# # -- PRINT ALL KEYS --------------------------------------


# # -- GET JSON FIELD --------------------------------------
# # --------------------------------------------------------

def getJsonField(jsonItem, field):
  """
  """
  
  if field in jsonItem:

    return jsonItem[field]
  
  else:

    return []

# # --------------------------------------------------------
# # -- GET JSON FIELD --------------------------------------


# # -- PRINT ALL TYPES -------------------------------------
# # --------------------------------------------------------

# name matching one in the deckFile.
def print_types(jsonFile):
  """
  load the json file into a provided list, so that we can 
  turn it into a DB.
  """

  # open the json file
  with open(jsonFile, 'r') as jsonItem:

    # load the file into the json parser.
    jsonLoadedItem = json.load(jsonItem)

    types = []

    # add all of the lines in the jsonObj.
    for jsonLine in jsonLoadedItem:

      type_str = ""

      for t in jsonLine['type_line'].split(' '):

        # print('->', t, t == "—", t == "-")
        # looks like they arent using normal hyphens
        if (t == '—' or t == '-'):
          break    

        type_str += t + " "

      if type_str[ :-1] not in types:
        types += [type_str[ :-1]]

      # if 'loyalty' in jsonLine:
        # print(jsonLine['loyalty'])
  
  print(types)

  return

# # --------------------------------------------------------
# # -- PRINT ALL TYPES -------------------------------------


# # -- MAIN FUNCTION ---------------------------------------
# # --------------------------------------------------------

# main function
def main():
  """
  """

  if (len(sys.argv) != 3):
    print("\nError 1:\npython3 parse.py deck scry-list")

  # figure out if we need to make a new database
  if False:
    make_new_database('scry.db')

  # if we have a source file that is newer than the DB or
  # a no DB file, we need to generate one.
  if True: 
    print(sys.argv[2])
    print_types(sys.argv[2])
    print_keys(sys.argv[2])

# # --------------------------------------------------------

# main
if (__name__ == '__main__'):
  """
  """

  main()

# # --------------------------------------------------------
# # -- MAIN FUNCTION ---------------------------------------


# ----------------------------------------------------------
# -- END OF FILE -------------------------------------------

