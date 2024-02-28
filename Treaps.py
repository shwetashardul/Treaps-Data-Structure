import random
class Node:
    def __init__(self, key, priority):
        self.key= key
        self.priority= priority
        self.left= None
        self.right= None

class Treaps:
    def __init__(self):
        self.root= None

    def l_rotate(self,p):
        if p is None or p.right is None: #cannot perform left rotation
          return p
        q=p.right
        p.right=q.left
        q.left=p
        return q

    def r_rotate(self,q):
        if q is None or q.left is None:  #cannot perform right rotation
          return q
        p=q.left
        q.left=p.right
        p.right=q
        return p

    def insert_node(self, root, key, priority): #logic for inserting a new node
        if root is None:
            return Node(key, priority)
        if key== root.key:
            root.priority=priority
        elif key<root.key: #insert in the left subtree
            root.left=self.insert_node(root.left, key, priority)
            if root.left.priority>root.priority:
                root=self.r_rotate(root)
        else:  #insert in the right subtree
            root.right= self.insert_node(root.right, key , priority)
            if root.right.priority> root.priority:
                root= self.l_rotate(root)

        return root

    def insertWithPriority(self, key, priority):
        self.root= self.insert_node(self.root,key,priority)

    def insert(self,key):
        priority=random.random()
        self.insertWithPriority(key, priority)

    def remove_node(self,root,key):
        if root is None:
            print(f"Key {key} was not found in the Treap.")
            return None,None
        if key<root.key:
            root.left, priority=self.remove_node(root.left,key)
        elif key>root.key:
            root.right, priority=self.remove_node(root.right,key)
        else:#Node Found
            if root.left is None:
                return root.right, root.priority
            elif root.right is None:
                return root.left,root.priority
            else:
                if root.left.priority>root.right.priority:
                    root=self.r_rotate(root) #right rotate then remove
                    root.right, priority= self.remove_node(root.right,key)
                else:
                    root=self.l_rotate(root) #left rotate then remove
                    root.left, priority= self.remove_node(root.left,key)

        return root, priority

    def remove(self,key):
        self.root, priority=self.remove_node(self.root, key)
        return priority

    def find_node(self,root,key):
        if root is None:
            return 0
        if key<root.key:
            return self.find_node(root.left,key)
        elif(key>root.key):
            return self.find_node(root.right,key)
        else:
            return root.priority

    def find(self,key):
        return self.find_node(self.root,key)

    def split_treap(self,node,key,depth=0):
        #print(f"Recursion depth: {depth}, Node key: {node.key if node else 'None'}")
        if not node:
            return(None, None)

        if key<node.key:
            left_split,right_split=self.split_treap(node.left,key)
            node.left=right_split

            if node.left and node.left.priority>node.priority:
                node=self.r_rotate(node)
            return (left_split,node)
        else:
            left_split,right_split=self.split_treap(node.right,key)
            node.right=left_split

            if node.right and node.right.priority>node.priority:
                node=self.l_rotate(node)
            return (node,right_split)

    def split(self,key):
        left_split,right_split=self.split_treap(self.root,key)
        self.root=right_split
        return left_split,right_split

    def join_treaps(self, root1,root2,depth=0):
        if depth>1000:
           print("Deep recursion detected")
           return None
        if not root1:
            return root2
        if not root2:
            return root1

        if root1.priority>root2.priority:
            root1.right=self.join_treaps(root1.right,root2)
            return root1
        else:
            root2.left=self.join_treaps(root1, root2.left)
            return root2
    def join(self,T):
        self.root=self.join_treaps(self.root, T.root)

    def treap_size(self,node):
        if node is None:
            return 0
        return (1+self.treap_size(node.left)+ self.treap_size(node.right))

    def size(self):
        return self.treap_size(self.root)

    #Printing the treaps

    def in_order_traversal(self, node, indent, last):
        if node is not None:
            self.in_order_traversal(node.left, indent +"   ", False)
            print(indent +("|--" if last else '|--')+ str(node.key)+"("+ str(node.priority)+")")
            self.in_order_traversal(node.right, indent +"   ", True)

    def print_treap(self):
        self.in_order_traversal(self.root," ", True)




def main():
  treap=Treaps()
  while True:
    print("\nOperations:")
    print("1: Insert with Priority")
    print("2: Insert a Key with random priority")
    print("3: Remove")
    print("4: Find")
    print("5: Split")
    print("6: Join")
    print("7: Size")
    print("8: Print Treap")
    print("9: Exit")
    choice= input("\nEnter your choice from the above operations:")

    if choice=="1":
      key=input("Enter key: ")
      priority= float(input("Enter priority: "))
      treap.insertWithPriority(key,priority)
      treap.print_treap()

    elif choice=="2":
      key=input("Enter key: ")
      treap.insert(key)
      treap.print_treap()

    elif choice=="3":
      key=input("Enter key to be removed: ")
      treap.remove(key)
      treap.print_treap()

    elif choice=="4":
      key=input("Enter key to be found: ")
      priority=treap.find(key)
      if priority!=0:
        print(f"Key {key} has priority {priority}")
      else:
        print(f"Key {key} is not found.")

    elif choice=="5":
      key=input("Enter key for split: ")
      left_root,right_root=treap.split(key)
      print("Split is done.\nNew treap with keys smaller than or equal to the given key is: ")
      treap.root=left_root
      treap.print_treap()
      print("\nNew treap with keys larger than the given key:")
      larger_treap= Treaps()
      larger_treap.root=right_root
      larger_treap.print_treap()

    elif choice=="6":
      if larger_treap is None:
        print("Perform Split Operation first.")
      else:
        treap.join(larger_treap)
        print("Join is completed. The trea now is:")
        treap.print_treap()

    elif choice=="7":
      print("Size of the Treap is:", treap.size())

    elif choice=="8":
      print("The current Treap is:")
      treap.print_treap()

    elif choice=="9":
      print("Exiting the program.")
      break

    else:
      print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()