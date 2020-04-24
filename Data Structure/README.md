# Data Structure

* Linear Data Structure
* Non Linear Data Strucure

## Array

`Array` is a container which can hold a fix number of items and these items should be of the same Data*Type. Most of the data strucutre make use of Arrays to implement their algorithm.

* Element : Each item stored in an Array is called an element.
* Index : Each location of an element in an array has a numerical index.

Note: Numpy Array is faster than python array

### Basic Operations

* `Traverse` * print all the array element one by one.
* `Insertion` * adds an element at the given index.
* `Deletion`* Deletes an element at the given index.
* `Search` * Search an element using the given index.
* `Update`* Updates an element at the given index.

## List

The `List` is a most versatile datatype in python which can be written as a list of comma*seprated values between square brackets.There are no restriction for list's element to the same data type.

## Tuples

A `Tuple` is a Sequence of immutable Python objects.Tuples are sequences, just like lists.The differences between tuple and list are, tuple are immutable.

## Dictionary

In `Dictionary`, each key value pair is seprated by (: colan). Indexing is very fast in dictionary. An empty dictionary is without any items is written with just two curly braces,like this {}.
Keys are unique to dict which values may not be.
Note : Key must be immutable.

## Maps

`Python Maps` also called chainmap is a type of data structure to manage multiple dictionaries together as one unit. The combined dictionary contains the key ana value pairs in a specific sequence eliminating and duplicating key.
The best use of chainMap is to search through multiple dictionaries at a time and get the proper key value pair mapping. we also see that these ChainMaps Behave as stack data structure.

## Linked List

A `linked` list is a sequence of data elements, which are connected together via links.Each data elements contains a connection to another data element in from of a pointer.Python doesn't have linked list in it's standard library.

## Heap

`Heap` is a special tree structure in which each parent node is less than or equal to its child Node. Then it is called `min Heap`. If each parent node is great er than or equal to it's child node then it is called a `max Heap`

It is very useful is implementing priority queues where the queue item with higher weightage is given more prioority in processing.

A heap is created by using python’s inbuilt library named heapq. This library has the relevant functions to carry out various operations on heap data structure. Below is a list of these functions.

* ***heapify*** - This function converts a regular list to a heap. In the resulting heap the smallest element gets pushed to the index position 0. But rest of the data elements are not necessarily sorted.
* ***heappush*** - This function adds an element to the heap without altering the current heap.
* ***heappop*** - This function returns the smallest data element from the heap.
* ***heapreplace*** - This function replaces the smallest data element with a new value supplied in the function.
