
import java.util.Random;

public class TestStringMatcher
{
	private static Random myrand = new Random();
	private static String genRandomString(char[] str)
	{
		for(int i = 0; i < str.length; i++)
			switch(myrand.nextInt(4))
			{
				case 0: str[i] = 'A'; break;
				case 1: str[i] = 'T'; break;
				case 2: str[i] = 'C'; break;
				case 3: str[i] = 'G'; break;
			}
		return new String(str);
	}
	private static boolean testStringMatcher(StringMatcher matcher)
	{
		char[] text = new char[2000];
		char[] pattern = new char[5];

		for(int i = 0; i < 1000; i++)
		{
			String txt = genRandomString(text);
			String pat = genRandomString(pattern);

			if(matcher.match(txt, pat) != txt.indexOf(pat))
				return false;
		}
		return true;
	}
	public static void main(String[] argv)
	{
		StringMatcher[] matchers = {
			new NaiveMatcher(), new KMPMatcher()
		};
		for(StringMatcher matcher: matchers)
			if(!testStringMatcher(matcher))
				System.out.println("WA: " + matcher);
	}
}
