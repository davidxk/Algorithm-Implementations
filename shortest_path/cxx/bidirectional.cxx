#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

int bidirectional(std::unordered_map<int, std::vector<int> >& adjList, const int source, const int dest)
{
	std::vector<std::unordered_set<int> > fronts =  {{source}, {dest}};
	std::vector<std::unordered_set<int> > visited = {{source}, {dest}};
	std::unordered_set<int> border;
	while(not fronts[0].empty() and not fronts[1].empty() and border.empty())
	{
		int smaller = fronts[0].size() < fronts[1].size() ? 0 : 1;
		int larger = not smaller;
		std::unordered_set<int> children;
		for(const auto& node: fronts[smaller])
			for(const auto& child: adjList[node])
			{
				if(fronts[larger].find(child) != fronts[larger].end())
					border.insert(child);
				if(visited[smaller].find(child) == visited[smaller].end())
				{
					children.insert(child);
					visited[smaller].insert(child);
				}
			}
		fronts[smaller] = children;
	}
	return 0;
}
