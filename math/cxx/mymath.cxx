#include <algorithm>

int gcd(int large, int small)
{
	while(small)
	{
		std::swap(large, small);
		small %= large;
	}
	return large;
}
