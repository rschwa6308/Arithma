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
    # print('get_value called on subpipe: ', subpipe)
    num_count = 0   # running tally of num of consecutive numbers
    try:
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
            else:
                num_count += 1
                if num_count >= 2:
                    return None
        return subpipe[0]
    except Exception:
        return None


# takes a list of pieces and returns success bool
def check(pieces):
    # initial checks
    for piece in pieces:
        # all on board
        if piece.grid[0] > 9:
            # print("not all on board")
            return False

        # all have at least 1 neighbor
        if len(get_neighbors(pieces, piece)) == 0:
            # print("not all have neighbors")
            return False

        # all "="s have an even number of neighbors
        if piece.data == "=":
            if len(get_neighbors(pieces, piece)) % 2 == 1:
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
        # print(p.data)

    # analyze pipe
    n = pipe_data.index("=")
    left = pipe_data[:n]
    right = pipe_data[n + 1:]
    right.reverse()  # operate towards "="

    try:
        # print(left)
        # print(get_value(left))
        # print("")
        # print(right)
        # print(get_value(right))

        return get_value(left) == get_value(right)

    except:
        # print("error")
        return False


# takes a list of pieces and returns success bool using scrabble-style rules
def check_scrabble(pieces):
    # initial checks
    for piece in pieces:
        # all on board
        if piece.grid[0] > 9:
            # print("not all on board")
            return False

        # all have at least 1 neighbor
        if len(get_neighbors(pieces, piece)) == 0:
            # print("not all have neighbors")
            return False

        # all "="s have an even number of neighbors
        if piece.data == "=":
            if len(get_neighbors(pieces, piece)) % 2 == 1:
                return False

    # build grid
    board = [[None for _ in range(10)] for _ in range(10)]
    for piece in pieces:
        board[piece.grid[1]][piece.grid[0]] = piece

    for piece in pieces:
        if piece.data == "=":

            # check row
            pos = list(piece.grid)
            left = []
            while pos[0] >= 0 and board[pos[1]][pos[0]]:
                left.append(board[pos[1]][pos[0]].data)
                pos[0] -= 1
            left.pop(0)
            left.reverse()

            pos = list(piece.grid)
            right = []
            while pos[0] <= 9 and board[pos[1]][pos[0]]:
                right.append(board[pos[1]][pos[0]].data)
                pos[0] += 1
            right.pop(0)

            if len(left) > 0 and len(right) > 0:
                if get_value(left) != get_value(right):
                    # print("left and right disagree")
                    return False
            else:
                # if exactly one side is missing, fail
                if max(len(left), len(right)) > 0:
                    return False

            # check column
            pos = list(piece.grid)
            top = []
            while pos[1] >= 0 and board[pos[1]][pos[0]]:
                top.append(board[pos[1]][pos[0]].data)
                pos[1] -= 1
            top.pop(0)
            top.reverse()

            pos = list(piece.grid)
            bottom = []
            while pos[1] <= 9 and board[pos[1]][pos[0]]:
                bottom.append(board[pos[1]][pos[0]].data)
                pos[1] += 1
            bottom.pop(0)

            if len(top) > 0 and len(bottom) > 0:
                if get_value(top) != get_value(bottom):
                    # print("top and bottom disagree")
                    return False
            else:
                # if exactly one side is missing, fail
                if max(len(top), len(bottom)) > 0:
                    return False

    return True
