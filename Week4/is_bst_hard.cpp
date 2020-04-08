#include <bits/stdc++.h>
using namespace std;

struct Node {
  long long int key;
  int left;
  int right;

  Node() : key(0), left(-1), right(-1) {}
  Node(int key_, int left_, int right_) : key(key_), left(left_), right(right_) {}
};
long long int pre_order(const vector<Node>& tree, int i, int dir, int& flag) {
  if(flag == 0) return 0;
  long long int smallest, largest;
  if(tree[i].left == -1) {
    if(tree[i].right == -1) return tree[i].key;
    else smallest = pre_order(tree, tree[i].right, 1, flag);
    if(flag == 0) return 0;
    if(tree[i].key > smallest) flag = 0;
    else {
      if(dir == -1) return smallest;
      else if(dir == 1) return tree[i].key;
      else return flag;
    }
  }
  else {
    largest = pre_order(tree, tree[i].left, -1, flag);
    if(tree[i].right == -1) {
      if(flag == 0) return 0;
      if(tree[i].key <= largest) flag = 0;
      else {
        if(dir == -1) return tree[i].key;
        else if(dir == 1) return largest;
        else return flag;
      }
      return 0;
    }
    else smallest = pre_order(tree, tree[i].right, 1, flag);
    if(flag == 0) return 0;
    if(tree[i].key > smallest || tree[i].key <= largest) flag = 0;
    else {
      if(dir == -1) return smallest;
      else if(dir == 1) return largest;
      else return flag;
    }
    return 0;
  }
  return 0;
}
bool IsBinarySearchTree(const vector<Node>& tree) {
  if(tree.size() == 0) return true;
  int flag = 1;
  pre_order(tree, 0, 0, flag);
  if(flag == 0) return false;
  return true;
}

int main() {
  int nodes;
  cin >> nodes;
  vector<Node> tree;
  for (int i = 0; i < nodes; ++i) {
    int key, left, right;
    cin >> key >> left >> right;
    tree.push_back(Node(key, left, right));
  }
  if (IsBinarySearchTree(tree)) {
    cout << "CORRECT" << endl;
  } 
  else {
    cout << "INCORRECT" << endl;
  }
  return 0;
}
