
int default_is_head(int elem);
int default_is_tail(int elem);
void three_way_partition(int* array, int n, int (*is_head)(int), 
		int (*is_tail)(int));
