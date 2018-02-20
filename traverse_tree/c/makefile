a.out: TreeNode.h ../../vector/myvector.* stack_traversal.c recursive_traversal.c test_traversal.c
	gcc test_traversal.c ../../vector/myvector.o
../../vector/myvector.o: ../../vector/myvector.h ../../vector/myvector.c
	pushd ../../vector; gcc -c myvector.c; popd

.PHONY: clean
clean:
	rm -f *.o a.out
