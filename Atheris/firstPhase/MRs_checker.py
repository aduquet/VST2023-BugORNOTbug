import pandas as pd

## 0 means violated
## 1 means not-violated

# ,id,input_a,input_b,output_add,output_sub,output_add_MR1,output_sub_MR1,output_add_MR2,output_sub_MR2,output_add_MR3,output_sub_MR3,output_add_MR4,output_sub_MR4

def MRsChecker(df):

    for index, row in df.iterrows():
        #### ADD
        ## MR_1 ##
        if row['output_add'] == row['output_add_MR1']:
            finalLog.at[index, 'MR1_checker_add'] = 'No-violated'

        if row['output_add'] != row['output_add_MR1']:
            finalLog.at[index, 'MR1_checker_add'] = 'Violated'

        ## MR_2 ##
        # Must to be <
        if row['output_add'] < row['output_add_MR2']:
            finalLog.at[index, 'MR2_checker_add'] = 'No-violated'

        if row['output_add'] >= row['output_add_MR2']:
            finalLog.at[index, 'MR2_checker_add'] = 'Violated'

        ## MR_3 ##
        if row['output_add'] == row['output_add_MR3']:
            finalLog.at[index, 'MR3_checker_add'] = 'No-violated'

        if row['output_add'] != row['output_add_MR3']:
            finalLog.at[index, 'MR3_checker_add'] = 'Violated'


        ## MR_4 ##
        if row['output_add'] == row['output_add_MR4']:
            finalLog.at[index, 'MR4_checker_add'] = 'No-violated'

        if row['output_add'] != row['output_add_MR4']:
            finalLog.at[index, 'MR4_checker_add'] = 'Violated'

        ### SUB

                ## MR_1 ##
        if row['output_sub'] == row['output_sub_MR1']:
            finalLog.at[index, 'MR1_checker_sub'] = 'No-violated'

        if row['output_sub'] != row['output_sub_MR1']:
            finalLog.at[index, 'MR1_checker_sub'] = 'Violated'

        ## MR_2 ##
        # Must to be <
        if row['output_sub'] < row['output_sub_MR2']:
            finalLog.at[index, 'MR2_checker_sub'] = 'No-violated'

        if row['output_sub'] >= row['output_sub_MR2']:
            finalLog.at[index, 'MR2_checker_sub'] = 'Violated'

        ## MR_3 ##
        if row['output_sub'] == row['output_sub_MR3']:
            finalLog.at[index, 'MR3_checker_sub'] = 'No-violated'

        if row['output_sub'] != row['output_sub_MR3']:
            finalLog.at[index, 'MR3_checker_sub'] = 'Violated'


        ## MR_4 ##
        if row['output_sub'] == row['output_sub_MR4']:
            finalLog.at[index, 'MR4_checker_sub'] = 'No-violated'

        if row['output_sub'] != row['output_sub_MR4']:
            finalLog.at[index, 'MR4_checker_sub'] = 'Violated'


def save(file_out):
    finalLog.to_csv(file_out + '.csv')

if __name__ == '__main__':
    
    import click

    @click.command()
    @click.option('-i', '--file', 'file_in', help='Path for getting the data')
    @click.option('-o', '--out', 'file_out', help='Name of the file in which data will be stored')

    def main(file_in, file_out):

        df = pd.read_csv(file_in, index_col=0)

        global finalLog
        finalLog = df.copy()

        MRsChecker(df)
        save(file_out)

main()

        


