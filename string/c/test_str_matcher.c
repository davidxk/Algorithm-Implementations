#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "kmp_matcher.h"

void gen_str(char* str, int size)
{
	int i;
	for(i = 0; i < size; i++)
		switch(rand() % 4)
		{
			case 0: str[i] = 'A'; break;
			case 1: str[i] = 'T'; break;
			case 2: str[i] = 'C'; break;
			case 3: str[i] = 'G'; break;
		}
	str[size - 1] = '\0';
}

int test_str_matcher(int (*matcher)(const char*, const char*))
{
	int i;
	char text[2001], pattern[6];

	char* ans = NULL;
	int retval = -1;
	for(i = 0; i < 1000; i++)
	{
		gen_str(text, 2001);
		gen_str(pattern, 6);

		ans = strstr(text, pattern);
		retval = matcher(text, pattern);

		if(ans == NULL && retval != -1)
			return 0;
		else if(ans != NULL && ans - text != retval)
			return 0;
	}
	return 1;
}

int main()
{
	if(!test_str_matcher(kmp_matcher))
		printf("WA: kmp_matcher\n");
	return 0;
}
