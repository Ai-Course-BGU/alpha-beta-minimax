import math
h = None


def alphabeta_max_h(current_game, _heuristic, depth=3):
    global h
    h = _heuristic
    
    return maximin(current_game,depth,-math.inf,math.inf)
    pass


def alphabeta_min_h(current_game, _heuristic, depth=3):
    global h
    h = _heuristic
    # add code here
    return minimax(current_game,depth,-math.inf,math.inf)
import math


def maximin(current_game, depth, alpha, beta):
    if current_game.is_terminal():
        return current_game.get_score(), None
    global h
    # Heuristic Check
    if depth == 0:
        val = h(current_game)
        # Optional: print(f"Max Heuristic: {val} \n{current_game.get_grid()}")
        return val, None

    v = -math.inf
    best_move = None # FIXED: Safety initialization
    moves = current_game.get_moves()
    
    for move in moves:
        # Pass h_func down
        mx, next_move = minimax(move, depth - 1, alpha, beta)
        
        if v < mx:
            v = mx
            best_move = move
            alpha = max(alpha, v)
        
        # Pruning
        if v >= beta:
            return v, None 
            
    return v, best_move

def minimax(current_game, depth, alpha, beta):
    if current_game.is_terminal():
        return current_game.get_score(), None
    global h
    # Heuristic Check
    if depth == 0:
        val = h(current_game)
        # Optional: print(f"Min Heuristic: {val} \n{current_game.get_grid()}")
        return val, None

    v = math.inf
    best_move = None # FIXED: Safety initialization
    moves = current_game.get_moves()
    
    for move in moves:
        # Pass h_func down
        mx, next_move = maximin(move, depth - 1, alpha, beta)
        
        if v > mx:
            v = mx
            best_move = move
            beta = min(beta, v)
        
        # Pruning
        if v <= alpha:
            return v, None

    return v, best_move
