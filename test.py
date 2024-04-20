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
                                    (18, 25): [2,False],
                                    (19, 25): [1,False],
                                    (18, 24): [2,False],
                                    (23, 23): [2,False]},
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



def search_attack(sheep):
    """return the attack command 
    
    parameters
    ----------
    sheep : the (x,y) coordinates of the sheep (tuples)

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
    sheep=[sheep[0],sheep[1]] # sheep
    new_distance = 0
    old_distance = 0
    # check with sheep is playing
    for sheep_1 in players['player_1']['sheeps'] : # Player 1
        sheep_1_list=[sheep_1[0],sheep_1[1]]
        if sheep_1_list  == sheep:
           sheep_player = 1
           sheep_1_hp = players["player_1"]["sheeps"][sheep_1][0]

    for sheep_2 in players['player_2']['sheeps'] : # Player 2
        sheep_2_list =[sheep_2[0],sheep_2[1]]
        if sheep_2_list == sheep:
           sheep_player = 2
           sheep_1_hp = players["player_2"]["sheeps"][sheep_2][0]
    new = 0
    if sheep_player == 1 : # fonction of the player 1
        for ennemi_sheep in players["player_2"]["sheeps"]:
            print(ennemi_sheep)
            ennemi_sheep_list =[ennemi_sheep[0],ennemi_sheep[1]] # Set a list of sheep
            if new == 0 :
                old_pos = ennemi_sheep
                new = 1
                sheep_old_hp = players["player_2"]["sheeps"][ennemi_sheep][0]
            else:
                # check the difference of hp of both of them
                sheep_new_hp = players["player_2"]["sheeps"][ennemi_sheep][0]
                compute_hp_new = sheep_1_hp - sheep_new_hp
                compute_hp_old = sheep_1_hp - sheep_old_hp
                print(sheep_1_hp,"-", sheep_new_hp, "=", compute_hp_new)
                print(sheep_1_hp, "-", sheep_old_hp, "=", compute_hp_old)
                if compute_hp_new > -1:
                    print("good")
                    new_distance = get_distance(ennemi_sheep,sheep)
                    old_distance = get_distance(ennemi_sheep,old_pos)
                    if new_distance == 1:
                        print("new_distance==1")
                        #return attack(sheep, ennemi_sheep)
                    elif new_distance <= old_distance:
                        print("new_distance <= old_distance")
                        if compute_hp_new > compute_hp_new:
                            print("compute_hp_new > compute_hp_new")
                            old_pos = ennemi_sheep
                    
    else : # PLayer 2
        for ennemi_sheep in players["player_1"]["sheeps"]:
            ennemi_sheep_list=[ennemi_sheep[0],ennemi_sheep[1]] # Set a list of sheep
            if new == 0 :
                old_pos = ennemi_sheep
                new = 1
                sheep_old_hp = players["player_1"]["sheeps"][ennemi_sheep][0]
            else:
                # check the difference of hp of both of them
                sheep_new_hp = players["player_1"]["sheeps"][ennemi_sheep][0]
                compute_hp_new = sheep_1_hp - sheep_new_hp
                compute_hp_old = sheep_1_hp - sheep_old_hp
                if compute_hp_new > -1:
                    new_distance = get_distance(ennemi_sheep,sheep)
                    old_distance = get_distance(ennemi_sheep,old_pos)
                    if new_distance == 1:
                        return attack(sheep, ennemi_sheep)
                    elif new_distance <= old_distance:
                        if compute_hp_new > compute_hp_new:
                            old_pos = ennemi_sheep
    if old_distance > 2:
        return #false
    else:
        print(old_pos)
        #move = find_path(sheep, old_pos)
        #return move_sheep(sheep, move)

print(search_attack((22, 22)))
