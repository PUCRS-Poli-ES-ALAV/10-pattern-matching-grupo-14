class RabinKarp:
    R = 256
    Q = 1000000007

    @staticmethod
    def hash(s, M):
        h = 0
        inst = 0
        iteracoes = 0

        for j in range(M):
            iteracoes += 1

            # h = (h * R + ord(s[j])) % Q
            h = (h * RabinKarp.R + ord(s[j])) % RabinKarp.Q

            inst += 1

        return h, iteracoes, inst

    @staticmethod
    def search(pat, txt):

        iteracoes = 0
        inst = 0

        M = len(pat)
        N = len(txt)

        # hash do padrão
        pat_hash, it_hash_pat, inst_hash_pat = RabinKarp.hash(pat, M)

        iteracoes += it_hash_pat
        inst += inst_hash_pat

        for i in range(N - M + 1):

            inst += 1

            sub = txt[i:i+M]

            # hash da substring atual
            txt_hash, it_hash_txt, inst_hash_txt = RabinKarp.hash(sub, M)

            iteracoes += it_hash_txt
            inst += inst_hash_txt

            # compara hashes
            iteracoes += 1
            inst += 1

            if pat_hash == txt_hash:

                inst += 1

                # evita colisão
                iteracoes += 1
                inst += 1

                if sub == pat:
                    inst += 1
                    return i, iteracoes, inst

        return -1, iteracoes, inst


# testes de desempenho

# melhor caso
s1m = "A" * 500000
s2m = "AAA"

# pior caso
s1p = "A" * 500000
s2p = "A" * 499999 + "B"

casos = [
    ("ABACADABRA", "CAD"),
    ("BANANA", "ANA"),
    ("CHOCOLATE", "HOCO"),
    ("TABUA", "BUA"),
    (s1m, s2m),
    (s1p, s2p),
]

for s1, s2 in casos:

    pos, it, inst = RabinKarp.search(s2, s1)

    print(f"Tamanho s1={len(s1)}, s2={len(s2)}")
    print(f"Posição: {pos}")
    print(f"Iterações: {it}")
    print(f"Instruções: {inst}")
    print("-" * 40)