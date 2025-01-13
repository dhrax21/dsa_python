

def sel_sort(nums):
        min_idx=-1
        size=len(nums)
        for i in range(size):
            min_idx=i
            for j in range(min_idx+1,size):
                if nums[j]<nums[min_idx]:
                    min_idx=j
            if i != min_idx:
                nums[i],nums[min_idx]=nums[min_idx],nums[i]

if __name__=="__main__":

    nums=[0,-1,45,2,54,56,-577,-21,1324]
    print(sel_sort(nums))
    print(nums)