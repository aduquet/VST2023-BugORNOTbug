import atheris
import pandas as pd
import shortuuid
import sys

with atheris.instrument_imports():
    from toy_example import calculator 

	
# @atheris.instrument_func
def test_add(data): 
    constant = 3
    fdp = atheris.FuzzedDataProvider(data)
    # input = fdp.ConsumeIntList(2,1)
    inputs = fdp.ConsumeIntListInRange(2, 10, 29)
    # mul = calculator(inputs[0], inputs[1]).multiplication()
    add = calculator(inputs[0], inputs[1]).add()
    sub = calculator(inputs[0], inputs[1]).subtraction()

    # MR1 TRANSFORTATION (Permutation of the input)
    # add = calculator(constant * inputs[1], constant * inputs[0]).add()
    # sub = calculator(constant * inputs[1], constant * inputs[0]).subtraction()

    # # MR2 TRANSFORTATION (Multiply by a positive constant )
    # add = calculator(constant * inputs[0], inputs[1]).add()
    # sub = calculator(constant * inputs[0], constant * inputs[1]).subtraction()

    # # MR3 TRANSFORTATION (Adding a positive constant to each operand )
    # add = calculator(constant  + inputs[0], constant + inputs[1]).add()
    # sub = calculator(constant + inputs[0], + inputs[1]).subtraction()

    # # MR4 TRANSFORTATION (Sub a positive constant to each operand )
    # add = calculator(constant + inputs[0], constant + inputs[1]).add()
    # sub = calculator(constant - inputs[0], constant - inputs[1]).subtraction()



    uniqID = shortuuid.uuid()
    new_instance = {
        'id': uniqID,
        'input_a': inputs[0],
        'input_b': inputs[1],
        # 'output_mul': mul,
        'output_sub': sub,
        'output_add': add,
        'output_add_MR1': calculator(inputs[1], inputs[0]).add(),
        'output_sub_MR1': calculator(inputs[1], inputs[0]).subtraction(),
        'output_add_MR2': calculator(inputs[0] * constant, inputs[1] * constant).add(),
        'output_sub_MR2': calculator(inputs[0] * constant, inputs[1] * constant).subtraction(),
        'output_add_MR3': calculator(inputs[0] + constant, inputs[1] + constant).add(),
        'output_sub_MR3': calculator(inputs[0] + constant, inputs[1] + constant).subtraction(),
        'output_add_MR4': calculator(inputs[0] - constant, inputs[1] - constant).add(),
        'output_sub_MR4': calculator(inputs[0] - constant, inputs[1] - constant).subtraction()
,            
        # 'method_call': 'mul',
    }

    # mainLog = mainLog.append(new_instance, ignore_index = True)

    mainLog.loc[len(mainLog.index)] = new_instance
    mainLog.to_csv('log.csv')



    # add = calculator(inputs[0],inputs[1]).add()
    # sub = calculator(inputs[0],inputs[1]).multiplication()
    # print(sub)

# def updateLog():
    # if not mainLog.empty:
        

def main():
    atheris.Setup(sys.argv,test_add)
    atheris.Fuzz()
    print('**** Done ****')


if __name__ == "__main__":
    global mainLog

    # col_names = [
    #     'id',
    #     'input_a',
    #     'input_b',
    #     # 'output_mul',
    #     'output_add',
    #     'output_sub',
    #     # 'method_call',
    # ]

    col_names = [
        'id',
        'input_a',
        'input_b',
        # 'output_mul',
        'output_add',
        'output_sub',
        'output_add_MR1',
        'output_sub_MR1',
        'output_add_MR2',
        'output_sub_MR2',
        'output_add_MR3',
        'output_sub_MR3',
        'output_add_MR4',
        'output_sub_MR4',        
        # 'method_call',
    ]
    mainLog = pd.DataFrame( columns = col_names, index=None)
    # print(mainLog)
    main()
    print('Done!')