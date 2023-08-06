import copy
import random

# Samet Enes Örsdemir 
# 150119661
class State: #state class
    
    def __init__(self, map, depth, parent, plyrmove):
        self.map = map
        self.depth = depth
        self.parent = parent
        self.plyrmove = plyrmove

    def print_board(self): #print board function
        print("\n")
        i = 0
        print("Turn:" + str(self.depth))
        #print("Player: " + str(self.plyrmove.id))
        for row in self.map:
            print("")
            for column in row:
                if(column == 1):
                    print("1", end = ' ')
                elif(column == 0):
                    print("O", end = ' ')  
                elif(column == 2):
                    print("2", end = ' ')  
            i += 1
class Player: # player class
    def __init__(self, id, piece_amount):
        self.id = id
        self.piece_amount = piece_amount

# board representation
initial_map = [
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]   
]

#objects
player1 = Player(1,28) 
player2 = Player(2,28)
initial_state = State(initial_map, depth=0,parent=None,plyrmove=player1)
states = [initial_state] # state list


# This function checks the suitability of the column, 
# whether there is enough space for the move command.
def check_move(state,move): # move is ok or not
    le = len(state.map)
    for row in range(le-1,-1,-1):
        if state.map[row][move-1] != 0:
            continue
        else: 
            return row,move-1
    return False

# This function, which has two, checks whether the game is over or not. 
# Returns the number 1 or 2 depending on the ending state of the game. 
# The reason for the existence of two is that one of them proceeds 
# through the class and the other through the map.
def check_win(state):
    map = state.map
    vertical_count = 0
    horizontal_count = 0
    # vertical search for 1---------------------------------
    for i in range(8):
        vertical_count = 0
        for row in map: 
            if row[i] == 1:
                vertical_count += 1
            else:
                vertical_count = 0
            if(vertical_count == 4):
                #print("win 1")
                return 1
    # ------------------------------------------------
    # vertical search for 2---------------------------------
    for i in range(8):
        vertical_count = 0
        for row in map: 
            if row[i] == 2:
                vertical_count += 1
            else:
                vertical_count = 0
            if(vertical_count == 4):
                #print("win 2")
                return 2
    # ------------------------------------------------
    # horizontal search for 1--------------------------
    for row in state.map:
        horizontal_count = 0
        for col in row:
            if (col == 1):
                horizontal_count += 1
            else:
                horizontal_count = 0
            if horizontal_count == 4:
                #print("win 1")
                return 1
    #--------------------------------------------------
    # horizontal search for 2--------------------------
    for row in state.map:
        horizontal_count = 0
        for col in row:
            if (col == 2):
                horizontal_count += 1
            else:
                horizontal_count = 0
            if horizontal_count == 4:
                #print("win 1")
                return 2
    #--------------------------------------------------
    # diagonal search for 1
    for i in range(len(map) - 3):
        for j in range(len(map[0]) - 3):
            if map[i][j] == 1 and map[i+1][j+1] == 1 and map[i+2][j+2] == 1 and map[i+3][j+3] == 1:
                return 1
            if map[i][j+3] == 1 and map[i+1][j+2] == 1 and map[i+2][j+1] == 1 and map[i+3][j] == 1:
                return 1
    #--------------------------------------------------
    # diagonal search for 2
    for i in range(len(map) - 3):
        for j in range(len(map[0]) - 3):
            if map[i][j] == 2 and map[i+1][j+1] == 2 and map[i+2][j+2] == 2 and map[i+3][j+3] == 2:
                return 2
            if map[i][j+3] == 2 and map[i+1][j+2] == 2 and map[i+2][j+1] == 2 and map[i+3][j] == 2:
                return 2
    #--------------------------------------------------
# This function, which has two, checks whether the game is over or not. 
# Returns the number 1 or 2 depending on the ending state of the game. 
# The reason for the existence of two is that one of them proceeds 
# through the class and the other through the map.
def check_win2(map):
    vertical_count = 0
    horizontal_count = 0
    # vertical search for 1---------------------------------
    for i in range(8):
        vertical_count = 0
        for row in map: 
            if row[i] == 1:
                vertical_count += 1
            else:
                vertical_count = 0
            if(vertical_count == 4):
                #print("win 1")
                return 1
    # ------------------------------------------------
    # vertical search for 2---------------------------------
    for i in range(8):
        vertical_count = 0
        for row in map: 
            if row[i] == 2:
                vertical_count += 1
            else:
                vertical_count = 0
            if(vertical_count == 4):
                #print("win 2")
                return 2
    # ------------------------------------------------
    # horizontal search for 1--------------------------
    for row in map:
        horizontal_count = 0
        for col in row:
            if (col == 1):
                horizontal_count += 1
            else:
                horizontal_count = 0
            if horizontal_count == 4:
                #print("win 1")
                return 1
    #--------------------------------------------------
    # horizontal search for 2--------------------------
    for row in map:
        horizontal_count = 0
        for col in row:
            if (col == 2):
                horizontal_count += 1
            else:
                horizontal_count = 0
            if horizontal_count == 4:
                #print("win 1")
                return 2
    #--------------------------------------------------
    # diagonal search for 1
    for i in range(len(map) - 3):
        for j in range(len(map[0]) - 3):
            if map[i][j] == 1 and map[i+1][j+1] == 1 and map[i+2][j+2] == 1 and map[i+3][j+3] == 1:
                
                return 1
            if map[i][j+3] == 1 and map[i+1][j+2] == 1 and map[i+2][j+1] == 1 and map[i+3][j] == 1:
                
                return 1
    #--------------------------------------------------
    # diagonal search for 2
    for i in range(len(map) - 3):
        for j in range(len(map[0]) - 3):
            if map[i][j] == 2 and map[i+1][j+1] == 2 and map[i+2][j+2] == 2 and map[i+3][j+3] == 2:
                
                return 2
            if map[i][j+3] == 2 and map[i+1][j+2] == 2 and map[i+2][j+1] == 2 and map[i+3][j] == 2:
                
                return 2
    #--------------------------------------------------

# This function is a function that adds all possible moves
# to the list by scanning the map and returns the list. 
def getAllMoves(map):
    moves = []
    le = len(map)
    for i in range (le-1,-1,-1):
        for j in range(len(map[i])):
            if (i != le-1):
                if(map[i+1][j] != 0 and map[i][j] == 0):
                    moves.append([i,j])
            if ( i == le-1 and map[i][j] == 0):
                moves.append([i,j])
    return moves

# This is a function that returns all the next playable positions 
# (i.e. children) of the sent node by adding it to a list.
def get_children(node,player): #
    children = []
    for col in range(len(node.map[0])):
        if not is_column_full(node.map, col):
            new_map = [row[:] for row in node.map]
            for row in range(len(new_map)-1, -1, -1):
                if new_map[row][col] == 0:
                    new_map[row][col] = player.id
                    break
            new_state = State(new_map, node.depth+1, node, player)
            #new_state.print_board()
            children.append(new_state)
    return children

# This function returns whether the column is full.
def is_column_full(board, col): #
    return board[0][col] != 0    

# This function returns all possible winning positions, 
# counting both for the player and for the opponent.
def possible_wins(board,player):
    opponent = 2 if player == 1 else 1
    opponent = 1 if player == 2 else 1
    player_wins = 0
    opponent_wins = 0
    
    # check rows for possible wins
    for row in board:
        for i in range(len(row) - 3):
            if row[i:i+4] == [player, player, player, 0]:
                player_wins += 1
            if row[i:i+4] == [opponent, opponent, opponent, 0]:
                opponent_wins += 1
    
    # check columns for possible wins
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if [board[row][col], board[row+1][col], board[row+2][col], board[row+3][col]] == [player, player, player, 0]:
                player_wins += 1
            if [board[row][col], board[row+1][col], board[row+2][col], board[row+3][col]] == [opponent, opponent, opponent, 0]:
                opponent_wins += 1
    
    # check diagonals for possible wins
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if [board[row][col], board[row+1][col+1], board[row+2][col+2], board[row+3][col+3]] == [player, player, player, 0]:
                player_wins += 1
            if [board[row][col], board[row+1][col+1], board[row+2][col+2], board[row+3][col+3]] == [opponent, opponent, opponent, 0]:
                opponent_wins += 1
            if [board[row][col+3], board[row+1][col+2], board[row+2][col+1], board[row+3][col]] == [player, player, player, 0]:
                player_wins += 1
            if [board[row][col+3], board[row+1][col+2], board[row+2][col+1], board[row+3][col]] == [opponent, opponent, opponent, 0]:
                opponent_wins += 1
    return player_wins, opponent_wins

# This function returns consecutive pieces of the same color, 
# counting for both the player and the opponent.
def consecutive_pieces(board, player):
    opponent = 2 if player == 1 else 1
    opponent = 1 if player == 2 else 1
    player_consecutive = 0
    opponent_consecutive = 0
    
    # check rows for consecutive pieces
    for row in board:
        player_count = 0
        opponent_count = 0
        for i in range(len(row)):
            if row[i] == player:
                player_count += 1
                opponent_count = 0
            elif row[i] == opponent:
                opponent_count += 1
                player_count = 0
            else:
                player_consecutive = max(player_consecutive, player_count)
                opponent_consecutive = max(opponent_consecutive, opponent_count)
                player_count = 0
                opponent_count = 0
        player_consecutive = max(player_consecutive, player_count)
        opponent_consecutive = max(opponent_consecutive, opponent_count)

    # check columns for consecutive pieces
    for col in range(len(board[0])):
        player_count = 0
        opponent_count = 0
        for row in range(len(board)):
            if board[row][col] == player:
                player_count += 1
                opponent_count = 0
            elif board[row][col] == opponent:
                opponent_count += 1
                player_count = 0
            else:
                player_consecutive = max(player_consecutive, player_count)
                opponent_consecutive = max(opponent_consecutive, opponent_count)
                player_count = 0
                opponent_count = 0
        player_consecutive = max(player_consecutive, player_count)
        opponent_consecutive = max(opponent_consecutive, opponent_count)

    # check diagonals for consecutive pieces
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            diagonal = []
            for i in range(4):
                diagonal.append(board[row+i][col+i])
            player_count = 0
            opponent_count = 0
            for i in diagonal:
                if i == player:
                    player_count += 1
                    opponent_count = 0
                elif i == opponent:
                    opponent_count += 1
                    player_count = 0
                else:
                    player_consecutive = max(player_consecutive, player_count)
                    opponent_consecutive = max(opponent_consecutive, opponent_count)
                    player_count = 0
                    opponent_count = 0
    return player_consecutive, opponent_consecutive

# This function counts the pieces that are symmetrically on the board. 
# Used by heuristics.
def symmetry(board,player):
    symmetry_count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == player and board[i][j] == board[len(board) - 1 - i][len(board[0]) - 1 - j]:
                symmetry_count += 1
    return symmetry_count


# This function scores for both the opponent and the player in all possible winning situations. 
# Then it scores the blocking positions against the opponent. 
# Finally, he gets the heuristic score by subtracting the opponent score from the player score.
def h1(map,player):
    player1score = 0
    opponentscore = 0
    opponent = 2 if player == 1 else 1
    opponent = 1 if player == 2 else 1
    
    for row in map: # Check rows
        for i in range(len(row) - 3):
            if row[i] == row[i+1] == row[i+2] == row[i+3] == player:
                player1score += 100
            if row[i] == row[i+1] == row[i+2] == row[i+3] == opponent:
                opponentscore += 100
    
    for col in range(len(map[0])): # Check columns
        for row in range(len(map) - 3):
            if map[row][col] == map[row+1][col] == map[row+2][col] == map[row+3][col] == player:
                player1score += 100
            if map[row][col] == map[row+1][col] == map[row+2][col] == map[row+3][col] == opponent:
                opponentscore += 100
    
    for row in range(len(map) - 3): # Check diagonals
        for col in range(len(map[0]) - 3):
            if map[row][col] == map[row+1][col+1] == map[row+2][col+2] == map[row+3][col+3] == player:
                player1score += 100
            if map[row][col] == map[row+1][col+1] == map[row+2][col+2] == map[row+3][col+3] == opponent:
                opponentscore += 100
            if map[row][col+3] == map[row+1][col+2] == map[row+2][col+1] == map[row+3][col] == player:
                player1score += 100
            if map[row][col+3] == map[row+1][col+2] == map[row+2][col+1] == map[row+3][col] == opponent:
                opponentscore += 100
    
    for row in map: #Check rows for blocking
        for i in range(len(row) - 3): 
            if row[i:i+4] == [opponent,opponent,opponent, "0"]:
                player1score += 90
            if row[i:i+4] == ["0", opponent, opponent, opponent]:
                player1score += 90
            if row[i:i+4] == [opponent,opponent,opponent, player]:
                player1score += 90
            if row[i:i+4] == [player, opponent, opponent, opponent]:
                player1score += 90
    
    for col in range(len(map[0])): # Check columns for blocking
        for row in range(len(map) - 3):
            if [map[row][col], map[row+1][col], map[row+2][col], map[row+3][col]] == [opponent, opponent, opponent, "0"]:
                player1score += 90
            if [map[row][col], map[row+1][col], map[row+2][col], map[row+3][col]] == ["0", opponent, opponent, opponent]:
                player1score += 90
            if [map[row][col], map[row+1][col], map[row+2][col], map[row+3][col]] == [opponent, opponent, opponent, player]:
                player1score += 90
            if [map[row][col], map[row+1][col], map[row+2][col], map[row+3][col]] == [player, opponent, opponent, opponent]:
                player1score += 90
    
    for row in range(len(map) - 3): # Check diagonals for blocking
        for col in range(len(map[0]) - 3):
            if [map[row][col], map[row+1][col+1], map[row+2][col+2], map[row+3][col+3]] == [opponent, opponent, opponent, "0"]:
                player1score += 90
            if [map[row][col+3], map[row+1][col+2], map[row+2][col+1], map[row+3][col]] == ["0", opponent, opponent, opponent]:
                player1score += 90
            if [map[row][col], map[row+1][col+1], map[row+2][col+2], map[row+3][col+3]] == [opponent, opponent, opponent, player]:
                player1score += 90
            if [map[row][col+3], map[row+1][col+2], map[row+2][col+1], map[row+3][col]] == [player, opponent, opponent, opponent]:
                player1score += 90
    return player1score - opponentscore

# This function calculates and returns the difference between player and opponent 
# by scoring all possible wins, consecutive pieces, symmetric status and 4 pieces.
def h2(board, player):
    opponent = 2 if player == 1 else 1
    opponent = 1 if player == 2 else 1
    player1score = 0
    player2score = 0
    
    for row in board: # check rows for player and opponent
        for i in range(len(row) - 3):
            if row[i:i+4] == [player]*4:
                player1score += 100
            elif row[i:i+4] == [opponent]*4:
                player2score += 100
            
    
    for col in range(len(board[0])): # check columns for player and opponent
        for row in range(len(board) - 3):
            if [board[row][col], board[row+1][col], board[row+2][col], board[row+3][col]] == [player]*4:
                player1score += 100
            elif [board[row][col], board[row+1][col], board[row+2][col], board[row+3][col]] == [opponent]*4:
                player2score += 100
            
    
    for row in range(len(board) - 3): # check diagonals for player and opponent
        for col in range(len(board[0]) - 3):
            if [board[row][col], board[row+1][col+1], board[row+2][col+2], board[row+3][col+3]] == [player]*4:
                player1score += 100
            elif [board[row][col], board[row+1][col+1], board[row+2][col+2], board[row+3][col+3]] == [opponent]*4:
                player2score += 100
            if [board[row][col+3], board[row+1][col+2], board[row+2][col+1], board[row+3][col]] == [player]*4:
                player1score += 100
            elif [board[row][col+3], board[row+1][col+2], board[row+2][col+1], board[row+3][col]] == [opponent]*4:
                player2score += 100
    
    
    for row in board: # check rows for blocking
        for i in range(len(row) - 3):
            if row[i:i+4] == [opponent, opponent, opponent, player]:
                player1score += 100
            if row[i:i+4] == [player, opponent, opponent, opponent]:
                player1score += 100
    
    
    for col in range(len(board[0])): # check columns for blocking
        for row in range(len(board) - 3):
            if [board[row][col], board[row+1][col], board[row+2][col], board[row+3][col]] == [opponent, opponent, opponent, player]:
                player1score += 100
            if [board[row][col], board[row+1][col], board[row+2][col], board[row+3][col]] == [player, opponent, opponent, opponent]:
                player1score += 100
    
    
        for row in range(len(board) - 3): # check diagonals for blocking
            for col in range(len(board[0]) - 3):
                if [board[row][col], board[row+1][col+1], board[row+2][col+2], board[row+3][col+3]] == [opponent, opponent, opponent, player]:
                    player1score += 100
                if [board[row][col+3], board[row+1][col+2], board[row+2][col+1], board[row+3][col]] == [player, opponent, opponent, opponent]:
                    player1score += 100

    # the number of possible winnings for both player and opponent
    player_wins, opponent_wins = possible_wins(board, player)
    player1score += (player_wins - opponent_wins) * 10
    
    # distance between the pieces
    player_consecutive, opponent_consecutive = consecutive_pieces(board, player)
    player1score += (player_consecutive - opponent_consecutive) * 5

    # symmetry board
    player_symmetry= symmetry(board, player)
    opponent_symmetry =symmetry(board, opponent)
    player1score += (player_symmetry - opponent_symmetry) * 5
    
    return player1score - player2score
    

# This function scores all possible win situations, 
# pieces in the middle column, blocked opponent win moves and 4 pieces.
# Finally, the player-oppenent returns the score difference.
def h3(board,player):
    player_1_score = 0
    player_2_score = 0

    
    for row in board: # horizontal wins
        for i in range(len(row) - 3):
            if row[i] == 1 and row[i+1] == 1 and row[i+2] == 1 and row[i+3] == 1:
                player_1_score += 100
            elif row[i] == 2 and row[i+1] == 2 and row[i+2] == 2 and row[i+3] == 2:
                player_2_score += 100

    
    for col in range(len(board[0])): # vertical wins
        for row in range(len(board) - 3):
            if board[row][col] == 1 and board[row+1][col] == 1 and board[row+2][col] == 1 and board[row+3][col] == 1:
                player_1_score += 100
            elif board[row][col] == 2 and board[row+1][col] == 2 and board[row+2][col] == 2 and board[row+3][col] == 2:
                player_2_score += 100

    
    for row in range(len(board) - 3): # diagonal wins
        for col in range(len(board[0]) - 3):
            if board[row][col] == 1 and board[row+1][col+1] == 1 and board[row+2][col+2] == 1 and board[row+3][col+3] == 1:
                player_1_score += 100
            elif board[row][col] == 2 and board[row+1][col+1] == 2 and board[row+2][col+2] == 2 and board[row+3][col+3] == 2:
                player_2_score += 100

            if board[row][col+3] == 1 and board[row+1][col+2] == 1 and board[row+2][col+1] == 1 and board[row+3][col] == 1:
                player_1_score += 100
            elif board[row][col+3] == 2 and board[row+1][col+2] == 2 and board[row+2][col+1] == 2 and board[row+3][col] == 2:
                player_2_score += 100

    
    for row in range(len(board)): # scoring moves
        for col in range(len(board[0])):
            if board[row][col] == 1:
                player_1_score += 5 * (len(board) - row)
            elif board[row][col] == 2:
                player_2_score += 5 * (len(board) - row)

    #  number of possible winning moves
    player_1_win_moves, player_2_win_moves = possible_wins(board, 1)
    player_1_score += 10 * player_1_win_moves
    player_2_score += 10 * player_2_win_moves
    # number of blocked opponent's winning moves
    player_1_block_moves = count_block_moves(board, 1)
    player_2_block_moves = count_block_moves(board, 2)
    player_1_score += 5 * player_1_block_moves
    player_2_score -= 5 * player_2_block_moves

    # number of pieces in the middle column
    middle_col = len(board[0]) // 2
    player_1_middle_pieces = count_pieces(board, 1, middle_col)
    player_2_middle_pieces = count_pieces(board, 2, middle_col)
    player_1_score += player_1_middle_pieces
    player_2_score -= player_2_middle_pieces

    # difference in scores
    if (player == 1):
        return player_1_score - player_2_score
    elif (player ==2):
        return player_2_score - player_1_score 


# This function counts all possible opponent blocking moves. 
# Used by heuristics.
def count_block_moves(board, player):
    count = 0
    for row in range(len(board) - 3):
        for col in range(len(board[0])):
            if board[row][col] == 0 and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                count += 1
    for row in range(len(board)):
        for col in range(len(board[0]) - 3):
            if board[row][col] == 0 and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                count += 1
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if board[row][col] == 0 and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                count += 1
    for row in range(len(board) - 3):
        for col in range(3, len(board[0])):
            if board[row][col] == 0 and board[row+1][col-1] == player and board[row+2][col-2] == player and board[row+3][col-3] == player:
                count += 1
    return count

#This function counts the pieces of the requested player in the desired column.
def count_pieces(board, player, col):
    count = 0
    for row in range(len(board)):
        if board[row][col] == player:
            count += 1
    return count


# This function implements the minimax algorithm using the selected heuristic. 
# While creating the tree by determining the depth limit, 
# it recursively calculates the score and returns the last score and 
# the best move by returning to the node started with the minimax algorithm.
#  With the alpha-beta method, it does not open unnecessary parts and increases performance.
def alphabeta_aivsai(player,node, depth, h, alpha, beta, maximizingPlayer, best_move = None): #
    if depth == 0 or check_win2(node.map) == 1 or check_win2(node.map) == 2 :
        if (h == 1):
            return h1(node.map, player.id), best_move
        elif (h == 2):
            return h2(node.map, player.id), best_move
        elif ( h == 3):
            return h3(node.map, player.id), best_move
                

    if maximizingPlayer:
        value = float('-inf')
        for child in get_children(node,player):
            child_value, _ = alphabeta_aivsai(player,child, depth - 1,h, alpha, beta, False, best_move)
            if child_value > value:
                best_move = copy.deepcopy(child.map)
            value = max(value, child_value)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value, best_move    
    else:
        value = float('inf')
        for child in get_children(node,player):
            child_value, _  = alphabeta_aivsai(player,child, depth - 1,h, alpha, beta, True, best_move)
            if child_value < value:
                best_move = copy.deepcopy(child.map)
                #print("\nbesttt:")
                #print(child.map)
            value = min(value, child_value)
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value, best_move

# Same as other alpha beta minimax. 
# The only difference is that there is no player information.
def alphabeta(node,h, depth, alpha, beta, maximizingPlayer, best_move = None): #
    if depth == 0 or check_win2(node.map) == 1 or check_win2(node.map) == 2 :
        if (h == 1):
            return h1(node.map, 1), best_move
        elif (h == 2):
            return h2(node.map, 1), best_move
        elif ( h == 3):
            return h3(node.map, 1), best_move
        
                

    if maximizingPlayer:
        value = float('-inf')
        for child in get_children(node,player1):
            #child.print_board()
            child_value, _ = alphabeta(child,h, depth - 1, alpha, beta, False, best_move)
            #print(value,child_value)
            if child_value > value:
                best_move = copy.deepcopy(child.map)
                #print(child_value)
                #print("\nbesttt:")
                #print(child.map)
            value = max(value, child_value)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value, best_move    
    else:
        value = float('inf')
        for child in get_children(node,player2):
            #child.print_board()
            child_value, _  = alphabeta(child,h, depth - 1, alpha, beta, True, best_move)
            
            if child_value < value:
                best_move = copy.deepcopy(child.map)
                #print("\nbesttt:")
                #print(child.map)
            value = min(value, child_value)
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value, best_move



# This function starts with a while loop that counts 56 parts. 
# It then continues the loop by pulling the instant state from the
# end of the states list. In the loop, the 1st player or the 2nd player 
# plays depending on the number of turns. It updates the board by 
# receiving column input from the player and continues the loop. 
# At the end of the loop, it checks the win status with the check_win() function. 
# The cycle continues until the game is over or there is a draw.
def player_vs_player(states,player1,player2):
    turn = 0
    while turn != 56:
        current_state = states[len(states)-1]
        current_state.print_board()
        if(turn % 2 == 0): # turn player1
            print("\nTurn for Player 1")
            while True:
                move = input("Choose your column: ")
                if(move == "" or move == " "):
                    print("Wrong input.")
                    continue
                if(int(move) > 8 or int(move) < 1):
                    print("Wrong input.")
                else:    
                    checked_move = check_move(current_state,int(move))
                    if(checked_move) == False: 
                        print("Column has fullfilled. Try another column.") 
                        continue
                    else: break    
            new_map = copy.deepcopy(current_state.map)
            new_map[checked_move[0]][checked_move[1]] = 1
            new_state = State(new_map, turn, parent=current_state,plyrmove=player1)
            states.append(new_state)
        if(turn % 2 == 1): # turn player2
            print("\nTurn for Player 2")
            while True:
                move = input("Choose your column: ")
                if(move == "" or move == " "):
                    print("Wrong input.")
                    continue
                if(int(move) > 8 or int(move) < 1):
                    print("Wrong input.")
                else:    
                    checked_move = check_move(current_state,int(move))
                    if(checked_move) == False: 
                        print("Column has fullfilled. Try another column.") 
                        continue
                    else: break  
            new_map = copy.deepcopy(current_state.map)
            new_map[checked_move[0]][checked_move[1]] = 2
            new_state = State(new_map, turn, parent=current_state,plyrmove=player2)
            states.append(new_state)
        checked_win = check_win(new_state)
        if checked_win == 1:
            new_state.print_board()
            print("\nPlayer 1 won!!! on turn ",str(turn))
            return
        elif checked_win == 2:
            new_state.print_board()
            print("\nPlayer 2 won!!!  on turn ",str(turn))   
            return 
        turn += 1
    print("Tie")

        
# This function is the function that manages the game to be played 
# between the player and the AI. The only difference from the 
# player_vs_player() function is that one of the players is ai. 
# When it's ai's turn, alpha-beta minimax is applied and the best move 
# returned is played, then it's the player's turn.
def player_vs_bestai(depth_limit,heuristic1):
    player1 = Player(1, 21)
    player2 = Player(2, 21)
    if heuristic1 == "h1":
        ai1_h = 1
    elif heuristic1 == "h2":
        ai1_h = 2
    elif heuristic1 == "h3":
        ai1_h = 3
    turn = 0

    while turn != 56:
        current_state = states[len(states)-1]
        current_state.print_board()
        if(turn % 2 == 0):
            print("\nAI's turn")
            print("Please wait.... AI is thinking....")
            value, best_move = alphabeta(current_state, ai1_h,depth_limit, float('-inf'), float('inf'), True)
            if value == 0:
                moves = getAllMoves(current_state.map)
                move = random.choice(moves) # random 
                new_map = copy.deepcopy(current_state.map)
                new_map[move[0]][move[1]] = 1
                new_state = State(new_map, turn, parent=current_state,plyrmove=player1)
                states.append(new_state)
            elif best_move != None:
                new_map = copy.deepcopy(best_move)
                new_state = State(new_map, turn, parent=current_state,plyrmove=player1)
                states.append(new_state)
            else: 
                moves = getAllMoves(current_state.map)
                move = moves[0] # random 
                new_map = copy.deepcopy(current_state.map)
                new_map[move[0]][move[1]] = 1
                new_state = State(new_map, turn, parent=current_state,plyrmove=player1)
                states.append(new_state)
        else:
            print("\nHuman's turn")
            while True:
                move = input("Choose your column: ")
                if(move == "" or move == " "):
                    print("Wrong input.")
                    continue
                if(int(move) > 8 or int(move) < 1):
                    print("Wrong input.")
                else:    
                    checked_move = check_move(current_state,int(move))
                    if(checked_move) == False: 
                        print("Column has fullfilled. Try another column.") 
                        continue
                    else: break  
            new_map = copy.deepcopy(current_state.map)
            #print(checked_move)
            new_map[checked_move[0]][checked_move[1]] = 2
            new_state = State(new_map, turn, parent=current_state,plyrmove=player2)
            states.append(new_state)
        checked_win = check_win(new_state)
        #print(checked_win)
        if checked_win == 1:
            new_state.print_board()
            print("\nAI won!!! at turn ",str(turn))
            return
        elif checked_win == 2:
            new_state.print_board()
            print("\nHuman won!!!  at turn ",str(turn))   
            return 
        turn += 1
    print("Tie!!!")    

# This function works with the same logic as other game management 
# functions. The only difference is that both sides are AI. 
# After the minimax is applied on both sides, the AI makes the next move. 
# If any score could not be calculated (ie the endgame is not clear), 
# it performs a random move.
def ai_vs_ai(depth_limit, depth_limit2, heuristic1, heuristic2):
    player1 = Player(1, 28)
    player2 = Player(2, 28)
    ai1_h = 0
    ai2_h = 0
    if heuristic1 == "h1":
        ai1_h = 1
    elif heuristic1 == "h2":
        ai1_h = 2
    elif heuristic1 == "h3":
        ai1_h = 3

    if heuristic2 == "h1":
        ai2_h = 1
    elif heuristic2 == "h2":
        ai2_h = 2
    elif heuristic2 == "h3":
        ai2_h = 3
    
    turn = 0
    while turn != 56:
        current_state = states[len(states)-1]
        current_state.print_board()
        if(turn % 2 == 0):
            print("\nAI-1's ("+ heuristic1  +") turn")
            print("Please wait.... AI-1 is thinking....")
            value, best_move = alphabeta_aivsai(player1,current_state, depth_limit, ai1_h ,float('-inf'), float('inf'), True)
            if value == 0:
                print("test1")
                moves = getAllMoves(current_state.map)
                move = random.choice(moves) # random olabilir
                new_map = copy.deepcopy(current_state.map)
                new_map[move[0]][move[1]] = 1
                print(new_map)
                new_state = State(new_map, turn, parent=current_state,plyrmove=player1)
                states.append(new_state)
            elif best_move != None:
                print("test2")
                new_map = copy.deepcopy(best_move)
                new_state = State(new_map, turn, parent=current_state,plyrmove=player1)
                states.append(new_state)  
            else: 
                print("test3")
                moves = getAllMoves(current_state.map)
                move = moves[0] # random olabilir
                new_map = copy.deepcopy(current_state.map)
                new_map[move[0]][move[1]] = 1
                new_state = State(new_map, turn, parent=current_state,plyrmove=player1)
                states.append(new_state)
        else:
            print("\nAI-2's ("+ heuristic2  +") turn")
            print("Please wait.... AI-2 is thinking....")
            value, best_move = alphabeta_aivsai(player2,current_state, depth_limit2, ai2_h, float('-inf'), float('inf'), True)
            if value == 0:
                print("test-alt1")
                moves = getAllMoves(current_state.map)
                move = random.choice(moves) # random olabilir
                
                new_map = copy.deepcopy(current_state.map)
                new_map[move[0]][move[1]] = 2
                new_state = State(new_map, turn, parent=current_state,plyrmove=player2)
                states.append(new_state)
            elif best_move != None:
                print("test-alt2")
                new_map = copy.deepcopy(best_move)
                new_state = State(new_map, turn, parent=current_state,plyrmove=player2)
                states.append(new_state)
            else: 
                print("test-alt3")
                moves = getAllMoves(current_state.map)
                move = moves[0] # random olabilir
                new_map = copy.deepcopy(current_state.map)
                new_map[move[0]][move[1]] = 2
                new_state = State(new_map, turn, parent=current_state,plyrmove=player2)
                states.append(new_state)
        checked_win = check_win(new_state)
        #print(checked_win)
        if checked_win == 1:
            new_state.print_board()
            print("\nAI-1 won!!! at turn ",str(turn))
            return
        elif checked_win == 2:
            new_state.print_board()
            print("n\AI-2 won!!!  at turn ",str(turn))   
            return 
        turn += 1
    print("Tie!!!")    
        
while True:
    print("\\\\\\\\\\\CONNECT FOUR GAME///////////")
    print("1. Player vs Player \n2. Player vs AI \n3. AI vs AI")
    states  = [initial_state]
    heuristics = ["h1","h2","h3"]
    item = input("Select a game mode(1 to 4): ")
    if item == '1':
        player_vs_player(states,player1,player2)
    elif item == '2':
        while True:
            depth = input("Type a depth-limit for AI (only even numbers, ex: 4): ")
            heuristic = input("Select a heuristic for AI (h1, h2, h3): ")
            if(int(depth) % 2 == 0 and heuristic in heuristics):
                player_vs_bestai(int(depth),heuristic)
                break
            else:
                print("wrong input...")
                continue
    elif item == '3':
        
        while True:
            depth = input("Type a depth-limit for AI-1 (only even numbers): ")
            heuristic = input("Select a heuristic for AI-1 (h1, h2, h3): ")
            depth2 = input("Type a depth-limit for AI-2 (only even numbers): ")
            heuristic2 = input("Select a heuristic for AI-2 (h1, h2, h3): ")
            if(int(depth) % 2 == 0 and int(depth2) % 2 == 0 and (heuristic in heuristics) and (heuristic2 in heuristics)):
                ai_vs_ai(int(depth),int(depth2),heuristic,heuristic2)
                #player_vs_bestai(depth)
                break
            else:
                print("wrong input...")
                continue
