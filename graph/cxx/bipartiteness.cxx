#include <queue>
#include <vector>

static bool bfs_alternate_test(std::vector<std::vector<int> > adjList, int node, std::vector<int> layer)
{
	std::queue<int> frontier;
	frontier.push(node);
	layer[node] = 0;
	while(not frontier.empty())
	{
		int node = frontier.front();
		frontier.pop();
		for(const int& child: adjList[node])
			if(layer[child] == layer[node])
				return false;
			else if(layer[child] == -1)
			{
				frontier.push(child);
				layer[child] = layer[node] ^ 1;
			}
	}
	return true;
}

bool is_bipartite(std::vector<std::vector<int> > adjList)
{
	std::vector<int> layer(adjList.size(), -1);
	for(int node = 0; node < adjList.size(); node++)
	{
		if(layer[node] == -1)
			if(not bfs_alternate_test(adjList, node, layer))
				return false;
	}
	return true;
}
