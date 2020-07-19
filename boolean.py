T = [0] * 1000
F = [0] * 1000
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
        return 1
    if target == "F":
        return 0
    
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
            print("OP IS ^")
            tmp = get_true(string, lhs) * get_false(string, rhs)
            print("Range is: " + str(rang) + " TMP = " + str(tmp))
            print(lhs)
            print(rhs)
            ntrue += tmp
            ntrue += get_false(string, lhs) * get_true(string, rhs)
        elif op == "&":
            # AND - This is only true when both are true, so we must multiply them.
            # If there are 3 ways on left and 0 on right, there are 0 ways.
            # If there are 3 ways on left and 2 on right, there are 6 ways.
            ntrue += get_true(string, lhs) * get_true(string, rhs)
        if ntrue > 0:
            #pass
            print("n true is non 0, adding total true to ntrue:" + str(total_true) + str(ntrue))
        total_true += ntrue
    #print(total_true)
    return total_true
 
 
def get_false(string, rang):
    low = rang[0]
    hi = rang[1]
    target = string[low:hi+1]
    #print("TARGET IS " + target)
    length = len(target)
    if target == "T":
        return 0
    if target == "F":
        return 1
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
        if nfalse > 0:
            #pass
            print("n true is non 0, adding total true to nfalse:" + str(total_false) + str(nfalse))
        total_false += nfalse
    #print(total_false)
    return total_false



# s = "T|F|T"
# tup = (0,len(s)-1)
# print(      get_true(s, tup)         )
# print("\n\n\n")
# s = "T|T&F^T"
# tup = (0,len(s)-1)
# print(      get_true(s, tup)         )
# print("\n\n\n")
s = "T|T&F^T"
tup = (0,len(s)-1)
print(      get_true(s, tup)         )

#code
# queries = int(input("How many queries? "))
# for i in range (0,queries):
#     length = int(input("Length of input string? "))
#     string = input("string: ")
#     res = get_true(string)
#     print(res)