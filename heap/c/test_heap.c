#include <assert.h>
#include <stdlib.h>
#include <time.h>
#include "heap.c"

int compare(const void* a, const void* b)
{
  if ( *(int*)a <  *(int*)b ) return -1;
  if ( *(int*)a >  *(int*)b ) return 1;
  return 0;
}

void testHeapify()
{
	const int N = 1000;
	int array[N];
	struct myvector vec;
	struct myvector* heap = &vec;
	for(int i = 0; i < N; i++)
	{
		array[i] = rand() % N;
		heap->push_back(heap, array[i]);
	}
	qsort(heap, N, sizeof(int), compare);
	heapify(heap);
	for(int i = 0; i< N; i++)
		assert(array[i] == heappop(heap));
}

void testHeappush()
{
	const int N = 1000;
	int array[N];
	struct myvector vec;
	struct myvector* heap = &vec;
	for(int i = 0; i < N; i++)
		array[i] = rand() % N;
	for(int i = 0; i < N; i++)
		heappush(heap, array[i]);
	qsort(heap, N, sizeof(int), compare);
	for(int i = 0; i< N; i++)
		assert(array[i] == heappop(heap));
}

int main()
{
	srand(time(0));
	return 0;
}
