def increment(arr, m):
    i = 0
    while i < m and arr[i] == 1:
        arr[i] = 0
        i+=1
    if i < m:
        arr[i] = 1


arr = [0,0,0]
m = 3

print("Array before increment function:", arr, end ="\n" )

for i in range(1, pow(2,m)+1):
    increment(arr,m)
    print(f"Array at {i} increment: {arr}" )


print("Array after increment function:", arr, end ="\n" )

