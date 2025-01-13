def insert_sort(arr):
    size=len(arr)
    # Traverse from the second element to the last element
    for i in range(1,size):
        # Store the current element to be compared
        key=arr[i]
        # Initialize the previous index
        j=i-1

        # Move elements that are greater than 'key' one position ahead
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1

        # Place 'key' at its correct position
        arr[j+1]=key

if __name__=="__main__":

    nums=[0,-1,45,2,54,56,-577,-21,1324]
    print(insert_sort(nums))
    print(nums)