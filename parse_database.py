
# -- DATABASE CREATION AND QUERIES -------------------------
# ----------------------------------------------------------


# # -- IMPORTS ---------------------------------------------
# # --------------------------------------------------------

# the sql library
import sqlite3

# TODO - look into using 'sqlcipher'
# # http://charlesleifer.com/blog/encrypted-sqlite-databases-with-python-and-sqlcipher/

# import the info table
from global_variables import create_info

# import the reference tables
from global_variables import create_ability_ref, create_abilities,  create_artist_ref, create_artists, create_legality_ref, create_formats, create_set_ref, create_sets, create_type_ref, create_types

# import the singlular tables
from global_variables import create_colors, create_costs, create_dates, create_images, create_layouts, create_rarity, create_artist_ref, create_stats

from global_variables import color_identities

from global_variables import create_queries, populate_queries

# # --------------------------------------------------------
# # -- IMPORTS ---------------------------------------------


# # -- DATABASE FUNCTIONS ----------------------------------
# # --------------------------------------------------------

def run_db_query(db_name, query):
  """
  Opens up a given database, runs a given query, then closes the connection.
  """

  connection = sqlite3.connect(db_name)
  cursor = connection.cursor()

  cursor.execute(query)

  connection.commit()
  connection.close()

# ----------------------------------------------------------

def make_new_database(db_name):
  """
  Run through all of the create table functions, as well as populate several of
  the tables.
  """

  # run through all the table creation queries
  for query in create_queries:
    run_db_query(db_name, query)

  # run through the queries that populate tables
  for query in populate_queries:
    run_db_query(db_name, query)

  # return out
  return

# # --------------------------------------------------------
# # -- DATABASE FUNCTIONS ----------------------------------


# # -- MAIN FUNCTION ---------------------------------------
# # --------------------------------------------------------

if (__name__ == '__main__'):
  """
  do the things
  """

  # make_new_database('scry.db')

  print(len(color_identities))

# # --------------------------------------------------------
# # -- MAIN FUNCTION ---------------------------------------


# ----------------------------------------------------------
# -- END OF FILE -------------------------------------------
