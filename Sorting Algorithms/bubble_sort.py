def bubbleSort(arr):
    ''' BubbleSort Algorithm Implementation in Python 3.0+
    arr : unorded list
    output : return list in ascending order.

    Example : 
    >>> bubbleSort([4,2,6,5,9,8])
    [2, 4, 5, 6, 8, 9]
    '''
    n = len(arr)
    for i in range(n):
        sort = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                sort = True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if not sort:
            break
    return arr

if __name__ == '__main__':
    import time
    user_input = input("Enter numbers separated by a comma:").strip()
    arr = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    print(*bubbleSort(arr),sep=',')
    print(f"Processing time: {time.process_time() - start}") 