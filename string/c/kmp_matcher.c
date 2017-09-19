#include <string.h>
#include <stdlib.h>

void compute_prefix_function(const char* pattern, int* pi)
{
	pi[0] = 0;
	int matched = 0, i;
	for(i = 1; i < strlen(pattern); i++)
	{
		while(matched > 0 && pattern[i] != pattern[matched])
			matched = pi[matched - 1];
		if(pattern[i] == pattern[matched])
			matched++;
		pi[i] = matched;
	}
}

int kmp_matcher(const char* text, const char* pattern)
{
	int* pi = (int*) malloc(sizeof(int) * strlen(pattern));
	compute_prefix_function(pattern, pi);

	int matched = 0, i;
	for(i = 0; i < strlen(text); i++)
	{
		while(matched > 0 && text[i] != pattern[matched])
			matched = pi[matched - 1];

		if(text[i] == pattern[matched])
			matched++;
		if(matched == strlen(pattern))
		{
			free(pi);
			return i - matched + 1;
		}
	}
	free(pi);
	return -1;
}
