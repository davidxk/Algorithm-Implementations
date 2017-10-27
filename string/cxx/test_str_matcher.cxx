#include <iostream>
#include <cstdlib>
#include "kmp_matcher.h"

void gen_str(std::string& str)
{
	for(int i = 0; i < str.size(); i++)
		switch(rand() % 4)
		{
			case 0: str[i] = 'A'; break;
			case 1: str[i] = 'T'; break;
			case 2: str[i] = 'C'; break;
			case 3: str[i] = 'G'; break;
		}
}

bool test_str_matcher(int (*matcher)(const std::string&, const std::string&))
{
	std::string text(2000, 'A'), pattern(5, 'T');
	for(int i = 0; i < 1000; i++)
	{
		gen_str(text);
		gen_str(pattern);

		if(text.find(pattern) != matcher(text, pattern))
			return false;
	}
	return true;
}

int main()
{
	if(!test_str_matcher(kmp_matcher))
		std::cout<<"WA: kmp_matcher"<<std::endl;
	return 0;
}
