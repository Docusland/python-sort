"""
Coding exercise for IT students.
The target of this script is to store different algorithms that sort an array.
"""


def selection_sort(to_sort: list) -> list:
    """
    The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
    from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

        1) The subarray which is already sorted.
        2) Remaining subarray which is unsorted.

        In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted
        subarray is picked and moved to the sorted subarray.

        Cost : Best = n x n, Average = n x n, Worst = n x n
    :param to_sort:
    :return:
    """
    return to_sort


def bubble_sort(to_sort: list) -> list:
    """
        Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if
        they are in wrong order.
        Cost : Best = n, Average = n x n, Worst = n x n
    """
    return to_sort


def insertion_sort(to_sort: list) -> list:
    """
    Sort a list whilst respecting insert sort algorithm.

    To sort an array of size n in ascending order:
        1: Iterate from arr[1] to arr[n] over the array.
        2: Compare the current element (key) to its predecessor.
        3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater
        elements one position up to make space for the swapped element.

    Cost : Best = n, Average = n x n, Worst = n x n

    :param to_sort: list to order
    :return: sorted list
    """
    return to_sort

def merge_sort(to_sort: list) -> list:
    """
    MergeSort(arr[], l,  r).
    If r > l
     1. Find the middle point to divide the array into two halves:
             middle m = (l+r)/2
     2. Call mergeSort for first half:
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(left, right)

     Cost : Best = n x log(n), Average = n x log(n), Worst = n x log(n)

    :param to_sort:
    :return:
    """
   
    return to_sort

def quick_sort(arr: list, start: int = None, end: int = None) -> list:
    """
    Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given
    array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

    Always pick first element as pivot.
    Always pick last element as pivot
    Pick a random element as pivot.
    Pick median as pivot.

    The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as
    pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and
    put all greater elements (greater than x) after x. All this should be done in linear time

    :param arr:
    :return:
    """
    
    return arr


def heap_sort(arr: list) ->list:
    """
    Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection
    sort where we first find the maximum element and place the maximum element at the end. We repeat the same process
    for the remaining elements.

    What is Binary Heap?
    Let us first define a Complete Binary Tree. A complete binary tree is a binary tree in which every level,
    except possibly the last, is completely filled, and all nodes are as far left as possible (Source Wikipedia)

    A Binary Heap is a Complete Binary Tree where items are stored in a special order such that value in a parent node
    is greater(or smaller) than the values in its two children nodes. The former is called as max heap and the latter
    is called min-heap. The heap can be represented by a binary tree or array.

    Why array based representation for Binary Heap?
    Since a Binary Heap is a Complete Binary Tree, it can be easily represented as an array and the array-based
    representation is space-efficient. If the parent node is stored at index I, the left child can be calculated
    by 2 * I + 1 and right child by 2 * I + 2 (assuming the indexing starts at 0).

    :param arr:
    :return:
    """

    

    return arr
