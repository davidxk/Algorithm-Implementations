
struct myvector
{
	void** data;
	int _size;
	int _capacity;
	void (*init)(struct myvector*);
	void (*copy)(struct myvector*, const struct myvector*);
	int (*empty)(struct myvector*);
	int (*size)(const struct myvector*);
	void (*push_back)(struct myvector*, void*);
	void (*pop_back)(struct myvector*);
	void* (*front)(const struct myvector*);
	void* (*back)(const struct myvector*);
	void (*destroy)(struct myvector*);
};

void init(struct myvector* vec);
void copy(struct myvector* vec, const struct myvector* other);
int empty(struct myvector* vec);
int size(const struct myvector* vec);
void push_back(struct myvector* vec, void* elem);
void pop_back(struct myvector* vec);
void* front(const struct myvector* vec);
void* back(const struct myvector* vec);
void destroy(struct myvector* vec);
