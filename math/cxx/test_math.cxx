#include <cassert>
#include "mymath.cxx"

void test_gcd()
{
	assert(gcd(16, 40) == 8);
	assert(gcd(100, 40) == 20);
}

int main()
{
	test_gcd();
	return 0;
}
