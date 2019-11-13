#include "bubble_sort.cxx"
#include "selection_sort.cxx"
#include "insertion_sort.cxx"
#include "merge_sort.cxx"
#include "heap_sort.cxx"
#include "quick_sort_hoare.cxx"
#include "quick_sort_lomuto.cxx"
#include "radix_exchange_sort.cxx"
#include "straight_radix_sort.cxx"
#include <algorithm>
#include <chrono>
#include <iostream>
#include <unordered_map>
#include <vector>

bool check_sort_impl(void (*func)(std::vector<int>&))
{
	const int times = 100;
	for(int j = 0; j < times; j++)
	{
		int size = rand() % 1000 + 1000;
		std::vector<int> array(size);
		for(int i = 0; i < size; i++)
			array[i] = rand() % size - size / 2;
		std::vector<int> original = array;
		func( array );
		sort(original.begin(), original.end());
		for(int i = 0; i < size; i++)
			if(array[i] != original[i])
				return false;
		if(array.size() != original.size())
			return false;
	}
	return true;
}

int main()
{
	typedef void (*sort_func)(std::vector<int>&);
	std::vector<sort_func> funcs = {
		bubble_sort, selection_sort, insertion_sort,
		merge_sort, heap_sort, quick_sort_hoare, quick_sort_lomuto,
		radix_exchange_sort, straight_radix_sort
	};
	std::vector<std::string> names = {
		"bubble_sort", "selection_sort", "insertion_sort",
		"merge_sort", "heap_sort", "quick_sort_hoare", "quick_sort_lomuto",
		"radix_exchange_sort", "straight_radix_sort"
	};
	bool isPass;
	std::chrono::system_clock::time_point begin, end;
	std::chrono::milliseconds runtime;
	for(int i = 0; i < funcs.size(); i++)
	{
		begin = std::chrono::system_clock::now();
		isPass = check_sort_impl(funcs[i]);
		end = std::chrono::system_clock::now();
		runtime = std::chrono::duration_cast<std::chrono::milliseconds>(end - begin);
		if(isPass)
			std::cout<<names[i]<<":\t"<<runtime.count()<<"ms"<<std::endl;
		else
			std::cout<<"Error at "<<names[i]<<std::endl;
	}
	return 0;
}
