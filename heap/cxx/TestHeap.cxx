#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <ctime>
#include <vector>
#include "heap.cxx"

void testHeapify()
{
	std::vector<int> heap;
	const int N = 1000;
	for(int i = 0; i < N; i++)
		heap.push_back(rand() % N);
	auto copy = std::vector<int>(heap);
	std::sort(copy.begin(), copy.end());
	heapify<int>(heap);
	for(int i = 0; i< N; i++)
		assert(copy[i] == heappop<int>(heap));
}

void testHeappush()
{
	std::vector<int> heap, array;
	const int N = 1000;
	for(int i = 0; i < N; i++)
		array.push_back(rand() % N);
	for(int i = 0; i < N; i++)
		heappush<int>(heap, array[i]);
	std::sort(array.begin(), array.end());
	for(int i = 0; i< N; i++)
		assert(array[i] == heappop<int>(heap));
}

int main()
{
	srand(time(nullptr));
	return 0;
}
