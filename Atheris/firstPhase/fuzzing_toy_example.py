from pathlib import Path
import subprocess
import pandas as pd
import os
import sys
import atheris


# if __name__ == '__main__':
#     args = sys.argv

#     import click

#     @click.command()
#     @click.option('-o', '--out', 'file_out', help = 'name for savig the logs')

#     def main(file_out):
#         subp = 'python3 src_tests_fuzzer.py -atheris_runs=1000'
#         subprocess.run(subp)
#         print(file_out)


# main()

# subp = 'python "/Users/alduck/Documents/PhDStuff_repo/VST2023/firstPhase/src_tests_fuzzer.py" -atheris_runs=1000'
# # subprocess.run(subp)
# # subprocess.call['Python3 src_tests_fuzzer.py']
# print(subprocess.check_call([sys.executable or 'python', 'src_tests_fuzzewr.py']))
# # subprocess.call('python3 src_tests_fuzzer.py -atheris_runs=1000', shell=True)

# print('DONE')

## python3 -m coverage run your_fuzzer.py -atheris_runs=10000  # Times to run
# python3 -m coverage html
# (cd htmlcov && python3 -m http.server 8000)

import subprocess
# command = 'home/project/python_files/run_file.py {} {} {}'.format(
#         arg1, arg2, arg3) # if you want to pass any arguments
# command = 'python3 src_tests_fuzzer.py -atheris_runs=1000'
command = 'python3 -m coverage run src_tests_fuzzer.py -atheris_runs=1000'
p = subprocess.Popen(
        [command],
        shell=True,
        stdin=None,
        # stdout=subprocess.PIPE,
        # stderr=subprocess.PIPE,
        close_fds=True)
out, err = p.communicate()

command = 'python3 -m coverage html'
p = subprocess.Popen(
        [command],
        shell=True,
        stdin=None,
        # stdout=subprocess.PIPE,
        # stderr=subprocess.PIPE,
        close_fds=True)
out, err = p.communicate()

# command = 'cd htmlcov && python3 -m http.server 8000'
# p = subprocess.Popen(
#         [command],
#         shell=True,
#         stdin=None,
#         # stdout=subprocess.PIPE,
#         # stderr=subprocess.PIPE,
#         close_fds=True)
# out, err = p.communicate()


