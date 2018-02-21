import java.math.*;
import java.util.Random;

class TestMyMath
{
	public static MyMath mymath = new MyMath();
	public static Random myrand = new Random();
	public static void testGCD()
	{
		for(int i = 0; i < 100; i++)
		{
			BigInteger a = new BigInteger(20, myrand);
			BigInteger b = new BigInteger(20, myrand);
			if(mymath.gcd(a.intValue(), b.intValue()) != a.gcd(b).intValue())
				System.out.println("GCD Error!");
		}
	}
	public static void main(String[] argv)
	{

	}
}
