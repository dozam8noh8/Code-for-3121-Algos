T = [[-1 for i in range (0,100)] for j in range(0,100)]
F = [[-1 for i in range (0,100)] for j in range(0,100)]
#print(T)
# for i in range (0, len(T)):
#     for j in range(0, len(F)):

def get_true(string,nothing):
    nOps = len(string)//2
    nBools = len(string)//2 + 1
    print("Number of booleans is " + str(nBools))
    print("String is " + string)
    # Since all diagonals of a the array represent a single boolean expression (either T or F)
    # We set these to their corresponding values so we can use them to calculate other values.
    for i in range(0,nBools, 1): #Only every 2 chars are T or F because we have operators!
        if string[i*2] == "T": # i*2 because only every second char in string is bool
            T[i][i] = 1
            F[i][i] = 0
        elif string[i*2] == "F":
            T[i][i] = 0
            F[i][i] = 1  

    print(T[1][1])
    # Just trying to get for [0][0...n]

    # if op == "|"
    # T[0][2] = T[0][0] * T[2][2] + T[0][0] * F[2][2] + F[0][0] + T[2][2]
    # T[0][4] = T[0][2] + T[4][4]
    # T[0][6] = T[0][4] + T[6][6]

    # There are n chars in a string and n-1 operators

    ## OWEN, we want to calculate them with gap in the outer loop
    ## [0][1], [1][2],[2][3] (these are the first possible values we can calculate)

    # gap is gap between i and j. We must split at 
    for gap in range(1,nBools):
        #if i == nBools break?

        # We want j and i changing at the same time. since we're going 0,1 1,2, 2,3 so on
        i = 0
        # j is going to stay equidistant from i (as far as gap)
        # more intuitive to think of j = i + gap
        for i in range(0, nBools): # Start from i+1 because we've already done the diagonals.
            j = i+gap
            if j >= nBools: # OWEN LOOK HERE!
                continue
            # range i, j is essentially gap...
            T[i][j] = 0
            F[i][j] = 0 # initialise these since we don't want them to be negative 1 if there are no ways to do things.
            for split_at in range(i, j): # after how many after i and before j do we want to split the expr into.
                #for split_at in range(i,j):

                opIndex = 1+ split_at* 2
                print("i, j is : " + str((i,j)) + " --- splitting at " + str(opIndex))
                print("Split into lower " + str((i, split_at)) + " " + str(T[i][split_at]) + ", upper " + str((split_at+1, j)) + " " +  str(T[split_at+1][j]) )
                op = string[opIndex] # The operators start at 1 and will occur every two characters
                print("OP is " + str(op))

                if op == "|":
                    T[i][j] += (T[i][split_at] * F[split_at+1][j])
                    T[i][j] += (F[i][split_at] * T[split_at+1][j])
                    T[i][j] += (T[i][split_at] * T[split_at+1][j])

                    F[i][j] += (F[i][split_at] * F[split_at+1][j])

                elif op == "&":
                    T[i][j] += (T[i][split_at] * T[split_at+1][j])

                    F[i][j] += (T[i][split_at] * F[split_at+1][j])
                    F[i][j] += (F[i][split_at] * T[split_at+1][j])
                    F[i][j] += (F[i][split_at] * F[split_at+1][j])


                elif op == "^":
                    T[i][j] += (T[i][split_at] * F[split_at+1][j])
                    T[i][j] += (F[i][split_at] * T[split_at+1][j])

                    F[i][j] += (T[i][split_at] * T[split_at+1][j])
                    F[i][j] += (F[i][split_at] * F[split_at+1][j])

                print("T[i][j] is " +  str(T[i][j]))
                print("F[i][j] is " +  str(F[i][j]))
    return T[0][nBools-1]

  
## RECURSIVE SOLUTION
# def get_true(string, rang, isTrue=1):
#     # odd indices will be operators (assuming we start with a boolean value)
#     # the number of ways a string is true depends on the number of ways
#     # two strings split at an operator is true, depending on that operator
#     # e.g. number of ways "True and True or True" is the number of ways of 
#     # True and (True or True) is true + number of ways (True and True) or True is true.
#     # And because the operator is an "and" for the first equation. 
#     # The left and right hand side must be true. So we solve the sub equation
#     #print("STRING IS " + string)
#     low = rang[0]
#     hi = rang[1]
#     target = string[low:hi+1]
#     length = len(target)
    
#     if target == "T":
#         T[low][hi] = 1
#         F[low][hi] = 0
#     elif target == "F":
#         F[low][hi] = 1
#         T[low][hi] = 0
    
#     if isTrue:
#         if T[low][hi] != -1:
#             return T[low][hi]
#     elif not isTrue:
#         if F[low][hi] != -1:
#             return F[low][hi]
#     # Go through all operators. 
#     # Pick operator, split into LHS eqn and RHS eqn.
#     ntrue = 0
#     nfalse = 0





#s = "T|F|T"
# tup = (0,len(s)-1)
# print(      get_true(s, tup)         )
# print("\n\n\n")
# s = "T|T&F^T"
# tup = (0,len(s)-1)
# print(      get_true(s, tup)         )
# print("\n\n\n")
s = "T&T|F|F^F^T^T^T&T^F^T&F|F^F^F&F&F|F|F^F^T|T&T"
tup = (0,len(s)-1)
print(      get_true(s, tup) % 1003      )

#code
# queries = int(input("How many queries? "))
# for i in range (0,queries):
#     length = int(input("Length of input string? "))
#     string = input("string: ")
#     res = get_true(string)
#     print(res)