
# -- DATABASE SCRIPTS --------------------------------------
# ----------------------------------------------------------


# # -- CREATE GENERAL INFO TABLE ---------------------------
# # --------------------------------------------------------

# CREATE CARD INFO TABLE STRING - check
create_info = """
  CREATE TABLE CardInformation (
    name CHAR(100),
    id INTEGER NOT NULL PRIMARY KEY,
    reprinted BOOLEAN,
    lang CHAR(16),
    loyalty CHAR(2),
    color_id INTEGER REFERENCES CardColors(color_id),
    cost_id INTEGER REFERENCES CardCosts(cost_id),
    date_id INTEGER REFERENCES CardDates(date_id),
    layout_id INTEGER REFERENCES CardLayouts(layout_id),
    rarity_id INTEGER REFERENCES CardRarity(rarity_id),
    stats_id INTEGER REFERENCES CardStats(stats_id),
    );"""
# --

# # --------------------------------------------------------
# # -- CREATE GENERAL INFO TABLE ---------------------------


# # -- CREATE REFERENCE TABLE PAIRS ------------------------
# # --------------------------------------------------------

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


# CREATE CARD SET TABLES STRING - check
create_set_ref = """
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

# # --------------------------------------------------------
# # -- CREATE REFERENCE TABLE PAIRS ------------------------


# # -- CREATE SINGLE TABLES --------------------------------
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


# CREATE CARD STAT TABLE STRING - check
create_stats = """
  CREATE TABLE CardStats (
    stats_id INTEGER PRIMARY KEY,
    power CHAR(3),
    toughness CHAR(3)
    );"""
# --

# # --------------------------------------------------------
# # -- DATABASE SCRIPTS ------------------------------------


# # -- COLOR IDENTITIES ------------------------------------
# # --------------------------------------------------------

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


# # --------------------------------------------------------
# # -- OTHER GLOBAL VARIABLES ------------------------------

# # -- OTHER GLOBAL VARIABLES ------------------------------
# # --------------------------------------------------------


# ----------------------------------------------------------
# -- END OF FILE -------------------------------------------
