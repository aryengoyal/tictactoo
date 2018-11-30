
# coding: utf-8

# In[32]:




# In[33]:


import os


# In[34]:



def disp_board(board):
    os.system("cls")
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('___|___|___')
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('___|___|___')
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')


# In[35]:


def player_input():
    marker = ''
    while not(marker =='X' or marker =='O'):
        marker = input('Player1 : What do you want to be X or O ? ')
        
    
    if marker =='X':
        return ('X','O')
    else:
        return ('O','X')  
                  


# In[36]:


def plcmrk(board,pos,marker):
    board[pos] = marker


# In[37]:


def wincheck(board,mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or
           (board[4]==mark and board[5]==mark and board[6]==mark)or
           (board[1]==mark and board[2]==mark and board[3]==mark)or
           (board[7]==mark and board[4]==mark and board[1]==mark)or
           (board[8]==mark and board[5]==mark and board[2]==mark)or
           (board[9]==mark and board[6]==mark and board[3]==mark)or
           (board[1]==mark and board[5]==mark and board[9]==mark)or
           (board[7]==mark and board[5]==mark and board[3]==mark))


# In[38]:


import random
def firststep():
    if random.randint(0,1) == 0 :
        print('Player1 will go first')
        return 'Player1'
    else:
        print('Player2 will go first')
        return 'Player2'


# In[39]:


def blank_space(board,pos):
    return board[pos] == ' '


# In[40]:


def full(board):
    for i in range(1,10):
        if blank_space(board,i):
            return False
    else:
        return True


# In[41]:


def choice(board):
    pos = ' '
    while pos not in ['1','2','3','4','5','6','7','8','9'] or not blank_space(board,int(pos)):
        pos = input('Choose your next option : (1-9)')
        
    return int(pos)



# In[42]:


def replay():
    x = input('Do you want to play again : Yes or No')
    if (x =='Yes' or x == 'yes'):
        return True
    else:
        return False


# In[43]:


print('TICTACTOO')

while True:
    
    myboard = [' ']*10
    player1marker,player2marker = player_input()
    a = firststep()
    x=1
    while x==1:
        
        if a == "Player1":
            disp_board(myboard)
            position = choice(myboard)
            plcmrk(myboard,position,player1marker)

            if wincheck(myboard,player1marker):
                disp_board(myboard)
                print('Player 1 wins')
                x=2
            elif full(myboard):
                    print('DRAW')
                    break
            else:
                a="Player2"
        else:
            disp_board(myboard)
            position = choice(myboard)
            plcmrk(myboard,position,player2marker)

            if wincheck(myboard,player2marker):
                disp_board(myboard)
                print('Player 2 wins')
                x=2
            elif full(myboard):
                    print('DRAW')
                    break
            else:
                a= "Player1"
            
    if not replay():
        break
        

