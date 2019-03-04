#include <unordered_map>
#include <unordered_set>
#include <vector>

void bfs(std::unordered_map<int, std::vector<int> >& adjList, int source)
{
	std::unordered_set<int> visited = { source };
	std::vector<int> fringe = { source };
	while(not fringe.empty())
	{
		std::vector<int> children;
		for(const auto& node: fringe)
			for(const auto& child: adjList[node])
				if(visited.find(child) != visited.end())
				{
					visited.insert(child);
					children.push_back(child);
				}
		fringe = children;
	}
}
