#include "binary_indexed_tree.h"

#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

BinaryIndexedTree* bit;
const int LENGTH = 100;
int array[LENGTH];

void set_up()
{
	for(int i = 0; i < LENGTH; i++)
		array[i] = rand() % 100;
	bit = bit_init(array, LENGTH);
}

void break_down()
{
	bit->destroy(bit);
	free(bit);
}

void test_get_sum()
{
	set_up();
	int right, sum;
	for(int cnt = 0; cnt < 100; cnt++)
	{
		right = rand() % LENGTH;
		sum = 0;
		for(int i = 0; i <= right; i++)
			sum += array[i];
		if(bit->get_sum(bit, right) != sum)
			printf("Error in test_get_sum: expect %d, got %d",
					sum, bit->get_sum(bit, right));
	}
	break_down();
}

void test_update()
{
	set_up();
	int right, sum;
	int index, delta;
	for(int cnt = 0; cnt < 100; cnt++)
	{
		index = rand() % LENGTH;
		delta = rand() % 100;
		array[index] += delta;
		bit->update(bit, index, delta);
		right = rand() % LENGTH;
		sum = 0;
		for(int i = 0; i <= right; i++)
			sum += array[i];
		assert(bit->get_sum(bit, right) == sum);
	}
	break_down();
}

void test_get_range()
{
	set_up();
	int left, right, sum;
	for(int cnt = 0; cnt < 100; cnt++)
	{
		left = rand() % LENGTH/2;
		right = left + rand() % LENGTH/2;
		sum = 0;
		for(int i = left; i <= right; i++)
			sum += array[i];
		assert(bit->get_range(bit, left, right) == sum);
	}
	break_down();
}

int main()
{
	srand(time(NULL));
	test_get_sum();
	test_update();
	test_get_range();

}
