# Treaps Implementation and Performance Analysis

## Overview

This project presents a Python implementation of Treaps, a unique data structure that combines the properties of binary search trees and heaps. Treaps ensure that operations such as insert, delete, and search are performed efficiently. The core idea behind treaps is to maintain a binary search tree based on the key and a heap based on priority, which is randomly assigned upon insertion.

## Features

### Insertion: 
Allows adding elements with specific keys and priorities, ensuring the tree's structure adheres to both binary search tree and heap properties.
### Deletion: 
Removes elements by key, maintaining the treap's invariant.
### Search: 
Finds an element's priority given its key, demonstrating the efficiency of search operations within the treap.
### Split: 
Divides the treap into two separate treaps based on a key value.
### Join: 
Merges two treaps into one, ensuring the resulting treap maintains the required properties.
### Size: 
Calculates the size of the treap, illustrating its dynamic nature.

## Usage

To utilize this implementation in your projects, simply import the Treaps class from the provided file. Here's a quick example to get you started:

from treaps import Treaps

'''Create a Treap instance'''

myTreap = Treaps()

'''Insert elements'''

myTreap.insert(10)

myTreap.insert(20)

'''Print the treap'''

myTreap.print_treap()

'''Remove an element'''

myTreap.remove(10)

'''Find an element'''

priority = myTreap.find(20)

print(f"Priority of 20: {priority}")

## Performance Analysis
The performance of the Treaps data structure was rigorously tested across various operations: insert, delete, find, split, and join. The analysis was conducted over a range of input sizes, from 1,000 to 30,000 elements, to evaluate the scalability and efficiency of the implementation.

## Key Findings

### Insertion and Deletion: 
Showed consistent performance, highlighting the efficiency of managing the treap's structure.
### Search: 
Demonstrated quick retrieval times, benefiting from the binary search tree properties.
### Split and Join: 
Were executed efficiently, proving the flexibility and dynamic nature of treaps in handling complex operations.

For detailed performance metrics, refer to the performance_analysis.py file.

## Conclusion:
This project underscores the practicality and efficiency of Treaps as a data structure for various applications requiring sorted data management with quick insertion, deletion, and search operations. The implementation and subsequent performance analysis offer valuable insights into its scalability and operational efficiency, making it a compelling choice for both academic exploration and real-world applications.
