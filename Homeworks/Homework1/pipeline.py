nodes = resevoir + houses
min_costs = [-1] * float("inf")
w = 1
c = 1

def get_min_cost(nodes):
    if len(nodes) == 1:
        return 0 
    if min_costs[nodes[0]] == float("inf"):
        for i in range(len(nodes)):
            min_costs[nodes[0]] = min(c * line_fit(nodes[0:i]) + w + get_min_cost(nodes[i + 1:len(nodes)]))
        else:
            return min_costs[nodes[0]]

    return min_costs[nodes[0]]