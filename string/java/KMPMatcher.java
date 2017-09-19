
class KMPMatcher implements StringMatcher
{
	public int match(String text, String pattern)
	{
		int[] pi = computePrefixFunction(pattern);
		int matched = 0;
		for(int i = 0; i < text.length(); i++)
		{
			while(matched > 0 && text.charAt(i) != pattern.charAt(matched))
				matched = pi[matched - 1];

			if(text.charAt(i) == pattern.charAt(matched))
				matched++;
			if(matched == pattern.length())
				return i - matched + 1;
		}
		return -1;
	}
	public int[] computePrefixFunction(String pattern)
	{
		int[] pi = new int[ pattern.length() ];
		int matched = 0;
		for(int i = 1; i < pattern.length(); i++)
		{
			while(matched > 0 && pattern.charAt(i) != pattern.charAt(matched))
				matched = pi[matched - 1];

			if(pattern.charAt(i) == pattern.charAt(matched))
				matched++;
			pi[i] = matched;
		}
		return pi;
	}
}

