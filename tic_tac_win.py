
#check for horizontal completeness
def check_horizontal(current_Arr,player):
    
    for i in range(0,3):

        count=current_Arr[i].count(player)
        
        if(count==3):
            game_status='1'
            return game_status
        else:
            game_status='0'    

    return game_status

#check for vertical completeness
def check_vertical(current_Arr,player):

    new_arr = [[0,0,0],
                [0,0,0],
                    [0,0,0]]
    for i in range(0,3):
        for j in range(0,3):
            new_arr[i][j]=current_Arr[j][i]
    game_status=check_horizontal(new_arr,player)  
         
    return game_status    

#check for diagonal completeness
def check_diagonal(current_Arr,player):
    diag_count=0
    inv_diag_count=0
    for i in range(0,3):
        for j in range(0,3):
            if(i+j==2 and current_Arr[i][j]==player):
                diag_count+=1
            if(i-j==0 and current_Arr[i][j]==player):
                inv_diag_count+=1    
    
    if(inv_diag_count==3 or diag_count==3):
        game_status='1'
    else:
        game_status='0'    
    
    print("d:"+game_status) 
    return game_status

def check_tic_tac_win(current_Arr,player):


    h_game_status=check_horizontal(current_Arr,player)

    v_game_status=check_vertical(current_Arr,player)

    d_game_status=check_diagonal(current_Arr,player) 

    if(h_game_status=='1' or v_game_status=='1' or d_game_status=='1'):
        game_status='1'
    else:
        game_status='0'    
    print(game_status)

    #game_status=player
    return game_status    

def get_current_charcounts(current_arr):
                   
    no_1s=0
    no_0s=0
    for i in range(0,len(current_arr)):
        no_1s=no_1s+current_arr[i].count('x')
        no_0s=no_0s+current_arr[i].count('0')
    return [no_0s,no_1s]  

# current_arr = [['0','x','x'],
#                ['0','','x'],
#                ['0','','0']]

# current_arr = [['0','x','x'],
#                ['0','0','x'],
#                ['','','0']]               

# current_arr = [['0','0','0'],
#                ['x','','x'],
#                ['x','','0']]

current_arr = [['x','','0'],
               ['x','0','x'],
               ['0','','0']]               

char_count = get_current_charcounts(current_arr)
zeros_count=char_count[0]
ones_count=char_count[1]

if(zeros_count>ones_count):
    last_player='0'
else:
    last_player='x'
    
        

status=check_tic_tac_win(current_arr,last_player) 
    
print(zeros_count)
print(ones_count)               

if(status=='1'):

    print(last_player+" Won")
else:
    print(last_player+" has not won")    