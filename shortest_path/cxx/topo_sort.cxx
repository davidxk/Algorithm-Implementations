#include <queue>
#include <unordered_map>
#include <vector>

template<class T>
std::vector<int> topo_sort(const std::unordered_map<T, std::vector<T> >& adjList)
{
	std::unordered_map<T, int> indegree;
	for(const auto& list: adjList)
		for(const auto& neighbour: list.second)
			indegree[neighbour]++;
	std::queue<T> fringe;
	for(const auto& node: adjList)
		if(indegree[node.first] == 0)
			fringe.push(node.first);
	std::vector<int> result;
	while(not fringe.empty())
	{
		auto node = fringe.front();
		result.push_back(node);
		fringe.pop();
		for(const auto& neighbour: adjList[node])
		{
			indegree[neighbour]--;
			if(indegree[neighbour] == 0)
				fringe.push(neighbour);
		}
	}
	return result;
}
