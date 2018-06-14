#include "bubble_sort.cxx"
#include "selection_sort.cxx"
#include "insertion_sort.cxx"
#include "merge_sort.cxx"
#include "heap_sort.cxx"
#include "quick_sort_hoare.cxx"
#include "quick_sort_lomuto.cxx"
#include <chrono>
#include <iostream>
#include <unordered_map>
#include <vector>

const int N = 5000;
std::vector<int> a(N);

bool check_monotonic(std::vector<int>& array)
{
	for(int i = 0; i < array.size(); i++)
	{
		if(array[i] < 0 || array[i] > N)
			return false;
		if(i >= 1 && array[i-1] > array[i])
			return false;
	}
	return true;
}

bool check_consistency(const std::vector<int>& original, const std::vector<int>& array)
{
	std::unordered_map<int, int> cnt;
	for(int i = 0; i < original.size(); i++)
		if(cnt.count( original[i] ) == 0)
			cnt[original[i]] = 1;
		else
			cnt[original[i]] += 1;

	for(int i = 0; i < array.size(); i++)
		if(cnt.find( original[i] ) == cnt.end())
			return false;
		else
			cnt[original[i]] -= 1;
	int sum = 0;
	for(std::unordered_map<int,int>::iterator it=cnt.begin(); it!=cnt.end(); it++)
		sum += it->second;
	return sum == 0;
}

int check_sort_impl(void (*func)(std::vector<int>&))
{
	for(int i = 0; i < N; i++)
		a[i] = rand() % N;
	std::vector<int> original = a;
	func( a );
	return check_monotonic( a ) && check_consistency(original, a);
}


int main()
{
	typedef void (*sort_func)(std::vector<int>&);
	std::vector<sort_func> funcs = { bubble_sort, selection_sort, insertion_sort,
		merge_sort, heap_sort, quick_sort_hoare, quick_sort_lomuto };
	std::vector<std::string> names = { "bubble_sort", "selection_sort", "insertion_sort",
		"merge_sort", "heap_sort", "quick_sort_hoare", "quick_sort_lomuto" };
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
