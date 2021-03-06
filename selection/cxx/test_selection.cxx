#include "quick_select.cxx"
#include "bfprt_select.cxx"

#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <vector>

void merge(std::vector<int>& array, int start, int center, int end)
{
	static std::vector<int> tmp(array.size());
	int i = start, j = center, k = 0;
	while(i < center && j < end)
		if(array[i] < array[j])
			tmp[ k++ ] = array[ i++ ];
		else
			tmp[ k++ ] = array[ j++ ];
	while(i < center)
		tmp[ k++ ] = array[ i++ ];
	while(j < end)
		tmp[ k++ ] = array[ j++ ];
	for(int i = 0; i < end - start; i++)
		array[start + i] = tmp[i];
}

void m_sort(std::vector<int>& array, int start, int end)
{
	if(end - start > 1)
	{
		int center = (start + end) / 2;
		m_sort(array, start, center);
		m_sort(array, center, end);
		merge(array, start, center, end);
	}
}

void merge_sort(std::vector<int>& array)
{
	return m_sort(array, 0, array.size());
}

bool check_select(std::vector<int>& array, int rank, int retval)
{
	merge_sort(array);
	return array[rank - 1] == retval;
}

bool test_select(int (*select)(std::vector<int>&, int))
{
	int volume = 5000;
	std::vector<int> array(volume);
	int rank, retval;
	for(int i = 0; i < 1000; i++)
	{
		for(int j = 0; j < volume; j++)
			array[j] = rand() % volume;
		rank = rand() % volume + 1;
		retval = select(array, rank);
		if(not check_select(array, rank, retval))
			return false;
	}
	return true;
}

int main()
{
	srand(time(NULL));
	typedef int (*select)(std::vector<int>&, int);
	select funcs[] = {
		quick_select, bfprt_select
	};
	for(select func: funcs)
		if(!test_select(func))
			std::cout<<"WA: "<<func<<std::endl;
		else
			std::cout<<func<<" done"<<std::endl;
}
