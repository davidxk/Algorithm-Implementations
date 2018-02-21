#include "../../vector/myvector.h"

void perc_down(struct myvector* array, int i, int size)
{
	int x = array->data[i];
	int child; 
	while(2 * i + 1 < size)
	{
		child = 2 * i + 1;
		if(child < size - 1 && array->data[child + 1] < array->data[child])
			child++;
		if(array->data[child] < x)
		{
			array->data[i] = array->data[child];
			i = child;
		}
		else
			break;
	}
	array->data[i] = x;
}

void heapify(struct myvector* array)
{
	int i;
	for(i = array->size(array)/2; i >= 0; i--)
		perc_down(array, i, array->size(array));
}

void heappush(struct myvector* array, int elem)
{
	array->push_back(array, elem);
	int i = array->size(array) - 1;
	int parent, tmp;
	while(i > 0)
	{
		parent = (i - 1) / 2;
		if(array->data[i] < array->data[parent])
		{
			tmp = array->data[i];
			array->data[i] = array->data[parent];
			array->data[parent] = array->data[i];
			i = parent;
		}
		else
			break;
	}
}

int heappop(struct myvector* array)
{
	int retval = array->data[0];
	array->data[0] = array->back(array);
	array->pop_back(array);
	perc_down(array, 0, array->size(array));
	return retval;
}
