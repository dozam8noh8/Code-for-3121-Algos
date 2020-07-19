T = [[-1 for i in range (0,100)] for j in range(0,100)]
F = [[-1 for i in range (0,100)] for j in range(0,100)]
#print(T)
# for i in range (0, len(T)):
#     for j in range(0, len(F)):

def get_true(string, rang):
    # odd indices will be operators (assuming we start with a boolean value)
    # the number of ways a string is true depends on the number of ways
    # two strings split at an operator is true, depending on that operator
    # e.g. number of ways "True and True or True" is the number of ways of 
    # True and (True or True) is true + number of ways (True and True) or True is true.
    # And because the operator is an "and" for the first equation. 
    # The left and right hand side must be true. So we solve the sub equation
    #print("STRING IS " + string)
    low = rang[0]
    hi = rang[1]
    target = string[low:hi+1]
    length = len(target)
    if target == "T":
        T[low][hi] = 1
        return 1
    if target == "F":
        T[low][hi] = 0
        return 0
    
    if T[low][hi] != -1:
        return T[low][hi]
    # Go through all operators. 
    # Pick operator, split into LHS eqn and RHS eqn.
    total_true = 0
    for i in range (low+ 1, hi+1, 2):
        #print("calling " + msg)
        #print("Operator is " + str(string[i]))
        op = string[i]
        lhs = (low,i-1)
        rhs = (i+1, hi)
        ntrue = 0
        if op == "|":
            # OR
            # Total lhs + rhs - (False LHS * FALSE RHS)
            # True LHS * False RHS) + False LHS * True RHS ) + (True LHS * True RHS)
            ntrue += get_true(string, lhs) * get_true(string, rhs)
            ntrue += get_true(string, lhs) * get_false(string, rhs)
            ntrue += get_false(string, lhs) * get_true(string, rhs)
        elif op == "^":
            # XOR
            # True LHS * False RHS + ( False LHS * True RHS )
            ntrue += get_true(string, lhs) * get_false(string, rhs)
            ntrue += get_false(string, lhs) * get_true(string, rhs)
        elif op == "&":
            # AND - This is only true when both are true, so we must multiply them.
            # If there are 3 ways on left and 0 on right, there are 0 ways.
            # If there are 3 ways on left and 2 on right, there are 6 ways.
            ntrue += get_true(string, lhs) * get_true(string, rhs)
        total_true += ntrue
    #print(total_true)
    T[low][hi] = total_true
    return total_true
 
 
def get_false(string, rang):
    low = rang[0]
    hi = rang[1]
    target = string[low:hi+1]
    length = len(target)
    if target == "T":
        F[low][hi] = 0
        return 0
    if target == "F":
        F[low][hi] = 1
        return 1

    if F[low][hi] != -1:
        return F[low][hi]
    # Go through all operators. 
    # Pick operator, split into LHS eqn and RHS eqn.
    total_false = 0
    for i in range (low + 1, hi+1, 2):
        #print("calling " + "get_false")
        #print("Operator is " + str(string[i]))
        op = string[i]
        lhs = (low,i-1)
        rhs = (i+1, hi)
        nfalse = 0
        if op == "|":
            nfalse += get_false(string, lhs) * get_false(string, rhs)

        elif op == "^":
            # XOR
            # True LHS * False RHS + ( False LHS * True RHS )
            nfalse += get_true(string, lhs) * get_true(string, rhs)
            nfalse += get_false(string, lhs) * get_false(string, rhs)
        elif op == "&":
            # AND - This is only true when both are true, so we must multiply them.
            # If there are 3 ways on left and 0 on right, there are 0 ways.
            # If there are 3 ways on left and 2 on right, there are 6 ways.
            nfalse += get_false(string, lhs) * get_true(string, rhs)
            nfalse += get_true(string, lhs) * get_false(string, rhs)
            nfalse += get_false(string, lhs) * get_false(string, rhs)
        total_false += nfalse
    F[low][hi] = total_false
    return total_false



# s = "T|F|T"
# tup = (0,len(s)-1)
# print(      get_true(s, tup)         )
# print("\n\n\n")
# s = "T|T&F^T"
# tup = (0,len(s)-1)
# print(      get_true(s, tup)         )
# print("\n\n\n")
s = "T&T|F|F^F^T^T^T&T^F^T&F|F^F^F&F&F|F|F^F^T|T&T"
tup = (0,len(s)-1)
print(      get_true(s, tup)  % 1003       )

#code
# queries = int(input("How many queries? "))
# for i in range (0,queries):
#     length = int(input("Length of input string? "))
#     string = input("string: ")
#     res = get_true(string)
#     print(res)