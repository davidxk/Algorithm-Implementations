# Tested
# Verified
def bidirectional(adjList, source, target):
    fronts = [set([source]), set([target])]
    visited = [set([source]), set([target])]
    cnt = [0, 0]
    prev = [{source: None}, {target: None}]
    border = set()
    if source == target:
        border.add(source)
    while all(fronts) and not border: 
        smaller = 0 if len(fronts[0]) < len(fronts[1]) else 1
        children = set()
        cnt[smaller] += 1
        for node in fronts[smaller]:
            for child in adjList[node]:
                if child in fronts[not smaller]:
                    border.add(child)
                if child not in visited[smaller]:
                    visited[smaller].add(node)
                    children.add(child)
                    prev[smaller][child] = node
        fronts[smaller] = children
    for node, parent in prev[1].items():
        prev[0][parent] = node
    return sum(cnt), prev[0]
