def advanced_heuristic(curr_state):
    return 0
def base_heuristic(curr_state):
    """
    Returns: (My Moves) - (Opponent Moves)
    Assumes Player 1 (index 0) is the Maximizer.
    """
    p1_moves = count_available_moves(curr_state, 0)
    p2_moves = count_available_moves(curr_state, 1)
    print(f"heu res {p1_moves - p2_moves }")
    print(curr_state.get_grid())
    # FIXED: Calculates (P1 - P2). 
    # Positive result = Good for P1. Negative result = Good for P2.
    return p1_moves - p2_moves 

def count_available_moves(current_game, player_idx):
    """
    OPTIMIZED: Uses pre-calculated vectors instead of nested loops.
    """
    grid = current_game.get_grid()
    curr_location = current_game.get_player_locations()[player_idx + 1]
    print(f"player {player_idx+1} , location is {curr_location}")
    rows = len(grid)
    cols = len(grid[0])
    valid_moves_count = 0

    # OPTIMIZATION:
    # Instead of calculating loop ranges and checking abs() every time,
    # we just iterate over the 8 known legal Knight-move offsets.
    # This is significantly faster for the CPU.
    move_offsets = [
        (1, 2), (1, -2), (-1, 2), (-1, -2),
        (2, 1), (2, -1), (-2, 1), (-2, -1)
    ]

    for dr, dc in move_offsets:
        new_r = curr_location[0] + dr
        new_c = curr_location[1] + dc

        # Check Bounds
        if 0 <= new_r < rows and 0 <= new_c < cols:
            # Check Empty Spot
            if grid[new_r][new_c] == 0:
                valid_moves_count += 1
                    
    return valid_moves_count