def look_for_grass(sheep):
    """return the best seed to go (2 seeds strategie)
    
    parameters
    ----------
    sheep: the sheep coordinates that will go to the choosen seed
    
    return
    ------
    the coordinates [x,y] of the seed to go (tuples)

    version
    -------
    specification : Heynen Scott-Socrate (v2 28/03/24)  
    """
    
    for seeds in map['seed']:
        x=2 #à terminer
    
    
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
    
    """

    orders = ''
    
    
    
    
    
    return orders
