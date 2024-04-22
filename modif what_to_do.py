def what_should_do(sheep,player_id,role=1):
    """prend les décision en fonction de la situation du mouton et donne le comportement à adopter
    
    parametre:
    sheep=position du mouton appartenant à l'ia(tuple)(x,y)
    role=si il est plus proche du spawn et qu'il n'es pas tout seul role=0 (boull)
    player_id= le numéo de joueur du mouton
    return:
    l'ordre à executer

    spécification:
    Arthur Yernaux 06/04/2024
    implémentation
    v1 19/04/2024 Arthur Yernaux
    v2 20/04/2024 Arthur Yernaux

    """

    mouton_coller=search_sheep(sheep,1)
    if len(mouton_coller) != 0 :
        return search_attack(sheep)
    

    if role==0 :
        seed=search_seeds(sheep,5)
        ennemy=search_sheep(sheep,5)
        all_ennemy=search_sheep(sheep,100)
        ennemy_proche=[]
        herbe=search_grass(sheep,1000,'a')
        for i in all_ennemy:
            for a in herbe:
                if get_distance(i,a)<5 and i not in ennemy_proche:
                    ennemy_proche.append(i)
        if len(seed) != 0 and len(search_grass(sheep,5,'a')) != 0 :
            if len(seed)==1:
                target=move_ia(sheep,seed[0])
                return move_sheep(sheep,target)
            else:
                target=move_ia(sheep,look_for_seed(sheep))
                return move_sheep(sheep,target)
            
        
        elif len(ennemy)!=0 and len(search_grass(sheep,5,'a')):

            return search_attack(sheep)
        
        elif len(ennemy_proche)!=0 :
            min=1000
            for b in ennemy_proche:
                distance=get_distance(b,sheep)
                if distance<min:
                    min=distance
                    ennemy_opti=b
            target=move_ia(sheep,ennemy_opti)
            return move_sheep(sheep,target)
        
        
        elif len(search_grass(sheep,100,'a'))>0:
            herbe=search_grass(sheep,100,'a')
            taille=map['map_size'].copy()
            taille[0]=math.floor(taille[0]/2)
            taille[1]=math.floor(taille[1]/2)
            min=1000
            for i in herbe:
                distance=get_distance(i,taille)
                if distance<min:
                    min=distance
                    grass_opti=i
            if sheep!=grass_opti:
                target=move_ia(sheep,grass_opti)
                return move_sheep(sheep,target)
            else:
                grass_opti[0]=grass_opti[0]+1
                target=move_ia(sheep,grass_opti)
                return move_sheep(sheep,target)
        else:
            spawn=map['spawn']['spawn_'+str(player_id)]
            if sheep[0]!= spawn[0]+1:
                spawn[0]=spawn[0]+1
                target=move_ia(sheep,spawn)
                return move_sheep(sheep,target)
            else:
                spawn[0]=spawn[0]-1
                target=move_ia(sheep,spawn)
                return move_sheep(sheep,target)
    

    else:
        ennemy=search_sheep(sheep,8)
        list_seed =search_seeds(sheep,10)
        ennemy_grass =search_grass(sheep,1000)
        player_team_sheep_1="player_2"
        for player_sheep in players['player_1']['sheeps']:
            if sheep==player_sheep:
                player_team_sheep_1="player_1"
            

        
        
        
        if what_in_the_box(sheep,'grass'):
            
            if player_team_sheep_1=="player_1":
                herbe=grass['player_2']
                if sheep in herbe:
                    orders = ' '+str(sheep[0])+'-'+str(sheep[1])+':*'
                    return orders
            elif player_team_sheep_1=="player_2":
                herbe=grass['player1']
                if sheep in herbe:
                    orders = ' '+str(sheep[0])+'-'+str(sheep[1])+':*'
                    return orders
        
        
        if len(ennemy)!=0:
            


            if player_team_sheep_1=="player_1":
                ennemy=players["player_2"]
                ennemy=ennemy["sheeps"]
                for ennemys in ennemy:
                    mouton=ennemy[ennemys]
                    if mouton[0]==1:
                        return search_attack(sheep)
                        
            else:
                ennemy=players["player_1"]
                ennemy=ennemy["sheeps"]
                for ennemys in ennemy:
                    mouton=ennemy[ennemys]
                    if mouton[0]==1:
                        return search_attack(sheep)

        elif len(list_seed)!=0:
            min=1000
            for seed in list_seed:
                distance=get_distance(seed,sheep)
                if distance<min:
                    min=distance
                    seed_opti=seed
            target=move_ia(sheep,seed_opti)
            return move_sheep(sheep,target)
        
        
        elif len(search_sheep(sheep,5))!=0:
            ennemy=search_sheep(sheep,5)
            return search_attack(sheep)

        else:
            min=1000
            for herbe in ennemy_grass:
                distance=get_distance(grass,sheep)
                if distance<min:
                    min=distance
                    grass_opti=herbe
            target=move_ia(sheep,grass_opti)
            return move_sheep(sheep,target)



#-------------------------------------------------------------------------------------------------------------------------------------------------------





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
    spawn_append=(map['spawn']['spawn_1'][0],map['spawn']['spawn_1'][1])
    wrong.append(spawn_append)
    spawn_append=(map['spawn']['spawn_2'][0],map['spawn']['spawn_2'][1])
    wrong.append(spawn_append)
    
    
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
