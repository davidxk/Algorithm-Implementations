#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

void insertion_sort(vector<int>& array)
{
	int x, j;
	for(int i = 0; i < array.size(); i++)
	{
		x = array[i];
		for(j = i - 1; j >= 0 && array[j] > x; j--)
			array[j + 1] = array[j];
		array[j + 1] = x;
	}
}

int main()
{
	const int N = 10;
	vector<int> a(N, 0);
	for(int i = 0; i < N; i++)
		a[i] = rand() % 50;
	insertion_sort(a);
	for(int i = 0; i < N; i++)
		cout<<a[i]<<' ';
	cout<<endl;

	return 0;
}
