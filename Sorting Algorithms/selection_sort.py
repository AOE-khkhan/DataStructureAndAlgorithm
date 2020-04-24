def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        minpos = i
        for j in range(i+1,n):
            if arr[minpos] > arr[j]:
                minpos = j
        arr[i],arr[minpos] = arr[minpos],arr[i]
    return arr 

if __name__ == '__main__':
    pass
