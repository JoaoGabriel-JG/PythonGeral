# A pesquisa binária é mais rapida que a normal pois não necessita percorrer todas as opções para achar a correta

def native_search(l, target):
    # exemplo: l = [1, 2, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1
