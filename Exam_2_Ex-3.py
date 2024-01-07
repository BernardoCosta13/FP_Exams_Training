def hasMine(listP, r, c):
    return 0 <= r < len(listP) and 0 <= c < len(listP[0]) and listP[r][c] == '#'

def neighbourMines(listP):
    dictMines = {}

    for r in range(len(listP)):
        for c in range(len(listP[0])):
            if listP[r][c] == '-':
                mines_count = 0
                positions = []

                # Check in all eight directions (horizontal, vertical, and diagonal)
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue

                        nr, nc = r + dr, c + dc
                        if hasMine(listP, nr, nc):
                            mines_count += 1
                            positions.append((nr, nc))

                if mines_count > 0:
                    dictMines.setdefault(mines_count, []).append((r, c))

    return dictMines

# Example usage:
listP = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

result = neighbourMines(listP)
print(result)
