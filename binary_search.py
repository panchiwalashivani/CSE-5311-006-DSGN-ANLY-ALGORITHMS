import time

def binary_search_rec(nums, target, low, high):
	if low > high:
		return -1

	# Finding the mid using floor division
	mid = low + ((high - low) // 2)

	# Target value is present at the middle of the array
	if nums[mid] == target:
		return mid

	# Target value is present in the low subarray
	elif target < nums[mid]:
		return binary_search_rec(nums, target, low, mid - 1)

	# Target value is present in the high subarray
	else:
		return binary_search_rec(nums, target, mid + 1, high)


def binary_search(nums, target):
	arr_sort = sorted(nums)  # Sorting array
	t2_start = time.perf_counter()
	result = binary_search_rec(arr_sort, target, 0, len(nums) - 1)
	t2_stop = time.perf_counter()
	#print("--- %s seconds ---" % str(t2_stop - t2_start))
	t2 = str(t2_stop-t2_start)+"s"
	if result != -1:
		return (result, arr_sort, t2)
	else:
		return (-1, arr_sort, t2)


# https://www.educative.io/courses/coderust-hacking-the-coding-interview/k5qJx