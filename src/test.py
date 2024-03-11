def dot(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res
        
def T(A):
    res = []
    for i in range(len(A[0])):
        res.append([])
        for j in range(len(A)):
            res[-1].append(A[j][i])
    # print(res)
    return res

def array_mult(A, B):
    B_T = T(B)
    C = []
    
    for y in range(len(A)):
        C.append([])
        for x in range(len(B_T)):
            C[-1].append(dot(A[y], B_T[x]))
    
    return C

M1 = [[1, 2, 3], [-2, 3, 7]]
M2 = [[1,0,0],[0,1,0],[0,0,1]]
print(array_mult(M1, M2))

M3 = [[1], [0], [-1]]
# print(M1)
print(array_mult(M1, M3))