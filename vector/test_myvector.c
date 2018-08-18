#include <stdio.h>
#include <stdlib.h>
#include "myvector.c"

int test_myvector()
{
	long i, j;
	struct myvector vec;
	init(&vec);
	for(i = 0; i < 9999; i++)
	{
		vec.push_back(&vec, (void*)i);
		if(vec.size(&vec) != i + 1 || vec._capacity < vec.size(&vec) ||
				vec.front(&vec) != (void*) 0 || vec.back(&vec) != (void*) i)
		{
			vec.destroy(&vec);
			return 0;
		}
		if(i < 512)
			continue;
		for(j = 0; j < i + 1; j++)
			if((long)vec.data[j] != j)
			{
				vec.destroy(&vec);
				return 0;
			}
	}
	struct myvector vec2;
	copy(&vec2, &vec);
	for(i = 0; i < 9999; i++)
		if(vec2.data[i] != (void*) i || vec.data[i] != (void*) i|| &vec2.data[i] == &vec.data[i])
		{
			vec.destroy(&vec);
			vec2.destroy(&vec2);
			return 0;
		}
	vec.destroy(&vec);
	vec2.destroy(&vec2);
	return 1;
}

int main()
{
	if(!test_myvector())
		printf("WA: myvector");
	return 0;
}
