from time import perf_counter
from implementations.naive import Naive
from implementations.rabin_karp import RabinKarp
from implementations.rabin_karp_rolling_hash import RabinKarpRolling
from implementations.knuth_morris_pratt import KMP

# casos de teste - 
# os primeiros 4 são pequenos para verificar a correção, 
# os últimos 2 são grandes para comparar desempenho

s1m = "A" * 500000
s2m = "AAA"
s1p = "A" * 500000
s2p = "A" * 499999 + "B"

casos = [
    ("Pequeno - fim",        "ABCD",                        "CD"),
    ("Pequeno - repeticao",  "AAAAAA",                      "AAA"),
    ("Pequeno - nao acha",   "ABCDEFG",                     "XYZ"),
    ("Pequeno - meio",       "ABCDCBDCBDACBDABDCBADF",      "ADF"),
    ("Grande - melhor caso", s1m,                           s2m),
    ("Grande - pior caso",   s1p,                           s2p),
]

algoritmos = [
    ("Naive",          lambda s1, s2: Naive.ver_ocorrencia(s1, s2)),
    ("RK s/ rolling",  lambda s1, s2: RabinKarp.search(s1, s2)),
    ("RK c/ rolling",  lambda s1, s2: RabinKarpRolling.search(s1, s2)),
    ("KMP",            lambda s1, s2: KMP.kmp_search(s1, s2)),
]

# tabela de resultados -

col = [28, 18, 8, 8, 14, 14, 10]
header = ["Caso", "Algoritmo", "|s1|", "|s2|", "Iterações", "Instruções", "Tempo (ms)"]

def linha(vals):
    return "  ".join(str(v).ljust(col[i]) if i < 2 else str(v).rjust(col[i]) for i, v in enumerate(vals))

print(linha(header))
print("-" * (sum(col) + 2 * len(col)))

for descricao, s1, s2 in casos:
    for nome, fn in algoritmos:
        t0 = perf_counter()
        pos, it, inst = fn(s1, s2)
        ms = (perf_counter() - t0) * 1000

        vals = [
            descricao,
            nome,
            len(s1),
            len(s2),
            f"{it:,}",
            f"{inst:,}",
            f"{ms:.2f}",
        ]
        print(linha(vals))
    print()