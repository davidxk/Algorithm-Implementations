#include "binary_indexed_tree.h"
#include <stdlib.h>
#include <string.h>

BinaryIndexedTree* bit_init(int* array, int n)
{
	BinaryIndexedTree*bit=(BinaryIndexedTree*)malloc(sizeof(BinaryIndexedTree));
	bit->get_sum = bit_get_sum;
	bit->update = bit_update;
	bit->get_range = bit_get_range;
	bit->destroy = bit_destroy;

	bit->tree = (int*)malloc(sizeof(int) * (n + 1));
	bit->treesz = n + 1;
	bit->tree[0] = 0;
	memcpy(bit->tree + 1, array, sizeof(int) * n);
	int i, j;
	for(i = 1; i < n + 1; i++)
	{
		j = i + (i & (-i));
		if(j < bit->treesz)
			bit->tree[j] += bit->tree[i];
	}
	return bit;
}

int bit_get_sum(BinaryIndexedTree* bit, int i)
{
	i += 1;
	int sum = 0;
	while(i > 0)
	{
		sum += bit->tree[i];
		i -= i & (-i);
	}
	return sum;
}

void bit_update(BinaryIndexedTree* bit, int i, int delta)
{
	i += 1;
	while(i < bit->treesz)
	{
		bit->tree[i] += delta;
		i += i & (-i);
	}
}

int bit_get_range(BinaryIndexedTree* bit, int i, int j)
{
	return bit_get_sum(bit, j) - bit_get_sum(bit, i - 1);
}

void bit_destroy(BinaryIndexedTree* bit)
{
	free(bit->tree);
	bit->treesz = 0;
	free(bit);
}
