N, M = map(int, input().split())
for i in range(N): #iterasi baris
    for j in range(N): #iterasi kolom
        if (i < M or i >= N - M or j < M or j >= N - M):
            print('*', end='')
        else:
            print(' ', end='')
    print()