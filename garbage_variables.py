# -- GARBAGE VARIABLES -------------------------------------
# ----------------------------------------------------------


# # -- IMPORT ----------------------------------------------
# # --------------------------------------------------------

import sqlite3

# # --------------------------------------------------------
# # -- IMPORT ----------------------------------------------


# # -- DATABASE SCRIPTS ------------------------------------
# # --------------------------------------------------------

# Function to create a table creation query
def create_table_query(table_name, table_item_list):
  """
  Given a table name and a list of items, in the format of:
  
  [{'name':'', 'type':'', 'length':'', 'not_null':'',
    'primary':'', 'reference':'', 'ref_table':'', 
    'ref_variable':''}, ...]
  
  output a database query to create a tablewith that specified 
  name and item list.

  Used Variables:

    Database Name
    table_name = 'colors'

    Table Items
    table_item_list = [{'name': 'Power', 'type': 'char', ...}, {'name': 'Toughness', 'type': 'char', ...}]

    Table Item String
    ItemStr = 'ManaColorID INT NOT NULL PRIMARY KEY'

    Table Creation Query
    QueryString = 'CREATE TABLE IF NOT EXISTS ManaColors (ManaColorID INT NOT NULL PRIMARY KEY, ...'
  """

  names = []

  # start out the query
  QueryString = 'CREATE TABLE IF NOT EXISTS {} (\n'.format(table_name)

  # start off with the item string with a name and a type
  for item in table_item_list:

    # check if that variable name already exists, if not, 
    # add it, if so, assert false.
    if (item['name'] in names):

      print('\n\ncreate_table_query: Duplicate Table provided `{}`.'.format(item['name']))
      
      assert(False)

    else:
      names += [item['name'], ]

    ItemStr = '\t{} {}'.format(item['name'], item['type'].upper())

    # if this is a string, then we should define a length
    # (I'm not going to use varchars, ill neglect them)
    if (item['length']):
      ItemStr += ' ({})'.format(item['length'])

    # if this needs to have a non-null value, add that.
    if (item['not_null'] == True):
      ItemStr += ' NOT NULL'

    # if the item is a reference to another table, add that.
    if (item['reference'] and not item['primary']):
      ItemStr += ' REFERENCES {}({})'.format(item['ref_table'], item['ref_variable'])

    # if the item is a primary key, then add that.
    if (item['primary'] and not item['reference']):
      ItemStr += ' PRIMARY KEY'

    # If this is not the last in the list, dont need a comma
    if (item != table_item_list[-1]):
      QueryString += ItemStr + ',\n'
    else:
      QueryString += ItemStr
  
  # return the create query
  return QueryString + '\n);'

# # --------------------------------------------------------
# # -- DATABASE SCRIPTS ------------------------------------


# # -- DATABASE PRIMARY KEYS -------------------------------
# # --------------------------------------------------------

AbilityID = {'name':'AbilityID', 'type':'int', 'length':'', 'not_null':True,
    'primary':True, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

CardID = {'name':'CardID', 'type':'int', 'length':'', 'not_null':True,
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

ColorIdentityRefID = {'name':'ColorIdentityID', 'type':'int', 'length':'', 
    'not_null':False, 'primary':False, 'reference':True, 'ref_table':'ManaColorIdentity', 
    'ref_variable':'ColorIdentityID'}    

CostRefID = {'name':'CostID', 'type':'int', 'length':'', 'not_null':False,
    'primary':False, 'reference':True, 'ref_table':'CardCosts', 
    'ref_variable':'CostID'}

LayoutRefID = {'name':'LayoutID', 'type':'int', 'length':'', 'not_null':False,
    'primary':False, 'reference':True, 'ref_table':'CardLayouts', 
    'ref_variable':'LayoutID'}

ManaColorRefID = {'name':'ManaColorID', 'type':'int', 'length':'', 'not_null':False,
    'primary':False, 'reference':True, 'ref_table':'ManaColors', 
    'ref_variable':'ManaColorID'}

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

AbilityText = {'name':'AbilityText', 'type':'text', 'length':'500', 'not_null':False,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

CardName = {'name':'CardName', 'type':'char', 'length':'100', 'not_null':True,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

ColorIdentityName = {'name':'ColorIdentityName', 'type':'text', 'length':'500', 'not_null':True,
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

ObjectType = {'name':'ObjectType', 'type':'char', 'length':'100', 'not_null':True,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

OracleID = {'name':'OracleId', 'type':'int', 'length':'', 'not_null':True,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

Power = {'name':'Power', 'type':'char', 'length':'10', 'not_null':False,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

Toughness = {'name':'Toughness', 'type':'char', 'length':'10', 'not_null':False,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

TypeText = {'name':'TypeText', 'type':'text', 'length':'500', 'not_null':True,
    'primary':False, 'reference':False, 'ref_table':'', 
    'ref_variable':''}

# # --------------------------------------------------------
# # -- DATABASE DATA ---------------------------------------


# # -- FIELD/TABLE LISTS -----------------------------------
# # --------------------------------------------------------

needed_fields = ['object', 'id', 'oracle_id', 'name', 'layout', 'mana_cost', 'cmc', 'type_line', 'oracle_text', 'power', 'toughness', 'colors', 'color_identity', 'loyalty']

DatabaseTableNames = ['CardInformation', 'AbilityReference', 'CardAbilities', 'TypeReference', 'CardTypes', 'ColorIdentity', 'ManaColorReference', 'ManaColors', 'CardLayouts', 'CardCosts', 'CardStats']

# # --------------------------------------------------------
# # -- FIELD/TABLE LISTS -----------------------------------


# # -- DATABASE QUERIES ------------------------------------
# # --------------------------------------------------------

TableCreationQueries = []

CardInfoTable = create_table_query('CardInformation', [CardID, CardName, CostRefID, StatsRefID, LayoutRefID, ColorIdentityRefID, ObjectType, OracleID])
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


# # -- POPULATE TABLES -------------------------------------
# # --------------------------------------------------------

# Function that fills the top three variables
def populate_color_queries():
  """
  Generate a list of Insert Queries for every Mana color that is listed in the 
  Mana Colors list, then add them to a returnable list.

  Used Variables:

    Mana Color Table Definition
    ManaColorsTable = create_table_query('ManaColors', [ManaColorID, ManaColorName, ManaColorSymbol])
    
    Mana Colors List
    CardColors = [ {'name':'Colorless', 'colorid':1, 'symbol':'C'}, ...]

    Database Query
    Query = 'INSERT INTO ManaColors (ColorName, ManaColorID, ColorSymbol) VALUES ('Colorless', 1, 'C');'

    Query List
    ColorList = ['INSERT INTO ManaColors (ColorName, ManaColorID, ColorSymbol) VALUES ('Colorless', 1, 'C');', ...]
  """
  
  ColorList = []
  
  # loop through the list of card colors (White, Blue, Black, Red, Green, and colorless)
  for Color in CardColors:

    # Create a the first half of the query the name, id, and symbol
    Query = 'INSERT INTO ManaColors ({}, {}, {})'.format(ManaColorName['name'], ManaColorID['name'], ManaColorSymbol['name'])

    # add the second half of the query, the data from the given color
    Query += ' VALUES (\'{}\', {}, \'{}\');'.format(Color['name'], Color['colorid'], Color['symbol'])

    # print(Query, '\n')
    
    ColorList += [Query, ]

  return ColorList

# # --------------------------------------------------------

def populate_color_identity_queries():
  """
  Return a list of queries to fill the Card Identity Table using the 
  ColorIdentities List's names and ids.

  Used Variables:

    Color Identity Table
    ColorIdentityTable = create_table_query('ColorIdentity', [ColorIdentityID, ColorIdentityName])

    Color Identities Obj
    ColorIdentities = [ {'identityname':'Colorless', 'identityid':1, 'colors':['C']}, ... ]

    Database Query
    Query = 'INSERT INTO ColorIdentity (ColorIdentityName, ColorIdentityID) VALUES ('Colorless', 1);'

    Query List
    ColorIdentityQueries = ['INSERT INTO ColorIdentity (ColorIdentityName, ColorIdentityID) VALUES ('Colorless', 1);', ...]
  """

  ColorIdentityQueries = []

  for Identity in ColorIdentities:

    Query = 'INSERT INTO ColorIdentity ({}, {})'.format(ColorIdentityName['name'], ColorIdentityID['name'])

    Query += ' VALUES (\'{}\', {});'.format(Identity['identityname'], Identity['identityid'])
    # print(Query, '\n')

    ColorIdentityQueries += [Query, ]

  return ColorIdentityQueries

# # --------------------------------------------------------

def populate_color_identity_ref_queries():
  """
  Using the Color and Color Identity Lists, for every Identity, match it with 
  the colors that are related, then create a query to add them to the 
  ColorReference Table, then Return that list out.

  Used Variables:

    Color Reference Table
    ManaColorRefTable = create_table_query('ManaColorReference', [ColorIdentityRefID, ManaColorRefID])

    Mana Colors List
    CardColors = [{'name':'Colorless', 'colorid':1, 'symbol':'C'}, ...]

    Color Identities List
    ColorIdentities = [{'identityname':'Colorless', 'identityid':1, 'colors':['C']}, ...]

    Database Query
    Query = 'INSERT INTO ManaColorReference (...'

    Query List
    ColorIdentityReferenceQueries = ['INSERT INTO ManaColorReference ...', ...]
  """

  ColorIdentityReferenceQueries = []

  # loop through all of the identities, matching all colors within each identity 
  # with the given mana colors, if they match, add their ids to the reference table. 
  for Identity in ColorIdentities:
    for IdentityColor in Identity['colors']:
      for ManaColor in CardColors:
        if (IdentityColor == ManaColor['symbol']):

          # create the first half of the query, specifying the two categories colorid and identityid
          Query = 'INSERT INTO ManaColorReference ({}, {})'.format(ColorIdentityRefID['name'], ManaColorRefID['name'])

          # create the second half of the query, adding the two ids.
          Query += ' VALUES ({}, {});'.format(Identity['identityid'], ManaColor['colorid'])
          # print(Query, '\n')

          # add the query to the list.
          ColorIdentityReferenceQueries += [Query, ]
  
  return ColorIdentityReferenceQueries

# # --------------------------------------------------------

def populate_table_truncate_queries():
  """
    Create queries to truncate all tables so they can be 
    re-populated.

    Used Variables:

      Truncate Query List
      DatabaseTruncateQueries = ['DELETE FROM colors;', 'DELETE FROM color_ref', ...]
  """

  DatabaseTruncateQueries = []

  for table in DatabaseTableNames:
    DatabaseTruncateQueries += ['DELETE FROM {};'.format(table), ]

  return DatabaseTruncateQueries

# # --------------------------------------------------------
# # -- POPULATE TABLES -------------------------------------


# # -- DATABASE CONNECTION ---------------------------------
# # --------------------------------------------------------

# modified from: https://www.sqlitetutorial.net/sqlite-python/creating-database/
def create_database_connection(db_file):
  """ 
    Given a file name, create and return a database connection.

    Used Variables:

      Database File Name
      db_file = 'db_file.txt'

      Database Connection
      conn = sqlite3.connect(db_file)
  """

  conn = None

  # attempt to create and/or connect to the database file.
  try:
    conn = sqlite3.connect(db_file)

  # if the attempt fails, print the exception and error message.
  except sqlite3.Error as e:

    print('\n\ncreate_database_connection: Connection connect failed. \n{}'.format(e))

    assert(False)

  # return the connection
  return conn

# # --------------------------------------------------------

def close_database_connection(conn):
  """
    Close a provided database connection if it exists.

    Used Variables:

      Database Connection
      conn = sqlite3.connect('db_file')
"""

  # if the connection exists, close it.
  try:
    conn.close()

  # if it fails, print an error message and assert false.
  except sqlite3.Error as e:

    print('\n\nclose_database_connection: Connection.close failed. \n{}'.format(e))
    assert(False)

  # else return True.
  return True

# # --------------------------------------------------------

def execute_database_query(conn, query):
  """ 
    Execute a provided query through a database connection,
    if it exists.

    Used Variables:

      Database Connection
      conn = sqlite3.connect('db_file')

      Database Cursor
      c = conn.cursor()

      Database Query
      query = 'SELECT * FROM colors;'
  """

  # attempt to execute the query through a cursor.
  try:
    c = conn.cursor()
    c.execute(query)

  # if the attempt fails, print out the failure, the query, and the exception.
  except sqlite3.Error as e:

    print('\n\nexecute_database_query: Execution of query failed. \n\t{} \n{}'.format(query, e))
    assert(False)

  # else return false.
  return True

# # --------------------------------------------------------
# # -- DATABASE CONNECTION ---------------------------------


# # -- GLOBAL QUERIES --------------------------------------
# # --------------------------------------------------------

FillCardColors = populate_color_queries()
FillColorIdentities = populate_color_identity_queries()
FillColorReferences = populate_color_identity_ref_queries()
TruncateTables = populate_table_truncate_queries()

# # --------------------------------------------------------
# # -- GLOBAL QUERIES --------------------------------------


# # -- MAIN FUNCTION ---------------------------------------
# # --------------------------------------------------------

# main function
def main(verbose=False):
  """
    Main function for this file.
  """

  # Print out all of the table creations
  if (verbose):

    for i in TableCreationQueries:
      print(i, '\n')

    print('# --')

  # run through the list of insert queries and print them
  if (verbose):

    for queryList in [FillCardColors, FillColorIdentities, FillColorReferences, TruncateTables]:
      for query in queryList:
        print(query)

      print('# --')

  # create/connect to the database file, 'mcard.db'
  dbconnect = create_database_connection('mcard.db')

  # if our connection exists, 
  if dbconnect:

    print('Executing Queries ...')

    # loop through the three lists of query, executing all queries inside.
    for queryList in [TableCreationQueries, TruncateTables, FillCardColors, FillColorIdentities, FillColorReferences]:
      for query in queryList:
        
        # print the query stripping out all newlines and tabs.
        if (verbose):
          print('\n---- "{}"'.format((query.replace('\t', '')).replace('\n', ' ')))

        # execute the query
        execute_database_query(dbconnect, query)

    print('Finished Executing.')

    close_database_connection(dbconnect)

  else:

    print('main: Database connection does not exist.')

    assert(False)

  return

# # --------------------------------------------------------

# main
if (__name__ == '__main__'):

  main(verbose=True)

# # --------------------------------------------------------
# # -- MAIN FUNCTION ---------------------------------------


# NOTES

# BROKEN QUERY EXISTS

# ----------------------------------------------------------
# -- END OF FILE -------------------------------------------
