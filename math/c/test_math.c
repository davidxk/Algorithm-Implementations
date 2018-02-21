#include <assert.h>
#include "mymath.c"

void test_gcd()
{
	assert(gcd(40, 16) == 8);
	assert(gcd(100, 16) == 4);
}

int main()
{
	test_gcd();
	return 0;
}
