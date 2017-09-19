#include <stdio.h>
#include <stdlib.h>
#include "myvector.c"

int test_myvector()
{
	int i, j;
	struct myvector vec;
	init(&vec);
	for(i = 0; i < 99999; i++)
	{
		vec.push_back(&vec, i);
		if(vec.size(&vec) != i + 1 || vec._capacity < vec.size(&vec))
		{
			vec.destroy(&vec);
			return 0;
		}
		if(i < 512)
			continue;
		for(j = 0; j < i + 1; j++)
			if(vec.data[j] != j)
			{
				vec.destroy(&vec);
				return 0;
			}
	}
	vec.destroy(&vec);
	return 1;
}

int main()
{
	printf("This test takes approximately 20 seconds to run ...\n");
	if(!test_myvector())
		printf("WA: myvector");
	return 0;
}
