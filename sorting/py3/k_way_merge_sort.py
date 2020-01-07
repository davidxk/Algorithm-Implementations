import heapq

def k_way_merge_sort(arrays):
    arrays = [array for array in arrays if array]
    heap = [(array[0], k, 0) for k, array in enumerate(arrays)]
    heapq.heapify(heap)
    result = []
    while heap:
        num, k, idx = heapq.heappop(heap)
        result.append(num)
        idx += 1
        if idx < len(arrays[k]):
            heapq.heappush(heap, (arrays[k][idx], k, idx))
    return result
