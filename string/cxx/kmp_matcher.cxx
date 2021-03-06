#include <string>
#include <vector>

void compute_prefix_function(const std::string& pattern, std::vector<int>& pi)
{
	int matched = 0;
	for(int i = 1; i < pattern.size(); i++)
	{
		while(matched > 0 and pattern[i] != pattern[matched])
			matched = pi[matched - 1];

		if(pattern[i] == pattern[matched])
			matched++;
		pi[i] = matched;
	}
}

int kmp_matcher(const std::string& text, const std::string& pattern)
{
	std::vector<int> pi(pattern.size(), 0);
	compute_prefix_function(pattern, pi);
	int matched = 0;
	for(int i = 0; i < text.size(); i++)
	{
		while(matched > 0 and text[i] != pattern[matched])
			matched = pi[matched - 1];

		if(text[i] == pattern[matched])
			matched++;
		if(matched == pattern.size())
			return i - matched + 1;
	}
	return -1;
}
