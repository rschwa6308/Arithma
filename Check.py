# check board


# takes a list of pieces and one piece within the list and returns #of neighbors it has
def get_neighbors(pieces, piece):
    neighbors = []
    for rest in pieces:  # lol rip
        if max(abs(piece.grid[0] - rest.grid[0]), abs(piece.grid[1] - rest.grid[1])) == 1 and abs(
                piece.grid[0] - rest.grid[0]) != abs(piece.grid[1] - rest.grid[1]):
            neighbors.append(rest)
    return neighbors


# takes a subpipe (left or right) and returns arithmetic value
def get_value(subpipe):
    for n in range(len(subpipe)):
        if subpipe[n] == "+":
            total = subpipe[n - 1] + subpipe[n + 1]
            post = subpipe[3:]
            post.insert(0, total)
            return get_value(post)
        elif subpipe[n] == u"×":
            total = subpipe[n - 1] * subpipe[n + 1]
            post = subpipe[3:]
            post.insert(0, total)
            return get_value(post)
        elif subpipe[n] == "-":
            total = subpipe[n - 1] - subpipe[n + 1]
            post = subpipe[3:]
            post.insert(0, total)
            return get_value(post)
        elif subpipe[n] == u"÷":
            total = float(subpipe[n - 1]) / float(subpipe[n + 1])
            post = subpipe[3:]
            post.insert(0, total)
            return get_value(post)
        elif subpipe[n] == "^":
            total = subpipe[n - 1] ** subpipe[n + 1]
            post = subpipe[3:]
            post.insert(0, total)
            return get_value(post)
    return subpipe[0]


# takes a list of pieces and returns success bool
def check(pieces):
    # initial checks
    for piece in pieces:
        # all on board
        if piece.grid[0] > 9:
            print("not all on board")
            return False

        # all have at least 1 neighbor
        if len(get_neighbors(pieces, piece)) == 0:
            print("not all have neighbors")
            return False

    # assemble pipe
    pipe = []
    for piece in pieces:
        if len(get_neighbors(pieces, piece)) == 1:
            pipe.append(piece)
            break

    for i in range(len(pieces) - 1):
        pipe.extend(get_neighbors(pieces, pipe[len(pipe) - 1]))
        pieces = [x for x in pieces if x not in pipe]

    pipe_data = []

    for p in pipe:
        pipe_data.append(p.data)
        print(p.data)

    # analyze pipe
    n = pipe_data.index("=")
    left = pipe_data[:n]
    right = pipe_data[n + 1:]
    right.reverse()  # operate towards "="

    try:
        print(left)
        print(get_value(left))
        print("")
        print(right)
        print(get_value(right))

        return get_value(left) == get_value(right)

    except:
        print("error")
        return False
