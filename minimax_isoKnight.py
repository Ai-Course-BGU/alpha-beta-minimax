import math

def maximin(current_game , alpha =-math.inf,beta=math.inf):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = -math.inf
    moves = current_game.get_moves()
    print (f"Maximin evaluating {len(moves)} moves from \n{current_game.get_grid()}")
    for move in moves:
        
        mx, next_move = minimax(move,alpha,beta)
        # print(f"Maximin checking move \nfrom\n {current_game.get_grid()} \n to  \n{move.get_grid()}\n with value {mx}")
        if v < mx:
            v = mx
            best_move = move
        
    return v, best_move

def minimax(current_game,alpha=-math.inf,beta=math.inf):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = math.inf
    moves = current_game.get_moves()
    print (f"Minimax evaluating {len(moves)} moves from \n{current_game.get_grid()}")
    for move in moves:
        mx, next_move = maximin(move,alpha,beta)
        # print(f"Minimax checking move \n{move.get_grid()}\n with value {mx}")
        if v > mx:
            v = mx
            best_move = move
    print (f"Minimax best move chosen with value {v} from \n{current_game.get_grid()}")
    return v, best_move

