
struct myvector
{
	int* data;
	int _size;
	int _capacity;
	void (*init)(struct myvector*);
	int (*empty)(struct myvector*);
	int (*size)(struct myvector*);
	void (*push_back)(struct myvector*, int);
	void (*pop_back)(struct myvector*);
	int (*back)(struct myvector*);
	void (*destroy)(struct myvector*);
};

void init(struct myvector* vec);
int empty(struct myvector* vec);
int size(struct myvector* vec);
void push_back(struct myvector* vec, int num);
void pop_back(struct myvector* vec);
int back(struct myvector* vec);
void destroy(struct myvector* vec);
