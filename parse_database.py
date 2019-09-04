# --

import sqlite3

from global_variables import *

# ----------------------------------------------------------


def make_db(db_name, data_obj):
  """
  Creates a test table in the database 'scry.db'.
  """

  connection = sqlite3.connect('scry.db')
  cursor = connection.cursor()

  table_string = """
  CREATE TABLE test (
    num INTEGER PRIMARY KEY, 
    type STRING);
    """

  cursor.execute(table_string)

  connection.commit()
  connection.close()

# ----------------------------------------------------------


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


def make_new_database():
  """
  Run through all of the create table functions, as well as populate several of
  the tables.
  """

  # name of the database that we are going to create
  db = 'scry.db'

  # a list of all the create table queries
  create_queries = [create_info, create_ability_ref, create_abilities, create_artists, create_colors, create_costs, create_dates, create_images, create_legality_ref, create_formats, create_layouts, create_rarity, create_set_reference, create_sets, create_type_ref, create_types]

  # run through all the table creation queries
  for query in create_queries:
    run_db_query(db, query)

  # 
  populate_queries = []

  for query in populate_queries:
    run_db_query(db, query)

  return

# --


if (__name__ == '__main__'):
  """
  do the things
  """

  make_new_database()