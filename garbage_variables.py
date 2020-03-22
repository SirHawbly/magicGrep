# -- GARBAGE VARIABLES -------------------------------------
# ----------------------------------------------------------


# # -- DATABASE SCRIPTS ------------------------------------
# # --------------------------------------------------------

# Function to create a table creation query
def create_table_query(table_name, table_item_list):
  """
  given a table name and a list of items, in the format of:
  
  [{'name':'', 'type':'', 'length':'', 'not_null':'',
    'primary':'', 'reference':'', 'ref_table':'', 
    'ref_variable':''}, ...]
  
  output a database query to create a tablewith that specified 
  name and item list.
  """

  names = []

  # start out the query
  query_string = 'CREATE TABLE {} (\n'.format(table_name)

  # start off with the item_string with a name and a type
  for item in table_item_list:

    # check if that variable name already exists, if not, 
    # add it, if so, assert false.
    if (item['name'] in names):
      assert(False)
    else:
      names += [item['name'], ]

    item_str = '\t{} {}'.format(item['name'], item['type'].upper())

    # if this is a string, then we should define a length
    # (I'm not going to use varchars, ill neglect them)
    if (item['length']):
      item_str += ' ({})'.format(item['length'])

    # if this needs to have a non-null value, add that.
    if (item['not_null'] == True):
      item_str += ' NOT NULL'

    # if the item is a reference to another table, add that.
    if (item['reference'] and not item['primary']):
      item_str += ' REFERENCES {}({})'.format(item['ref_table'], item['ref_variable'])

    # if the item is a primary key, then add that.
    if (item['primary'] and not item['reference']):
      item_str += ' PRIMARY KEY'

    # If this is not the last in the list, dont need a comma
    if (item != table_item_list[-1]):
      query_string += item_str + ',\n'
    else:
      query_string += item_str
  
  # return the create query
  return query_string + '\n);'

# # --------------------------------------------------------
# # -- DATABASE SCRIPTS ------------------------------------


# # -- DATABASE PRIMARY KEYS -------------------------------
# # --------------------------------------------------------

AbilityID = {'name':'AbilityID', 'type':'int', 'length':'', 'not_null':True,
    'primary':True, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

CardID = {'name':'CardId', 'type':'int', 'length':'', 'not_null':True,
    'primary':True, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

ColorIdentityID = {'name':'ColorIdentityID', 'type':'int', 'length':'', 'not_null':True,
    'primary':True, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

CostID = {'name':'CostID', 'type':'int', 'length':'', 'not_null':True,
    'primary':True, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

LayoutID = {'name':'LayoutID', 'type':'int', 'length':'', 'not_null':True,
    'primary':True, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

ManaColorID = {'name':'ManaColorID', 'type':'int', 'length':'', 'not_null':True,
    'primary':True, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

StatID = {'name':'StatID', 'type':'int', 'length':'', 'not_null':True,
    'primary':True, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

TypeID = {'name':'TypeID', 'type':'int', 'length':'', 'not_null':True,
    'primary':True, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

# # --------------------------------------------------------
# # -- DATABASE PRIMARY KEYS -------------------------------


# # -- DATABASE REFERECENT KEYS ----------------------------
# # --------------------------------------------------------

AbilityRefID = {'name':'AbilityID', 'type':'int', 'length':'', 'not_null':False,
    'primary':False, 'reference':True, 'ref_table':'CardAbilities', 
    'ref_variable':'AbilityID'}

CardRefID = {'name':'CardId', 'type':'int', 'length':'', 'not_null':False,
    'primary':False, 'reference':True, 'ref_table':'CardInformation', 
    'ref_variable':'CardId'}

ColorIdentityRefID = {'name':'ColorIdentityID', 'type':'int', 'length':'', 'not_null':False,
    'primary':False, 'reference':True, 'ref_table':'ManaColorIdentity', 
    'ref_variable':'ColorIdentityID'}    

CostRefID = {'name':'CostID', 'type':'int', 'length':'', 'not_null':False,
    'primary':False, 'reference':True, 'ref_table':'CardCosts', 
    'ref_variable':'CostID'}

ManaColorRefID = {'name':'ManaColorID', 'type':'int', 'length':'', 'not_null':False,
    'primary':False, 'reference':True, 'ref_table':'ManaColors', 
    'ref_variable':'ManaColorID'}

LayoutRefID = {'name':'LayoutID', 'type':'int', 'length':'', 'not_null':False,
    'primary':False, 'reference':True, 'ref_table':'CardLayouts', 
    'ref_variable':'LayoutID'}

StatsRefID = {'name':'StatsID', 'type':'int', 'length':'', 'not_null':False,
    'primary':False, 'reference':True, 'ref_table':'CardStats', 
    'ref_variable':'StatsID'}
    
TypeRefID = {'name':'TypeID', 'type':'int', 'length':'', 'not_null':False,
    'primary':False, 'reference':True, 'ref_table':'CardTypes', 
    'ref_variable':'TypeID'}

# # --------------------------------------------------------
# # -- DATABASE REFERECENT KEYS ----------------------------


# # -- DATABASE DATA ---------------------------------------
# # --------------------------------------------------------

AbilityText = {'name':'AbilityText', 'type':'char', 'length':'500', 'not_null':False,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

CardName = {'name':'CardName', 'type':'char', 'length':'100', 'not_null':True,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

ColorIdentityName = {'name':'ColorIdentityName', 'type':'char', 'length':'500', 'not_null':True,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

ConvertedManaCost = {'name':'ConvertedManaCost', 'type':'float', 'length':'', 'not_null':True,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

LayoutName = {'name':'LayoutName', 'type':'char', 'length':'20', 'not_null':True,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

Loyalty = {'name':'Loyalty', 'type':'char', 'length':'10', 'not_null':False,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}
    
ManaColorName = {'name':'ColorName', 'type':'char', 'length':'10', 'not_null':True,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

ManaColorSymbol = {'name':'ColorSymbol', 'type':'char', 'length':'1', 'not_null':True,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

ManaCost = {'name':'ManaCost', 'type':'char', 'length':'20', 'not_null':True,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

Power = {'name':'Power', 'type':'char', 'length':'10', 'not_null':False,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

Toughness = {'name':'Toughness', 'type':'char', 'length':'10', 'not_null':False,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

TypeText = {'name':'TypeText', 'type':'char', 'length':'500', 'not_null':True,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

# # --------------------------------------------------------
# # -- DATABASE DATA ---------------------------------------


# # -- DATABASE QUERIES ------------------------------------
# # --------------------------------------------------------

TableCreationQueries = []

CardInfoTable = create_table_query('CardInformation', [CardID, CardName, CostRefID, StatsRefID, LayoutRefID, ColorIdentityRefID])
TableCreationQueries += [CardInfoTable, ]

AbilityRefTable = create_table_query('AbilityReference', [CardRefID, AbilityRefID])
TableCreationQueries += [AbilityRefTable, ]

AbilitiesTable = create_table_query('CardAbilities', [AbilityID, AbilityText])
TableCreationQueries += [AbilitiesTable, ]

TypeRefTable = create_table_query('TypeReference', [CardRefID, TypeRefID])
TableCreationQueries += [TypeRefTable, ]

TypesTable = create_table_query('CardTypes', [TypeID, TypeText])
TableCreationQueries += [TypesTable, ]

ColorIdentityTable = create_table_query('ColorIdentity', [ColorIdentityID, ColorIdentityName])
TableCreationQueries += [ColorIdentityTable, ]

ManaColorRefTable = create_table_query('ManaColorReference', [ColorIdentityRefID, ManaColorRefID])
TableCreationQueries += [ManaColorRefTable, ]

ManaColorsTable = create_table_query('ManaColors', [ManaColorID, ManaColorName, ManaColorSymbol])
TableCreationQueries += [ManaColorsTable, ]

CardLayoutsTable = create_table_query('CardLayouts', [LayoutID, LayoutName])
TableCreationQueries += [CardLayoutsTable, ]

CardCostsTable = create_table_query('CardCosts', [CostID, ManaCost, ColorIdentityRefID, ConvertedManaCost])
TableCreationQueries += [CardCostsTable, ]

CardStatsTable = create_table_query('CardStats', [StatID, Loyalty, Power, Toughness])
TableCreationQueries += [CardStatsTable, ]

# Print out all of the tables above for testing
for i in TableCreationQueries:
  print(i, '\n')

# # --------------------------------------------------------
# # -- DATABASE QUERIES ------------------------------------


# # -- COLOR VALUES ----------------------------------------
# # --------------------------------------------------------

# ALL BASE CARD COLORS
CardColors = [

  {'name':'Colorless', 'colorid':1, 'symbol':'C'},
  {'name':'Red', 'colorid':2, 'symbol':'R'},
  {'name':'Black', 'colorid':3, 'symbol':'B'},
  {'name':'Blue', 'colorid':4, 'symbol':'U'},
  {'name':'Green', 'colorid':5, 'symbol':'G'},
  {'name':'White', 'colorid':6, 'symbol':'W'}
]

# ALL COLOR IDENTITIES
ColorIdentities = [

  # 0 color
  {'identityname':'Colorless', 'identityid':1, 'colors':['C']},

  # 1 color
  {'identityname':'Mono Red', 'identityid':2, 'colors':['R']},
  {'identityname':'Mono Black', 'identityid':3, 'colors':['B']},
  {'identityname':'Mono Blue', 'identityid':4, 'colors':['U']},
  {'identityname':'Mono Green', 'identityid':5, 'colors':['G']},
  {'identityname':'Mono White', 'identityid':6, 'colors':['W']},
  
  # 2 color
  {'identityname':'Azorius', 'identityid':7, 'colors':['W', 'U']},
  {'identityname':'Dimir', 'identityid':8, 'colors':['U', 'B']},
  {'identityname':'Rakdos', 'identityid':9, 'colors':['B', 'R']},
  {'identityname':'Gruul', 'identityid':10, 'colors':['R', 'G']},
  {'identityname':'Selesnya', 'identityid':11, 'colors':['G', 'W']},
  {'identityname':'Orzhov', 'identityid':12, 'colors':['W', 'B']},
  {'identityname':'Izzet', 'identityid':13, 'colors':['U', 'R']},
  {'identityname':'Golgari', 'identityid':14, 'colors':['B', 'G']},
  {'identityname':'Boros', 'identityid':15, 'colors':['R', 'W']},
  {'identityname':'Simic', 'identityid':16, 'colors':['G', 'U']},

  # 3 color
  {'identityname':'Jund', 'identityid':17, 'colors':['R', 'G', 'B']},
  {'identityname':'Bant', 'identityid':18, 'colors':['W', 'G', 'U']},
  {'identityname':'Grixis', 'identityid':19, 'colors':['B', 'R', 'U']},
  {'identityname':'Naya', 'identityid':20, 'colors':['G', 'W', 'R']},
  {'identityname':'Esper', 'identityid':21, 'colors':['U', 'W', 'B']},
  {'identityname':'Jeskai', 'identityid':22, 'colors':['W', 'U', 'R']},
  {'identityname':'Mardu', 'identityid':23, 'colors':['B', 'W', 'R']},
  {'identityname':'Sultai', 'identityid':24, 'colors':['G', 'B', 'U']},
  {'identityname':'Temur', 'identityid':25, 'colors':['G', 'U', 'R']},
  {'identityname':'Abzan', 'identityid':26, 'colors':['G', 'W', 'B']},

  # 4 color
  {'identityname':'Chaos', 'identityid':27, 'colors':['U', 'R', 'B', 'G']},
  {'identityname':'Aggression', 'identityid':28, 'colors':['W', 'R', 'B', 'G']},
  {'identityname':'Altruism', 'identityid':29, 'colors':['U', 'W', 'R', 'G']},
  {'identityname':'Growth', 'identityid':30, 'colors':['U', 'W', 'B', 'G']},
  {'identityname':'Artifice', 'identityid':31, 'colors':['U', 'W', 'R', 'B']},

  # 5 color
  {'identityname':'Domain', 'identityid':32, 'colors':['W', 'U', 'B', 'R', 'G']},
]

# # --------------------------------------------------------
# # -- COLOR VALUES ----------------------------------------


# # -- JSON FILE FIELDS ------------------------------------
# # --------------------------------------------------------

selected_fields = ['id', 'oracle_id', 'layout', 'released_at', 'image_uris', 'mana_cost', 'cmc', 'colors', 'color_identity', 'name', 'type_line', 'oracle_text', 'power', 'toughness', 'legalities', 'set', 'set_name', 'reprint', 'artist', 'rarity', 'lang']

needed_fields = ['object', 'id', 'oracle_id', 'name', 'released_at', 'scryfall_uri', 'layout', 'mana_cost', 'cmc', 'type_line', 'oracle_text', 'power', 'toughness', 'colors', 'color_identity', 'legalities', 'set', 'set_name', 'set_type', 'rarity', 'loyalty']

all_fields = ['object', 'id', 'oracle_id', 'multiverse_ids', 'name', 'lang', 'released_at', 'uri', 'scryfall_uri', 'layout', 'highres_image', 'image_uris', 'mana_cost', 'cmc', 'type_line', 'oracle_text', 'power', 'toughness', 'colors', 'color_identity', 'legalities', 'games', 'reserved', 'foil', 'nonfoil', 'oversized', 'promo', 'reprint', 'variation', 'set', 'set_name', 'set_type', 'set_uri', 'set_search_uri', 'scryfall_set_uri', 'rulings_uri', 'prints_search_uri', 'collector_number', 'digital', 'rarity', 'card_back_id', 'artist', 'artist_ids', 'illustration_id', 'border_color', 'frame', 'full_art', 'textless', 'booster', 'story_spotlight', 'edhrec_rank', 'related_uris', 'frame_effects', 'preview', 'card_faces', 'flavor_text', 'loyalty', 'all_parts', 'tcgplayer_id', 'promo_types', 'mtgo_id', 'frame_effect', 'watermark', 'arena_id', 'variation_of', 'color_indicator', 'printed_name', 'printed_type_line', 'printed_text', 'mtgo_foil_id', 'life_modifier', 'hand_modifier']

# # --------------------------------------------------------
# # -- JSON FILE FIELDS ------------------------------------


# # -- POPULATE TABLES -------------------------------------
# # --------------------------------------------------------

# Function that fills the top three variables
def PopulateColorQuries():
  """
  Generate a list of Insert Queries for every Mana color that is listed in the 
  Mana Colors list, then add them to a returnable list.

  Mana Color Table Definition
  ManaColorsTable = create_table_query('ManaColors', [ManaColorID, ManaColorName, ManaColorSymbol])
  
  Mana Colors List
  CardColors = [ {'name':'Colorless', 'colorid':1, 'symbol':'C'}, ...]
  """
  
  PopulateList = []
  
  for Color in CardColors:

    Query = 'INSERT INTO ManaColors ({}, {}, {})'.format(ManaColorName['name'], ManaColorID['name'], ManaColorSymbol['name'])

    Query += ' VALUES (\'{}\', {}, \'{}\')'.format(Color['name'], Color['colorid'], Color['symbol'])
    
    print(Query, '\n')
    
    PopulateList += [Query, ]

  return PopulateList

# # --------------------------------------------------------

def PopulateColorIdentityQueries():
  """
  
  Color Identity Table
  ColorIdentityTable = create_table_query('ColorIdentity', [ColorIdentityID, ColorIdentityName])

  Mana Colors List
  CardColors = [ {'name':'Colorless', 'colorid':1, 'symbol':'C'}, ...]

  Color Identities List Form
  ColorIdentities = [ {'identityname':'Colorless', 'identityid':1, 'colors':['C']}, ... ]
  """

  ColorIdentityQueries = []

  for Identity in ColorIdentities:

    Query = 'INSERT INTO ColorIdentity ({}, {})'.format(ColorIdentityName['name'], ColorIdentityID['name'])

    Query += ' VALUES (\'{}\', {})'.format(Identity['identityname'], Identity['identityid'])
    
    print(Query, '\n')

    ColorIdentityQueries += [Query, ]

  return ColorIdentityQueries

# # --------------------------------------------------------

def PopulateColorIdentityRefQueries():
  """
  
  Color Reference Table
  ManaColorRefTable = create_table_query('ManaColorReference', [ColorIdentityRefID, ManaColorRefID])

  Mana Colors List
  CardColors = [ {'name':'Colorless', 'colorid':1, 'symbol':'C'}, ...]

  Color Identities List Form
  ColorIdentities = [ {'identityname':'Colorless', 'identityid':1, 'colors':['C']}, ... ]
  """

  ColorIdentityReferenceQueries = []

  for Identity in ColorIdentities:

    for IdentityColor in Identity['colors']:

      for ManaColor in CardColors:
        
        if (IdentityColor == ManaColor['symbol']):

          Query = 'INSERT INTO ManaColorReference ({}, {})'.format(ColorIdentityRefID['name'], ManaColorRefID['name'])

          Query += ' VALUES (\'{}\', {})'.format(Identity['identityid'], ManaColor['symbol'])

          print(Query, '\n')

          ColorIdentityReferenceQueries += [Query, ]

  return ColorIdentityReferenceQueries

# # --------------------------------------------------------

FillCardColors = PopulateColorQuries()
FillColorIdentities = PopulateColorIdentityQueries()
FillColorReferences = PopulateColorIdentityRefQueries()

# # --------------------------------------------------------
# # -- POPULATE TABLES -------------------------------------


# # -- GLOBALS ---------------------------------------------
# # --------------------------------------------------------



# # --------------------------------------------------------
# # -- GLOBALS ---------------------------------------------


# # -- OTHER GLOBAL VARIABLES ------------------------------
# # --------------------------------------------------------

# # --------------------------------------------------------
# # -- OTHER GLOBAL VARIABLES ------------------------------


# # -- MAIN FUNCTION ---------------------------------------
# # --------------------------------------------------------

# main function
def main():
  """
  """

  return

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
