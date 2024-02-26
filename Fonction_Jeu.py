def get_distance(entity1_coordinates,entity2_coordinates):
    """Get the distance (distance between two entities)
    parameters
    -----------
    entity1_coordinates: the coordinates of the first entity (list or tuples)
    entity2_coordinates: the coordinates of the second entity (list or tuples)
    returns
    -----------
    distance: the distance between two entities (int)
    
    version
    -------
    specification: Remacle Thomas (v1 24/02/24)"""
    

def create_map_dictio():
    """create a dictionary with every usefull informations about the map creation from the map file

    notes
    -----
    the file should be in ./maps/

    version
    -------
    specification: Heynen Scott-Socrate (v1 20/02/24)
    """

def is_game_over():
    """check if the game is over

    returns
    -------
    True if the game is over, False otherwise (bool)

    version
    -------
    specification : Heynen Scott-Socrate (v1 20/02/24)"""

#
def display_map(map,player,seed):
    """display the map from the dictionary of create_map_dictio()
    parameters
    ----------
    map : dictionary of the map with the size of the map, rocks, player spawn and seeds (dic)
    players : dictionary of the different sheeps and their ownership (dic)
    grass : dictionary of the grass and their ownership (dic)

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """  
#
def try_spawn_sheep(sheep):
    """Spawn a sheep if possible
    parameters
    ----------
    sheep : player number (bol)
    
    notes
    -----
    if sheep is 0 -> it is player 1 (blue color)
    if sheep is 1 -> it is player 2 (red color)

    version
    -------
    specification: Heynen Scott-Socrate (v1 23/02/24)
    """

def set_grass (coordinates):
    """Set a grass at the sheep position if the seed is neutral
    parameters
    -------------
    coordinates: coordinates of the sheep
    version
    -------
    specification: Remacle Thomas (v1 24/02/24)"""
    
def growth_grass():
    """Growth all the grass, in fact add 1 to the life_stats and call grass_propagation if the live_stats is 11
    version
    -------
    specification: Remacle Thomas (v1 24/02/24)"""
    
def grass_propagation (coordinates):
    """Plant grass ont the all 8 box surroundings
    parameters
    ----------
    coordinates : coordinates (x,y) of the grass that will grow (tuples)
    version
    -------
    specification: Heynen Scott-Socrate (v1 23/02/24)
    """
def delete_emoji (emoji_coordonate):
    """delete the emoji we need 
    parameters
    ----------
    emoji_coordonate: coordonate in x,y of the emoji we want to delete, in fact remplace by a double space (tuples or list depend if the emoji is element of 
    the map or a sheep)
    version
    -------
    specification: Heynen Scott-Socrate (v1 23/02/24)
    """
def create_emoji (emoji_coordinate,emoji):
    """spawn the emoji we need 
    parameters
    ----------
    emoji_coordinate: coordinate in x,y of the emoji wanted to be create (tuples or list depend if the emoji is element of the map or a sheep)
    emoji: the emoji wanted to be spawn (str)
    version
    -------
    specification: Remacle Thomas (v1 25/02/24)
    """

def attack_sheep(sheep,attack_coordinates):
    """Attack a sheep if he is near enough to be attacked
    parameters
    ----------
    sheep : players sheep who attack (bol)      
    attack_coordinates: position in x and y where the sheep attacked is (tuples)
    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def move_sheep (old_coordinates,new_coordinates):
    """Move a sheep or attack if an another sheep is already there
    parameters
    ----------
    old_coordinates : coordinate in x,y of the sheep where he was (list)
    new_coordinates : coordinate in x,y of the sheep where it will move (list)
    
    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def sheep_graze(sheep, sheep_coordinates):
     """Graze a grass if the sheep is on this case
    parameters
    ----------
    sheep : player sheep (bol)
    sheep_coordinates: coordinates in x,y of the sheep (list)
    return
    ------
    emojii_deleted: coordinate in x and y of the grass that will be eaten (tuples)

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def translate_orders (player,messsage):
    """Translate a string message into a list to be usable for the program
    parameters
    ----------
    player : The player where the message from (bool)
    message : get the player message (str)
    
    return 
    orders: a list with every separate order. The orders are in the chronologic order (the first one is for the first phase) (list)
    ------

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def game_function ():
    """Read the list created by traslated_orders() and call others functions to play the game
    version 
    ---------------
    specification: Remacle Thomas (V1 26/02/24)"""

def look_rock(case_coordonate):
    """Look if a sheep can spawn or move on a case.
    parameters
    -----------
    case_coordonate: The coordonate x and y of the case we wanted to see (tuples)
    return
    -----------
    type: return if there are a rock, the limit of the maps or nothing. (str)
    version
    -------
    specification: Arthur Yernaux (v1 23/02/24)
    """
def look_sheep(case_coordonate):
    """Look if a sheep can spawn or move on a box.
    parameters
    -----------
    case_coordonate: The coordonate x and y of the case we wanted to see (tuples)
    return
    -----------
    type: return if there are a sheep the limit of the maps or nothing. (str) 
    version
    -------
    specification: Arthur Yernaux (v1 23/02/24)
    """

def look_seed(case_coordinates):
    """Look if a sheep can spawn or move on a case.
    parameters
    -----------
    case_coordinates: The coordinates (x,y) of the box wanted to be seen (tuples)
    return
    -----------
    type: return if there are a seed, the limit of the maps or nothing. (str)
    version
    -------
    specification: Arthur Yernaux (v1 23/02/24)
    """

def look_grass(coordinates):
    """Look if a grass can spawn on a box.
    parameters
    -----------
    coordinate: The coordinates (x,y) of the box we wanted to grow the grass (tuples)
    return
    -----------
    type: return True if the grass can spawn, return False otherwise (bool)
    version
    -------
    specification: Arthur Yernaux (v1 23/02/24)
    """
def check_void(coordinates):
    """Look if the box is outside of the map
    -----------
    coordinates: The coordinates (x,y) of the box to check (tuples)
    return
    -----------
    type: return True if the box is outside of the map, return False otherwise (bool) 
    version
    -------
    specification: Arthur Yernaux (v1 23/02/24)
    """
