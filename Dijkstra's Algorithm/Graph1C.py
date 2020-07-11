# I don't like the quotes, sorry
start, a, b, c, d, e, finish = "Start", "A", "B", "C", "D", "E", "Finish"
infinity = float("inf")
# =======  Graph B  =======
C = {}
C[start] = {}   # Start Node
C[start][a] = 2
C[start][b] = 2
C[a] = {}       # A Node
C[a][b] = 2
C[b] = {}       # B Node
C[b][c] = 2
C[b][finish] = 2
C[c] = {}       # C Node
C[c][a] = -1
C[c][finish] = 2
C[finish] = {} # Finish Node
# ===== Costs =====
c_c = {}
c_c[a] = 2
c_c[b] = 2
c_c[c], c_c[finish] = infinity, infinity
# ===== Parents =====
c_p = {}
c_p[a] = start
c_p[b] = start
c_p[c], c_p[finish] = None, None
