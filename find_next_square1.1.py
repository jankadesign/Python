
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    root = sq**0.5
    if root.is_integer():
        return (root+1)**2
    else: return -1

print find_next_square(15)