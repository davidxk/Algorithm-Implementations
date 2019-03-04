#ifndef __HASH_TABLE__
#define __HASH_TABLE__

#include <algorithm>
#include <list>
#include <vector>

template<typename T>
class HashTable
{
public:
	explicit HashTable();
	bool contains(const T& x) const;
	void clear();
	bool insert(const T& x);
	bool erase(const T& x);
	int size() { return _size; };
private:
	static int primes[32];
	std::vector<std::list<T> > table;
	int _size;
	int _primeIdx;
	void rehash();
	int myhash(const T& x) const;
};

template<typename T>
int hash(const T& x);

#endif

template<typename T>
HashTable<T>::HashTable(): _primeIdx(0)
{
	_size = primes[_primeIdx];
}

template<typename T>
int HashTable<T>::primes[32] = {
	53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317,
	196613, 393241, 786433, 1572869, 3145739, 6291469, 12582917, 25165843,
	50331653, 100663319, 201326611, 402653189, 805306457, 1610612741
};

template<typename T>
int HashTable<T>::myhash(const T& x) const
{
	int hashVal = hash(x);
	hashVal %= table.size();
	if(hashVal < 0)
		hashVal += table.size();
	return hashVal;
}

template<typename T>
void HashTable<T>::clear()
{
	for(int i = 0; i < table.size(); i++)
		table[i].clear();
}

template<typename T>
bool HashTable<T>::contains(const T& x) const
{
	const std::list<T>& theList = table[myhash(x)];
	return std::find(theList.begin(), theList.end(), x) != theList.end();
}

template<typename T>
bool HashTable<T>::erase(const T& x)
{
	std::list<T>& theList = table[myhash(x)];
	typename std::list<T>::iterator it = std::find(theList.begin(), theList.end(), x);

	if(it == theList.end())
		return false;
	theList.erase(it);
	_size--;
	return true;
}

template<typename T>
bool HashTable<T>::insert(const T& x)
{
	std::list<T>& theList = table[myhash(x)];
	if(std::find(theList.begin(), theList.end(), x) != theList.end())
		return false;
	theList.push_back(x);
	if(++_size > table.size())
		this->rehash();
	return true;
}

template<typename T>
void HashTable<T>::rehash()
{
	std::vector<std::list<T> > oldTable( primes[++_primeIdx] );
	table.swap(oldTable);
	_size = 0;
	for(int i = 0; i < oldTable.size(); i++)
	{
		typename std::list<T>::iterator it = oldTable[i].begin();
		while(it != oldTable[i].end())
			this->insert(*it++);
	}
}
