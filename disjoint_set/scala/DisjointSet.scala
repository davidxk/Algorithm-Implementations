import collection.mutable
import collection.immutable

class DisjointSet[T](elems: Iterable[T]) {
  val height = new mutable.HashMap[T, Int]()
  val parent = new mutable.HashMap[T, T]()
  for(elem <- elems) {
    parent(elem) = elem;
    height(elem) = 1
  }

  def makeSet(elem: T) {
    parent(elem) = elem;
    height(elem) = 1
  }
  def findSet(elem: T): T = {
    if(parent(elem) != elem)
      parent(elem) = findSet(parent(elem))
    return parent(elem)
  }
  def union(elemA: T, elemB: T) {
    val rootA: T = parent(elemA)
    val rootB: T = parent(elemB)
    if(rootA != rootB)
      link(rootA, rootB)
  }
  def link(rootA: T, rootB: T) {
    if(height(rootA) > height(rootB)) {
      parent(rootB) = rootA
      height.remove(rootB)
    } else {
      if(height(rootA) == height(rootB))
        height(rootB) += 1
      height.remove(rootA)
      parent(rootA) = rootB
    }
  }
  def count(): Int = {
    return height.size
  }
  def clear() {
    height.clear()
    parent.clear()
  }
  def partition(): immutable.Iterable[Seq[T]] = {
    val mapping = mutable.HashMap[T, mutable.ArrayBuffer[T]]().empty
    for((elem, daddy) <- parent) {
      if(!mapping.contains(daddy))
        mapping(daddy) = new mutable.ArrayBuffer[T]()
      mapping(daddy) += elem
    }
    val parts = immutable.Iterable[Seq[T]]() ++ mapping
      .values
      .map(_.toSeq)
    return parts
  }
}
