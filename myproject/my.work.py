import numpy as np
import time
import matplotlib.pyplot as plt
import copy
import random

N = 1000  # amount of numbers
list_ch = []  # list of the insertion algorithm
list_bubble = []  # list of bubble algorithm
list_shaker = []  # list of the shaker algorithm
list_quick_sort = []  # quick sort list
list_pyramid = []  # pyramid sorting list
list_mergeSort = []  # merge sort list
a = 0  # amount of time entries


# ----------------------------------------------------------------------------
def ch(N, arr):
    """
    insertion sorting function
    """
    start_time = time.perf_counter()

    for i in range(N - 1):
        for j in range(N - i - 1):
            if arr[j] < arr[j + 1]:
                c = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = c
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time  # reading the time spent
    # print('Elapsed time: ',elapsed_time)
    return elapsed_time


def bubble(N, arr):
    """
    bubble sorting function
    """
    start_time = time.perf_counter()

    for i in range(N - 1, 0, -1):
        for j in range(N - 1, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time


def shaker(N, arr):
    """
    shaker sorting function
    """
    start_time = time.perf_counter()

    for j in range(N - 1):
        for i in range(0, N - 1, +1):
            # print(arr)
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        N -= 1
        for i in range(N - 1, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time


def quick_sort(N, arr):
    def q_sort(arr):
        """
        quick sort function
        """
        if len(arr) > 1:
            x = arr[random.randint(0, len(arr) - 1)]
            low = [i for i in arr if i < x]
            eq = [i for i in arr if i == x]
            hi = [i for i in arr if i > x]
            arr = q_sort(low) + eq + q_sort(hi)
        return arr

    start_time = time.perf_counter()

    q_sort(arr)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time


def pyramid(N, arr):
    """
    pyramid sorting function
    """
    def heapify(arr, N, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < N and arr[i] < arr[l]:
            largest = l
        if r < N and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            (arr[i], arr[largest]) = (arr[largest], arr[i])
            heapify(arr, N, largest)

    def heapSort(arr):
        nonlocal N
        for i in range(N // 2 - 1, -1, -1):
            heapify(arr, N, i)
        for i in range(N - 1, 0, -1):
            (arr[i], arr[0]) = (arr[0], arr[i])
            heapify(arr, i, 0)

    N = len(arr)

    start_time = time.perf_counter()
    heapSort(arr)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time


def mergeSort(N, arr):
    """
    merge sorting function
    """
    def merge(arr, N):
        if len(arr) > 1:
            mid = len(arr) // 2
            lefthalf = arr[:mid]
            righthalf = arr[mid:]

            merge(lefthalf, N)
            merge(righthalf, N)

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    arr[k] = lefthalf[i]
                    i = i + 1
                else:
                    arr[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                arr[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                arr[k] = righthalf[j]
                j = j + 1
                k = k + 1

    start_time = time.perf_counter()
    merge(arr, N)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print('1 - The insertion algorithm', '\n',
      '2 - Bubble Algorithm', '\n',
      '3 - The Shaker algorithm', '\n',
      '4 - Quick sorting', '\n',
      '5 - Pyramid sorting', '\n',
      '6 - Merge sorting', '\n',
      '0 - Exit', '\n')
choose = input('Select the sorting method: ')

if '4' in choose or '5' in choose or '6' in choose:
    N = 10000
    step = 5000
    N_end = 100000
else:
    step = 1000
    N_end = 5000

# THE MAIN CYCLE
while N <= N_end:
    if '4' in choose or '5' in choose or '6' in choose:
        arr4 = np.random.randint(0, 100, N)  # an array with random numbers in the range 0-100
        arr5 = copy.deepcopy(arr4)
        arr6 = copy.deepcopy(arr4)
    else:
        arr = np.random.randint(0, 100, N)  # an array with random numbers in the range 0-100
        arr2 = copy.deepcopy(arr)
        arr3 = copy.deepcopy(arr)

    # the insertion algorithm ----------------------------------------
    if '1' in choose:
        elapsed_time = ch(N, arr)

        list_ch.insert(a, elapsed_time)  # recording the time spent
    # ---------------------------------------------------------

    # bubble algorithm ---------------------------------------
    if "2" in choose:
        elapsed_time = bubble(N, arr2)

        list_bubble.insert(a, elapsed_time)
    # ---------------------------------------------------------
    # the shaker algorithm
    if '3' in choose:
        elapsed_time = shaker(N, arr3)

        list_shaker.insert(a, elapsed_time)

    # the quick sorting algorithm -----------------------------
    if '4' in choose:
        elapsed_time = quick_sort(N, arr4)

        list_quick_sort.insert(a, elapsed_time)
    # ---------------------------------------------------------
    # the pyramid sorting algorithm
    if '5' in choose:
        elapsed_time = pyramid(N, arr5)

        list_pyramid.insert(a, elapsed_time)
    # ---------------------------------------------------------
    # merge sorting algorithm
    if '6' in choose:
        elapsed_time = mergeSort(N, arr6)

        list_mergeSort.insert(a, elapsed_time)

    if '0' in choose:
        exit()

    print("Iteration", a)
    a = a + 1
    N = N + step
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


if '1' in choose:
    print('List1 = ', list_ch)
    plt.plot(list_ch, label='The insertion algorithm')
    # plt.legend(('The insertion algorithm'))
if '2' in choose:
    print('List2 = ', list_bubble)
    plt.plot(list_bubble, label='Bubble algorithm')
    # plt.legend(('Bubble algorithm'))
if '3' in choose:
    print('List3 = ', list_shaker)
    plt.plot(list_shaker, label='The shaker algorithm')
    # plt.legend(('The shaker algorithm'))
if '4' in choose:
    print('List4 = ', list_quick_sort)
    plt.plot(list_quick_sort, label='The quick sorting algorithm')
    # plt.legend(('The quick sorting algorithm'))
if '5' in choose:
    print('List5 = ', list_pyramid)
    plt.plot(list_pyramid, label='The pyramid sorting algorithm')
    # plt.legend(('The pyramid sorting algorithm'))
if '6' in choose:
    print('List6 = ', list_mergeSort)
    plt.plot(list_mergeSort, label='Merge sorting algorithm')
    # plt.legend(('Merge sorting algorithm'))

plt.legend()
plt.show()