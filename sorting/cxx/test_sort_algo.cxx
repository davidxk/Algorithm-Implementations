#include "bubble_sort.cxx"
#include "insertion_sort.cxx"
#include "merge_sort.cxx"
#include "heap_sort.cxx"
#include "quick_sort_hoare.cxx"
#include "quick_sort_lomuto.cxx"
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

const int N = 5000;
vector<int> a(N);

bool check_monotonic(vector<int>& array)
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

bool check_consistency(const vector<int>& original, const vector<int>& array)
{
	unordered_map<int, int> cnt;
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
	for(unordered_map<int,int>::iterator it=cnt.begin(); it!=cnt.end(); it++)
		sum += it->second;
	return sum == 0;
}

int check_sort_impl(void (*func)(vector<int>&))
{
	for(int i = 0; i < N; i++)
		a[i] = rand() % N;
	vector<int> original = a;
	func( a );
	return check_monotonic( a ) && check_consistency(original, a);
}


int main()
{
	typedef void (*sort_func)(vector<int>&);
	vector<sort_func> funcs;
	funcs.push_back(bubble_sort);
	funcs.push_back(insertion_sort);
	funcs.push_back(merge_sort);
	funcs.push_back(heap_sort);
	funcs.push_back(quick_sort_hoare);
	funcs.push_back(quick_sort_lomuto);
	for(int i = 0; i < funcs.size(); i++)
		if( !check_sort_impl(funcs[i]) )
			cout<<"Error at funcs["<<i<<"]"<<endl;
	return 0;
}
