"""
Collection of the core mathematical operators used throughout the code base.
"""

import math


# ## Task 0.1

# Implementation of a prelude of elementary functions.


def mul(x, y):
    ":math:`f(x, y) = x * y`"
    # TODO: Implement for Task 0.1.
    return x * y


def id(x):
    ":math:`f(x) = x`"
    # TODO: Implement for Task 0.1.
    return x


def add(x, y):
    ":math:`f(x, y) = x + y`"
    # TODO: Implement for Task 0.1.
    return x + y


def neg(x):
    ":math:`f(x) = -x`"
    # TODO: Implement for Task 0.1.
    return -x if x != 0 else 0


def lt(x, y):
    ":math:`f(x) =` 1.0 if x is less than y else 0.0"
    # TODO: Implement for Task 0.1.
    return 1.0 if x < y else 0.0


def eq(x, y):
    ":math:`f(x) =` 1.0 if x is equal to y else 0.0"
    # TODO: Implement for Task 0.1.
    return 1.0 if x == y else 0.0


def max(x, y):
    ":math:`f(x) =` x if x is greater than y else y"
    # TODO: Implement for Task 0.1.
    return x if x > y else y


def is_close(x, y):
    ":math:`f(x) = |x - y| < 1e-2` "
    # TODO: Implement for Task 0.1.
    return True if abs(x - y) < exp(-2) else False


def sigmoid(x):
    r"""
    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}`

    (See `<https://en.wikipedia.org/wiki/Sigmoid_function>`_ .)

    Calculate as

    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}` if x >= 0 else :math:`\frac{e^x}{(1.0 + e^{x})}`

    for stability.

    Args:
        x (float): input

    Returns:
        float : sigmoid value
    """
    # TODO: Implement for Task 0.1.
    return 1.0 / (1.0 + exp(-x)) if x >= 0 else (math.exp(x)) / (1.0 + exp(x))


def relu(x):
    """
    :math:`f(x) =` x if x is greater than 0, else 0

    (See `<https://en.wikipedia.org/wiki/Rectifier_(neural_networks)>`_ .)

    Args:
        x (float): input

    Returns:
        float : relu value
    """
    # TODO: Implement for Task 0.1.
    return x if x > 0 else 0


EPS = 1e-6


def log(x):
    ":math:`f(x) = log(x)`"
    return math.log(x + EPS)


def exp(x):
    ":math:`f(x) = e^{x}`"
    return math.exp(x)


def log_back(x, d):
    r"If :math:`f = log` as above, compute d :math:`d \times f'(x)`"
    # TODO: Implement for Task 0.1.
    return d * log(x)


def inv(x):
    ":math:`f(x) = 1/x`"
    # TODO: Implement for Task 0.1.
    try:
        return 1 / x
    except ZeroDivisionError:
        raise ZeroDivisionError("The denominator should not be 0")


def inv_back(x, d):
    r"If :math:`f(x) = 1/x` compute d :math:`d \times f'(x)`"
    # TODO: Implement for Task 0.1.
    try:
        return -1 * d * (1 / x ** 2) if x == (1 / x) else 0
    except ZeroDivisionError:
        raise ZeroDivisionError("The denominator should not be 0")


def relu_back(x, d):
    r"If :math:`f = relu` compute d :math:`d \times f'(x)`"
    # TODO: Implement for Task 0.1.
    return d * 0 if x <= 0 else d * 1


# ## Task 0.3

# Small library of elementary higher-order functions for practice.


def map(fn):
    """
    Higher-order map.

    .. image:: figs/Ops/maplist.png


    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (one-arg function): Function from one value to one value.

    Returns:
        function : A function that takes a list, applies `fn` to each element, and returns a
        new list
    """
    # TODO: Implement for Task 0.3.
    def apply(ls):
        return fn(ls)

    return apply


def negList(ls):
    "Use :func:`map` and :func:`neg` to negate each element in `ls`"
    # TODO: Implement for Task 0.3.
    return [-x for x in ls]


def zipWith(fn):
    """
    Higher-order zipwith (or map2).
    .. image:: figs/Ops/ziplist.png
    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_
    Args:
        fn (two-arg function): combine two value

    Returns:
        function : takes two equally sized lists `ls1` and `ls2`, produce a new list by
        applying fn(x, y) on each pair of elements.

    """

    def apply(ls1, ls2):
        if len(ls1) == 0:
            return 0
        return [fn(ls1[x], ls2[x]) for x in range(len(ls1))]

    # TODO: Implement for Task 0.3.
    return apply


def addLists(ls1, ls2):
    "Add the elements of `ls1` and `ls2` using :func:`zipWith` and :func:`add`"
    # TODO: Implement for Task 0.3.
    add_list = zipWith(add)
    return add_list(ls1, ls2)


def reduce(fn, start):
    r"""
    Higher-order reduce.

    .. image:: figs/Ops/reducelist.png


    Args:
        fn (two-arg function): combine two values
        start (float): start value :math:`x_0`

    Returns:
        function : function that takes a list `ls` of elements
        :math:`x_1 \ldots x_n` and computes the reduction :math:`fn(x_3, fn(x_2,
        fn(x_1, x_0)))`
    """
    # TODO: Implement for Task 0.3.
    def apply(ls):
        result = start
        for i in range(1, len(ls)):
            result = fn(ls[i], result)
        return result

    return apply


def sum(ls):
    "Sum up a list using :func:`reduce` and :func:`add`."
    # TODO: Implement for Task 0.3.
    red = reduce(add, ls[0])
    return red(ls)


def prod(ls):
    "Product of a list using :func:`reduce` and :func:`mul`."
    # TODO: Implement for Task 0.3.
    red = reduce(mul, ls[0])
    return red(ls)
