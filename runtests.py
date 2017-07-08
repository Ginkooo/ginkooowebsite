#!/usr/bin/python3

import os
import importlib.util
import unittest


def get_instantion_function_pairs_from_module(module) -> list:
    """get_instantion_function_pairs_from_module
    Instantiate every class inheriting from unittest.TestCase and
    call every function starting with "check",
    passing correct instantion to it

    :param module: Module to look for test classes in
    :type module: module

    :rtype: list - List like [(instance, function)]
    """
    test_classes = []
    for elem in dir(module):
        attr = getattr(module, elem)
        try:
            if issubclass(attr, unittest.TestCase):
                test_classes.append(attr)
        except TypeError:
            pass
    pairs = []
    for c in test_classes:
        instantion = c()
        for attr in dir(c):
            if attr.startswith('check') and callable(getattr(c, attr)):
                pairs.append((instantion, getattr(c, attr)))
    return pairs


def run_tests_from(filepath: str):
    """run_tests_from
    Loads module from given filepath and run tests within it

    :param filepath: Rlative path to the module
    :type filepath: str
    """
    filename = os.path.basename(filepath).split('.')[0]
    spec = importlib.util.spec_from_file_location(filename, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    pairs = get_instantion_function_pairs_from_module(module)
    for instantion, function in pairs:
        print('Running {}...'.format(function.__name__), end=' ')
        function(instantion)
        print('OK')
    print('RAN {} TESTS'.format(len(pairs)))


if __name__ == '__main__':
    test_scripts = []
    for root, dirs, files in os.walk('./tests'):
        if '__pycache__' in root:
            continue
        for f in files:
            if f.startswith('__'):
                continue
            run_tests_from(os.path.join(root, f))
