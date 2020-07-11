# I don't like the quotes, sorry
start, a, b, c, d, e, finish = "Start", "A", "B", "C", "D", "E", "Finish"
infinity = float("inf")
# =======  Graph B  =======
B = {}
B[start] = {}   # Start Node
B[start][a] = 10
B[a] = {}       # A Node
B[a][c] = 20
B[b] = {}       # B Node
B[b][a] = 1
B[c] = {}       # C Node
B[c][b] = 1
B[c][finish] = 30
B[finish] = {} # Finish Node
# ===== Costs =====
b_c = {}
b_c[a] = 10
b_c[b] = infinity
b_c[c], b_c[finish] = infinity, infinity
# ===== Parents =====
b_p = {}
b_p[a] = start
b_p[b] = None
b_p[c], b_p[finish] = None, None
