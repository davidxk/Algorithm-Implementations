#include <algorithm>
#include <vector>

template<class T>
static void perc_down(std::vector<T>& array, int i, int size)
{
	T x = array[i];
	int child;
	while(2 * i + 1 < size)
	{
		child = 2 * i + 1;
		if(child < size - 1 and array[child + 1] < array[child])
			child++;
		if(array[child] < x)
		{
			array[i] = array[child];
			i = child;
		}
		else
			break;
		array[i] = x;
	}
}

template<class T>
void heapify(std::vector<T>& array)
{
	for(int i = array.size() / 2; i >= 0; i--)
		perc_down(array, i, array.size());
}

template<class T>
void heappush(std::vector<T> array, T elem)
{
	array.push_back(elem);
	int i = array.size() - 1;
	int parent;
	while(i > 0)
	{
		parent = (i - 1) / 2;
		if(array[i] < array[parent])
		{
			std::swap(array[i], array[parent]);
			i = parent;
		}
		else
			break;
	}
}

template<class T>
T heappop(std::vector<T> array)
{
	T retval = array[0];
	array[0] = array.back();
	array.pop_back();
	perc_down(array, 0, array.size());
	return retval;
}
