def partition(nums, left, right):
    pivot = nums[left]
    l, r = left + 1, right
    while l <= r:
        if nums[l] < pivot and nums[r] > pivot:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1
        if nums[l] >= pivot:
            l += 1
        if nums[r] <= pivot:
            r -= 1
    nums[left], nums[r] = nums[r], nums[left]
    return r


def kthlargest(nums, k):
    left, right = 0, len(nums)-1
    while True:
        pos = partition(nums, left, right)
        if pos == k-1:
            return nums[pos]
        if pos > k-1:
            right = pos-1
        else:
            left = pos+1


print(kthlargest([3, 5, 1, 4, 2], 2))