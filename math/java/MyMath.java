
class MyMath
{
	public int gcd(int large, int small)
	{
		if(small == 0)
			return large;
		return gcd(small, large % small);
	}
}
