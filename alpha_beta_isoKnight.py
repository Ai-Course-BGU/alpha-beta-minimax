import math

def alphabeta_max(current_game):
    return maximin(current_game)

def alphabeta_min(current_game):
    return minimax(current_game)

def maximin(current_game, alpha=-math.inf, beta=math.inf):
    if current_game.is_terminal():
        return current_game.get_score(), None
    
    v = -math.inf
    best_move = None # <--- FIX 1: Initialize this to prevent crash
    moves = current_game.get_moves()
    
    for move in moves:
        mx, next_move = minimax(move, alpha, beta)
        
        if v < mx:
            v = mx
            best_move = move
            # Alpha update is correct here
            alpha = max(alpha, v) 
        
        # <--- FIX 2: Use >= for better pruning efficiency
        if v >= beta:
            return v, None 
            
    return v, best_move

def minimax(current_game, alpha=-math.inf, beta=math.inf):
    if current_game.is_terminal():
        return current_game.get_score(), None
    
    v = math.inf
    best_move = None # <--- FIX 1: Initialize this to prevent crash
    moves = current_game.get_moves()
    
    for move in moves:
        mx, next_move = maximin(move, alpha, beta)

        if v > mx:
            v = mx
            best_move = move
            # Beta update is correct here
            beta = min(beta, v) 
        
        # <--- FIX 2: Use <= for better pruning efficiency
        if v <= alpha:
            return v, None
            
    return v, best_move