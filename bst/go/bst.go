package main

// TreeNode is a node in a binary search tree
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// BinarySearchTree supports O(log n) set operations
type BinarySearchTree struct {
	root *TreeNode
}

// TODO: Test on leetcode
func (bst *BinarySearchTree) find(value int) bool {
	curr := bst.root
	for curr != nil {
		if value < curr.Val {
			curr = curr.Left
		} else if value > curr.Val {
			curr = curr.Right
		} else {
			return true
		}
	}
	return false
}

// TESTED on LeetCode
func (bst *BinarySearchTree) insert(value int) bool {
	if bst.root == nil {
		bst.root = &TreeNode{Val: value}
		return true
	}
	var prev, curr *TreeNode = nil, bst.root
	for curr != nil {
		prev = curr
		if value < curr.Val {
			curr = curr.Left
		} else if value > curr.Val {
			curr = curr.Right
		} else {
			return false
		}
	}
	if value < prev.Val {
		prev.Left = &TreeNode{Val: value}
	} else {
		prev.Right = &TreeNode{Val: value}
	}
	return true
}

// TODO: Test on leetcode
func (bst *BinarySearchTree) erase(value int) bool {
	var prev, curr *TreeNode = nil, bst.root
	for curr != nil && value != curr.Val {
		prev = curr
		if value < curr.Val {
			curr = curr.Left
		} else {
			curr = curr.Right
		}
	}
	if curr == nil {
		return false
	}
	if curr.Left != nil && curr.Right != nil {
		succ := curr.Right
		for curr.Left != nil {
			succ = succ.Left
		}
		succ.Left = curr.Left
		curr = curr.Right
	} else if curr.Left != nil {
		curr = curr.Left
	} else {
		curr = curr.Right
	}

	if value < prev.Val {
		prev.Left = curr
	} else if value > prev.Val {
		prev.Right = curr
	} else {
		bst.root = curr
	}
	return true
}
