"""
    Barry Barron
    Principles of Computing 7/2016 Week 1, Mini-project 1
    Merge function for 2048 game
    CodeSkulpter link http://www.codeskulptor.org/#user41_J1T44jaXXX_2.py
"""
def merge(line):
    """
    Function that merges a single row or column in 2048
    """
    original_length = len(line)
    empty_space = 0 # set empty cells to zero

    # slide all tiles towards the front (left or top) by removing empty spaces (zero values)
    while empty_space in line:
        line.remove(empty_space)

    for tile in xrange(len(line)):
        # arrived at the end of list
        if tile + 1 > len(line) - 1:
            break
        # merge pair of eligible neighbors
        if line[tile] == line[tile + 1]:
            line[tile] *= 2
            del line[tile + 1]
            line.insert(tile + 1, empty_space)

    # slide all the tiles towards the front and fill the rest with zeros
    while empty_space in line:
        line.remove(empty_space)
    while len(line) != original_length:
        line.append(empty_space)

    return line

# Test code with given sample data
print merge([2,0,2,4])
print merge([0,0,2,2])
print merge([2,2,0,0])
print merge([2,2,2,2,2])
print merge([8,16,16,8])
print merge ([8,8])
