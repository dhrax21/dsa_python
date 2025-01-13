def bubb_sort(nums):
    size = len(nums)
    swapped=False
    for i in range(size):
        for j in range(0, size-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped=True
        if swapped==False:
            print("already sorted !")
            break

if __name__ == "__main__":
    nums = [-577, -21, 0, 2, 45, 54, 56, 1324]
    (bubb_sort(nums))
    print(nums)