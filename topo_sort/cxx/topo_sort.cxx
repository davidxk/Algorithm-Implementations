#include <climits>
#include <vector>
#include <stack>

std::vector<int> topo_sort(int nNodes, std::vector<std::pair<int, int> > edges)
{
	std::vector<std::vector<int> > adjList(nNodes, std::vector<int>());
	std::vector<int> indegree(nNodes, 0);
	for(const std::pair<int, int>& edge: edges)
	{
		adjList[edge.first].push_back(edge.second);
		indegree[edge.second]++;
	}
	std::stack<int> front;
	for(int node = 0; node < nNodes; node++)
		if(indegree[node] == 0)
			front.push(node);
	std::vector<int> result;
	while(not front.empty())
	{
		int node = front.top();
		result.push_back(node);
		front.pop();
		for(const int& child: adjList[node])
		{
			indegree[child]--;
			if(indegree[child] == 0)
				front.push(child);
		}
	}
	for(int node = 0; node < nNodes; node++)
		if(indegree[node] != 0)
		{
			result.clear();
			break;
		}
	return result;
}

std::vector<int> viterbi_shortest_path(int nNodes, std::vector<std::vector<int> > edges)
{
	std::vector<std::vector<std::pair<int, int> > > adjList(nNodes, std::vector<std::pair<int, int> >());
	std::vector<int> indegree(nNodes, 0);
	int u, v, w;
	for(const std::vector<int>& edge: edges)
	{
		u = edge[0], v = edge[1], w = edge[2];
		adjList[u].push_back(std::make_pair(v, w));
		indegree[v]++;
	}
	std::stack<int> front;
	std::vector<int> dist(nNodes, INT_MAX);
	for(int node = 0; node < nNodes; node++)
		if(indegree[node] == 0)
		{
			front.push(node);
			dist[node] = 0;
		}
	while(not front.empty())
	{
		int node = front.top();
		front.pop();
		for(const std::pair<int, int>& child: adjList[node])
		{
			if(dist[node] + child.second < dist[child.first])
				dist[child.first] = dist[node] + child.second;
			indegree[child.first] -= 1;
			if(indegree[child.first] == 0)
				front.push(child.first);
		}
	}
	return dist;
}

enum Color{ WHITE = 0, GREY = 1, BLACK = 2 };
static void dfs_visit(int node, std::vector<std::vector<int> > adjList,
		std::vector<Color>& color, std::vector<int>& result)
{
	if(color[node] == GREY)
		return;
	color[node] = GREY;
	for(const int& child: adjList[node])
		if(color[child] == WHITE)
			dfs_visit(child, adjList, color, result);
	color[node] = BLACK;
	result.push_back(node);
}

std::vector<int> dfs_based(int nNodes, std::vector<std::pair<int, int> > edges)
{
	std::vector<std::vector<int> > adjList(nNodes, std::vector<int>());
	for(const std::pair<int, int>& edge: edges)
		adjList[edge.second].push_back(edge.first);
	std::vector<Color> color(nNodes, WHITE);
	std::vector<int> result;
	for(int node = 0; node < nNodes; node++)
		if(color[node] == WHITE)
			dfs_visit(node, adjList, color, result);
	return result;
}

static int dp_visit(int node, std::vector<std::vector<std::pair<int, int> > > adjList, std::vector<int>& dist)
{
	if(dist[node] != INT_MAX)
		return dist[node];
	int child, weight;
	for(const std::pair<int, int>& item: adjList[node])
	{
		child = item.first, weight = item.second;
		dist[child] = std::min(dp_visit(child, adjList, dist) + weight, dist[child]);
	}
	if(dist[node] == INT_MAX)
		dist[node] = 0;
	return dist[node];
}

std::vector<int> dp_shortest_path(int nNodes, std::vector<std::vector<int> > edges)
{
	std::vector<std::vector<std::pair<int, int> > > adjList(nNodes, std::vector<std::pair<int, int> >());
	int u, v, w;
	for(const std::vector<int>& edge: edges)
	{
		u = edge[0], v = edge[1], w = edge[2];
		adjList[v].push_back(std::make_pair(u, w));
	}
	std::vector<int> dist(nNodes, INT_MAX);
	for(int node = 0; node < nNodes; node++)
		dp_visit(node, adjList, dist);
	return dist;
}
