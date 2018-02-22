
struct myvector
{
	void** data;
	int _size;
	int _capacity;
	void (*init)(struct myvector*);
	int (*empty)(struct myvector*);
	int (*size)(struct myvector*);
	void (*push_back)(struct myvector*, void*);
	void (*pop_back)(struct myvector*);
	void* (*back)(struct myvector*);
	void (*destroy)(struct myvector*);
};

void init(struct myvector* vec);
int empty(struct myvector* vec);
int size(struct myvector* vec);
void push_back(struct myvector* vec, void* elem);
void pop_back(struct myvector* vec);
void* back(struct myvector* vec);
void destroy(struct myvector* vec);
