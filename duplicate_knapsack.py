
""" HITS MAX RECURSION DEPTH, LETS TRY BOTTOM UP"""
max_values = [-1]* 10000
max_values[0] = 0
# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    print(k, arr)
    if k <= 0:
        return 0
    return find_max(k, arr)

def find_max(target_weight, item_weights):
    max = -1
    if target_weight == 0:
        return 0
 
    for i, weight in enumerate(item_weights):
        if weight > target_weight:
            continue
        if max_values[target_weight - weight] != -1: # We have a memoized value
             potential_max = max_values[target_weight  - weight]+ weight
        else:
            potential_max = find_max(target_weight - weight, arr) + weight
        if i == 0: 
            max = potential_max
        elif potential_max > max:
            max = potential_max      

    #print("Target weight is " + str(target_weight) + "  max is" + str(max)) 
    if max == -1:
        max = 0
    max_values[target_weight] = max # At the end of looping through everything, we have found the max.

    return max









# item_weights = [1, 2,  3,  4,  5]
# item_values = [10, 30, 70, 50, 60 ]

# max_weight = 7
# max_values = [-1] * max_weight
# def find_max(target_weight):
#     max = -1
#     if target_weight == 0:
#         return 0


#     # Max weight is max weight with 
#     for i, (weight, value) in enumerate(zip(item_weights, item_values)):
#         #print("Weight is " + str(weight) + "value is " + str(value))
#         if weight > target_weight:
#             continue
#         if max_values[target_weight - weight - 1] != -1: # We have a memoized value
#             potential_max = max_values[target_weight  - weight - 1]
#         else:
#             potential_max = find_max(target_weight - weight) + value
#         if potential_max > max:
#             max = potential_max      

  
#     max_values[target_weight-1] = max # At the end of looping through everything, we have found the max.
#     return max
# print(find_max(max_weight))
# print(max_values)

