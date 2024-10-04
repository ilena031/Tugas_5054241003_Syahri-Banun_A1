# number of elements
N = int(input())
# array A
A = list(map(int, input().split()))
# array B
B = list(map(int, input().split()))
#amount of l,r
T = int(input())
# Process each
results = []
for _ in range(T):
    l, r = map(int, input().split()) #index array
    
    # Calculate sums for the subarrays 
    sum_A = 0
    for i in range (l,r+1):
        sum_A += A[i]
    sum_B = 0 
    for i in range (l,r+1) :
        sum_B += B[i]
    
    # Compare the sums
    if sum_A == sum_B:
        print("YA")
    else:
        print("TIDAK")


