from read_input import membaca_input, jarakEuclidian

# total cost for nodes visited
kamusBeban = membaca_input()


def Astar(start, goal):
    kamusHeuristic = buatkamusHeuristic(goal)
    cost = {start: 0}

    # OPEN SET
    opened = []
    # CLOSE SET
    closed = []
    # CURRENT PLACE
    current = start
    # ADD CURRENT TO OPEN 
    opened.append([current, kamusHeuristic[current]])
    while True:

        current = min(opened, key=lambda x: x[1])

        checked_node = current[0]
 
        closed.append(current)

        opened.remove(current)

        if (closed[-1][0] == goal):
            break

        for children in kamusBeban[checked_node].items():

            if children[0] in [closed_nodes[0] for closed_nodes in closed]:
                continue

            cost.update({children[0]: cost[checked_node] + children[1]})

            current_fval = cost[checked_node] + kamusHeuristic[children[0]] + children[1]

            temp = [children[0], current_fval]
            opened.append(temp)


    last_node = goal
    ordered_sequence = []
    ordered_sequence.append(goal)

    for i in range(len(closed) - 2, -1, -1):

        check_node = closed[i][0]

        if last_node in [children[0] for children in kamusBeban[check_node].items()]:
            if (cost[check_node] + kamusBeban[check_node][last_node] == cost[last_node]):
                ordered_sequence.append(check_node)
                last_node = check_node
    # Reverse ordering from ordered_sequence
    ordered_sequence.reverse()
    return ordered_sequence


def buatkamusHeuristic(goal):
    kamusHeuristic = dict()
    for nodes in kamusBeban:
        kamusHeuristic[nodes] = jarakEuclidian(nodes, goal)
    return kamusHeuristic
