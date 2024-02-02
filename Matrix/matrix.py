import sys
Soul=[]
def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

def print_solution(s, i, j):

    if i == j:
        print(f"A {i},", end="")
        Soul.append(f"A{i}")
    else:
        Soul.append("(")
        print_solution(s, i, s[i][j])
        print_solution(s, s[i][j] + 1, j)
        Soul.append(")")
        return ''.join(Soul)

def main(n, p):

    m, s = matrix_chain_order(p)
    return print_solution(s, 1, n),m,s
