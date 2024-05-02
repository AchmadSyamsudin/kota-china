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
