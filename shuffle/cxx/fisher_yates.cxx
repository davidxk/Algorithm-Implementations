#include "fisher_yates.h"

#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <vector>

void fisher_yates(std::vector<int>& array)
{
	int j;
	for(int i = array.size() - 1; i >= 0; i--)
	{
		j = rand() % (i + 1);
		std::swap(array[i], array[j]);
	}
}

void fisher_yates_front(std::vector<int>& array)
{
	int j;
	for(int i = 0; i < array.size(); i++)
	{
		j = i + rand() % (array.size() - i);
		std::swap(array[i], array[j]);
	}
}
