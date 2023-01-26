import sys
import zlib
import atheris
import coverage

import ast

from pathlib import Path

from mutatest import run
from mutatest import transformers
from mutatest.api import Genome, GenomeGroup, MutationException
from mutatest.filters import CoverageFilter, CategoryCodeFilter

with atheris.instrument_imports():
    from toy_example import calculator 

	
# @atheris.instrument_func
def test_add(data): 
    # cov.start()

    # cov.start()

    fdp = atheris.FuzzedDataProvider(data)
    # input = fdp.ConsumeIntList(2,1)
    input = fdp.ConsumeIntListInRange(2, 0, 9)
    assert calculator(input[0], input[1]).multiplication() == calculator(input[1], input[0]).multiplication()
    print('start')
    print('Inputs: ', input )
    print('Result: ', calculator(input[0], input[1]).multiplication())
    print('end')
    print('******')
    # cov.stop()
    # cov.save()
    # try:
    #     cov.html_report()
    # except:
    #     pass
    # print('a: ', a)
    # print('b: ', b)
	# try:
		# print(calculator(a,b).subtraction())
	
	# except zlib.error:
  		# pass
#.. call your code ..
# cov = Coverage()
# cov.stop()

# cov.html_report(directory='covhtml')


# cov = cover/age.Coverage()

# .. call your code ..
atheris.Setup(sys.argv,test_add)
atheris.Fuzz()
# cov.stop()
# cov.save()
# cov.html_report()
print('**** Done ****')

