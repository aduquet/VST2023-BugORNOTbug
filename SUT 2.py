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
        # mrInputs = pd.read_csv('MRsInputs.csv', index_col= 0)

        df_output = df.copy()
        # df['output'] = 0

        for index, row in df.iterrows():
            constant = df.at[index, 'const']

            if row['operand'] == 'sum':
                df_output.at[index, 'output'] = sum(row['input_a'], row['input_b'])

            if row['operand'] == 'sub':
                df_output.at[index, 'output'] = sub(row['input_a'], row['input_b'])

        # MR1 TRANSFORTATION (Permutation of the input)
        for index, row in df.iterrows():
            if row['operand'] == 'sum':

                df_output.at[index, 'MR1_input_a'] = row['input_b']
                df_output.at[index, 'MR1_input_b'] = row['input_a']
                df_output.at[index, 'MR1_inputs'] = '(' + str(row['input_b']) + ',' + str(row['input_a']) + ')'
                df_output.at[index, 'MR1_output'] = sum( row['input_b'], row['input_a'])

            if row['operand'] == 'sub':

                df_output.at[index, 'MR1_input_a'] = row['input_b']
                df_output.at[index, 'MR1_input_b'] = row['input_a']
                df_output.at[index, 'MR1_inputs'] = '(' + str(row['input_b']) + ',' + str(row['input_a']) + ')'
                df_output.at[index, 'MR1_output'] = sub(row['input_b'], row['input_a'])

        # MR2 TRANSFORTATION (Multiply by a positive constant )
        for index, row in df.iterrows():

            if row['operand'] == 'sum':
                a = row['input_a'] * constant
                b = row['input_b'] * constant

                df_output.at[index, 'MR2_input_a'] = a
                df_output.at[index, 'MR2_input_b'] = b
                df_output.at[index, 'MR2_inputs'] = '(' + str(a) + ',' + str(b) + ')'
                df_output.at[index, 'MR2_output'] = sum(a, b)

            if row['operand'] == 'sub':
                a = row['input_a'] * constant
                b = row['input_b'] * constant

                df_output.at[index, 'MR2_input_a'] = a
                df_output.at[index, 'MR2_input_b'] = b
                df_output.at[index, 'MR2_inputs'] = '(' + str(a) + ',' + str(b) + ')'
                df_output.at[index, 'MR2_output'] = sub(a, b)

        # MR3 TRANSFORTATION (Adding a positive constant to each operand )
        for index, row in df.iterrows():
            
            if row['operand'] == 'sum':
                a = row['input_a'] + constant
                b = row['input_b'] + constant
                
                df_output.at[index, 'MR3_input_a'] = a
                df_output.at[index, 'MR3_input_b'] = b
                df_output.at[index, 'MR3_inputs'] = '(' + str(a) + ',' + str(b) + ')'
                df_output.at[index, 'MR3_output'] = sum(a, b)

            if row['operand'] == 'sub':
                a = row['input_a'] + constant
                b = row['input_b'] + constant

                df_output.at[index, 'MR3_input_a'] = a
                df_output.at[index, 'MR3_input_b'] = b
                df_output.at[index, 'MR3_inputs'] = '(' + str(a) + ',' + str(b) + ')'
                df_output.at[index, 'MR3_output'] = sub(a, b)

        # MR4 TRANSFORTATION (Adding a positive constant to each operand )
        for index, row in df.iterrows():

            if row['operand'] == 'sum':
                a = row['input_a'] - constant
                b = row['input_b'] - constant
                
                df_output.at[index, 'MR4_input_a'] = a
                df_output.at[index, 'MR4_input_b'] = b
                df_output.at[index, 'MR4_inputs'] = '(' + str(a) + ',' + str(b) + ')'
                df_output.at[index, 'MR4_output'] = sum(a, b)

            if row['operand'] == 'sub':
                a = row['input_a'] - constant
                b = row['input_b'] - constant
                df_output.at[index, 'MR4_input_a'] = a
                df_output.at[index, 'MR4_input_b'] = b
                df_output.at[index, 'MR4_inputs'] = '(' + str(a) + ',' + str(b) + ')'
                df_output.at[index, 'MR4_output'] = sub(a, b)

        df_output.to_csv(file_out + '.csv')

main()