import matplotlib.pyplot as plt
from typing import List
import pandas as pd
import numpy as np
import random

def sum(a,b):
    return a + b

def sub(a,b):
    return a - b

if __name__ == '__main__':
    
    import click

    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-o', '--out', 'file_out', help='Name of the file in which data will be stored')

    def main(file_in, file_out):

        df = pd.read_csv(file_in, index_col = 0 )
        mrInputs = pd.read_csv('randonFuncCalls_files/MRsInputs.csv', index_col= 0)

        df_output = df.copy()
        # df['output'] = 0

        for index, row in df.iterrows():
            if row['operand_str'] == 'sum':
                df_output.at[index, 'output'] = sub(row['input_a'], row['input_b'])
                df_output.at[index, 'operand_str'] = 'sub'
                df_output.at[index, 'operand'] = 1

            if row['operand_str'] == 'sub':
                df_output.at[index, 'output'] = sub(row['input_a'], row['input_b'])
                df_output.at[index, 'operand'] = 1


        # MR1 TRANSFORTATION (Permutation of the input)
        for index, row in df.iterrows():
            df_output.at[index, 'operand'] = 1
            if row['operand_str'] == 'sum':

                df_output.at[index, 'MR1_input_a'] = row['input_b']
                df_output.at[index, 'MR1_input_b'] = row['input_a']
                df_output.at[index, 'MR1_output'] = sub( row['input_b'], row['input_a'])
                df_output.at[index, 'operand_str'] = 'sub'
                

            if row['operand_str'] == 'sub':

                df_output.at[index, 'MR1_input_a'] = row['input_b']
                df_output.at[index, 'MR1_input_b'] = row['input_a']
                df_output.at[index, 'MR1_output'] = sub(row['input_b'], row['input_a'])


        # MR2 TRANSFORTATION (Multiply by a positive constant )
        for index, row in df.iterrows():
            df_output.at[index, 'operand'] = 1

            constant = mrInputs.at[index, 'MR_2']
            df_output.at[index, 'constant_MR2'] = constant
            if row['operand_str'] == 'sum':
                a = row['input_a'] * constant
                b = row['input_b'] * constant

                df_output.at[index, 'MR2_input_a'] = a
                df_output.at[index, 'MR2_input_b'] = b
                df_output.at[index, 'MR2_output'] = sub(a, b)
                df_output.at[index, 'operand_str'] = 'sub'
                df_output.at[index, 'operand'] = 1

            if row['operand_str'] == 'sub':
                a = row['input_a'] * constant
                b = row['input_b'] * constant

                df_output.at[index, 'MR2_input_a'] = a
                df_output.at[index, 'MR2_input_b'] = b
                df_output.at[index, 'MR2_output'] = sub(a, b)


        # MR3 TRANSFORTATION (Adding a positive constant to each operand )
        for index, row in df.iterrows():
            df_output.at[index, 'operand'] = 1
            constant = mrInputs.at[index, 'MR_3']
            df_output.at[index, 'constant_MR3'] = constant
            if row['operand_str'] == 'sum':
                a = row['input_a'] + constant
                b = row['input_b'] + constant
                
                df_output.at[index, 'MR3_input_a'] = a
                df_output.at[index, 'MR3_input_b'] = b
                df_output.at[index, 'MR3_output'] = sub(a, b)
                df_output.at[index, 'operand_str'] = 'sub'
                df_output.at[index, 'operand'] = 1

            if row['operand_str'] == 'sub':
                a = row['input_a'] + constant
                b = row['input_b'] + constant

                df_output.at[index, 'MR3_input_a'] = a
                df_output.at[index, 'MR3_input_b'] = b
                df_output.at[index, 'MR3_output'] = sub(a, b)
                df_output.at[index, 'operand_str'] = 'sub'
                df_output.at[index, 'operand'] = 0

        # MR4 TRANSFORTATION (Adding a positive constant to each operand )
        for index, row in df.iterrows():
            df_output.at[index, 'operand'] = 1

            constant = mrInputs.at[index, 'MR_4']
            df_output.at[index, 'constant_MR4'] = constant
            if row['operand_str'] == 'sum':
                a = row['input_a'] - constant
                b = row['input_b'] - constant
                
                df_output.at[index, 'MR4_input_a'] = a
                df_output.at[index, 'MR4_input_b'] = b
                df_output.at[index, 'MR4_output'] = sub(a, b)
                df_output.at[index, 'operand_str'] = 'sub'
                df_output.at[index, 'operand'] = 1

            if row['operand_str'] == 'sub':
                a = row['input_a'] - constant
                b = row['input_b'] - constant

                df_output.at[index, 'MR4_input_a'] = a
                df_output.at[index, 'MR4_input_b'] = b
                df_output.at[index, 'MR4_output'] = sub(a, b)

        df_output.to_csv(file_out + '_sub.csv')

        print(df_output)
main()