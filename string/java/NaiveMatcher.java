
public class NaiveMatcher implements StringMatcher
{
	public int match(String text, String pattern)
	{
		int j;
		for(int i = 0; i < text.length() - pattern.length(); i++)
		{
			for(j = 0; j < pattern.length(); j++)
				if(text.charAt(i + j) != pattern.charAt(j))
					break;
			if(j == pattern.length())
				return i;
		}
		return -1;
	}
}
