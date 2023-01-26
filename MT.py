import pandas as pd
import shortuuid
import sys
from SUT import calculator 


def SutExecution(input_a, input_b, op):
    
    if op == 'sum':
        return calculator(input_b, input_a).add()
    if op == 'sub':
        return calculator(input_b, input_a).subtraction()
    if op == 'mul':
        return calculator(input_b, input_a).multiplication()
    if op == 'div':
        return calculator(input_b, input_a).division()

# Test Data Transformation

def TestDataTransformation(input_a, input_b, MR, op, const):

    # MR1 TRANSFORTATION (Permutation of the input)
    if MR == 'mr1':
        if op == 'sum':
            return calculator(input_b, input_a).add()
        if op == 'sub':
            return calculator(input_b, input_a).subtraction()
        if op == 'mul':
            return calculator(input_b, input_a).multiplication()
        if op == 'div':
            return calculator(input_b, input_a).division()

    # MR2 TRANSFORTATION (Multiply by a positive constant )
    if MR == 'mr2':

        input_a = input_a * const
        input_b = input_b * const

        if op == 'sum':
            return calculator(input_a, input_b).add()
        if op == 'sub':
            return calculator(input_a, input_b).subtraction()
        if op == 'mul':
            return calculator(input_a, input_b).multiplication()
        if op == 'div':
            return calculator(input_a, input_b).division()

    # MR3 TRANSFORTATION (Adding a positive constant to each operand )

    if MR == 'mr3':
        input_a = input_a + const
        input_b = input_b + const

        if op == 'sum':
            return calculator(input_a, input_b).add()
        if op == 'sub':
            return calculator(input_a, input_b).subtraction()
        if op == 'mul':
            return calculator(input_a, input_b).multiplication()
        if op == 'div':
            return calculator(input_a, input_b).division()

    # MR4 TRANSFORTATION (Adding a positive constant to each operand )

    if MR == 'mr4':
        input_a = input_a - const
        input_b = input_b - const

        if op == 'sum':
            return calculator(input_a, input_b).add()
        if op == 'sub':
            return calculator(input_a, input_b).subtraction()
        if op == 'mul':
            return calculator(input_a, input_b).multiplication()
        if op == 'div':
            return calculator(input_a, input_b).division()

# MRs Checker
def MRsChecker(output, t_output, mr):

    if mr == 'mr1':    
        ## MR_1 ##
        if output == t_output:
            return 'No-violated'

        if output != t_output:
            return 'Violated'

    if mr == 'mr2':
        ## MR_2 ##
        # Must to be <
            if output < t_output:
                return 'No-violated'

            if output >= t_output:
                return 'Violated'


    if mr == 'mr3':
        ## MR_3 ##
        if output == t_output:
            return 'No-violated'

        if output != t_output:
            return 'Violated'


    if mr == 'mr4':
        ## MR_4 ##
        if output == t_output:
            return 'No-violated'

        if output != t_output:
            return 'Violated'


# SUT excecution
def save(file_out):
    df_output.to_csv(file_out + '.csv')

# read test data

if __name__ == '__main__':
    
    import click

    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-o', '--out', 'file_out', help='Name of the file in which data will be stored')

    def main(file_in, file_out):
        
        df = pd.read_csv(file_in, index_col = 0 )

        global df_output
        df_output = df.copy()
        # df['output'] = 0

        # mrs = ['mr1', 'mr2', 'mr3', 'mr4']

        for index, row in df.iterrows():
            const = df.at[index, 'const']

            if row['operand'] == 'sum':
                output_sum = SutExecution(row['input_a'], row['input_b'], 'sum')
                output_transformed_data_sum_mr1 = TestDataTransformation(row['input_a'], row['input_b'], 'mr1', 'sum', const)
                output_transformed_data_sum_mr2 = TestDataTransformation(row['input_a'], row['input_b'], 'mr2', 'sum', const)
                output_transformed_data_sum_mr3 = TestDataTransformation(row['input_a'], row['input_b'], 'mr3', 'sum', const)
                output_transformed_data_sum_mr4 = TestDataTransformation(row['input_a'], row['input_b'], 'mr4', 'sum', const)
                checker_mr1_sum = MRsChecker(output=output_sum, t_output= output_transformed_data_sum_mr1, mr = 'mr1')
                checker_mr2_sum = MRsChecker(output=output_sum, t_output= output_transformed_data_sum_mr2, mr = 'mr2')
                checker_mr3_sum = MRsChecker(output=output_sum, t_output= output_transformed_data_sum_mr3, mr = 'mr3')
                checker_mr4_sum = MRsChecker(output=output_sum, t_output= output_transformed_data_sum_mr4, mr = 'mr4')

                df_output.at[index, 'MR1'] = checker_mr1_sum
                df_output.at[index, 'MR2'] = checker_mr2_sum
                df_output.at[index, 'MR3'] = checker_mr3_sum
                df_output.at[index, 'MR4'] = checker_mr4_sum
                # for i in mrs:
                    # MRsChecker(output=output_sum, t_output= output_transformed_data_sum_mr1, mr = i)


            if row['operand'] == 'sub':
                output_sub = SutExecution(row['input_a'], row['input_b'], 'sub')
                output_transformed_data_sub_mr1 = TestDataTransformation(row['input_a'], row['input_b'], 'mr1', 'sub', const)
                output_transformed_data_sub_mr2 = TestDataTransformation(row['input_a'], row['input_b'], 'mr2', 'sub', const)
                output_transformed_data_sub_mr3 = TestDataTransformation(row['input_a'], row['input_b'], 'mr3', 'sub', const)
                output_transformed_data_sub_mr4 = TestDataTransformation(row['input_a'], row['input_b'], 'mr4', 'sub', const)            

                checker_mr1_sub = MRsChecker(output=output_sub, t_output= output_transformed_data_sub_mr1, mr = 'mr1')
                checker_mr2_sub = MRsChecker(output=output_sub, t_output= output_transformed_data_sub_mr2, mr = 'mr2')
                checker_mr3_sub = MRsChecker(output=output_sub, t_output= output_transformed_data_sub_mr3, mr = 'mr3')
                checker_mr4_sub = MRsChecker(output=output_sub, t_output= output_transformed_data_sub_mr4, mr = 'mr4')

                df_output.at[index, 'MR1'] = checker_mr1_sub
                df_output.at[index, 'MR2'] = checker_mr2_sub
                df_output.at[index, 'MR3'] = checker_mr3_sub
                df_output.at[index, 'MR4'] = checker_mr4_sub

            if row['operand'] == 'mul':
                output_mul = SutExecution(row['input_a'], row['input_b'], 'mul')
                output_transformed_data_mul_mr1 = TestDataTransformation(row['input_a'], row['input_b'], 'mr1', 'mul', const)
                output_transformed_data_mul_mr2 = TestDataTransformation(row['input_a'], row['input_b'], 'mr2', 'mul', const)
                output_transformed_data_mul_mr3 = TestDataTransformation(row['input_a'], row['input_b'], 'mr3', 'mul', const)
                output_transformed_data_mul_mr4 = TestDataTransformation(row['input_a'], row['input_b'], 'mr4', 'mul', const) 

                checker_mr1_mul = MRsChecker(output=output_mul, t_output= output_transformed_data_mul_mr1, mr = 'mr1')
                checker_mr2_mul = MRsChecker(output=output_mul, t_output= output_transformed_data_mul_mr2, mr = 'mr2')
                checker_mr3_mul = MRsChecker(output=output_mul, t_output= output_transformed_data_mul_mr3, mr = 'mr3')
                checker_mr4_mul = MRsChecker(output=output_mul, t_output= output_transformed_data_mul_mr4, mr = 'mr4')

                df_output.at[index, 'MR1'] = checker_mr1_mul
                df_output.at[index, 'MR2'] = checker_mr2_mul
                df_output.at[index, 'MR3'] = checker_mr3_mul
                df_output.at[index, 'MR4'] = checker_mr4_mul

            # if row['operand'] == 'div':
            #     output_div = SutExecution(row['input_a'], row['input_b'], 'div')
            #     output_transformed_data_div_mr1 = TestDataTransformation(row['input_a'], row['input_b'], 'mr1', 'div', const)
            #     output_transformed_data_div_mr2 = TestDataTransformation(row['input_a'], row['input_b'], 'mr2', 'div', const)
            #     output_transformed_data_div_mr3 = TestDataTransformation(row['input_a'], row['input_b'], 'mr3', 'div', const)
            #     output_transformed_data_div_mr4 = TestDataTransformation(row['input_a'], row['input_b'], 'mr4', 'div', const)

            #     checker_mr1_div = MRsChecker(output=output_div, t_output= output_transformed_data_div_mr1, mr = 'mr1')
            #     checker_mr2_div = MRsChecker(output=output_div, t_output= output_transformed_data_div_mr2, mr = 'mr2')
            #     checker_mr3_div = MRsChecker(output=output_div, t_output= output_transformed_data_div_mr3, mr = 'mr3')
            #     checker_mr4_div = MRsChecker(output=output_div, t_output= output_transformed_data_div_mr4, mr = 'mr4')

        save(file_out)


main()





