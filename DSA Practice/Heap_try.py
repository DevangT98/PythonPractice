def min_heapify(A,i):
    smallest = i
    L = 2 * i + 1
    R = 2 * i + 2

    if (L <= len(A) - 1 and A[L] < A[smallest]):
        smallest = L
  
    if (R <= len(A) - 1 and A[R] < A[smallest]):
        smallest = R

    if (smallest != i):
        A[i],A[smallest] = A[smallest], A[i]
    
        min_heapify(A,smallest)



A = [5, 9 , 43, 22 , 45, 37, 1, 3, 2]

print(f"Array before min heapify is {A}")

lastNonLeafNode = (len(A)//2) - 1
for j in range(lastNonLeafNode,-1, -1):
        min_heapify(A,j)

print(f"Array after min heapify is {A}")

def heap_set_value(A,i,value):
    lastNonLeafNode = (len(A)//2) - 1
    
    print(f"Heap original value at index {i} = {A[i]}")
    A[i] = value 
    for j in range(lastNonLeafNode,-1, -1):
        min_heapify(A,j)
    
    print(f"Heap changed value at index {i} = {A[i]}")
    return A
print (f"Array after switching value and min heapify: {heap_set_value(A,5,4)}")


