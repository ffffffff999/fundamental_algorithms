p = 1 # начальный узел
q = 4 # конечный узел
pq = [[1, 2], [2, 3], [3, 0], [0, 5], [3, 4]]


def check_link(a, b): # функция провеки связи между p и q
    position = a
    visited = []
    while pq != []:
        if position == pq[0][0]: # проверяет есть ли ребро у данного узла
            visited.append(position)
            position = pq[0][1]
            pq.remove(pq[0])
            if position == b:
                return "YES"
        else:
            position = visited[len(visited) - 1]
            visited = visited[:len(visited) - 1]
    return 0

def count_usel(array): # функция подсчета кеоличества вершин
    a = set(i for l in array for i in l) # номера узлов графа
    return len(a)

print(check_link(1, 4))
