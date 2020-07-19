# The value at the i, jth index is the cost. 
port_costs = [
[0, 1, 25, 1],
[0, 0, 4, 15],
[0, 0, 0, 5],
[0, 0, 0, 0],
]

# 4 nodes
# 0,1 = 1
# 0,2 = 2
# 0,3 = 5

# 1,2 = 5

print (port_costs[0][3])
cheapests = [-1] * len(port_costs) 
cheapests[0] = 0
route = [-1]* len(port_costs)
def get_cheapest_travel(target):
    # The cost to port 1 is the cost to port 0 + the cost of 0 - 1
    # The cost of port 2 is either
    # - The cost to port 0, then from 0 to 2 
    # - The cost to port 1, then from 1 to 2
    if cheapests[target] != -1:
        return cheapests[target]
    max_cost = 10000
    if target == 0: # The cheapest cost to port 0 is 0
        return 0
    for j in range (0, target):
        cost = get_cheapest_travel(j) + port_costs[j][target]
        if cost < max_cost:
            max_cost = cost
            max_port = j
    cheapests[target] = max_cost
    route[target] = max_port
    return max_cost


def construct_path():
    seen = []
    for step in route:
        if step in seen:
            continue
        print(str(step) + " -> ")
        seen.append(step)

    print(len(port_costs))


get_cheapest_travel(3)

print("The cheapest path is " + str(cheapests))
print(construct_path())

