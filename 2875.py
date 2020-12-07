N, M, K = map(int, input().split())
N_d = N % 2
N = int(N/2)
if N>M:
    K -= 2*(N-M)
    N = M
elif N<M:
    K -= (M-N)
    M = N
K -= N_d
while(K>0):
    if K>0:
        K -= 3
        N -= 1
        M -= 1
if N<M:
    print(N)
else:
    print(M)