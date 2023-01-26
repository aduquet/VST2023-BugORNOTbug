# python3 SUT_onlySum.py -i randonFuncCalls_files/fuzzerInputs_v11.csv -o log
# python3 SUT_onlySub.py -i randonFuncCalls_files/fuzzerInputs_v11.csv -o log

python3 SUT_onlySum_sameConstant.py -i randonFuncCalls_files/fuzzerInputs_v11.csv -o log
python3 SUT_onlySub_sameConstant.py -i randonFuncCalls_files/fuzzerInputs_v11.csv -o log