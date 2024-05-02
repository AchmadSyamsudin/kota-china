def perjalanan(graf, awal, akhir):
    stack = [(awal, [awal])]
    while stack:
        (node, path) = stack.pop()
        for next_node in graf.get(node, []):
            if next_node in path:
                continue
            if next_node == akhir:
                yield path + [next_node]
            else:
                stack.append((next_node, path + [next_node]))

def print_rute(rute):
    for i, path in enumerate(rute, start=1):
        print(f'Rute {i}: {" -> ".join(path)}')
