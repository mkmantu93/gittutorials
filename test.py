def solution(buckets):
    n = len(buckets)
    ball_positions = [i for i in range(n) if buckets[i] == 'B']  # Track ball positions
    ball_count = len(ball_positions)  # Count of balls

    # Check if arrangement is possible
    if ball_count > (n + 1) // 2:
        return -1

    min_moves = n  # Initialize with a high number (more than max possible moves)
    # Check starting positions for the alternating pattern
    for start in range(n - 2 * ball_count + 2):
        current_moves = 0
        for j in range(start, start + 2 * ball_count, 2):
            if j not in ball_positions:
                current_moves += 1  # Count how many moves needed
        min_moves = min(min_moves, current_moves)  # Update minimum moves

    return min_moves

# Example tests
# Uncomment these lines for testing
# print(solution("..B....B.BB"))  # Expected output: 2
# print(solution("BB.B.BBB..."))  # Expected output: 4
# print(solution(".BBB.B"))       # Expected output: -1
# print(solution("......B.B"))    # Expected output: 0
