# Algoritmo de Rabin-Karp com Rolling Hash para busca de substring
class RabinKarpRolling:
    R = 256
    Q = 1000000007

    # função principal de busca Rabin-Karp com rolling hash
    @staticmethod
    def search(pat, txt):
        iteracoes = 0
        instrucoes = 0
        M = len(pat)
        N = len(txt)
        if M > N:
            return -1, iteracoes, instrucoes

        # Pré-calcula R^(M-1) % Q para o rolling hash
        RM = 1
        for _ in range(M - 1):
            RM = (RM * RabinKarpRolling.R) % RabinKarpRolling.Q
            instrucoes += 1

        # Hash inicial do padrão e da primeira janela
        pat_hash = 0
        txt_hash = 0
        for i in range(M):
            iteracoes += 1
            pat_hash = (pat_hash * RabinKarpRolling.R + ord(pat[i])) % RabinKarpRolling.Q
            txt_hash = (txt_hash * RabinKarpRolling.R + ord(txt[i])) % RabinKarpRolling.Q
            instrucoes += 2

        # Verifica posição 0
        iteracoes += 1
        instrucoes += 1
        if pat_hash == txt_hash:
            instrucoes += 1
            if txt[:M] == pat:
                instrucoes += 1
                return 0, iteracoes, instrucoes

        for i in range(1, N - M + 1):
            iteracoes += 1
            # Remove o char que saiu, adiciona o char que entrou
            txt_hash = (RabinKarpRolling.R * (txt_hash - ord(txt[i - 1]) * RM) + ord(txt[i + M - 1])) % RabinKarpRolling.Q
            instrucoes += 3

            instrucoes += 1
            if pat_hash == txt_hash:
                instrucoes += 1
                iteracoes += 1
                if txt[i:i + M] == pat:
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
        pos, it, inst = RabinKarpRolling.search(s1, s2) 
        print(f"Tamanho s1={len(s1)}, s2={len(s2)}")
        print(f"Posição: {pos}")
        print(f"Iterações: {it}")
        print(f"Instruções: {inst}")
        print("-" * 30)