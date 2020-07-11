# I don't like the quotes, sorry
start, a, b, c, d, e, finish = "Start", "A", "B", "C", "D", "E", "Finish"
infinity = float("inf")
# =======  Graph A  =======
A = {}
A[start] = {}   # Start Node
A[start][a] = 5
A[start][b] = 2
A[a] = {}       # A Node
A[a][d] = 4
A[a][c] = 2
A[b] = {}       # B Node
A[b][a] = 8
A[b][c] = 7
A[c] = {}       # C Node
A[c][finish] = 1
A[d] = {}       # D Node
A[d][c] = 6
A[d][finish] = 3
A[finish] = {} # Finish Node
# ===== Costs =====
a_c = {}
a_c[a] = 5
a_c[b] = 2
a_c[c], a_c[d], a_c[finish] = infinity, infinity, infinity
# ===== Parents =====
a_p = {}
a_p[a] = start
a_p[b] = start
a_p[c], a_p[d], a_p[finish] = None, None, None
