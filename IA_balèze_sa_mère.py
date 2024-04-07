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
    implémentation : Remacle Thomas (v1 24/02/24)"""
    entity1_coordinates=[entity1_coordinates[0],entity1_coordinates[1]]
    entity2_coordinates=[entity2_coordinates[0],entity2_coordinates[1]]  #Transform the coordinates
    x_value=abs(entity2_coordinates[0]-entity1_coordinates[0]) #Calculate the distance between the coordinates_x
    y_value=abs(entity2_coordinates[1]-entity1_coordinates[1]) #Calculate the distance between the coordinates_y
    return_value=x_value+y_value  #Total distance 
    return return_value

def look_for_grass(sheep):
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
    implémentation : Remacle Thomas (v1 24/02/24)
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
    
    orders += ' '+str(sheep[0])+'-'+str(sheep[1])+':*'
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

def create_sheepxseed(id):
    """return a dico with the first sheep with the seed goal
    
    parameters
    ----------
    id : the player id 1 or 2 (int)
    
    return
    ------
    dico : the dico with the first sheep and the seed he reach to capture"""
    dico = {}
    dico['sheep_1']='coordinates' : players['player_'+str(id)][sheeps]



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
    implementation : Heynen Scott-Socrate (v1 )
    
    """
    turn = map['nbr_of_turns']
    orders = 'sheep'

    if turn == 0:
        
    
    if turn >= 15:
        seed search
    
    
    
    
    
    return orders





wrong=[]

def move_IA(location,target,wrong):
    '''raproche le mouton de la cible par un chemin optimal
    parametre:
    
    location=l'endroit ou ce trouve le mouton [xx-xx](liste)
    target=l'endroit ou le mouton veut arriver [xx-xx](liste)
    wrong=les cases qui sont obstruées (liste)
    
    return:
    order=l'ordre a executer [xx-xx:@yy-yy] (liste)
  
    '''
    
    if location[0]>target[0] and location[1]>target[1]:
        
        move=(location[0]-1,location[1]-1)
    
        if what_in_the_box(move,'rock') or what_in_the_box(move,'sheep'):
            wrong.append(move)
        else:
            return move

        
    elif location[0]<target[0] and location[1]>target[1]:
        
        move=(location[0]+1,location[1]-1)
    
        if what_in_the_box(move,'rock') or what_in_the_box(move,'sheep'):
            wrong.append(move)     
        else:
            return move


    elif location[0]>target[0] and location[1]<target[1]:
       
        move=(location[0]-1,location[1]+1)
       
        if what_in_the_box(move,'rock') or what_in_the_box(move,'sheep'):
           wrong.append(move)
        else:
            return move

    
    elif location[0]>target[0] and location[1]<target[1]:
        
        move=(location[0]+1,location[1]+1)
    
        if what_in_the_box(move,'rock') or what_in_the_box(move,'sheep'):
            wrong.append(move)      
        else:
            return move


    elif location[0]==target[0] and location[1]>target[1]:
       
        move=(location[0],location[1]-1)
        
        if what_in_the_box(move,'rock') or what_in_the_box(move,'sheep'):
            wrong.append(move)
        else:
            return move
        

    elif location[0]==target[0] and location[1]<target[1]:

        move=(location[0],location[1]+1)
    
        if what_in_the_box(move,'rock') or what_in_the_box(move,'sheep'):
            wrong.append(move)           
        else:
            return move

    
    elif location[0]<target[0] and location[1]==target[1]:
       
        move=(location[0]+1,location[1])
    
        if what_in_the_box(move,'rock') or what_in_the_box(move,'sheep'):
            wrong.append(move)
        else:
            return move

    
    elif location[0]>target[0] and location[1]==target[1]:
       
        move=(location[0]-1,location[1])
    
        if what_in_the_box(move,'rock') or what_in_the_box(move,'sheep'):
            wrong.append(move)
        else:
            return move
        
