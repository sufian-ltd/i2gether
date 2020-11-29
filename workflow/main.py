from apps.stm_icx_route import StmIcxRoute
from apps.script_generator import ScriptGenerator
from apps.dpc_parsing import DPCParsing
from apps.consistency_check import ConsistencyCheck
from apps.dpc_script_generator import DPCScriptGenerator
from workflow import config

stm_icx_route_obj = StmIcxRoute()
script_generator_obj = ScriptGenerator()
dpc_parsing_obj = DPCParsing()
consistency_check_obj = ConsistencyCheck()
dpc_script_generator_obj = DPCScriptGenerator()

office_plan_data, signalling_plan_data, cic_plan_data, ckt_plan_data = stm_icx_route_obj.stm_icx_check(
    f'{config.stm_file_location}stm_icx_route.xlsx')

location = f'{config.script_location}'
stm_list_script_name = f'{config.stm_list_script_name}'
stm_add_script_name = f'{config.stm_add_script_name}'
stm_dpc_list_script_name = f'{config.stm_dpc_list_script_name}'
stm_consistency_list_script_name = f'{config.stm_consistency_list_script_name}'

# output file parsing
result_file_path = f'{config.result_file_path}'
consistency_file_path = f'{config.consistency_file_path}'

script_generator_obj.lst_script_generation(office_plan_data, signalling_plan_data, location, stm_list_script_name)
script_generator_obj.add_script_generation_for_ipc(office_plan_data, cic_plan_data, location, stm_add_script_name)
script_generator_obj.lst_script_generation_for_dpc(office_plan_data, signalling_plan_data, location,
                                                   stm_dpc_list_script_name)
script_generator_obj.dpc_add_script_generate(office_plan_data, signalling_plan_data, ckt_plan_data, location,
                                             stm_add_script_name)
script_generator_obj.consistency_list_script_generate(office_plan_data, signalling_plan_data, location,
                                                      stm_consistency_list_script_name)
