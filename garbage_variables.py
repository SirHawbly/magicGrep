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
      item_str += " PRIMARY KEY"

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

CardName = {'name':'Name', 'type':'char', 'length':'100', 'not_null':True,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

ColorIdentityText = {'name':'ColorIdentityText', 'type':'char', 'length':'500', 'not_null':True,
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

CardInfoTable = create_table_query('CardInformation', 
   [CardID, CardName, CostRefID, StatsRefID, LayoutRefID, ColorIdentityRefID])

AbilityRefTable = create_table_query('AbilityReference', 
    [CardRefID, AbilityRefID])

AbilitiesTable = create_table_query('CardAbilities', 
    [AbilityID, AbilityText])

TypeRefTable = create_table_query('TypeReference', 
   [CardRefID, TypeRefID])

TypesTable = create_table_query('CardTypes', 
    [TypeID, TypeText])

ColorIdentityTable = create_table_query('ColorIdentity', 
    [ColorIdentityID, ColorIdentityText])

ManaColorRefTable = create_table_query('ManaColorReference', 
    [ColorIdentityRefID, ManaColorRefID])

ManaColorsTable = create_table_query('ManaColors', 
    [ManaColorID, ManaColorName, ManaColorSymbol])

CardLayoutsTable = create_table_query('CardLayouts', 
    [LayoutID, LayoutName])

CardCostsTable = create_table_query('CardCosts', 
    [CostID, ManaCost, ColorIdentityRefID, ConvertedManaCost])

CardStatsTable = create_table_query('CardStats', 
    [StatID, Loyalty, Power, Toughness])

# Print out all of the tables above for testing
for i in [CardInfoTable, AbilityRefTable, AbilitiesTable, TypeRefTable, TypesTable,  
    ColorIdentityTable, ManaColorRefTable, ManaColorsTable, CardLayoutsTable, 
    CardCostsTable, CardStatsTable]:
  print(i, '\n')

# # --------------------------------------------------------
# # -- DATABASE QUERIES ------------------------------------


# # -- COLOR IDENTITIES ------------------------------------
# # --------------------------------------------------------

# ALL BASE CARD COLORS
card_colors = {

  "Colorless": "C",
  "Red": "R",
  "Black": "B",
  "Blue": "U",
  "Green": "G",
  "White": "W",
}

# ALL COLOR IDENTITIES
color_identities = {

  # 0 color
  "Colorless": ["C"],

  # 1 color
  "Mono Red": ["R"],
  "Mono Black": ["B"],
  "Mono Blue": ["U"],
  "Mono Green": ["G"],
  "Mono White": ["W"],
  
  # 2 color
  "Azorius": ["W", "U"],
  "Dimir": ["U", "B"],
  "Rakdos": ["B", "R"],
  "Gruul": ["R", "G"],
  "Selesnya": ["G", "W"],
  "Orzhov": ["W", "B"],
  "Izzet": ["U", "R"],
  "Golgari": ["B", "G"],
  "Boros": ["R", "W"],
  "Simic": ["G", "U"],

  # 3 color
  "Jund": ["R", "G", "B"],
  "Bant": ["W", "G", "U"],
  "Grixis": ["B", "R", "U"],
  "Naya": ["G", "W", "R"],
  "Esper": ["U", "W", "B"],
  "Jeskai": ["W", "U", "R"],
  "Mardu": ["B", "W", "R"],
  "Sultai": ["G", "B", "U"],
  "Temur": ["G", "U", "R"],
  "Abzan": ["G", "W", "B"],

  # 4 color
  "Chaos": ["U", "R", "B", "G"],
  "Aggression": ["W", "R", "B", "G"],
  "Altruism": ["U", "W", "R", "G"],
  "Growth": ["U", "W", "B", "G"],
  "Artifice": ["U", "W", "R", "B"],

  # 5 color
  "Domain": ["W", "U", "B", "R", "G"],
}

# # --------------------------------------------------------
# # -- COLOR IDENTITIES ------------------------------------


# # -- JSON FILE FIELDS ------------------------------------
# # --------------------------------------------------------

selected_fields = ['id', 'oracle_id', 'layout', 'released_at', 'image_uris', 'mana_cost', 'cmc', 'colors', 'color_identity', 'name', 'type_line', 'oracle_text', 'power', 'toughness', 'legalities', 'set', 'set_name', 'reprint', 'artist', 'rarity', 'lang']

needed_fields = ['object', 'id', 'oracle_id', 'name', 'released_at', 'scryfall_uri', 'layout', 'mana_cost', 'cmc', 'type_line', 'oracle_text', 'power', 'toughness', 'colors', 'color_identity', 'legalities', 'set', 'set_name', 'set_type', 'rarity', 'loyalty']

all_fields = ['object', 'id', 'oracle_id', 'multiverse_ids', 'name', 'lang', 'released_at', 'uri', 'scryfall_uri', 'layout', 'highres_image', 'image_uris', 'mana_cost', 'cmc', 'type_line', 'oracle_text', 'power', 'toughness', 'colors', 'color_identity', 'legalities', 'games', 'reserved', 'foil', 'nonfoil', 'oversized', 'promo', 'reprint', 'variation', 'set', 'set_name', 'set_type', 'set_uri', 'set_search_uri', 'scryfall_set_uri', 'rulings_uri', 'prints_search_uri', 'collector_number', 'digital', 'rarity', 'card_back_id', 'artist', 'artist_ids', 'illustration_id', 'border_color', 'frame', 'full_art', 'textless', 'booster', 'story_spotlight', 'edhrec_rank', 'related_uris', 'frame_effects', 'preview', 'card_faces', 'flavor_text', 'loyalty', 'all_parts', 'tcgplayer_id', 'promo_types', 'mtgo_id', 'frame_effect', 'watermark', 'arena_id', 'variation_of', 'color_indicator', 'printed_name', 'printed_type_line', 'printed_text', 'mtgo_foil_id', 'life_modifier', 'hand_modifier']

# # --------------------------------------------------------
# # -- JSON FILE FIELDS ------------------------------------


# # -- POPULATE TABLES -------------------------------------
# # --------------------------------------------------------

fill_card_colors = []
fill_card_color_reference = []
fill_card_color_identities = []

# Function that fills the top three variables
def populate_colors():
  """
  """
  
  return


# # --------------------------------------------------------
# # -- POPULATE TABLES -------------------------------------


# # -- GLOBALS ---------------------------------------------
# # --------------------------------------------------------

# create_queries = []

# populate_queries = [populate_colors]

# # --------------------------------------------------------
# # -- GLOBALS ---------------------------------------------


# # -- OTHER GLOBAL VARIABLES ------------------------------
# # --------------------------------------------------------

# # --------------------------------------------------------
# # -- OTHER GLOBAL VARIABLES ------------------------------


# ----------------------------------------------------------
# -- END OF FILE -------------------------------------------
