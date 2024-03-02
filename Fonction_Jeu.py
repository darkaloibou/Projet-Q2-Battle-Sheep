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
    specification : Heynen Scott-Socrate (v1 20/02/24) => V2 A VALIDER"""
    
    if (players['player_1']['nbr_of_grass'] >= 100 ) or ( players['player_2']['nbr_of_grass'] >= 100 ) : #look if a player have > 100 grass
        return True 
    elif map['nbr_of_turns'] >= 20 and ( players['player_1']['nbr_of_grass'] ==0 or players['player_2']['nbr_of_grass'] == 0 ):
        return True
    else:
        return False

def display_map(map):
    """display the map from the dictionary of create_map_dictio()
    parameters
    ----------
    map : all the elements of the dicitonnary of the map
    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    specification: Aloïs Baurant (v2 02/03/24)
    """
    # Recharger la map a chaque round ? 
    # Charge la taille de la map et met la longeur de la map en x et y.
    x = map["map_size"][0]
    y = map["map_size"][1]
    # Construction du damier
    while y > 0:
        if y %2 == 0:
            print((term.peru_on_seagreen('  ')+term.on_darkolivegreen('  '))*int(x/2))
        else:
            print((term.on_darkolivegreen('  ')+term.peru_on_seagreen('  '))*int(x/2))
        y -= 1
    # Va chercher tout les éléments de la map
    for rock in map["rocks"] :
        create_emoji(map["rocks"[rock]],​"🪨")

    for sapwns in map["sapwns"] :
        create_emoji(map["sapwns"[spawn]],​"​ ") # Voir comment display les spawn de moutons

    for seed in map["seeds"] :
        create_emoji(map["seeds"[seed]],​"​🌱")
    # Il faut regarder si on display la map 1 fois et modifier les élémément ou on recharge la map a chaque tours
    # Dictonary ; Length
    # playerscore_1=str(count_grass(Dictonary['player_grass1']))
    # playerscore_2=str(count_grass(Dictonary['player_grass2']))
    # minus=(len(playerscore_1))
    # print (term.move_xy(Length*2-minus,0)+term.blue+playerscore_1)
    # print (term.move_xy(0,0)+term.red+playerscore_2)
    # print (term.home)

def try_spawn_sheep(sheep):
    """Spawn a sheep if possible
    parameters
    ----------
    sheep : player number (int)
    
    notes
    -----
    if sheep is 0 -> it is player 1 (blue color)
    if sheep is 1 -> it is player 2 (red color)

    version
    -------
    specification: Heynen Scott-Socrate (v1 23/02/24)
    """

def set_grass (coordinates):
    """Set a grass at the sheep position if the seed isn't already take by a player
    parameters
    -------------
    coordinates: coordinates of the sheep
    version
    -------
    specification: Remacle Thomas (v1 24/02/24)"""
    
def growth_grass():
    """Growth all the grass, in fact add 1 to the life_stats and call grass_propagation if the live_stats is 10
    version
    -------
    specification: Remacle Thomas (v1 24/02/24)"""
    
def grass_propagation (coordinates):
    """Plant grass on the all 8 box surroundings
    parameters
    ----------
    coordinates : coordinates (x,y) of the grass that will grow (tuples)
    version
    -------
    specification: Heynen Scott-Socrate (v1 23/02/24)
    """
def delete_emoji (emoji_coordinates):
    """delete the emoji we need 
    parameters
    ----------
    emoji_coordinates: coordinates (x,y) of the emoji to delete, in fact remplace by a double space (tuples or list depend if the emoji is element of 
    the map or a sheep/grass)
    version
    -------
    specification: Heynen Scott-Socrate (v1 23/02/24)
    """
def create_emoji (emoji_coordinates,emoji):
    """spawn the emoji we need 
    parameters
    ----------
    emoji_coordinates: coordinate in (x,y) of the emoji wanted to be created (tuples or list depend if the emoji is element of the map or a sheep/grass)
    emoji: the emoji wanted to be spawn (str)
    version
    -------
    specification: Remacle Thomas (v1 25/02/24)
    """
    emoji_d=["🐑","🐐", "🌾"]
    if emoji in emoji_d[0]:
        print(term.move_xy(emoji_coordinates[0],emoji_coordinates[1])+term.on_red+emoji)
    elif emoji in emoji_d [1]:
        print(term.move_xy(emoji_coordinates[0],emoji_coordinates[1])+term.on_blue+emoji)
    elif emoji in emoji_d[2]:
        for grass_i in grass:
            if grass[grass_i]['xy']==emoji_coordinates:
                if grass[grass_i]['life_state']==0:
                    print(term.move_xy(emoji_coordinates[0],emoji_coordinates[1])+term.on_red+emoji)
                else:
                    print(term.move_xy(emoji_coordinates[0],emoji_coordinates[1])+term.on_blue+emoji)
    else:
        coordinate=emoji_coordinates[0]/2
        if emoji_coordinates[1]%2!=0:
            if (coordinate)%2==0:
                print (term.move_xy(emoji_coordinates[0],emoji_coordinates[1])+term.peru_on_seagreen+emoji)
            else:
                print (term.move_xy(emoji_coordinates[0],emoji_coordinates[1])+term.on_darkolivegreen+emoji)
        else:
            if (coordinate)%2==0:
                print (term.move_xy(emoji_coordinates[0],emoji_coordinates[1])+term.on_darkolivegreen+emoji)
            else:
                print (term.move_xy(emoji_coordinates[0],emoji_coordinates[1])+term.peru_on_seagreen+emoji)
    
def attack_sheep(sheep,attack_coordinates):
    """Attack a sheep if he is near enough to be attacked
    parameters
    ----------
    sheep : players sheep who attack (0 for player 1, 1 for player 2) (int)     
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
     """Graze a grass if the sheep is on this box
    parameters
    ----------
    sheep : player sheep (0 for player 1, 1 for player 2) (int)
    sheep_coordinates: coordinates (x,y) of the sheep (list)
    return
    ------
    emojii_deleted: coordinates (x,y) of the grass that will be eaten (tuples)

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def translate_orders(player,messsage):
    """Translate a string message into a list to be usable for the program
    parameters
    ----------
    player : The player that wrote the message, 0 if player 1 , 1 if player 2 (bool)
    message : get the player message (str)
    
    return 
    orders: a list with every separate order. The orders are in the chronologic order (the first one is for the first phase) (list)
    ------

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def game_function():   #j'ai changé la spécification mais il faut que je demande au tuteur ou assistant pour la mettre dans se dossier
    """Read the list created by traslated_orders() and call others functions to play the game
    version 
    ---------------
    specification: Remacle Thomas (V1 26/02/24)"""
    for order in player_1_orders : # ATTENTION les coordonnée sont x2
        if order=='sheep':
            try_spawn_sheep(1)
    for order in player_2_orders :
        if order=='sheep':
            try_spawn_sheep(2)
    growth_grass() #il faut regarder si on fusionne growth_grass et grass_propagation
    for order in player_1_orders:
        if 'x' in order:
            order_string=order.split(":")
            attack_coordinates=order_string[2][1:]
            enemy_coordinates=attack_coordinates.split("-")  #demander si on mets les coordonées du mouton qui attaque pour être sur qu'il peut attaquer
            attack_sheep(1,enemy_coordinates)
    for order in player_2_orders:
        if 'x' in order:
            order_string=order.split(":")
            attack_coordinates=order_string[2][1:]
            enemy_coordinates=attack_coordinates.split("-")  #demander si on mets les coordonées du mouton qui attaque pour être sur qu'il peut attaquer
            attack_sheep(2,enemy_coordinates) #voir si on bouge les moutons aprés l'attaque pour éviter des problémes de tours
    for order in player_1_orders:
        if '@' in order:
            order_string=order.split(":")
            coordinate=order_string[2][1:]
            new_coordinates=coordinate.split("-")
            coordinate=order_string[1]
            old_coordinates=coordinate.split("-")
            move_sheep(old_coordinates,new_coordinates)
    for order in player_2_orders:
        if '@' in order:
            order_string=order.split(":")
            coordinate=order_string[2][1:]
            new_coordinates=coordinate.split("-")
            coordinate=order_string[1]
            old_coordinates=coordinate.split("-")
            move_sheep(old_coordinates,new_coordinates)
    for order in player_1_orders:
        if '*' in order:
            order_string=order.split(":")
            coordinate=order_string[1]
            grass_coordinate=coordinate.split("-")
            sheep_graze(0,grass_coordinate)
    for order in player_2_orders:
        if '*' in order:
            order_string=order.split(":")
            coordinate=order_string[1]
            grass_coordinate=coordinate.split("-")
            sheep_graze(1,grass_coordinate)

def look_rock(case_coordinates):
    """Look if there are a rock on the case or not
    
    parameters
    -----------
    case_coordinates: The coordinates (x,y) of the case we wanted to check (tuples)
    
    return
    -----------
    type: return 1 if there is a rock return 0 otherwise (bool)
    
    version
    -------
    specification: Arthur Yernaux (v1 23/02/24)
    """
def look_sheep(box_coordinates):
    """Look if there are a sheep on the case or not
    parameters
    -----------
    box_coordinates: The coordinates (x,y) of the box to check (tuples)
    
    return
    -----------
    type: type: return 1 if there is a sheep return 0 otherwise (bool)
    
    version
    -------
    specification: Arthur Yernaux (v1 23/02/24)
    """

def look_seed(box_coordinates):
    """Look if there is a seed on the box or not.
    parameters
    -----------
    box_coordinates: The coordinates (x,y) of the box to check (tuples)
    
    return
    -----------
    type: return if there are a seed on the case 1 if True 0 if False (bool)
    
    version
    -------
    specification: Arthur Yernaux (v1 23/02/24)
    """

def look_grass(coordinates):
    """Look if there is a grass or not in this box.
    parameters
    -----------
    coordinate: The coordinates (x,y) of the grass to grow (tuples)
    return
    -----------
    type: return 1 if there is a grass return 0 otherwise (bool)
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
