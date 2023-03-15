#!/usr/bin/env python3
import sys
import numpy as np

def main():
    print_header("Check version")
    print_version()

    print_header("NumPy: the absolute basics for beginners")

    print_header("How to create a basic array")
    print("np.array([1, 2, 3]):\n", np.array([1, 2, 3]))
    print("np.zeros(2):\n", np.zeros(2))
    print("np.ones(2):\n", np.ones(2))
    print("np.empty(4):\n", np.empty(4))
    print("np.arange(5):\n", np.arange(5))
    print("np.arange(2, 12, 2):\n", np.arange(2, 12, 2))
    print("np.linspace(0, 12, num=5):\n", np.linspace(0, 12, num=5))
    print("np.ones(2, dtype=np.int64):\n", np.ones(2, dtype=np.int64))

    print_header("Adding, removing, and sorting elements")
    arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
    print("arr\n", arr)
    print("np.sort(arr):\n", np.sort(arr), "\n")
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    print(" a ", a, "\n", "b ", b)
    print("np.concatenate((a, b)):\n", np.concatenate((a, b)))

    print_header("How do you know the shape and size of an array?")
    array_example = np.array([[[0, 1, 2, 3],
                               [4, 5, 6, 7]],
                              [[10, 20, 30, 40],
                               [11, 21, 31, 41]],
                              [[100, 110, 120, 130],
                               [40, 50, 60, 70]]])
    print("array_example:\n", array_example, "\n")
    print("array_example.ndim:\n", array_example.ndim)
    print("array_example.size:\n", array_example.size)
    print("array_example.shape:\n", array_example.shape)

    print_header("Can you reshape an array?")
    a = np.arange(6)
    print("a ", a)
    print("a.reshape(3, 2):\n", a.reshape(3, 2))

    print_header("How to convert a 1D array into a 2D array (how to add a new axis to an array)")
    a = np.array([1, 2, 3, 4, 5, 6])
    a.shape
    row_vector = a[np.newaxis, :]
    row_vector.shape
    col_vector = a[:, np.newaxis]
    col_vector.shape
    print("a:", a, "\n", "a.shape:", a.shape)
    print("row_vector = a[np.newaxis, :] \nrow_vector.shape:", row_vector.shape)
    print("col_vector = a[:, np.newaxis] \ncol_vector.shape:", col_vector.shape)

    print_header("Indexing and slicing")

    data = np.array([1, 2, 3, 4, 5])
    print("data:      ", data)
    print("data[0:2]: ", data[0:2])
    print("data[1:]:  ", data[1:])
    print("data[-2:]: ", data[-2:])
    print("data[::-1]:", data[::-1], "\n")

    a = np.array([[0, -1, -2, -3], [1, 2, 3, 4], [5, 8, 11, 14]])
    print("a:\n", a)
    print("a[a < 5]:\n", a[a < 5])
    five_up = (a >= 5)
    print("five_up = (a >= 5),  a[five_up]:\n", a[five_up])
    print("a[(a > 2) & (a < 11)]:\n", a[(a > 2) & (a < 11)])

    print("a:\n", a)
    b = np.nonzero(a < 3)
    # In this example, a tuple of arrays was returned: one for each dimension.
    print("b=np.nonzero(a < 3):\n", b)
    print("(row indices, column indices)")
    print("list(zip(b[0], b[1])):\n", list(zip(b[0], b[1])), "\n")
    #list_of_coordinates = list(zip(b[0], b[1]))
    #for coord in list_of_coordinates:
    #    print(coord)

    print_header("How to create an array from existing data")







    
    print_header("")
    #print(":\n", ,"\n")
    print(":\n", "\n")
    print(":\n", )


def print_version():
    print(sys.version)

def print_header(msg):
    line = '=' * (len(msg) + 2)
    print(f'\n{line}')
    print(f' {msg} ')
    print(f'{line}')

if __name__ == '__main__':
    main()
