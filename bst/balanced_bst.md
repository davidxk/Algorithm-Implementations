# BST
| Operation   | Complexity |
| ---------   | --------   |
| first()     | O(log n)   |
| last()      | O(log n)   |
| add(x)      | O(log n)   |
| remove(x)   | O(log n)   |
| contains(x) | O(log n)   |
| floor(x)    | O(log n)   |
| ceiling(x)  | O(log n)   |

BST is the ultimate, heavy-weight weapon that provides useful operations running in logarithmic time. However, due to the complexity in implementing a balanced BST, we often want to use some simpler alternative methods, for example a heap or a sorted list. Here is a comparison.

## Compared to Heap
Binary Search Tree stores value information of a set of data like a heap. While heap only support O(log n) find minimum operation, BST offers more fine grind operations within logarithmic time.

* remove(x)
* contains(x)
* floor(x)
* ceiling(x)

Essentially, it maintains not only the information of the maximum or minimum, but comparative relationship between *all pair of nodes* in the tree.

Another difference is that BST is a set which doesn't contain any duplicate elements while a heap could contain duplicate elements.

## Compared to Sorted List
An alternative to a BST is using a sorted list, which supports many of the operations provided by a BST within the same complexity.

| Operation   | Complexity |
| ---------   | --------   |
| first()     | O(1)       |
| last()      | O(1)       |
| contains(x) | O(log n)   |
| floor(x)    | O(log n)   |
| ceiling(x)  | O(log n)   |

However the data has to be read-only, since modification to the sorted list takes O(n) time.

A sorted list may also include duplicate values which is not typically supported by a BST.

## Balanced Binary Search Tree
A binary search tree of height `h` can support any of the basic dynamic-set operations—such as SEARCH, PREDECESSOR, SUCCESSOR, MINIMUM, MAXIMUM, INSERT, and DELETE—in O(log n) time. Thus, the set operations are fast if the height of the search tree is small. If its height is large, however, the set operations may run no faster than with a linked list.

For example If the input comes into a tree presorted, then a series of inserts will take quadratic time and give a very expensive implementation of a linked list, since the tree will consist only of nodes with no left children. One solution to this problem is to insist on an extra structural condition called balance: no node is allowed to get too deep.

A red-black tree is a binary search tree with one extra bit of storage per node: its color, which can be either RED or BLACK. By constraining the node colors on any simple path from the root to a leaf, red-black trees ensure that no such path is more than twice as long as any other, so that the tree is approximately balanced.

An AVL (Adelson-Velskii and Landis) tree is a binary search tree with a balance condition that insist for every node in the tree, the height of the left and rightsubtrees can differ by at most 1.

AVL tree was the first self-balancing binary search tree to be invented. It is named after its two Soviet inventors, Georgy Adelson-Velsky and Evgenii Landis, who published it in their 1962 paper.

## Red-Black Tree vs. AVL Tree
> What's the main reason for choosing Red black trees instead of AVL trees?

* For a look-up intensive task use an AVL tree.
* For an insert intensive tasks use a Red-Black tree.

AVL trees maintain a more rigid balance than red-black trees. The path from the root to the deepest leaf in an AVL tree is at most ~1.44 lg(n+2), while in red black trees it's at most ~2 lg (n+1).

As a result, lookup in an AVL tree is typically faster, but this comes at the cost of slower insertion and deletion due to more rotation operations. So use an AVL tree if you expect the number of lookups to dominate the number of updates to the tree.

For a Red Black tree, rebalancing operations necessary to restore the tree properties takes is O(1) time. At most a double left or right rotation is needed. For an AVL tree, rebalancing complexity O(log N). This is where Red Black tree gains over AVL.

The reason it matters that red-black trees require O(1) rebalancing operations, comes up in the application to persistent data structures. A persistent data structure makes it possible to roll back any algorithm to a previous step. To do so, it must keep a trail of updates. Any persistent data structure based on an AVL tree is going to have to store O(log n) times as many updates as one based on a red-black tree. So ultimately, the constant-rebalancing is necessary to improve the speed of certain algorithms.

> What are the application of Red black tree?

Red-black trees are more general purpose. They do relatively well on add, remove, and look-up but AVL trees have faster look-ups at the cost of slower add/remove. Red-black tree is used in the following:

* Java: java.util.TreeMap , java.util.TreeSet
* C++ STL: map, multimap, multiset
* Linux kernel: completely fair scheduler, linux/rbtree.h
