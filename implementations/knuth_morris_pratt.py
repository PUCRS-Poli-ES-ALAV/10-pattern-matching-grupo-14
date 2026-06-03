# Algoritmo de Knuth-Morris-Pratt (KMP) para busca de substring
class KMP:
    
    # função para calcular o array de prefixo (lps - longest prefix-suffix)
    @staticmethod
    def compute_lps(pat, counters):
        M = len(pat)
        lps = [0] * M
        len_ = 0
        i = 1

        while i < M:
            counters['iter'] += 1
            if pat[i] == pat[len_]:
                counters['inst'] += 1
                len_ += 1
                lps[i] = len_
                i += 1
            else:
                counters['inst'] += 1
                if len_ != 0:
                    counters['inst'] += 1
                    len_ = lps[len_ - 1]
                else:
                    counters['inst'] += 2
                    lps[i] = 0
                    i += 1

        return lps

    # função principal de busca KMP
    @staticmethod
    def kmp_search(txt, pat):
        N = len(txt)
        M = len(pat)
        iter = 0
        inst = 0

        if M == 0:
            return 0, iter, inst

        counters = {'iter': 0, 'inst': 0}
        lps = KMP.compute_lps(pat, counters)
        iter += counters['iter']
        inst += counters['inst']

        i = 0
        j = 0

        while i < N:
            iter += 1
            if pat[j] == txt[i]:
                inst += 2
                i += 1
                j += 1

            if j == M:
                inst += 1
                return i - j, iter, inst

            elif i < N and pat[j] != txt[i]:
                inst += 1
                if j != 0:
                    inst += 1
                    j = lps[j - 1]
                else:
                    inst += 1
                    i += 1

        return -1, iter, inst

if __name__ == "__main__":
    # testes de desempenho

    s1m = "A" * 500000
    s2m = "AAA"

    s1p = "A" * 500000
    s2p = "A" * 499999 + "B"

    casos = [
        ("ABCD", "CD"),
        ("AAAAAA", "AAA"),
        ("ABCDEFG", "XYZ"),
        ("ABCDCBDCBDACBDABDCBADF", "ADF"),
        (s1m, s2m),
        (s1p, s2p),
    ]

    for s1, s2 in casos:
        pos, it, inst = KMP.kmp_search(s1, s2) 
        print(f"Tamanho s1={len(s1)}, s2={len(s2)}")
        print(f"Posição: {pos}")
        print(f"Iterações: {it}")
        print(f"Instruções: {inst}")
        print("-" * 30)