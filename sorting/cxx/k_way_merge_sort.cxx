#include <queue>
#include <vector>

std::vector<int> k_way_merge_sort(const std::vector<std::vector<int> >& arrays)
{
	std::vector<int> indices;
	std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int> >,
		std::greater<> > heap;
	for(int k = 0; k < arrays.size(); k++)
		if(!arrays[k].empty())
		{
			indices.push_back(0);
			heap.push(std::make_pair(arrays[k][0], k));
		}
	std::vector<int> result;
	std::pair<int, int> top;
	int k;
	while(!heap.empty())
	{
		top = heap.top();
		k = top.second;
		result.push_back(top.first);
		heap.pop();
		indices[k]++;
		if(indices[k] < arrays[top.second].size())
			heap.push(std::make_pair(arrays[k][indices[k]], k));
	}
	return result;
}
