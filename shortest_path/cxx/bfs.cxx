#include <deque>
#include <unordered_set>
#include <vector>

// UNTESTED

// Nodes are 0 .. n-1 by default
void bfs(std::vector<std::vector<int> > adjList)
{
	std::deque<int> front(1, 0);
	std::unordered_set<int> visited;
	while(!front.empty())
	{
		int frontLen = front.size();
		for(int i = 0; i < frontLen; i++)
		{
			int node = front.front();
			front.pop_front();
			for(const int& child: adjList[node])
				if(visited.find(child) == visited.end())
				{
					front.push_back(child);
					visited.insert(child);
				}
		}
	}
}
