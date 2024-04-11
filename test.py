map = {'rocks': {'rock_1': [11, 22],
                 'rock_2': [35, 14]},
       'spawn': {'spawn_1': [18, 29],
                 'spawn_2': [25, 12]},
       'map_size': [60, 40],
       'seed': {'seed_1': [47, 18],
                'seed_2': [22, 37]},
       'nbr_of_turns': 100}

players = {'player_1': {'sheeps': {(22, 22): [3,False],
                                    (45, 23): [3,False]},  # vérif
                         'nbr_of_grass': 40},

            'player_2': {'sheeps': {(21, 22): [3,False],
                                    (18, 25): [3,False]},
                         'nbr_of_grass': 0}}

grass= {'player_1':{(21,21):3},
'player_2':{(23,23):2,(24,24):2,(25,25):2,(21,21):3}}

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
    specification: Remacle Thomas (v1 24/02/24)
    implémentation : Remacle Thomas (v1 24/02/24)
                     Remacle Thomas (v1.1 24/02/24)"""
    return_value=0
    entity1_coordinates=[entity1_coordinates[0],entity1_coordinates[1]]
    entity2_coordinates=[entity2_coordinates[0],entity2_coordinates[1]]  #Transform the coordinates
    x_value=abs(entity2_coordinates[0]-entity1_coordinates[0]) #Calculate the distance between the coordinates_x
    y_value=abs(entity2_coordinates[1]-entity1_coordinates[1]) #Calculate the distance between the coordinates_y
    if x_value>y_value:
        return_value=x_value #Total distance 
    else:
        return_value=y_value    #Take the highest value to measure the distance between entity1_coordinates and entity2_coordinates
    return return_value



def graze(sheep):
    """return the graze command 
    
    parameters
    ----------
    sheep : the (x,y) coordinates of the sheep who graze (tuples)

    returns
    -------
    orders: the order to add to the order list (str)

    notes
    -----
    this function don't check if the order is valide
    
    version
    -------
    specification : Heynen Scott-Socrate (v2 28/03/24)
    implementation : Heynen Scott-Socrate (v1 29/03/24)"""
    grass_list=[]
    sheep=[sheep[0],sheep[1]] # sheep
    x_sheep = sheep[0] # coordinate of the sheep in x
    x_sheep = sheep[1] # coordinate of the sheep in y
    old_total = 0
    total = 0
    new = 0

    # check with sheep is playing
    for sheep_1 in players['player_1']['sheeps'] : # Player 1
        sheep_1=[sheep[0],sheep[1]]
        if sheep_1  == sheep:
           sheep_player = 1

    for sheep_2 in players['player_2']['sheeps'] : # Player 2
        sheep_2=[sheep[0],sheep[1]]
        if sheep_2 == sheep:
           sheep_player = 2

    # Create a list with all grass
    if sheep_player == 1:
        for i_grass in grass["player_1"]:
            grass_list.append(i_grass)
    else:
        for i_grass in grass["player_2"]:
            grass_list.append(i_grass)
    # Check the grass witch one is the better
    for i_grass in grass_list:
        if new == 0: # Check if the function work for the first time
            old_distance = i_grass
            new = 1
            for u_grass in grass_list: # Compute how mutch grass there is around this grass. 
                    compute_grass = get_distance(i_grass,u_grass)
                    if compute_grass <= 2: # If it is around the grass
                        old_total += 1
        else:
            compute_new = get_distance(sheep,i_grass)
            compute_old = get_distance(sheep,old_distance)
            if compute_new==0 or compute_old == 0: # if sheep is on the grass
                graze == 1
            elif compute_new < compute_old: # Check if the new valor is better than the old one
                old_distance = i_grass
            elif compute_new == compute_old: # If the valor is the same
                for u_grass in grass_list: # Compute how mutch grass there is around this grass. 
                    compute_grass = get_distance(i_grass,u_grass)
                    if compute_grass <= 2: # If it is around the grass
                        total += 1
                    if total > old_total: # if the total of grass is better than the old one ?
                        old_total = total
                        old_distance = i_grass

    print(old_distance)
    #orders += ' '+str(sheep[0])+'-'+str(sheep[1])+':*'
    #return orders

graze((22, 22))