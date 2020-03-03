def heap_sort(heap):
    heap_size = len(heap)
    # build heap
    for i in range(heap_size // 2 - 1, -1, -1):  # 从第一个非叶结点开始调整堆
        max_heapify(heap, heap_size, i)

    # heap sort
    for i in range(heap_size - 1, 0, -1):
        heap[i], heap[0] = heap[0], heap[i]  # 交换根节点和最后一个结点
        max_heapify(heap, i, 0)
    return heap


def max_heapify(heap, heap_size, node):  # 对堆heap[:heapsize]中的node结点进行堆调整
    left = node * 2 + 1
    right = left + 1
    larger = node
    if left < heap_size and heap[left] > heap[larger]:
        larger = left
    if right < heap_size and heap[right] > heap[larger]:
        larger = right
    if larger != node:
        heap[larger], heap[node] = heap[node], heap[larger]
        max_heapify(heap, heap_size, larger)
