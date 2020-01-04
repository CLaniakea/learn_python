# import os
# print([d for d in os.listdir('.')])

L1 = ['Hello', 'World', 18, 'Apple', None]
# way 1
'''
L2=[]
for it in L1:
    if isinstance(it,str):
        L2.append(it.lower())
'''
# way 2
#L2=[s.lower() for s in L2]

# way 3
L2=[it.lower() for it in L1 if isinstance(it,str)]
print(L2)