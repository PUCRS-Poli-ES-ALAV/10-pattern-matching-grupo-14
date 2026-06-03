# Algoritmo de Rabin-Karp para busca de substring
class RabinKarp:
    R = 256
    Q = 1000000007  # número primo grande

    # funcao para calcular o hash de uma string
    @staticmethod
    def hash(s, M):
        h = 0
        iteracoes = 0
        instrucoes = 0

        for j in range(M):
            iteracoes += 1

            h = (h * RabinKarp.R + ord(s[j])) % RabinKarp.Q

            instrucoes += 1

        return h, iteracoes, instrucoes

    # função principal de busca Rabin-Karp
    @staticmethod
    def search(pat, txt):
        iteracoes = 0
        instrucoes = 0

        M = len(pat)
        N = len(txt)

        # Calcula hash do padrão
        pat_hash, it_hash_pat, inst_hash_pat = RabinKarp.hash(pat, M)

        iteracoes += it_hash_pat
        instrucoes += inst_hash_pat

        # Percorre todas as posições possíveis
        for i in range(N - M + 1):
            instrucoes += 1

            # Janela atual do texto
            sub = txt[i:i + M]

            # Calcula hash da janela
            txt_hash, it_hash_txt, inst_hash_txt = RabinKarp.hash(sub, M)

            iteracoes += it_hash_txt
            instrucoes += inst_hash_txt

            # Compara hashes
            iteracoes += 1
            instrucoes += 1

            if pat_hash == txt_hash:
                instrucoes += 1

                # Verificação para evitar colisões
                iteracoes += 1
                instrucoes += 1

                if sub == pat:
                    instrucoes += 1
                    return i, iteracoes, instrucoes

        return -1, iteracoes, instrucoes

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
        pos, it, inst = RabinKarp.search(s1, s2) 
        print(f"Tamanho s1={len(s1)}, s2={len(s2)}")
        print(f"Posição: {pos}")
        print(f"Iterações: {it}")
        print(f"Instruções: {inst}")
        print("-" * 30)