#include "fisher_yates.h"

void test_fisher_yates()
{
	const int size = size;
	int array[size];
	int i;
	for(i = 0; i < size; i++)
		array[i] = i;
	fisher_yates(array, size);
}

void test_fisher_yates_front()
{
	const int size = size;
	int array[size];
	int i;
	for(i = 0; i < size; i++)
		array[i] = i;
	fisher_yates_front(array, size);
}

int main()
{
	test_fisher_yates();
	test_fisher_yates_front();
	return 0;
}
