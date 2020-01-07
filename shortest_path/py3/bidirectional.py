# Tested
# Verified
def bidirectional(adjList, source, target):
    fronts = [[source], [target]]
    visited = [set([source]), set([target])]
    cnt = [0, 0]
    prev = [{source: None}, {target: None}]
    border = []
    if source == target:
        border.append(source)
    while all(fronts) and not border: 
        smaller = 0 if len(fronts[0]) < len(fronts[1]) else 1
        children = []
        cnt[smaller] += 1
        for node in fronts[smaller]:
            for child in adjList[node]:
                if child in visited[not smaller]:
                    border.append(child)
                if child not in visited[smaller]:
                    visited[smaller].add(child)
                    children.append(child)
                    prev[smaller][child] = node
        fronts[smaller] = children
    for node, parent in prev[1].items():
        prev[0][parent] = node
    return sum(cnt), prev[0]
