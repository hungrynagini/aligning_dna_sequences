import math
import time


def greedy(str1, str2, mat=4, mis=-2, ind=-4, X):
    M = len(str1) - 1
    N = len(str2) - 1
    i = 0
    S_ = lambda i, j, d: ((i + j) * mat / 2) - d * (mat - mis)
    R = [[-math.inf for i in range(max(M, N)+1)] for j in range(max(M, N)+1)]
    T = [None for i in range(max(M, N)+1)]
    while i < min(M, N) and str1[i] == str2[i]:
        i += 1
    R[0][0] = i
    T_ = S_(i, i, 0)
    T[0] = T_
    d, L, U = 0, 0, 0

    while True:
        d += 1
        d_ = max(d - math.floor((X + mat / 2) / (mat - mis)) - 1, 0)
        for k in range(L - 1, U + 2):
            print("k{}".format(k))
            first, second, third = -math.inf, -math.inf, -math.inf
            if L < k:
                first = R[d - 1][k - 1] + 1
                print("first{}".format(first))
            if L <= k <= U:
                second = R[d - 1][k] + 1
                print("second{}".format(second))
            if k < U:
                third = R[d - 1][k + 1]
                print("third{}".format(third))

            i = max(first, second, third)

            j = i - k
            print(j)

            if i > -math.inf and S_(i, j, d) >= T[d_] - X:
                while i <= M and j <= N and str1[i] == str2[j]:
                    i += 1
                    j += 1
                if k >= 0:
                    R[d][k] = i
                print("R[d][k]{} {}".format(R[d][k], j))
                T_ = max(T_, S_(i, j, d))
            else:
                print("d{}k{}".format(d, k))
                R[d][k] = -math.inf

        T[d] = T_
        print(R[d])
        for i in range(max(M, N)+1):
            if R[d][i] > -math.inf:
                L = i
                print("L{}".format(L))
                break

        for i in range(max(M, N), -1, -1):
            if R[d][i] > - math.inf:
                U = i
                print("U{}".format(U))
                break

        for i in range(max(M, N), -1, -1):
            if R[d][i] == N + i:
                L = max(L, i + 2)
                break

        for i in range(max(M, N)+1):
            if R[d][i] == M:
                U = min(U, i-2)
                break
        print("U{},L{}".format(U, L))
        print(T)
        if L > U + 2 or d > max(M, N)-1:
            break

    return T_


if __name__ == "__main__":
    a = time.time()
    b = greedy("agcgcaacctagagtgttcaaaacttgatttgcaggctggtcatagatctatcgatgctctctgatgtaatgtgccgctcgactcgtctatcgcctaatg",
               "gcgcagcctagggtgttaaaactgattgcagggtggtcttaattatcgatgctccctgatctagcgccgcgcgactggttaacgcctcatg",
               4, -2, -4, 10000000)
    print(b)
    print(time.time()-a)