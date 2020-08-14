import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
''' ~~~~ IMPLEMENTING A BST Optimizing some inefficient code ''' 
# Creating a BST DS
class BSTNode:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

    # BST INSERT METHOD
    # Insert the given value into the tree
    def insert(self, value):
        # check if the value is less than the current node's value
        if value < self.value:
            # does the current node have a left child?
            if self.left:
                self.left.insert(value)
                # otherwise, it doesn't have a left child and we can park the new node here
            else:
                self.left = BSTNode(value)
        # otherwise the value is greater or equal to the current node's value
        else:
            # does the current node have a right child?
            if self.right:
                # if it does, call the right child's `insert` method to repeat the process
                self.right.insert(value)
            #otherwise, it doesn't have a right child, we can park the new node here
            else:
                self.right = BSTNode(value)
    # CONTAIN CHECK IF BST HAS THE STORED VALUE            
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target <= self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target) # recursion loop left
        else: 
            if self.right is None:
                return False
            else:
                return self.right.contains(target) # recursion loop right

bst = BSTNode("")
for name_1 in names_1:
    bst.insert(name_1)
for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
