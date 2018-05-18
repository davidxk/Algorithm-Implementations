#include "HashSet.h"

HashSet::HashSet(): primeIdx(0), _size(0)
{
	table.resize(primes[primeIdx]);
}

int HashSet::primes[32] = {
	53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317,
	196613, 393241, 786433, 1572869, 3145739, 6291469, 12582917, 25165843,
	50331653, 100663319, 201326611, 402653189, 805306457, 1610612741
};

int HashSet::myhash(const int& x) const
{
	int hashVal = x;
	hashVal %= table.size();
	if(hashVal < 0)
		hashVal += table.size();
	return hashVal;
}

void HashSet::clear()
{
	_size = 0;
	for(int i = 0; i < table.size(); i++)
		table[i].clear();
}

bool HashSet::contains(const int& x) const
{
	const std::list<int>& theList = table[myhash(x)];
	return std::find(theList.begin(), theList.end(), x) != theList.end();
}

bool HashSet::erase(const int& x)
{
	std::list<int>& theList = table[myhash(x)];
	std::list<int>::iterator it = std::find(theList.begin(), theList.end(), x);

	if(it == theList.end())
		return false;
	theList.erase(it);
	_size--;
	return true;
}

bool HashSet::insert(const int& x)
{
	std::list<int>& theList = table[myhash(x)];
	if(std::find(theList.begin(), theList.end(), x) != theList.end())
		return false;
	theList.push_back(x);
	if(++_size > table.size())
		this->rehash();
	return true;
}

void HashSet::rehash()
{
	std::vector<std::list<int> > oldTable( primes[++primeIdx] );
	table.swap(oldTable);
	_size = 0;
	for(int i = 0; i < oldTable.size(); i++)
	{
		std::list<int>::iterator it = oldTable[i].begin();
		while(it != oldTable[i].end())
			this->insert(*it++);
	}
}
