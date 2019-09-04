

# ----------------------------------------------------------

# CREATE CARD TABLE STRING - check
create_info = """
  CREATE TABLE CardInformation (
    name CHAR(100),
    id INTEGER NOT NULL PRIMARY KEY,
    reprinted BOOLEAN,
    lang CHAR(16),
    color_id INTEGER REFERENCES CardColors(color_id),
    cost_id INTEGER REFERENCES CardCosts(cost_id),
    date_id INTEGER REFERENCES CardDates(date_id),
    layout_id INTEGER REFERENCES CardLayouts(layout_id),
    rarity_id INTEGER REFERENCES CardRarity(rarity_id),
    stats_id INTEGER REFERENCES CardStats(stats_id),
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


# CREATE CARD ARTIST TABLES STRINGS - check
create_artist_ref = """
  CREATE TABLE CardArtistReference (
    id INTEGER REFERENCES CardInformation(id), 
    artist_name INTEGER REFERENCES CardArtists(artist_name)
    );"""

create_artists = """
  CREATE TABLE CardArtists (
    artist_id INTEGER NOT NULL PRIMARY KEY,
    artist_name CHAR(50)
    );"""
# --


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


# CREATE CARD DATE TABLE STRING - check
create_dates = """
  CREATE TABLE CardDates (
    date_id INTEGER PRIMARY KEY, 
    date CHAR(20)
    );"""
# --


# CREATE CARD IMAGE TABLE STRING
create_images = """
  CREATE TABLE CardImages (
    id REFERENCES CardInformation(id),
    small CHAR(150),
    normal CHAR(150),
    large CHAR(150),
    png CHAR(150),
    art_crop CHAR(150),
    border_crop CHAR(150)
    );"""
# --


# CREATE CARD FORMAT TABLES STRING - check
create_legality_ref = """
  CREATE TABLE CardLegalityReference (
    id INTEGER REFERENCES CardInformation(id),
    format_id INTEGER REFERENCES CardLegality(format_id)
    );"""

create_formats = """
  CREATE TABLE CardFormats (
    format_id INTEGER PRIMARY KEY, 
    format CHAR(20)
    );"""
# --


# CREATE CARD LAYOUT TABLE STRING - check
create_layouts = """
  CREATE TABLE CardLayouts (
    layout_id INTEGER PRIMARY KEY,
    layout_string CHAR(20)
    );"""
# --


# CREATE CARD RARITY TABLE STRING - check
create_rarity = """
  CREATE TABLE CardRarity (
    rarity_id INTEGER PRIMARY KEY, 
    rarity CHAR(10)
    );"""
# --  


# CREATE CARD SET TABLES STRING - check
create_set_reference = """
  CREATE TABLE CardSetReference (
    id INTEGER, 
    set_id INTEGER
    );"""

create_sets = """
  CREATE TABLE CardSets (
    set_id INTEGER PRIMARY KEY, 
    set_symbol CHAR(10),
    set_name CHAR(50)
    );"""
# --


# CREATE CARD STAT TABLE STRING - check
create_stats = """
  CREATE TABLE CardStats (
    stats_id INTEGER PRIMARY KEY,
    power CHAR(3),
    toughness CHAR(3)
    );"""
# --


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


# ----------------------------------------------------------


# magic color identities
color_identities = {

  # none
  "Colorless": ["C"],

  # monos
  "Mono Red": ["R"],
  "Mono Black": ["B"],
  "Mono Blue": ["U"],
  "Mono Green": ["G"],
  "Mono White": ["W"],
  
  # duals
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

  # triads
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

  # quads
  "Chaos": ["U", "R", "B", "G"],
  "Aggression": ["W", "R", "B", "G"],
  "Altruism": ["U", "W", "R", "G"],
  "Growth": ["U", "W", "B", "G"],
  "Artifice": ["U", "W", "R", "B"],

  # five
  "Domain": ["W", "U", "B", "R", "G"],
}


# ----------------------------------------------------------
