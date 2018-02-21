
int gcd(int big, int small)
{
	if(small == 0)
		return big;
	return gcd(small, big % small);
}
