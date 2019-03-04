#include <queue>
#include <vector>
#include "DisjointSet.h"

static void bfs(std::vector<std::vector<int> > adjList, int source, std::vector<bool> visited)
{
	std::queue<int> frontier;
	frontier.push(source);
	visited[source] = true;
	while(not frontier.empty())
	{
		int node = frontier.front();
		frontier.pop();
		for(const int& child: adjList[node])
			if(not visited[child])
			{
				visited[child] = true;
				frontier.push(child);
			}
	}
}

int cnt_connected_component(std::vector<std::vector<int> > adjList)
{
	std::vector<bool> visited(adjList.size(), false);
	int cnt = 0;
	for(int node = 0; node < adjList.size(); node++)
		if(not visited[node])
		{
			bfs(adjList, node, visited);
			cnt++;
		}
	return cnt;
}

DisjointSet connected_component(std::vector<std::vector<int> > adjList)
{
	DisjointSet dj(adjList.size());
	for(int node = 0; node < adjList.size(); node++)
		for(const int& child: adjList[node])
			dj.unionSet(node, child);
	return dj;
}
