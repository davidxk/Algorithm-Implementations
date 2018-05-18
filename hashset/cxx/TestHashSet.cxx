#include <cassert>
#include <cstdlib>
#include "HashSet.h"

void testInsert(HashSet& dict, int size)
{
	for(int i = 0; i < 1000; i++)
	{
		assert(dict.size() == i);
		dict.insert(i);
		assert(dict.contains(i));
		assert(not dict.contains(i + 1));
		assert(dict.contains(rand() % (i + 1)));
	}
	assert(dict.size() == size);
}

void testErase(HashSet& dict, int size)
{
	for(int i = 0; i < 1000; i++)
	{
		assert(dict.size() == size - i);
		assert(dict.contains(i));
		dict.erase(i);
		assert(dict.size() == size - i - 1);
		assert(not dict.contains(i));
	}
}

int main()
{
	const int size = 1000;
	HashSet dict;
	testInsert(dict, size);
	testErase(dict, size);
	testInsert(dict, size);
	testErase(dict, size);
	testInsert(dict, size);
	dict.clear();
	for(int i = 0; i < 1000; i++)
		assert(not dict.contains(i));
	assert(dict.size() == 0);
}
