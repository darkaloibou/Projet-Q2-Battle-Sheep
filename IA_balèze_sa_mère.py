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

def look_for_seed(sheep):
    """return the best seed to go (2 seeds strategie)
    
    parameters
    ----------
    sheep: the sheep coordinates that will go to the choosen seed
    
    return
    ------
    the coordinates (x,y) of the seed to go (tuples)

    version
    -------
    specification : Heynen Scott-Socrate (v2 28/03/24)
    implémentation : Remacle Thomas (v1 02/04/24)
    """
    seeds_dic =map['seed'].copy()  #Copy the dictionnary of the seeds
    x_map=str(map['map_size'][0])
    x_map=int(x_map[0])
    y_map=str(map['map_size'][1])
    y_map=int(y_map[0])
    minus=(x_map+y_map)/2   #Calculate the minus, the minus is the tolarance of distance when you trying to find the seeds 
    minus=math.floor(minus)
    return_coordinate=(0,0)
    min_distance=100000
    sheep=[sheep[0],sheep[1]]
    seeds_list=[]
    other_seed_list=[]
    for seeds in seeds_dic:
        distance=get_distance(sheep,seeds_dic[seeds])
        if min_distance>distance:
            min_distance=distance
            return_coordinate=seeds_dic[seeds]
            seeds_list=[]
            other_seed_list=[]
            seeds_list.append(seeds_dic[seeds])
            other_seed_list.append(seeds)        # This loop finds the seed closest to the sheep
    min_distance=get_distance(sheep,return_coordinate)
    del seeds_dic[other_seed_list[0]]  #Delete the found seed in the seeds_dic dictionnary to avoid finding it again
    for seeds in seeds_dic:
        distance=get_distance(sheep,seeds_dic[seeds])
        if min_distance>=distance-minus:
            seeds_list.append(seeds_dic[seeds])
            other_seed_list.append(seeds)   # This loop finds the seeds closer enough, the notion of close enough is derterminate with the minus variable
    other_seed_list=other_seed_list[1:]
    for seed in other_seed_list:
        del seeds_dic[seed]    #Delete the found seed in the seeds_dic dictionnary to avoid finding it again
    if len(seeds_list)<2:
        return return_coordinate   #If there are only one seed
    else:
        min_distance=[]
        for seeds in seeds_list:
            seed_min_distance=[]
            for compare_seeds in map['seed']:
                distance=get_distance(seeds,map['seed'][compare_seeds])
                if not distance==0:
                    seed_min_distance.append(distance)
            min_distance.append(min(seed_min_distance))    #Find the nearest seed from all the seed previously chose
        seed_min=min(min_distance)
        grass_coordinate=[]
        count=0                                  
        for number in min_distance:
            if number==seed_min:
                grass_coordinate.append(seeds_list[count]) #Take the nearests seed
            count+=1
        min_distance=1000000
        return_coordinate=(0,0)
        for final_seed in grass_coordinate:
            distance=get_distance(sheep,final_seed)  
            if min_distance>distance:
                min_distance=distance
                return_coordinate=final_seed   # Decide the seed of the sheep will
        return return_coordinate
def look_for_seed_alternative(sheep):
    """return the best seed to go (2 seeds strategie)
    
    parameters
    ----------
    sheep: the sheep coordinates that will go to the choosen seed
    
    return
    ------
    the coordinates (x,y) of the seed to go (tuples)

    version
    -------
    specification : Heynen Scott-Socrate (v2 28/03/24)
    implémentation : Remacle Thomas (v1 02/04/24)
    """
    seeds_dic =map['seed'].copy()  #Copy the dictionnary of the seeds
    x_map=str(map['map_size'][0])
    x_map=int(x_map[0])
    y_map=str(map['map_size'][1])
    y_map=int(y_map[0])
    minus=(x_map+y_map)/2   #Calculate the minus, the minus is the tolarance of distance when you trying to find the seeds 
    range_map=math.floor(minus)
    return_coordinate=(0,0)
    min_distance=100000
    sheep=[sheep[0],sheep[1]]
    seeds_list=[]
    other_seed_list=[]
    for seeds in seeds_dic:
        distance=get_distance(sheep,seeds_dic[seeds])
        if min_distance>distance:
            min_distance=distance
            return_coordinate=seeds_dic[seeds]
            seeds_list=[]
            other_seed_list=[]
            seeds_list.append(seeds_dic[seeds])
            other_seed_list.append(seeds)        # This loop finds the seed closest to the sheep
    min_distance=1000000
    del seeds_dic[other_seed_list[0]]  #Delete the found seed in the seeds_dic dictionnary to avoid finding it again
    for seeds in seeds_dic:
        distance=get_distance(sheep,seeds_dic[seeds])
        if min_distance>distance:
            min_distance=distance
            return_coordinate=seeds_dic[seeds]
            seed_value=seeds_dic[seeds]
            seed_name=seeds 
    seeds_list.append(seed_value)
    other_seed_list.append(seed_name) 
    del seeds_dic[other_seed_list[1]]
    xy_list=[]
    for x_value in range (range_map+1):
        if not x_value==0:
            x_neg_append=-x_value
            xy_list.append(x_value)
            xy_list.append(x_neg_append)
        else:
            xy_list.append(x_value)
    number_of_seeds={}
    for seed in other_seed_list:
        count=0
        for x_values in (xy_list):
            for y_values in (xy_list):
                coordinate=[map['seed'][seed][0]+x_values,map['seed'][seed][1]+y_values]
                if not coordinate==map['seed'][seed]:
                    for m_seeds in map['seed']:
                        if coordinate==map['seed'][m_seeds]:
                            count+=1
        seeds_coordinates=map['seed'][seed]
        seeds_coordinates=(seeds_coordinates[0],seeds_coordinates[1])
        number_of_seeds[seeds_coordinates]=count
    if number_of_seeds[(seeds_list[0][0],seeds_list[0][1])]>=number_of_seeds[(seeds_list[1][0],seeds_list[1][1])]:
        return_coordinate=(seeds_list[0][0],seeds_list[0][1])
    else:
        return_coordinate=(seeds_list[1][0],seeds_list[1][1])
                            
    print (number_of_seeds)
    return return_coordinate            
    
def find_path():
    """"""
    if target[0] > sheep[0] and target[1] < sheep[1]:
    if target[0] < sheep[0] and target[1] > sheep[1]:
    if target[0] > sheep[0] and target[1] < sheep[1]:
    if target[0] < sheep[0] and target[1] > sheep[1]:

    if target[0] > sheep[0]: #Ennemi on the right
    if target[0] < sheep[0]: #Ennemi on the left
    if target[1] > sheep[1]: #Ennemi on the top
    if target[1] < sheep[1]: #Ennemi on the buttom
    
def attack(sheep1,sheep2):
    """return the attack command 
    
    parameters
    ----------
    sheep1 : the (x,y) coordinates of the attacker sheep (tuples)
    sheep2 : the (x,y) coordinates of the sheep that is attacked (tuples)
    
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
    
    orders = ' '+str(sheep1[0])+'-'+str(sheep1[1])+':x'+str(sheep2[0])+'-'+str(sheep2[1])
    return orders
def search_sheep (sheep,distance):
    """return the sheeps coordinates near a sheep
    parameters
    ----------
    sheep : the (x,y) coordinates of the sheep to look for what to do (tuples)
    distance: the distance of the search (int)
    returns
    -------
    sheeps_coordinates: A list of the coordinate around the sheep

    version
    -------
    specification : Remacle Thomas (v1 14/04/24)
    """
    xy=[0]
    player_team_sheep_1="player_2"
    for player_sheep in players['player_1']['sheeps']:
        if sheep==player_sheep:
            player_team_sheep_1="player_1"
    for i in range(distance+1):
        if i!=0:
            xy.append(i)
            i=-i
            xy.append(i)
    sheeps_coordinates=[]
    for minus in xy:
        for more in xy:
            if not (minus==0 and more==0):
                search_coordinate=[sheep[0]+minus,sheep[1]+more]
                if what_in_the_box(search_coordinate,'sheep'):
                    player_team_sheep_2="player_2"
                    search_coordinate=(search_coordinate[0],search_coordinate[1])
                    for player_sheep in players['player_1']['sheeps']:
                        if search_coordinate==player_sheep:
                            player_team_sheep_2="player_1"
                    if player_team_sheep_1!=player_team_sheep_2:
                        sheeps_coordinates.append(search_coordinate)
    return sheeps_coordinates
def search_grass (sheep,distance,owner_grass='e'):
    """return the grass coordinates near a sheep
    parameters
    ----------
    sheep : the (x,y) coordinates of the sheep to look for what to do (tuples)
    distance: the distance of the search (int)
    returns
    -------
    grass_coordinates: A list of the coordinate around the sheep

    version
    -------
    specification : Remacle Thomas (v1 14/04/24)
    """
    xy=[0]
    player_team_sheep_1="player_2"
    for player_sheep in players['player_1']['sheeps']:
        if sheep==player_sheep:
            player_team_sheep_1="player_1"
    for i in range(distance+1):
        if i!=0:
            xy.append(i)
            i=-i
            xy.append(i)
    sheeps_coordinates=[]
    for minus in xy:
        for more in xy:
            search_coordinate=[sheep[0]+minus,sheep[1]+more]
            if what_in_the_box(search_coordinate,'grass'):
                player_grass_team="player_2"
                search_coordinate=(search_coordinate[0],search_coordinate[1])
                for player_grass in grass['player_1']:
                    if search_coordinate==player_grass:
                        player_grass_team="player_1"
                if owner_grass=='a':
                    if player_team_sheep_1==player_grass_team:
                        sheeps_coordinates.append(search_coordinate)
                else:
                    if player_team_sheep_1!=player_grass_team:
                        sheeps_coordinates.append(search_coordinate)
    return sheeps_coordinates
def search_seeds (sheep,distance):
    """return the grass coordinates near a sheep
    parameters
    ----------
    sheep : the (x,y) coordinates of the sheep to look for what to do (tuples)
    distance: the distance of the search (int)
    returns
    -------
    grass_coordinates: A list of the coordinate around the sheep

    version
    -------
    specification : Remacle Thomas (v1 14/04/24)
    """
    xy=[0]
    for i in range(distance+1):
        if i!=0:
            xy.append(i)
            i=-i
            xy.append(i)
    sheeps_coordinates=[]
    for minus in xy:
        for more in xy:
            if not (minus==0 and more==0):
                search_coordinate=[sheep[0]+minus,sheep[1]+more]
                if_value=False
                for seed in map['seed']:
                    if search_coordinate==map['seed'][seed]:
                        if_value=True
                if if_value:
                    search_coordinate=(search_coordinate[0],search_coordinate[1])
                    sheeps_coordinates.append(search_coordinate)
    return sheeps_coordinates
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
                if compute_hp_new > -1:
                    new_distance = get_distance(ennemi_sheep,sheep)
                    old_distance = get_distance(ennemi_sheep,old_pos)
                    if new_distance == 1:
                        return attack(sheep, ennemi_sheep)
                    elif new_distance <= old_distance:
                        if compute_hp_new > compute_hp_new:
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
        move = find_path(sheep, old_pos)
        return move_sheep(sheep, move)
        
    #orders += ' '+str(sheep[0])+'-'+str(sheep[1])+':*'
    #return orders


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
    if graze == 1:
        orders = ' '+str(sheep[0])+'-'+str(sheep[1])+':*'
    else:
        aim = move_ia(sheep,old_distance)
        orders = ' '+str(old_coordinates[0])+'-'+str(old_coordinates[1])+':@'+str(aim[0])+'-'+str(aim[1])
    return orders
def move_sheep(old_coordinates, new_coordinates):
    """return the move command 
    
    parameters
    ----------
    old_coordinates : the (x,y) coordinates of the sheep before the shift (tuples)
    new_coordinates : the (x,y) coordinates of the sheep after the shift (tuples)
    
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

    orders = ' '+str(old_coordinates[0])+'-'+str(old_coordinates[1])+':@'+str(new_coordinates[0])+'-'+str(new_coordinates[1])
    return orders

def create_sheepxseed(sheep,seed):
    """return a dico with the first sheep with the seed goal
    
    parameters
    ----------
    sheep : the (x,y) coordinates of the sheep to add to the list (tuples)    
    seed : the (x,y) coordinates of the seed to link to the sheep (list)
    
    return
    ------
    seed_targets : the dico with the sheep and the seed he reach to capture
    
    version
    -------
    specification : Heynen Scott-Socrate (v2 28/03/24)"""

    targets[sheep] = [seed,True]

#exemple du dico des seed
#------------------------------------------------

seed_targets = {(x,y) : {[x,y],True], #premier x,y c'est mouton et les 2eme c'est la graine qu'il vise. le True c'est pour dire que sa graine à déjà été calculée
                (x,y) : {[x,y],False]}


sheep_targets = {(x,y) : {[x,y],False]}
#fonction de l'IA
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# main function - if necessary, other parameters can be used
def get_AI_orders(game, player_id):
    """Return orders of AI.
    
    Parameters
    ----------
    game: game data structure (dict)
    player_id: player id of AI (int)

    Returns
    -------
    orders: orders of AI (str)

    version
    -------
    specification : Heynen Scott-Socrate (v2 29/03/24)
    implementation : Heynen Scott-Socrate (v2 15/04/24)
    
    """
    turn = map['nbr_of_turns']
    orders = 'sheep'
    
    max_map = max(map['map_size'])
    search_turns = int (max_map - (max_map / 2))  # calcul the number of turn to only search seed (depend of the map size)

    for sheep in players['player_'+str(player_id)]['sheeps']:
        free_to_action = True    
        
        if turn <= search_turns or players['player_'+str(player_id)]['nbr_of_grass'] < 30: #for the seed search only turns
            
            target_seed = look_for_seed(sheep)
            
            if player_id == 1:  #look if there is a sheep in a 1 box distance and attack (player 1)
                for ennemi_sheep in players["player_2"]["sheeps"]:
                    distance = get_distance(ennemi_sheep,sheep)
                    if distance == 1:
                        orders += attack(sheep,ennemi_sheep)
                        free_to_action = False
                
            if player_id == 2:  #look if there is a sheep in a 1 box distance and attack (player 2)
                for ennemi_sheep in players["player_2"]["sheeps"]:
                    distance = get_distance(ennemi_sheep,sheep)
                    if distance == 1:
                        orders += attack(sheep,ennemi_sheep)    
                        free_to_action = False
                
            if free_to_action:
                orders += str(move_sheep(sheep,move_ia(sheep,target_seed))) #move the sheep to the seed     #verif si move_ia return bien seulement coordonnées
                
            """if tuple(target) == sheep: #reset the sheep when he captured the seed      #verif si le tuple() existe!!!! 
                seed_targets[sheep][1]=False #transforme en False"""
                
        if turn > search_turns:
            minimum_distance = 999
                
            for sheep_role in players['player_'+str(player_id)]['sheeps']: # look for the role of the sheep (0 = defend)
                distance = get_distance(map['spawn']['spawn_'+str(player_id)],sheep_role)
                if distance < minimum_distance:
                    minimum_distance = distance # down to the nearest sheep
                    defend_sheep = sheep_role
                        
                        
            if defend_sheep == sheep:      
                orders += str(choose_what_to_do(sheep,0))
                free_to_action = False
            else :
                orders += str(choose_what_to_do(sheep,1))
                free_to_action = False
    
    return orders


def choose_what_to_do(sheep):
    """return the action to do 
    
    parameters
    ----------
    sheep : the (x,y) coordinates of the sheep to look for what to do (tuples)

    returns
    -------
    order : the thing to do for the sheep already in a correct form for the game (str) 
    
    version
    -------
    specification : Heynen Scott-Socrate (v3 15/04/24)
    """

def move_ia(location,target):
    """search the best path to the target
    parameter:
   
    location = curent location of the sheep (x,y) (tuple)
    target = the final destination the sheep want to go (x,y) (tuple)
    
    return:

    move = the coordinate of the case where the sheep need to move [x,y] (list)
    
    spécification 28/03 Arthur Yeranux
    v1 06/04 Arthur Yernaux
    v2 11/04 Arthur Yernaux"""
    location=[location[0],location[1]]
    target=[target[0],target[1]]
    wrong=[]
    xy=[0,1,-1]
    for minus in xy:
        for more in xy:
            if not (minus==0 and more==0):
                if what_in_the_box([location[0]+minus,location[1]+more],'sheep') or what_in_the_box([location[0]+minus,location[1]+more],'rock'):
                    wrong.append([location[0]+minus,location[1]+more])
    if what_in_the_box([location[0]+1,location[1]],'sheep') or what_in_the_box([location[0]+1,location[1]],'rock'):
        wrong.append([location[0]+1,location[1]])
    move = location
    
    if location[0]>target[0] and location[1]>target[1]:
        move=[location[0]-1,location[1]-1]
        

    elif location[0]<target[0] and location[1]>target[1]:
        move=[location[0]+1,location[1]-1]
    

    elif location[0]>target[0] and location[1]<target[1]:
        move=[location[0]-1,location[1]+1]
       
    
    elif location[0]<target[0] and location[1]<target[1]:
        move=[location[0]+1,location[1]+1]
    

    elif location[0]==target[0] and location[1]>target[1]:
        move=[location[0],location[1]-1]
        

    elif location[0]==target[0] and location[1]<target[1]:
        move=[location[0],location[1]+1]
    
    
    elif location[0]<target[0] and location[1]==target[1]:
        move=[location[0]+1,location[1]]
    

    elif location[0]>target[0] and location[1]==target[1]:
        move=[location[0]-1,location[1]]
    
    if move not in wrong:
        return (move[0],move[1])
    
    else:
       
        difx=location[0]-target[0]
        dify=location[1]-target[1]
        
        if abs(difx)>=abs(dify):
           
            if difx>0:
                for i in [1,0,-1]:
                    move=[location[0]-1,location[1]+i]
                    if move not in wrong:
                        return (move[0],move[1])
                if dify>0:
                    move=[location[0],location[1]-1]
                    return (move[0],move[1])
                else:
                    move=[location[0],location[1]+1]
                    return (move[0],move[1])
               

            else:
                
                for i in [1,0,-1]:
                    move=[location[0]+1,location[1]+i]
                    if move not in wrong:
                        return (move[0],move[1])
                if dify>0:
                    move=[location[0],location[1]-1]
                    return (move[0],move[1])
                else:
                    move=[location[0],location[1]+1]
                    return (move[0],move[1])


        if abs(difx)<abs(dify):
            
            if dify>0:
                                
                for i in [1,0,-1]:
                    move=[location[0]+i,location[1]-1]
                    if move not in wrong:
                        return (move[0],move[1])
                if difx>0:
                    move=[location[0]-1,location[1]]
                    return (move[0],move[1])
                else:
                    move=[location[0]+1,location[1]]
                    return (move[0],move[1])


            else:
                for i in [1,0,-1]:
                    move=[location[0]+i,location[1]+1]
                    if move not in wrong:
                        return (move[0],move[1])
                if difx>0:
                    move=[location[0]-1,location[1]]
                    return (move[0],move[1])
                else:
                    move=[location[0]+1,location[1]]
                    return (move[0],move[1])
