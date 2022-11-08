# A pesquisa normal percorre todo o array até achar o igual solicitado
def naive_search(l, target):
    # exemplo: l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# A pesquisa binária é mais rapida que a normal pois não necessita percorrer todas as opções para achar a correta
# Dividir e conuistar

def binary_search(l, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    # exemplo l = [1, 3, 5, 10, 12] # retorna 3
    midpoint = (len(l)) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)

if __name__ == '__main__':
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))
