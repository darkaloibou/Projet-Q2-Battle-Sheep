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
    

def create_map_dictio(map_path):
    """create a dictionary with every usefull informations about the map creation from the map file

    parameters
    ----------
    the path to the map file

    version
    -------
    specification: Heynen Scott-Socrate (v1 20/02/24) V2 à confirmer
    """
    map={}
    


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

def try_spawn_sheep(grp):
    """Spawn a sheep if possible
    parameters
    ----------
    grp : player number (int)
    
    notes
    -----
    if grp is 1 -> it is player 1 (blue color)
    if grp is 2 -> it is player 2 (red color)

    version
    -------
    specification: Heynen Scott-Socrate (v1 23/02/24)
    """
    if grp == 1
        for sheep in players['player_1']['sheeps']:
            if map['spawn']['spawn_1'] == players['player_1']['sheeps'][sheep]['xy']: #attention x,y bouge? #look if the spawn is free to spawn a sheep
                return
        spawn_sheep() # à vérif quel fonction 
    else:
        for sheep in players['player_2']['sheeps']:
            if map['spawn']['spawn_2'] == players['player_2']['sheeps'][sheep]['xy']: #attention x,y bouge? #look if the spawn is free to spawn a sheep
                return
        spawn_sheep() # à vérif quel fonction 

def set_grass (coordinates,emoji):
    """Set a grass at the sheep position if the seed isn't already take by a player
    parameters
    -------------
    emoji: The emoji of the sheep 
    coordinates: coordinates of the sheep
    version
    -------
    specification: Remacle Thomas (v1.1 24/02/24)"""
    emoji_d=["🐑","🐐"]
    for seed in map['seed']:
        if coordinates==map['seed'][seed]:
            del map ['seed'][seed]
            if emoji==emoji_d[0]:
                grass[coordinates]={'age':1,'life_stats':1}
            else:
                grass[coordinates]={'age':1,'life_stats':2}
    
def update_grass (coordinates):
    """Plant grass on the all 8 box surroundings
    parameters
    ----------
    coordinates : coordinates (x,y) of the grass that will grow (tuples)
    version
    -------
    specification: Heynen Scott-Socrate (v1 23/02/24)
    """
    for herbs in grass:  #ATTENTION A BIEN CREER UN DICO GRASS DANS LA MAIN FONCTION
        grass[herbs]['age'] += 1
        if grass[herbs]['age'] == 10:
            grass['grass_'+str(len(grass)+1)] = {'xy':[x,y],'age':0, player:1} #attention xy et player pas définis
            #prblm si il y a déjà une plante ça va la reset
def manage_emoji (emoji_coordinates,emoji=' '): 
    """change the emoji we need to change
    parameters
    ----------
    emoji_coordinates: coordinate in (x,y) of the emoji wanted to be created (tuples or list depend if the emoji is element of the map or a sheep/grass)
    emoji: the emoji wanted to be spawn, by default recreate the case without emoji on the box (str)
    version
    -------
    specification: Remacle Thomas (v1.1 25/02/24)
    """
    ""
    emoji_d=["🐑","🐐", "🌾"]
    if emoji in emoji_d[0]:
        print(term.move_xy(emoji_coordinates[0],emoji_coordinates[1])+term.on_red+emoji)
    elif emoji in emoji_d [1]:
        print(term.move_xy(emoji_coordinates[0],emoji_coordinates[1])+term.on_blue+emoji)
    elif emoji in emoji_d[2]:
        for grass_i in grass:
            if grass[grass_i]==emoji_coordinates:
                if grass[grass_i]['life_state']==1:
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
    
def attack_sheep(sheep,attack_coordinates): #Il faut ajouter les coordonées du mouton qui attaque
    """Attack a sheep if he is near enough to be attacked
    parameters
    ----------
    sheep : players sheep who attack (0 for player 1, 1 for player 2) (int)     
    attack_coordinates: position in x and y where the sheep attacked is (tuples)
    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """

def move_sheep (old_coordinates,new_coordinates): # ! (scott) ATTENTION IL FAUT RETIRER LE FAIT QU'IL ATTACK SI IL Y A UN MOUTON !
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

def translate_orders(player):
    """Translate a string message into a list to be usable for the program
    parameters
    ----------
    player : The player that wrote the message, 0 if player 1 , 1 if player 2 (bool)
    message : ask the player the message
    
    return 
    orders: a list with every separate order. The orders are in the chronologic order (the first one is for the first phase) (list)
    ------

    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """
    
    get_order = str(input("Insert your instruction"))
    return split_all_order = get_order.split(',')
    

def game_function():   #j'ai changé la spécification mais il faut que je demande au tuteur ou assistant pour la mettre dans se dossier
    """Read the list created by traslated_orders() and call others functions to play the game
    version 
    ---------------
    specification: Remacle Thomas (V1 26/02/24)"""
   for order in player_1_orders :
        if order=='sheep':
            try_spawn_sheep(1)
    for order in player_2_orders :
        if order=='sheep':
            try_spawn_sheep(2)
    growth_grass() #il faut regarder si on fusionne growth_grass et grass_propagation
    my_attacl_list=[]
    for order in player_1_orders:
        if 'x' in order:
            my_attacl_list.append(order)
    for order in player_2_orders:
        if 'x' in order:
            my_attacl_list.append(order)
    attack_count=0
    for attack in my_attacl_list: 
        order_string=order.split(":")
        attack_coordinates=order_string[1][1:]
        enemy_coordinates=attack_coordinates.split("-")
        attacker_coordinates=order_string[0].split("-")
        if not can_attack(attacker_coordinates,enemy_coordinates):  #demander si on mets les coordonées du mouton qui attaque pour être sur qu'il peut attaquer
            my_attacl_list.remove(attack)
    for attack in my_attacl_list:
        order_string=order.split(":")
        attack_coordinates=order_string[1][1:]
        enemy_coordinates=attack_coordinates.split("-")
        attacker_coordinates=order_string[0].split("-")
        attack_sheep(attacker_coordinates,enemy_coordinates)
    for order in player_1_orders:
        if '@' in order:
            order_string=order.split(":")
            coordinate=order_string[1][1:]
            new_coordinates=coordinate.split("-")
            coordinate=order_string[0]
            old_coordinates=coordinate.split("-")
            move_sheep(old_coordinates,new_coordinates)
    for order in player_2_orders:
        if '@' in order:
            order_string=order.split(":")
            coordinate=order_string[1][1:]
            new_coordinates=coordinate.split("-")
            coordinate=order_string[0]
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

def can_move(xy_sheep, xy_destination):  #je vais le prendre (scott)
    '''check if a sheep can move to the box 

    parameters
    ----------
    xy_destination :  the (x,y) coordinates where the sheep is (list)
    xy_destination : the (x,y) coordinates where the sheep want to go (list)

    returns
    -------
    return True if the sheep can move, return False otherwise (bool)
        
    version
    -------
    specification: Heynen Scott-Socrate (v1 09/03/24)
    '''
    
    if -1 > xy_destination[0] - xy_sheep[0] or xy_destination[0] - xy_sheep[0] > 1: #look if the sheep is more than 1 box away (abscissa only)
        return False
    elif -1 > xy_destination[1] - xy_sheep[1] or xy_destination[1] - xy_sheep[1] >1 : #look if the sheep is more than 1 box away (ordinate only)
        return False
    elif what_in_the_box(xy_destination,'rock'):
        return False
    elif what_in_the_box('void'):
        return False
    elif what_in_the_box('spawn'):
        return False
    elif what_in_the_box('sheep'):
        return False 
    else:
        return True

def can_graze():


def is_in_the_box(xy,search):
    '''return True if there is the asked-thing in the box 
    
    parameters
    ----------
    xy : the [x,y] coordinates where search (list)
    search : the specific element to search:
                -put 'rock' to search for rock, 
                -put 'sheep' for sheep, 
                -put 'void' to see if it's outside of the map
                -put 'spawn' to see if there is a spawn
                -put 'grass' for grass
                (str)
                
    return
    ------
    return True if the searched element is on the box, return False otherwise (bool)
    
    version
    -------
    specification: Heynen Scott-Socrate (v1 09/03/24)'''
                
    if search == 'rock':
        for rock in map['rocks']:
            if xy == map['rocks'][rock]:
                return True
            else:
                return False
            
    if search == 'spawn':
        for spawn in map['spawn']:
            if xy == map['spawn'][spawn]:
                return True
            else:
                return False
            
    if search == 'void':
        if xy[0]> map['map_size'][0]: #look if outside (abscissa only)
            return True
        elif xy[1]> map['map_size'][1]: #look if outside (ordinate only)
            return True
        else:
            return False
        
    if search == 'grass':
        for herbs in grass:
            if xy == grass[herbs]['xy']:
                return True
        return False
    
    if search == 'sheep':
        for sheep in players['player_1']['sheeps']:
            if xy == players['player_1']['sheeps'][sheep]['xy']:
                return True
        for sheep in players['player_2']['sheeps']:
            if xy == players['player_2']['sheeps'][sheep]['xy']:
                return True
        return False

def can_attack (sheep,target):
    """Look if you can attack an other sheep or not
   
    variable:
    sheep : your own position (x,y)tuple
    target: the coordonate of the sheep you want attack (x,y)tuple
  
    return:
    answer: true if you can false if you can't (bool)

    Version:
    Arthur 10/03 v1
    """
    listx=[target[0]-1,target[0],target[0]+1]
    listy=[target[1]-1,target[1],target[1]+1]
    if sheep[0] not in listx :
        answer=0
    elif sheep[1]not in listy :
        answer=0
    else:
        answer=1
    return answer

