#ifndef __HASH_TABLE__
#define __HASH_TABLE__

#include <algorithm>
#include <list>
#include <vector>

class HashSet
{
public:
	explicit HashSet();
	bool contains(const int& x) const;
	void clear();
	bool insert(const int& x);
	bool erase(const int& x);
	int size() { return _size; };
private:
	static int primes[32];
	std::vector<std::list<int> > table;
	int _size;
	int primeIdx;
	void rehash();
	int myhash(const int& x) const;
};

#endif
