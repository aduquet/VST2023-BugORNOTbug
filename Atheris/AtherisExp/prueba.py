import struct
import atheris
from calculator import *
import sys

with atheris.instrument_imports():
  import calculator

# def TestOneInput(data1):
#   print('data:', data1)  
# #   print('data1:', data1[1])
# #   print('data2:', data1[0])

# def TestOneInput2( data):
#   print('data:', data)  
# #   print('data1:', data1[1])

# atheris.Setup(sys.argv[0], [TestOneInput, TestOneInput2])
# atheris.Fuzz()

@atheris.instrument_func  # Instrument the TestOneInput function itself
def TestOneInput(data):
  """The entry point for our fuzzer.

  This is a callback that will be repeatedly invoked with different arguments
  after Fuzz() is called.
  We translate the arbitrary byte string into a format our function being fuzzed
  can understand, then call it.

  Args:
    data: Bytestring coming from the fuzzing engine.
  """
  print(len(data))
  print('data decode: ', type(data))
  if len(data) != 4:
    # num2 = struct.unpack('<I', data)
    print('++++++++', len(data))
    return  # Input must be 4 byte integer.

  
  number, = struct.unpack('<I', data)
  print('*** NUM ***', number, len(data))
  print(type(number))
  cal = Calculator()
  print(cal(a = number, b = number))

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()