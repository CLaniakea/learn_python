def findMinAndMax(L):
    if not L:
        return (None,None)
    else:
        min = max = L[0]
        for it in L:
            if it < min:
                min=it
            elif it > max:
                max = it
    return (min,max)

L=[]
print(findMinAndMax(L))
L=[7]
print(findMinAndMax(L))
L=[7,1]
print(findMinAndMax(L))