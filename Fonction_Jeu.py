def get_distance(entity1_coordonate,entity2_coordonate):
    """Get the distance (distane between two entites)
    parameters
    -----------
    entity1_coordonate: the coordonate of the first entity (list or tuples)
    entity2_coordonate: the coordonate of the second entity (list or tuples)
    returns
    -----------
    distance: the distance between two entites (int)
    
    version
    -------
    specification: Remacle Thomas (v1 24/02/24)"""
    

def create_map_dictio():
    """create a dictionary with every usefull informations about the map creation from the #map file#

    notes
    -----
    the file should be in ./maps/

    version
    -------
    specification: Heynen Scott-Socrate (v1 20/02/24)
    """

def is_game_over():
    """check if game is over

    returns
    -------
    true if the game is over, false otherwise (bool)

    version
    -------
    specification : Heynen Scott-Socrate (v1 20/02/24)"""


def display_map(map,player,seed):
    """display the map from the diction
    parameters
    ----------
    
    map : dictonary of the map with the size of the map, rocks, player spawn and seeds (dic)
    players : dictonary of the différent sheeps and their ownership (dic)
    grass : dictonary of the grass and their ownership (dic)

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """  

def try_spawn_sheep(sheep):
    """Spawn a sheep if it's needed
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

def set_grass (coordonate):
    """Set a grass a the sheep position if the seed is neutral
    parameters
    -------------
    coordonate: coordonate of the sheep
    version
    -------
    specification: Remacle Thomas (v1 24/02/24)"""
    
def growth_grass():
    """Growth all the grass, in fact add 1 to the life_stats and call grass_propagation if the live_stats is 11
    version
    -------
    specification: Remacle Thomas (v1 24/02/24)"""
    
def grass_propagation (coordonate):
    """Propage the grass around
    parameters
    ----------
    grass_coordinate : coordonate in x,y of the grass that will grow (tuples)
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
def create_emoji (emoji_coordonate,emoji):
    """spawn the emoji we need 
    parameters
    ----------
    emoji_coordonate: coordonate in x,y of the emoji we want to create (tuples or list depend if the emoji is element of the map or a sheep)
    emoji: the emoji we want to spawn (str)
    version
    -------
    specification: Remacle Thomas (v1 25/02/24)
    """

def attack_sheep(sheep,attack_coordonate):
    """Attack a sheep if he is near enough to be attack
    parameters
    ----------
    sheep : players sheep who attack (bol)      
    attack_coordonate: position in x and y where the sheep attacked is (tuples)
    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def move_sheep (old_coordonate,new_coordonate):
    """Move a sheep if he want to move or if i was attack
    parameters
    ----------
    old_coordinate : coordinate in x,y of the sheep where he was (list)
    new_coordinate : coordinate in x,y of the sheep where it will move (list)
    
    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def sheep_graze(sheep, sheep_coordonate):
     """Graze a grass if the sheep is on this case and the case
    parameters
    ----------
    sheep : player sheep (bol)
    sheep_coordonate: placement in x and y of the sheep (list)
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
    """Read the list created by traslated orders and call other function to play the game
    version 
    ---------------
    specification: Remacle Thomas (V1 26/02/24)"""

def look_rock(case_coordonate):
    """Look if there are a rock on the case or not.
    parameters
    -----------
    case_coordonate: The coordonate x and y of the case we wanted to see (tuples)
    return
    -----------
    type: return if there are a rock on the case or not 1 if True 0 if False (bool)
    version
    -------
    specification: Arthur Yernaux (v1 23/02/24)
    """
def look_sheep(case_coordonate):
    """Look if there are a sheep on the case or not.
    parameters
    -----------
    case_coordonate: The coordonate x and y of the case we wanted to see (tuples)
    return
    -----------
    type: return if there are a sheep on the case or not 1 if True 0 if False (bool)
    version
    -------
    specification: Arthur Yernaux (v1 23/02/24)
    """

def look_seed(case_coordonate):
    """Look if there are a seed on the case or not.
    parameters
    -----------
    case_coordonate: The coordonate x and y of the case we wanted to analyse (tuples)
    return
    -----------
    type: return if there are a seed on the case 1 if True 0 if False (bool)
    version
    -------
    specification: Arthur Yernaux (v1 23/02/24)
    """

def look_grass(case_coordonate):
    """Look if there are a grass or not in this case.
    parameters
    -----------
    case_coordonate: The coordonate x and y of the case we wanted to analyse (tuples)
    return
    -----------
    type: return if there are a grass on the case or not 1 if True 0 if False (bool)
    version
    -------
    specification: Arthur Yernaux (v1 23/02/24)
    """
def look_void(case_coordonate):
    """Look the case where we want to go or set up something is outside the map
    -----------
    case_coordonate: The coordonate x and y of the case wanted to analyse (tuples)
    return
    -----------
    type: return if the case is empty or not, 1 if empty 0 if not empty (bool) 
    version
    -------
    specification: Arthur Yernaux (v1 23/02/24)
    """
