#!/usr/bin/env python3

from json import load, dump, dumps
from glob import glob
from os import environ
from os.path import join
from sys import argv, exit
import os
import re


def run_single_test(data_dir, output_dir):
    from pytest import main
    from shutil import copyfile
    src = join(os.path.dirname(os.path.abspath(__file__)), 'task7.py')
    dst = join(output_dir, 'task7.py')
    copyfile(src, dst)

    from task7 import find_modified_max_argmax
    class A(int):
        def __init__(self):
            pass
    
    args =  [
        ([1, 3, 4, 4.5], lambda x: x ** 2, (16, 2)),
        (["str", "1", 23, 4, 65], lambda x: -x + 2, (-2, 1)),
        (["str", 4, 4.5, 2, '-2', '3', -8], lambda x: abs(x) - 10, (-2, 2)),
        (["str", '-2', '3'], lambda x: abs(x) - 10, ()),
        ([A(), 1, 2], lambda x: x, (2, 1)),
        ([], lambda x: abs(x) - 10, ())
    ]

    counter = 0

    for arg in args:
        if find_modified_max_argmax(arg[0], arg[1]) == arg[2]:
            counter += 1

    with open(join(output_dir, 'result'), 'w') as f:
        f.write(str(counter))

def check_test(data_dir):
    output_dir = os.path.join(data_dir, 'output')

    with open(join(output_dir, 'task7.py')) as f:
        code = re.sub(r'\s', '', f.read())

    res = f'Ok. len = {len(code)}'

    with open(join(output_dir, 'result')) as f:
        counter = int(f.read())

    if counter != 6:
        res = 'Not Ok'

    print(res)

    return res

def grade(data_dir):
    results = load(open(join(data_dir, 'results.json')))
    ok_count = 0
    code_len = None

    for result in results:
        if result['status'].startswith('Ok'):
            ok_count += 1
            if len(result['status']) > 2:
                # task7, "Ok. len = {len(code)}"
                code_len = result['status'][10:]
    total_count = len(results)
    description = '%02d/%02d' % (ok_count, total_count)
    if code_len:
        description = description + ' len: ' + code_len

    if code_len:
        if int(code_len) <= 126:
            mark = 3
        elif int(code_len) <= 135:
            mark = 2
        else:
            mark = 1
    else:
        mark = 0

    res = {'description': description, 'mark': mark}

    if environ.get('CHECKER'):
        print(dumps(res))
    return res


if __name__ == '__main__':
    if environ.get('CHECKER'):
        # Script is running in testing system
        if len(argv) != 4:
            print('Usage: %s mode data_dir output_dir' % argv[0])
            exit(0)

        mode, data_dir, output_dir = argv[1], argv[2], argv[3]

        if mode == 'run_single_test':
            run_single_test(data_dir, output_dir)
        elif mode == 'check_test':
            check_test(data_dir)
        elif mode == 'grade':
            grade(data_dir)
    else:
        # Script is running locally
        if len(argv) != 3:
            print(f'Usage: {argv[0]} test/unittest test_name')
            exit(0)

        from re import sub
        from os import makedirs
        from os.path import basename, exists
        from shutil import copytree

        mode, test_name = argv[1], argv[2]
        test_dir = glob(f'python_intro_public_test/[0-9][0-9]_{mode}_{test_name}_input')
        if not test_dir:
            print('Test not found')
            exit(0)

        input_dir = test_dir[0]
        output_dir = sub(r'input$', 'check', input_dir)
        run_output_dir = join(output_dir, 'output')
        run_single_test(input_dir, run_output_dir)
        status = check_test(output_dir)
        results = [{'status': status}]
        dump(results, open(join(input_dir, 'results.json'), 'w'))
        grade(input_dir)
