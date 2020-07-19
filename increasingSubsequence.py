
test1 = [1,2,3,4,5]
test2 = [22,13, 15, 1000,1001,1002,10003,10004, 77, 18, 199, 205, 65, 66,67]
def increasing(arr):
    print("Starting subsequences")
    global subsequences
    subsequences = [0] * len(arr)
    #print(subsequences)
    subsequences[0] = 1
    findMaxSubsequence(arr)
    print("Subsequences were -> ", subsequences)
    return max(subsequences)



def findMaxSubsequence(arr):
    # Find all subsequences size < length - 1 that have last value <= arr[length-1]
    if subsequences[len(arr)-1]: # If we already have a result stored in our array.
        print("Returning early, we already have a value here")
        return subsequences[len(arr)-1]
    length = len(arr)
    #print(length)
    for i in range (0, length-1):
# If the subsequence at [i-1] ends with a number less than the current number being looked at.
            if findMaxSubsequence(arr[0:i+1]) > subsequences[length-1] and arr[i] <= arr[length-1]: # If that subsequence is > than the current max value, update it.
                subsequences[length-1] = subsequences[i]
    
    subsequences[length-1] += 1 # Add one for the actual element that we have at that index.
    print(subsequences[length-1])
    return subsequences[length-1]

#print(increasing(test1))
print(increasing(test2))