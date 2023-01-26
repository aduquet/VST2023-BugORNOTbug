import pandas as pd

## 0 means violated
## 1 means not-violated

def MRsChecker(df):

    for index, row in df.iterrows():
        
        ## MR_1 ##
        if row['output'] == row['MR1_output']:
            finalLog.at[index, 'MR1_checker'] = 'No-violated'

        if row['output'] != row['MR1_output']:
            finalLog.at[index, 'MR1_checker'] = 'Violated'

        ## MR_2 ##
        # Must to be <
        if row['output'] < row['MR2_output']:
            finalLog.at[index, 'MR2_checker'] = 'No-violated'

        if row['output'] >= row['MR2_output']:
            finalLog.at[index, 'MR2_checker'] = 'Violated'

        ## MR_3 ##
        if row['output'] == row['MR3_output']:
            finalLog.at[index, 'MR3_checker'] = 'No-violated'

        if row['output'] != row['MR3_output']:
            finalLog.at[index, 'MR3_checker'] = 'Violated'


        ## MR_4 ##
        if row['output'] == row['MR4_output']:
            finalLog.at[index, 'MR4_checker'] = 'No-violated'

        if row['output'] != row['MR4_output']:
            finalLog.at[index, 'MR4_checker'] = 'Violated'



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

        


