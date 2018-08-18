#include <stdlib.h>
#include <string.h>
#include "myvector.h"

void init(struct myvector* vec)
{
	vec->init = init;
	vec->copy = copy;
	vec->size = size;
	vec->push_back = push_back;
	vec->front = front;
	vec->back = back;
	vec->destroy = destroy;
	vec->_size = 0;
	vec->_capacity = 512;
	vec->data = (void**) malloc(sizeof(void*) * vec->_capacity);
}

void copy(struct myvector* vec, const struct myvector* other)
{
	vec->init = init;
	vec->copy = copy;
	vec->size = size;
	vec->push_back = push_back;
	vec->front = front;
	vec->back = back;
	vec->destroy = destroy;
	vec->_size = other->_size;
	vec->_capacity = other->_capacity;
	vec->data = (void**) malloc(sizeof(void*) * vec->_capacity);
	memcpy(vec->data, other->data, sizeof(void*) * vec->_capacity);
}

int empty(struct myvector* vec)
{
	return vec->_size == 0;
}

int size(const struct myvector* vec)
{
	return vec->_size;
}
 
void push_back(struct myvector* vec, void* elem)
{
	vec->_size++;
	if(vec->_size > vec->_capacity)
	{
		void* newloc = (void**) malloc(sizeof(void*) * vec->_capacity * 2);
		memcpy(newloc, vec->data, sizeof(void*) * vec->_capacity);
		free(vec->data);
		vec->data = newloc;
		vec->_capacity *= 2;
	}
	vec->data[vec->_size - 1] = elem;
}

void pop_back(struct myvector* vec)
{
	vec->_size -= 1;
}

void* front(const struct myvector* vec)
{
	return vec->data[0];
}

void* back(const struct myvector* vec)
{
	return vec->data[vec->_size - 1];
}

void destroy(struct myvector* vec)
{
	free(vec->data);
	vec->data = NULL;
	vec->_size = 0;
	vec->_capacity = 0;
}
