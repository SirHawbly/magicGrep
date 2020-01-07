
# -- DATABASE SCRIPTS --------------------------------------
# ----------------------------------------------------------


# # -- CREATE GENERAL INFO TABLE ---------------------------
# # -------------------------------------------------------- 

# CREATE CARD INFO TABLE STRING - check
create_info = """
  CREATE TABLE CardInformation (
    id INTEGER NOT NULL PRIMARY KEY,
    name CHAR(100),
    lang CHAR(16),
    color_id INTEGER REFERENCES CardColors(color_id),
    cost_id INTEGER REFERENCES CardCosts(cost_id),
    layout_id INTEGER REFERENCES CardLayouts(layout_id),
    stats_id INTEGER REFERENCES CardStats(stats_id),
    );"""
# --

# # -------------------------------------------------------- 
# # -- CREATE GENERAL INFO TABLE ---------------------------


# # -- CREATE REFERENCE TABLE PAIRS ------------------------
# # --------------------------------------------------------

# CREATE CARD TYPE TABLES STRING - check
create_type_ref = """
  CREATE TABLE CardTypeReference (
    id INTEGER REFERENCES CardInformation(id),
    type_id INTEGER REFERENCES CardTypes(type_id)
    );"""

create_types = """
  CREATE TABLE CardTypes (
    type_id INTEGER NOT NULL PRIMARY KEY,
    type_line CHAR(200)
    );"""
# --

# CREATE CARD ABILITY TABLES STRINGS - check
create_ability_ref = """
  CREATE TABLE CardAbilityReference (
    id INTEGER REFERENCES CardInformation(id), 
    ability_id INTEGER REFERENCES CardAbilities(ability_id)
    );"""

create_abilities = """
  CREATE TABLE CardAbilities (
    ability_id INTEGER PRIMARY KEY, 
    oracle_text VARCHAR(256)
    );"""
# --

# # --------------------------------------------------------
# # -- CREATE REFERENCE TABLE PAIRS ------------------------


# # -- CREATE SINGULAR TABLES ------------------------------
# # --------------------------------------------------------

# CREATE CARD COLOR TABLE STRING - check
create_colors = """
  CREATE TABLE CardColors 
    color_id INTEGER NOT NULL PRIMARY KEY,
    identity_name CHAR(20),
    colors CHAR(5)
    );"""
# --


# CREATE CARD COST TABLE STRING - check
create_costs = """
  CREATE TABLE CardCosts (
    cost_id INTEGER PRIMARY KEY,
    mana_cost CHAR(10),
    cmc INTEGER
    );"""
# --

# CREATE CARD LAYOUT TABLE STRING - check
create_layouts = """
  CREATE TABLE CardLayouts (
    layout_id INTEGER PRIMARY KEY,
    layout_string CHAR(20)
    );"""
# --

# CREATE CARD STAT TABLE STRING - check
create_stats = """
  CREATE TABLE CardStats (
    stats_id INTEGER PRIMARY KEY,
    power CHAR(3),
    toughness CHAR(3),
    loyalty CHAR(3)
    );"""
# --

# # --------------------------------------------------------
# # -- CREATE SINGLE TABLES --------------------------------


# -- DATABASE SCRIPTS --------------------------------------
# ----------------------------------------------------------