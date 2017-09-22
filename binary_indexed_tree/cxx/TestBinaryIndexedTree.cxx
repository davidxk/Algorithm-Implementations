#include "BinaryIndexedTree.h"

#include <cassert>
#include <cstdlib>
#include <ctime>

void testGetSum()
{
	const int LENGTH = 100;
	std::vector<int> array(100);
	for(int i = 0; i < LENGTH; i++)
		array[i] = rand() % 100;
	BinaryIndexedTree bit(array);
	int right, sum;
	for(int cnt = 0; cnt < 100; cnt++)
	{
		right = rand() % LENGTH;
		sum = 0;
		for(int i = 0; i <= right; i++)
			sum += array[i];
		assert(bit.getSum(right) == sum);
	}
}

void testUpdate()
{
	const int LENGTH = 100;
	std::vector<int> array(100);
	for(int i = 0; i < LENGTH; i++)
		array[i] = rand() % 100;
	BinaryIndexedTree bit(array);
	int right, sum;
	int index, delta;
	for(int cnt = 0; cnt < 100; cnt++)
	{
		index = rand() % LENGTH;
		delta = rand() % 100;
		array[index] += delta;
		bit.update(index, delta);
		right = rand() % LENGTH;
		sum = 0;
		for(int i = 0; i <= right; i++)
			sum += array[i];
		assert(bit.getSum(right) == sum);
	}
}

void testGetRange()
{
	const int LENGTH = 100;
	std::vector<int> array(100);
	for(int i = 0; i < LENGTH; i++)
		array[i] = rand() % 100;
	BinaryIndexedTree bit(array);
	int left, right, sum;
	for(int cnt = 0; cnt < 100; cnt++)
	{
		left = rand() % LENGTH/2;
		right = left + rand() % LENGTH/2;
		sum = 0;
		for(int i = left; i <= right; i++)
			sum += array[i];
		assert(bit.getRange(left, right) == sum);
	}
}

int main()
{
	srand(time(NULL));
	testGetSum();
	testUpdate();
	testGetRange();
}
