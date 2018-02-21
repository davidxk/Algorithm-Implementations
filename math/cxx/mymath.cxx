#include <algorithm>

int gcd(int big, int small)
{
	while(small)
	{
		std::swap(big, small);
		small %= big;
	}
	return big;
}
