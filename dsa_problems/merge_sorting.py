def merge_sort(arr):
    if len(arr)<=1:
        return

    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge_two_lists(left,right,arr)


def merge_two_lists(a,b,arr):
    len_a=len(a)
    len_b=len(b)
    i=j=k=0

    while i<len_a and j<len_b:
            if a[i] <= b[j]:
                arr[k]=a[i]
                i+=1
            else:
                arr[k]=b[j]
                j+=1
            k+=1
    while i<len_a:
              arr[k]=a[i]
              i+=1
              k+=1
    while j<len_b:
              arr[k]=b[j]
              j+=1
              k+=1


if __name__ == "__main__" :
    # a=[5,8,12,55,-1,-2]
    b=[7,9,34,-56,-100,200,300]

    merge_sort(b)
    print(b)


