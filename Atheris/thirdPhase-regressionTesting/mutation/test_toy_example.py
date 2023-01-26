from toy_example import calculator
# import pandas as pd

def test_add():

    # inputs = pd.read_csv('log_1000.csv', index_col= 0)

    assert calculator(2,4).add == 6
