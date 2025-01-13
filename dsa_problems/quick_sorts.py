def swap(a,b,arr):
    if a != b:
        temp=arr[a]
        arr[a]=arr[b]
        arr[b]=temp


# for dividing the array into two parts-
def partition(arr,start,end):
    pivot_idx=start

    pivot=arr[pivot_idx]

    while start<end:
        while start<len(arr) and  arr[start]<=pivot:
            start+=1

        while arr[end]>pivot:
            end-=1

        if start<end:
            swap(start,end,arr)

    swap(pivot_idx,end,arr)
    return end


def quick_sort(arr,start,end):
    if start<end:
        pi=partition(arr,start,end)

        quick_sort(arr,start,pi-1)
        quick_sort(arr,pi+1,end)


if __name__ == "__main__":
     elements=[11,9,29,-5,0,23,56]
     quick_sort(elements,0,len(elements)-1)
     print(elements)