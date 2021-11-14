import importlib
import sys

from TK_1 import get_from_console
from TK_2 import get_min_max_numb
from TK_3 import divide_by_average
from TK_4 import multiply_by_average

import_TK_5 = importlib.import_module("TK-5")


def main():
    void_arr = []
    first_arr = get_from_console()
    print(first_arr)

    result_arr = [get_min_max_numb(first_arr), divide_by_average(first_arr), multiply_by_average(first_arr),
                  import_TK_5.square(first_arr)]
    print(result_arr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
