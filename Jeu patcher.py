import blessed, time
term = blessed.Terminal()
print(term.clear)
map = {'rocks': {'rock_1': [11, 22],
                 'rock_2': [35, 14]},
       'spawn': {'spawn_1': [18, 29],
                 'spawn_2': [26, 12]},
       'map_size': [60, 40],
       'seed': {'seed_1': [44, 18],
                'seed_2': [22, 37]},
       'nbr_of_turns': 100}

players = {'player_1': {'sheeps': {(18, 29): [3,False],
                                    (45, 23): [3,False]},  # vérif
                         'nbr_of_grass': 400},

            'player_2': {'sheeps': {(26, 12): [3,False],
                                    (18, 25): [3,False]},
                         'nbr_of_grass': 400}}

grass= {'player_1':{(20,16):2,(12,45):3},
'player_2':{(12,2):2}}
print (term.clear)
def show_high_score(Length):
    playerscore_1=str(players['player_1']['nbr_of_grass'])
    playerscore_2=str(players['player_2']['nbr_of_grass'])
    minus=(len(playerscore_1))
    print (term.move_xy(((Length*2)-14)-minus,0)+term.blue+"Player score :"+playerscore_1)
    print (term.move_xy(0,0)+term.red+"Player score :"+playerscore_2)
    print (term.home)
         
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
    réalisation: Arthur (v1 14/03)
    """
    fh=open('./plateau.bsh','r')
    lines=fh.readlines()
    dict={}
    
    for line in lines:
        if line =='map:\n':
            txt=lines[1]
            txt=txt.split()
            dict['map_size']=[txt[0],txt[1]]
        if line =='spawn:\n':
            spawn={}
            txt=lines[3]
            txt=txt.split()
            if txt[0]=="1":
                spawn['spawn_1']=[txt[1],txt[2]]
                txt=lines[4]
                txt=txt.split()
                spawn['spawn_2']=[txt[1],txt[2]]
            else:
                spawn['spawn_2']=[txt[1],txt[2]]
                txt=lines[4]
                txt=txt.split()
                spawn['spawn_1']=[txt[1],txt[2]]
            dict['spawn']=spawn
        if line=='seeds:\n':
            i=6
            nb=0
            seed={}
            longueur=len(lines)
            while lines[i]!='rocks:\n':
                nb+=1
                txt=lines[i]
                txt=txt.split()
                seed[('seed_%d')%(nb)]=[txt[0],txt[1]]
                i+=1
            dict['seed']=seed
            rocks={}
            nb=1
            i+=1
            while i<longueur:
                
                txt=lines[i]
                txt=txt.split()
                rocks[('rock_%d')%(nb)]=[txt[0],txt[1]]
                nb+=1
                i+=1
            dict['rocks']=rocks

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
        manage_emoji(map["rocks"][rock],"🪨")

    manage_emoji(map["spawn"]['spawn_1'],"​🐑") # Voir comment display les spawn de moutons
    manage_emoji(map["spawn"]['spawn_2'],"​🐐")
    for seed in map["seed"] :
        manage_emoji(map["seed"][seed],"​🌱")
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
    count=0
    if grp==1:
        spawn_point=map['spawn']['spawn_1']
        spawn_point=(spawn_point[0],spawn_point[1])
        for sheep in players['player_1']['sheeps']:
            count+=1
            if spawn_point == sheep: #attention x,y bouge? #look if the spawn is free to spawn a sheep
                return count
        if (count*30)>players['player_1']['nbr_of_grass']:
            return count
        else:
            players['player_1']['sheeps'][spawn_point]=3
            manage_emoji(spawn_point,"🐑")
    else:
        spawn_point=map['spawn']['spawn_2']
        spawn_point=(spawn_point[0],spawn_point[1])
        for sheep in players['player_2']['sheeps']:
            count+=1
            if spawn_point== sheep: #attention x,y bouge? #look if the spawn is free to spawn a sheep
                return count
        if (count*30)>players['player_2']['nbr_of_grass']:
            return count
        else:
            players['player_2']['sheeps'][spawn_point]=3
            manage_emoji(spawn_point,"🐐")

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
    
def grass_propagation (mature_grass,life_state):
    """ The function propage the grass if it's needed 
    parameters
    -----------------------
    mature_grass: A list of grass need to be propaged (list)
    life_state: If the grass is possed by player_1 or player_2 (str)
    version
    ----------
    specification: Remacle Thomas (v1 14/03/24)
    implementation: Remacle Thomas (v1 14/03/24)"""
    
    for herbs in mature_grass:
            coordinate=herbs
            numbers=[-1,1]
            for x_term in numbers:
                if not what_in_the_box ([(coordinate[0]+x_term),coordinate[1]],'void') and not what_in_the_box([(coordinate[0]+x_term),coordinate[1]],'rock') and not what_in_the_box([(coordinate[0]+x_term),coordinate[1]],'grass'):
                    grass[life_state][(coordinate[0]+x_term),coordinate[1]]=1
                    if not what_in_the_box ([(coordinate[0]+x_term),coordinate[1]],'sheep'):
                        manage_emoji([(coordinate[0]+x_term),coordinate[1]],"🌾")
            for y_term in numbers:
                if not what_in_the_box ([(coordinate[0]),(coordinate[1]+y_term)],'void') and not what_in_the_box([(coordinate[0]),(coordinate[1]+y_term)],'rock') and not what_in_the_box([(coordinate[0]),(coordinate[1]+y_term)],'grass'):
                    grass[life_state][(coordinate[0]),(coordinate[1]+y_term)]=1
                    if not what_in_the_box([coordinate[0],(coordinate[1]+y_term)],'sheep'):
                        manage_emoji([coordinate[0],(coordinate[1]+y_term)],"🌾")
def update_grass ():
    """Grow grass and plant grass on the all 4 box surroundings 
    parameters
    ----------
    version
    -------
    specification: Heynen Scott-Socrate (v1 23/02/24)
    implementation:Heynen Scott-Socrate (v1 23/02/24)
                   Remacle Thomas (v2 14/03/24)
                   Remacle Thomas (v2.1 14/03/24)
    """ #si la grass est à 10
    mature_grass_1=[]
    mature_grass_2=[]
    for herbs in grass['player_1']:  #ATTENTION A BIEN CREER UN DICO GRASS DANS LA MAIN FONCTION
        grass['player_1'][herbs] += 1
        if grass['player_1'][herbs]== 10:
            mature_grass_1.append(herbs)
    for herbs in grass['player_2']:  #ATTENTION A BIEN CREER UN DICO GRASS DANS LA MAIN FONCTION
        grass['player_2'][herbs] += 1
        if grass['player_2'][herbs] == 10:
            mature_grass_2.append(herbs)
    grass_propagation(mature_grass_1,'player_1')
    grass_propagation(mature_grass_2,'player_2')
        
    
def manage_emoji (emoji_coordinates,emoji='  '): 
    """change the emoji we need to change
    parameters
    ----------
    emoji_coordinates: coordinate in (x,y) of the emoji wanted to be created (tuples or list depend if the emoji is element of the map or a sheep/grass)
    emoji: the emoji wanted to be spawn, by default recreate the case without emoji on the box (str)
    version
    -------
    specification: Remacle Thomas (v1.1 25/02/24)
    implementaion: Remacle Thomas (v1 4/03/24)
                   Remacle Thomas (v1.1 4/03/24)
    """
    ""
    emoji_coordinates=(int(emoji_coordinates[0]),int(emoji_coordinates[1]))
    emoji_d=["🐑","🐐", "🌾"]
    if emoji in emoji_d[0]:
        print(term.move_xy(emoji_coordinates[0]*2,emoji_coordinates[1])+term.on_red+emoji)
    elif emoji in emoji_d [1]:
        print(term.move_xy(emoji_coordinates[0]*2,emoji_coordinates[1])+term.on_blue+emoji)
    elif emoji in emoji_d[2]:
        for grass_i in grass['player_1']:
            if grass_i==emoji_coordinates:
                    print(term.move_xy(emoji_coordinates[0]*2,emoji_coordinates[1])+term.on_red+emoji)
        for grass_i in grass['player_2']:
            if grass_i==emoji_coordinates:
                    print(term.move_xy(emoji_coordinates[0]*2,emoji_coordinates[1])+term.on_blue+emoji)
    else:
        coordinate=emoji_coordinates[0]/2
        if emoji_coordinates[1]%2!=0:
            if (coordinate)%2==0:
                print (term.move_xy(emoji_coordinates[0]*2,emoji_coordinates[1])+term.peru_on_seagreen+emoji)
            else:
                print (term.move_xy(emoji_coordinates[0]*2,emoji_coordinates[1])+term.on_darkolivegreen+emoji)
        else:
            if (coordinate)%2==0:
                print (term.move_xy(emoji_coordinates[0]*2,emoji_coordinates[1])+term.on_darkolivegreen+emoji)
            else:
                print (term.move_xy(emoji_coordinates[0]*2,emoji_coordinates[1])+term.peru_on_seagreen+emoji)

    
def attack_sheep(attack_coordinates,enemy_coordinates): #Il faut ajouter les coordonées du mouton qui attaque
    """Attack a sheep if he is near enough to be attacked
    parameters
    ----------
    attack_coordinates : players sheep who attack (0 for player 1, 1 for player 2) (bool)     
    enemy_coordinates: position in x and y where the sheep attacked is (tuples)
    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
     specification: Aloïs Baurant (v2 13/03/24)
    """
    enemy_coordinates=((int(enemy_coordinates[0]),(int(enemy_coordinates[1]))))
    attack_coordinates=((int(attack_coordinates[0]),(int(attack_coordinates[1]))))
    if check_sheep_team(enemy_coordinates)==1:
        player='player_1'
        attack_player='player_2'
    else:
        player='player_2'
        attack_player='player_1'
    players[attack_player]['sheeps'][attack_coordinates][1]=True
    if attack_coordinates[0] < enemy_coordinates[0] and attack_coordinates[1] < enemy_coordinates[1]: #    if old_x < new_1 and old_y < new_1
        if players[player]['sheeps'][enemy_coordinates][0]>= 2 :# vérifie la vie du mouton si elle ne tombe pas a 0 (= mort)
            players[player]['sheeps'][enemy_coordinates][0] -= 1 # enlève une vie
            move_coordinates = [enemy_coordinates[0],enemy_coordinates[1]] # Crée le nouvelle emplacement
            move_coordinates[0] += 5 # Déplacement de 5 vers la droite
            move_coordinates[1] += 5 # déplacement de 5 vers le haut  
            move_coordinates = (move_coordinates[0],move_coordinates[1])
            return_coordinate=[enemy_coordinates,move_coordinates]# bouge le mouton
        else : # Supprime le mouton
            del player[player]['sheeps'][enemy_coordinates]
            manage_emoji(enemy_coordinates)
        
    elif attack_coordinates[0] < enemy_coordinates[0] and attack_coordinates[1] > enemy_coordinates[1]: #     if old_x < new_1 and old_y > new_1
        if players[player]['sheeps'][enemy_coordinates][0] >= 2 :# vérifie la vie du mouton si elle ne tombe pas a 0 (= mort)
            players[player]['sheeps'][enemy_coordinates][0]-=1 # enlève une vie
            move_coordinates = [enemy_coordinates[0],enemy_coordinates[1]] # Crée le nouvelle emplacement
            move_coordinates[0] += 5 # Déplacement de 5 vers la droite
            move_coordinates[1] -= 5 # déplacement de 5 vers le bas  
            move_coordinates = (move_coordinates[0],move_coordinates[1])
            return_coordinate=[enemy_coordinates,move_coordinates]# bouge le mouton
        else : # Supprime le mouton
            del player[player]['sheeps'][enemy_coordinates]
            manage_emoji(enemy_coordinates)

    elif attack_coordinates[0] > enemy_coordinates[0] and attack_coordinates[1] < enemy_coordinates[1]: #     if old_x > new_1 and old_y < new_1
        if players[player]['sheeps'][enemy_coordinates][0] >= 2 :# vérifie la vie du mouton si elle ne tombe pas a 0 (= mort)
            players[player]['sheeps'][enemy_coordinates][0] -= 1 # enlève une vie
            move_coordinates = [enemy_coordinates[0],enemy_coordinates[1]] # Crée le nouvelle emplacement
            move_coordinates[0] -= 5 # Déplacement de 5 vers la gauche
            move_coordinates[1] += 5 # déplacement de 5 vers le haut  
            move_coordinates = (move_coordinates[0],move_coordinates[1])
            return_coordinate=[enemy_coordinates,move_coordinates]# bouge le mouton
        else : # Supprime le mouton
            del player[player]['sheeps'][enemy_coordinates]
            manage_emoji(enemy_coordinates)

    elif attack_coordinates[0] > enemy_coordinates[0] and attack_coordinates[1] > enemy_coordinates[1]: #     if old_x > new_1 and old_y > new_1
        if players[player]['sheeps'][enemy_coordinates][0] >= 2 :# vérifie la vie du mouton si elle ne tombe pas a 0 (= mort)
            players[player]['sheeps'][enemy_coordinates][0] -= 1 # enlève une vie
            move_coordinates = [enemy_coordinates[0],enemy_coordinates[1]] # Crée le nouvelle emplacement
            move_coordinates[0] -= 5 # Déplacement de 5 vers la gauche
            move_coordinates[1] -= 5 # déplacement de 5 vers le bas 
            move_coordinates = (move_coordinates[0],move_coordinates[1]) 
            return_coordinate=[enemy_coordinates,move_coordinates]# bouge le mouton
        else : # Supprime le mouton
            del player[player]['sheeps'][enemy_coordinates]
            manage_emoji(enemy_coordinates)

    # attaque en haut; doite, gauche, bas

    elif attack_coordinates[0] > enemy_coordinates[0]: #    if old_x > new_x
        if players[player]['sheeps'][enemy_coordinates][0] >= 2 :# vérifie la vie du mouton si elle ne tombe pas a 0 (= mort)
            players[player]['sheeps'][enemy_coordinates][0] -= 1 # enlève une vie
            move_coordinates = [enemy_coordinates[0],enemy_coordinates[1]]  # Crée le nouvelle emplacement
            move_coordinates[0] -= 5 # Déplacement de 5 vers la gauche
            move_coordinates = (move_coordinates[0],move_coordinates[1])
            return_coordinate=[enemy_coordinates,move_coordinates]# bouge le mouton
        else : # Supprime le mouton
            del player[player]['sheeps'][enemy_coordinates]
            manage_emoji(enemy_coordinates)

    elif attack_coordinates[0] < enemy_coordinates[0]: #     if old_x < new_x
        if players[player]['sheeps'][enemy_coordinates][0] >= 2 :# vérifie la vie du mouton si elle ne tombe pas a 0 (= mort)
            players[player]['sheeps'][enemy_coordinates][0] -= 1 # enlève une vie
            move_coordinates = [enemy_coordinates[0],enemy_coordinates[1]] # Crée le nouvelle emplacement
            move_coordinates[0] += 5 # Déplacement de 5 vers la droite
            move_coordinates = (move_coordinates[0],move_coordinates[1])
            return_coordinate=[enemy_coordinates,move_coordinates]# bouge le mouton
        else : # Supprime le mouton
            del player[player]['sheeps'][enemy_coordinates]
            manage_emoji(enemy_coordinates)

    elif attack_coordinates[1] < enemy_coordinates[1]: #     if old_y > new_y
        if players[player]['sheeps'][enemy_coordinates][0] >= 2 :# vérifie la vie du mouton si elle ne tombe pas a 0 (= mort)
            players[player]['sheeps'][enemy_coordinates][0] -= 1 # enlève une vie
            move_coordinates = [enemy_coordinates[0],enemy_coordinates[1]] # Crée le nouvelle emplacement
            move_coordinates[1] += 5 # déplacement de 5 vers la bas  
            move_coordinates = (move_coordinates[0],move_coordinates[1])
            return_coordinate=[enemy_coordinates,move_coordinates]# bouge le mouton
        else : # Supprime le mouton
            del player[player]['sheeps'][enemy_coordinates]
            manage_emoji(enemy_coordinates)

    elif attack_coordinates[1] > enemy_coordinates[1]: #     if old_y < new_y
        if players[player]['sheeps'][enemy_coordinates][0] >= 2 :# vérifie la vie du mouton si elle ne tombe pas a 0 (= mort)
            players[player]['sheeps'][enemy_coordinates][0] -= 1 # enlève une vie
            move_coordinates = [enemy_coordinates[0],enemy_coordinates[1]] # Crée le nouvelle emplacement
            move_coordinates[1] -= 5 # déplacement de 5 vers le haut
            move_coordinates = (move_coordinates[0],move_coordinates[1])  
            return_coordinate=[enemy_coordinates,move_coordinates]# bouge le mouton
        else : # Supprime le mouton
            del player[player]['sheeps'][enemy_coordinates]
            manage_emoji(enemy_coordinates)
    return return_coordinate

def move_sheep (old_coordinates,new_coordinates,attack=0): # ! (scott) ATTENTION IL FAUT RETIRER LE FAIT QU'IL ATTACK SI IL Y A UN MOUTON !
    """Move a sheep or attack if an another sheep is already there  
    parameters
    ----------
    attack : if the function need to move more or not the sheep
    old_coordinates : coordinate in x,y of the sheep where he was (list)
    new_coordinates : coordinate in x,y of the sheep where it will move (list)
    
    version
    -------
    specification: Aloïs Baurant (v1 23/02/24)
    """
    old_coordinates=((int(old_coordinates[0])),(int(old_coordinates[1])))
    new_coordinates=((int(new_coordinates[0])),(int(new_coordinates[1])))
    kill_sheep=0
    move=0
    respawn_grass=0
    for sheep_1 in players['player_1']['sheeps'] : # Joueur 1
        if sheep_1  == old_coordinates:
            sheep = "🐑"
            player = "player_1"

    for sheep_2 in players['player_2']['sheeps'] : # Joeueur 2
        if sheep_2 == old_coordinates:
            sheep = "🐐"
            player = "player_2"
    if attack == 1 :# Bouge le mouton sur la carte
        for rock in map["rocks"] :
            if new_coordinates == rock :
                kill_sheep = 1
        
        for spawn in map['spawn'] :
            if new_coordinates == spawn :
                move = 1

        # if sheep get attacked == 0
        if new_coordinates[0] < 0 or new_coordinates[1] < 0 or kill_sheep == 1 or new_coordinates[0] > map['map_size'][0] or new_coordinates[1] > map['map_size'][1] :
                del players[player]['sheeps'][old_coordinates]
                manage_emoji(old_coordinates)
                kill_sheep=1

    # vérifie si il y avais une herbe a la position du mouton
    for herbs in grass['player_1']:
        if old_coordinates == herbs :
            respawn_grass = 1

    for herbs in grass['player_2']:
        if old_coordinates == herbs :
            respawn_grass = 1

    if kill_sheep != 1: #regarde dans la base de donnée les moutons
        if move == 1 :
            new_coordinates[0] += 1
            new_coordinates[1] += 1
        new_coordinates=(new_coordinates[0],new_coordinates[1])
        
        manage_emoji(old_coordinates)
        manage_emoji(new_coordinates,sheep)
        
        alife = players[player]['sheeps'][old_coordinates]
        del players[player]['sheeps'][old_coordinates]
        players[player]['sheeps'][new_coordinates]=alife

        if respawn_grass == 1:
            manage_emoji(old_coordinates)

#    Code poubelle, mais que je supprime pas car je ne le sens pas.
#    if old_coordinates[0] > new_coordinates[0]:
#        if attack == 1
#            old_coordinates[1] != new_coordinates[1]:
#            manage_emoji(old_coordinates)
#            manage_emoji(new_coordinates,sheep)
#
#    if old_coordinates[0] < new_coordinates[0]:
#        if attack == 1
#            old_coordinates[1] != new_coordinates[1]:
#            manage_emoji(old_coordinates)
#            manage_emoji(new_coordinates,sheep)
#
#    if old_coordinates[1] > new_coordinates[1]:
#        if attack == 1
#            old_coordinates[1] != new_coordinates[1]:
#            manage_emoji(old_coordinates)
#            manage_emoji(new_coordinates,sheep)
#
#    if old_coordinates[1] < new_coordinates[1]:
#        if attack == 1
#            old_coordinates[1] != new_coordinates[1]:
#            manage_emoji(old_coordinates)
#            manage_emoji(new_coordinates,sheep)


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
    if what_in_the_box(sheep_coordinates,"grass"):
        return 0
    sheep_coordinates=((int(sheep_coordinates[0])),(int(sheep_coordinates[1])))
    all_sheep_coordinates=[]
    if sheep==0:
        for sheep in players["player_1"]['sheeps']:
            if players["player_1"]['sheeps'][sheep_coordinates][1]==False:
                all_sheep_coordinates.append(sheep)
    else:
        for sheep in players["player_2"]['sheeps']:
            if players["player_2"]['sheeps'][sheep_coordinates][1]==False:
                all_sheep_coordinates.append(sheep)
    if not sheep_coordinates in all_sheep_coordinates:
        return 0
    else:
        for herbs in grass['player_1']:
            if herbs==sheep_coordinates:
                player='player_1'
        for herbs in grass['player_2']:
            if herbs==sheep_coordinates:
                player='player_2'
        del grass[player][sheep_coordinates]

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
    
    
    split_all_order = get_order.split(' ')
    return split_all_order
    
def check_sheep_team(coordinates):
    """Gives the team the sheep belongs
    Parameters
    -------------------------
    coordinate: The coordinates of the sheep
    return
    ----------------------------
    team: The sheep team (0 if there not the sheep, 1 if the sheep belong to player 1, 2 if the sheep belong to player 2) (int)
    """
    coordinates=((int(coordinates[0]),(int(coordinates[1]))))
    for sheep_1 in players['player_1']['sheeps'] : # Joueur 1
        if sheep_1  == coordinates:
            return 1
    for sheep_2 in players['player_2']['sheeps'] : # Joueur 1
        if sheep_2  == coordinates:
            return 2
    return 0

def game_function(player_1_orders,player_2_orders):   #j'ai changé la spécification mais il faut que je demande au tuteur ou assistant pour la mettre dans se dossier
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
    update_grass() #il faut regarder si on fusionne growth_grass et grass_propagation
    my_attacl_list=[]
    move_attack=[]
    for order in player_1_orders:
        if 'x' in order:
            order_string=order.split(":")
            attack_coordinates=order_string[0]
            coordinate=attack_coordinates.split("-")
            coordinate=(coordinate[0],coordinate[1])
            if check_sheep_team(coordinate)==1:
                coordinates=((int(coordinate[0]),(int(coordinate[1]))))
                if not players['player_1']['sheeps'][coordinates][1]:
                    my_attacl_list.append(order)
                    players['player_1']['sheeps'][coordinates][1]=True
    for order in player_2_orders:
        if 'x' in order:
            order_string=order.split(":")
            attack_coordinates=order_string[0]
            coordinate=attack_coordinates.split("-")
            coordinate=(coordinate[0],coordinate[1])
            if check_sheep_team(coordinate)==2:
                coordinates=((int(coordinate[0]),(int(coordinate[1]))))
                if not players['player_2']['sheeps'][coordinates][1]:
                    my_attacl_list.append(order)
                    players['player_2']['sheeps'][coordinates][1]=True
    for attack in my_attacl_list:
        order_string=attack.split(":")
        attack_coordinates=order_string[1][1:]
        enemy_coordinates=attack_coordinates.split("-")
        attacker_coordinates=order_string[0].split("-")
        if not can_attack(attacker_coordinates,enemy_coordinates):  #demander si on mets les coordonées du mouton qui attaque pour être sur qu'il peut attaquer
            my_attacl_list.remove(attack)
    for attack_z in my_attacl_list:
        order_string=attack_z.split(":")
        attack_coordinates=order_string[1][1:]
        enemy_coordinates=attack_coordinates.split("-")
        attacker_coordinates=order_string[0].split("-")
        move_attack.append(attack_sheep(attacker_coordinates,enemy_coordinates))
    for my_list in move_attack:
        move_sheep(my_list[0],my_list[1],1)
    for order in player_1_orders:
        if '@' in order:
            order_string=order.split(":")
            coordinate=order_string[1][1:]
            new_coordinates=coordinate.split("-")
            coordinate=order_string[0]
            old_coordinates=coordinate.split("-")
            coordinate=(old_coordinates[0],old_coordinates[1])
            if check_sheep_team(coordinate) ==1 and can_move(old_coordinates,new_coordinates,1):
                coordinates=((int(coordinate[0]),(int(coordinate[1]))))
                if not players['player_1']['sheeps'][coordinates][1]:
                    move_sheep(old_coordinates,new_coordinates)
                    players['player_1']['sheeps'][coordinates][1]=True
    for order in player_2_orders:
        if '@' in order:
            order_string=order.split(":")
            coordinate=order_string[1][1:]
            new_coordinates=coordinate.split("-")
            coordinate=order_string[0]
            old_coordinates=coordinate.split("-")
            coordinate=(old_coordinates[0],old_coordinates[1])
            if check_sheep_team(coordinate) ==2 and can_move(old_coordinates,new_coordinates,2):
                coordinates=((int(coordinate[0]),(int(coordinate[1]))))
                if not players['player_2']['sheeps'][coordinates][1]:
                    move_sheep(old_coordinates,new_coordinates)
                    players['player_2']['sheeps'][coordinates][1]=True
    for order in player_1_orders:
        if '*' in order:
            order_string=order.split(":")
            coordinate=order_string[0]
            grass_coordinate=coordinate.split("-")
            coordinate=(grass_coordinate[0],grass_coordinate[1])
            if check_sheep_team(coordinate) ==1:
                sheep_graze(0,grass_coordinate)
    for order in player_2_orders:
        if '*' in order:
            order_string=order.split(":")
            coordinate=order_string[0]
            grass_coordinate=coordinate.split("-")
            coordinate=(grass_coordinate[0],grass_coordinate[1])
            if check_sheep_team(coordinate) ==2:
                sheep_graze(1,grass_coordinate)
    for player_sheep in players['player_1']['sheeps']:
        players["player_1"]['sheeps'][player_sheep][1]=False
    for player_sheep2 in players['player_2']['sheeps']:
        players["player_2"]['sheeps'][player_sheep2][1]=False

def can_move(xy_sheep, xy_destination,team):  #je vais le prendre (scott)
    '''check if a sheep can move to the box 

    parameters
    ----------
    xy_destination :  the (x,y) coordinates where the sheep is (tuples)
    xy_destination : the (x,y) coordinates where the sheep want to go (tuples)
    team: the team of the sheep

    returns
    -------
    return True if the sheep can move, return False otherwise (bool)
        
    version
    -------
    specification: Heynen Scott-Socrate (v1 09/03/24)
    '''
    xy_sheep=((int(xy_sheep[0])),(int(xy_sheep[1])))
    xy_destination=((int(xy_destination[0])),(int(xy_destination[1])))
    if team==1:
        if players['player_1']['sheeps'][xy_sheep][1]:
            return False
    if team==2:
        if players['player_2']['sheeps'][xy_sheep][1]:
            return False
    
    if -1 > xy_destination[0] - xy_sheep[0] or xy_destination[0] - xy_sheep[0] > 1: #look if the sheep is more than 1 box away (abscissa only)
        return False
    elif -1 > xy_destination[1] - xy_sheep[1] or xy_destination[1] - xy_sheep[1] >1 : #look if the sheep is more than 1 box away (ordinate only)
        return False
    elif what_in_the_box(xy_destination,'rock'):
        return False
    elif what_in_the_box(xy_destination,'void'):
        return False
    elif what_in_the_box(xy_destination,'spawn'):
        return False
    elif what_in_the_box(xy_destination,'sheep'):
        return False 
    else:
        return True



def what_in_the_box(xy,search):
    '''return True if there is the asked-thing in the box 
    
    parameters
    ----------
    xy : the (x,y) coordinates where search (tuples)
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
    xy=((int(xy[0])),(int(xy[1])))
    if search == 'rock':
        for rock in map['rocks']:
            if xy == map['rocks'][rock]:
                return True
            
        return False
            
    if search == 'spawn':
        for spawn in map['spawn']:
            if xy == map['spawn'][spawn]:
                return True
        return False
            
    if search == 'void':
        if xy[0] >= map['map_size'][0] or xy[0] < 0 : #look  if outside (abscissa only)
            return True
        if xy[1]> map['map_size'][1] or xy[1] < 1 : #look if outside (ordinate only)
            return True
        else:
            return False
    
    if search == 'grass':
        for herbs in grass:
            if xy == herbs:
                return True
        return False
    
    if search == 'sheep':
        for sheep in players['player_1']['sheeps']:
            if xy == sheep:
                return True
        for sheep in players['player_2']['sheeps']:
            if xy == sheep:
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
    target=[(int(target[0])),(int(target[1]))]
    sheep=[(int(sheep[0])),(int(sheep[1]))]
    listx=[target[0]-1,target[0],target[0]+1]
    listy=[target[1]-1,target[1],target[1]+1]
    if sheep[0] not in listx :
        answer=False
    elif sheep[1]not in listy :
        answer=False
    else:
        answer=True
    return answer

def check_syntax_order(order):
    """look if the syntax of an order is correct

    parameter:
    order: the order to check (list)

    return:
    newliste: a list with all the correct order
  
    version: 
    V2 Arthur (23/03)"""
    liste=order
    newliste=[]
    for i in liste:

        if i=='sheep':
            newliste.append(i)
        else:
                txt=i
                number=['0','1','2','3','4','5','6','7','8','9']
                caractere=['@','x']
                if 5<=len(txt) and 12>=len(txt):
                    if txt[0] in number:
                        a=1
                        while txt[a] in number:
                            a+=1            
                        if txt[a]=='-':
                            a+=1
                            if txt[a] in number:
                                while txt[a] in number:
                                    a+=1
                            
                                if txt[a]==':':
                                    a+=1
                                    if txt[a] in caractere:
                                        a+=1
                                        

                                        if txt[a] in number:
                                            

                                            while txt[a] in number:
                                                a+=1
                                            if txt[a]=='-':
                                                a+=1
                                                

                                                if (len(txt)-a)==1:
                                                    if (txt[a] in number):
                                                        newliste.append(i)
                                                elif len(txt)-a==2:
                                                    if (txt[a] in number) and (txt[a+1] in number):

                                                        newliste.append(i)

                                    
                                    
                                    elif (txt[a]=='*')and (len(txt)==(a+1)):
                                        newliste.append(i)
    return newliste

display_map(map)


#manage_emoji((20,22),"🐑")
#manage_emoji((20,21),"🐐")
#manage_emoji((20,16),"🌾")
#time.sleep(2)
#game_function(['20-22:x20-21'],['20-16:*'])  
#print (term.white+term.on_black)
#print (grass['player_1'])
