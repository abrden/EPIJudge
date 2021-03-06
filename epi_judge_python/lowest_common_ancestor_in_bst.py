from test_framework.test_failure_exception import TestFailureException
from test_framework.test_utils import enable_timer_hook
from test_framework.binary_tree_utils import must_find_node


# Input nodes are nonempty and the key at s is less than or equal to that at b.
def find_LCA(tree, s, b):
    # Implement this placeholder.
    return None


@enable_timer_hook
def lca_wrapper(timer, tree, s, b):
    timer.start()
    result = find_LCA(tree, must_find_node(tree, s), must_find_node(tree, b))
    timer.stop()
    if result is None:
        raise TestFailureException("Result can't be None")
    return result.data


from test_framework import test_utils_generic_main, test_utils

if __name__ == '__main__':
    test_utils_generic_main.generic_test_main(
        'lowest_common_ancestor_in_bst.tsv', lca_wrapper)
