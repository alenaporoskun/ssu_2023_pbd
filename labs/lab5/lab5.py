
import numpy as np


def main():
    #print_header("NumPy: the absolute basics for beginners")
    #print_with_lines("How to create a basic array")
    #print("How to create a basic array")
    print_header_1line("How to create a basic array")
    print("np.array([1, 2, 3]):\n", np.array([1, 2, 3]))
    print("np.zeros(2):\n", np.zeros(2))
    print("np.ones(2):\n", np.ones(2))
    print("np.empty(4):\n", np.empty(4))
    print("np.arange(5):\n", np.arange(5))
    print("np.arange(2, 12, 2):\n", np.arange(2, 12, 2))
    print("np.linspace(0, 12, num=5):\n", np.linspace(0, 12, num=5))
    print("np.ones(2, dtype=np.int64):\n", np.ones(2, dtype=np.int64))

    print_header_1line("Adding, removing, and sorting elements")
    arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
    print("arr\n", arr)
    print("np.sort(arr):\n", np.sort(arr), "\n")
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    print(" a ", a, "\n", "b ", b)
    print("np.concatenate((a, b)):\n", np.concatenate((a, b)))

    print_header_1line("How do you know the shape and size of an array?")
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

    print_header_1line("Can you reshape an array?")
    a = np.arange(6)
    print("a ", a)
    print("a.reshape(3, 2):\n", a.reshape(3, 2))



    #print(":\n", ,"\n")
    print(":\n", "\n")
    print(":\n", )

def print_header(msg):
    line = '=' * (len(msg) + 2)
    print(f'\n{line}')
    print(f' {msg} ')
    print(f'{line}')

def print_header_1line(msg):
    line = '=' * (len(msg) + 2)
    print(f'\n{line}')
    print(f' {msg} \n')

def decor_func(func):
    def wrap(text):
        print("------------------")
        print(func(text))
        print("------------------")
    return wrap

@decor_func
def print_with_lines(text):
    return text

if __name__ == '__main__':
    main()
