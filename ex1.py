def ver_ocorrencia(s1, s2):

    iter = 0
    inst = 0

    # percorre s1 até onde ainda cabe s2
    for i in range(len(s1) - len(s2) + 1):
        encontrou = True
        inst += 1

        # compara caractere por caractere
        for j in range(len(s2)):
            iter += 1
            inst += 1

            if s1[i + j] != s2[j]:
                encontrou = False
                inst += 1
                break

        # se encontrou toda a substring
        if encontrou:
            inst += 1
            return i, iter, inst

    return -1, iter, inst  # -1 se não encontrar

# testes de desempenho

# melhor caso:
s1m = "A" * 500000
s2m = "AAA"

# pior caso: 
s1p = "A" * 500000
s2p = "A" * 499999 + "B"

casos = [
    ("ABCD", "CD"),
    ("AAAAAA", "AAA"),
    ("ABCDEFG", "XYZ"),
    ("ABCDCBDCBDACBDABDCBADF", "ADF"),
    (s1m, s2m),
    (s1p, s2p)
]

for s1, s2 in casos:
    pos, it, inst = ver_ocorrencia(s1, s2)
    print(f"Tamanho s1={len(s1)}, s2={len(s2)}")
    print(f"Posição: {pos}")
    print(f"Iterações: {it}")
    print(f"Instruções: {inst}")
    print("-" * 30)