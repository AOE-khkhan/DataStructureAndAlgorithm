import heapq

newList = [21, 2, 45, 67, 34]

heapq.heapify(newList)                                 # this function converts regular list to a heap.
print(newList)

heapq.heappush(newList,10)                             # heappush will add element
print(newList)

heapq.heappop(newList)                                 # removing from heap Smallest element
print(newList)

heapq.heapreplace(newList,1)                           # heapreplace will smallest element from heap
print(newList)