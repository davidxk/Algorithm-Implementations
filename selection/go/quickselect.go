package main

// TESTED on LeetCode

// QuickSelect returns the k'th largest number in the array
func QuickSelect(nums []int, rank int) int {
	qSelect(nums, 0, len(nums)-1, rank-1)
	return nums[rank-1]
}

func qSelect(nums []int, left, right, rank int) {
	if right-left < 10 {
		insertionSort(nums, left, right)
		return
	}
	center := partition(nums, left, right)
	if rank < center {
		qSelect(nums, left, center-1, rank)
	} else if rank > center {
		qSelect(nums, center+1, right, rank)
	}
}

func insertionSort(nums []int, left, right int) {
	var j, x int
	for i := left + 1; i < right+1; i++ {
		x = nums[i]
		for j = i - 1; j >= left && nums[j] > x; j-- {
			nums[j+1] = nums[j]
		}
		nums[j+1] = x
	}
}

func median3(nums []int, left, right int) int {
	center := left + (right-left)/2
	tmp := []int{nums[left], nums[center], nums[right]}
	insertionSort(tmp, 0, 2)
	nums[left], nums[center], nums[right] = tmp[0], tmp[2], tmp[1]
	return nums[right]
}

func partition(nums []int, left, right int) int {
	pivot := median3(nums, left, right)
	var i, j int = left + 1, right - 1
	for {
		for nums[i] < pivot {
			i++
		}
		for pivot < nums[j] {
			j--
		}
		if i >= j {
			nums[i], nums[right] = nums[right], nums[i]
			return i
		}
		nums[i], nums[j] = nums[j], nums[i]
		i++
		j--
	}
}
