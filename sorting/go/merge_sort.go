package sorting

func merge_sort(array []int) {
	var temp []int = make([]int, len(array))
	m_sort(array, 0, len(array), temp)
}

func m_sort(array []int, start int, end int, temp []int) {
	if end-start > 1 {
		var middle int = (start + end) / 2
		m_sort(array, start, middle, temp)
		m_sort(array, middle, end, temp)
		merge(array, start, middle, end, temp)
	}
}

func merge(array []int, start, middle, end int, temp []int) {
	var i, j, k int = start, middle, 0
	for i < middle && j < end {
		if array[i] < array[j] {
			temp[k] = array[i]
			i++
		} else {
			temp[k] = array[j]
			j++
		}
		k++
	}
	for i < middle {
		temp[k] = array[i]
		i++
		j++
	}
	for j < end {
		temp[k] = array[j]
		j++
		k++
	}
	for i = 0; i < k; i++ {
		array[start+i] = temp[i]
	}
}
