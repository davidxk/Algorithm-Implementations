#include "fisher_yates.h"

#include <vector>

void test_fisher_yates()
{
	std::vector<int> array(100);
	for(int i = 0; i < 100; i++)
		array[i] = i;
	fisher_yates(array);
}

void test_fisher_yates_front()
{
	std::vector<int> array(100);
	for(int i = 0; i < 100; i++)
		array[i] = i;
	fisher_yates_front(array);
}

int main()
{
	test_fisher_yates();
	test_fisher_yates_front();
	return 0;
}
