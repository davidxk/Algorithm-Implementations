#include <vector>

bool default_is_head(int elem);
bool default_is_tail(int elem);
void three_way_partition(std::vector<int>& array,
		bool (*is_head)(int) = default_is_head,
		bool (*is_tail)(int) = default_is_tail);
