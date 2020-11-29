base_location = r'E:/I2Gether/'
script_location = f'{base_location}STM_Expansion_for_ICX_Route/scripts/'
stm_file_location = f'{base_location}STM_Expansion_for_ICX_Route/'
# stm_lst_script_name = f'stm_lst_script.txt'
# stm_add_ipc_script_name = f'stm_add_ipc_script.txt'
# stm_lst_dpc_script_name = f'stm_lst_dpc_script.txt'
# stm_add_dpc_script_name = f'stm_lst_dpc_script.txt'

stm_list_script_name = f'stmlistscript.txt'
stm_dpc_list_script_name = f'stmdpclistscript.txt'
stm_consistency_list_script_name = f'stmconsistencylistscript.txt'
stm_add_script_name = f'stmaddscript.txt'

# ouputfile
result_file_location = f'{base_location}STM_Expansion_for_ICX_Route/output/'
result_file_name = f'stmdpclst_20201119120229_itautobot_8852.rst'
result_file_path = f'{result_file_location}{result_file_name}'

# consistency check
consistency_output_file_name = f'nemsc_20201122184738_itautobot_8952.rst'
consistency_file_path = f'{result_file_location}{consistency_output_file_name}'

dsp_output_file_name = f'dspcmd_20201126181539_itautobot_267.rst'
dsp_output_file_path = f'{result_file_location}{dsp_output_file_name}'

# dpc1 mscn
mscn_values = {
    "DG05": "8801801000068",
    "DGO6": "8801801000064",
    "DGO10": "8801801000065",
    "CG11": "8801801000062",
    "CG12": "8801801000067"
}

# msc code for run
command_code = {
    "DG05": "{DG05_MSOFTX}",
    "DG08_MGW12": "{DG08_MGW12}"
}
