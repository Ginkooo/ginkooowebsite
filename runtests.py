#!/usr/bin/python3

import os
import importlib.util


def run_tests_from(filepath: str):
    filename = os.path.basename(filepath).split('.')[0]
    spec = importlib.util.spec_from_file_location(filename, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    print(dir(module))


if __name__ == '__main__':
    test_scripts = []
    for root, dirs, files in os.walk('./tests'):
        if '__pycache__' in root:
            continue
        for f in files:
            if f.startswith('__'):
                continue
            run_tests_from(os.path.join(root, f))
