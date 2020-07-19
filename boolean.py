T = [[-1 for i in range (0,100)] for j in range(0,100)]
F = [[-1 for i in range (0,100)] for j in range(0,100)]
#print(T)
# for i in range (0, len(T)):
#     for j in range(0, len(F)):

def get_true(string, rang, isTrue=1):
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
        F[low][hi] = 0
    elif target == "F":
        F[low][hi] = 1
        T[low][hi] = 0
    
    if isTrue:
        if T[low][hi] != -1:
            return T[low][hi]
    elif not isTrue:
        if F[low][hi] != -1:
            return F[low][hi]
    # Go through all operators. 
    # Pick operator, split into LHS eqn and RHS eqn.
    ntrue = 0
    nfalse = 0





    for i in range (low+ 1, hi+1, 2):

        op = string[i]
        lhs = (low,i-1)
        rhs = (i+1, hi)

        if op == "|":
            if isTrue:
                ntrue += get_true(string, lhs) * get_true(string, rhs)
                ntrue += get_true(string, lhs) * get_true(string, rhs, 0)
                ntrue += get_true(string, lhs, 0) * get_true(string, rhs)
            if not isTrue:
                nfalse += get_true(string, lhs, 0) * get_true(string, rhs, 0)
        elif op == "^":
            if isTrue:
                ntrue += get_true(string, lhs) * get_true(string, rhs, 0)
                ntrue += get_true(string, lhs, 0) * get_true(string, rhs)
            if not isTrue:
                nfalse += get_true(string, lhs) * get_true(string, rhs)
                nfalse += get_true(string, lhs, 0) * get_true(string, rhs, 0)
        elif op == "&":
            if isTrue:
                ntrue += get_true(string, lhs) * get_true(string, rhs)
            elif not isTrue:
                nfalse += get_true(string, lhs, 0) * get_true(string, rhs)
                nfalse += get_true(string, lhs) * get_true(string, rhs, 0)
                nfalse += get_true(string, lhs, 0) * get_true(string, rhs, 0)

    if isTrue:
        T[low][hi] = ntrue
        return ntrue
    elif not isTrue:
        F[low][hi] = nfalse
        return nfalse


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