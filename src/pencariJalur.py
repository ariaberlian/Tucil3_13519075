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
        node_dikunjungi = current[0]
        closed.append(current)
        opened.remove(current)

        if (closed[-1][0] == goal):
            break
        for anak in kamusBeban[node_dikunjungi].items():
            if anak[0] in [closed_nodes[0] for closed_nodes in closed]:
                continue
            cost.update({anak[0]: cost[node_dikunjungi] + anak[1]})
            current_fval = cost[node_dikunjungi] + kamusHeuristic[anak[0]] + anak[1]
            temp = [anak[0], current_fval]
            opened.append(temp)

    last_node = goal
    alur_terpendek = []
    alur_terpendek.append(goal)

    for i in range(len(closed) - 2, -1, -1):
        check_node = closed[i][0]
        if last_node in [anak[0] for anak in kamusBeban[check_node].items()]:
            if (cost[check_node] + kamusBeban[check_node][last_node] == cost[last_node]):
                alur_terpendek.append(check_node)
                last_node = check_node
    alur_terpendek.reverse()
    return alur_terpendek


def buatkamusHeuristic(goal):
    kamusHeuristic = dict()
    for nodes in kamusBeban:
        kamusHeuristic[nodes] = jarakEuclidian(nodes, goal)
    return kamusHeuristic
