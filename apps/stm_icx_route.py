import pandas as pd


class StmIcxRoute:

    def __init__(self):
        pass

    def stm_icx_check(self, loc):
        # fetching excel data
        # encoding = 'ISO-8859-1'

        try:
            office_df = pd.read_excel(loc, 'Office')
            signalling_df = pd.read_excel(loc, 'Signalling')
            cic_df = pd.read_excel(loc, 'CIC')
            ckt_df = pd.read_excel(loc, 'Ckt selection mode')

            # print(pd.read_excel(loc).columns)

            # print(excel_all_data)
            # extracting all columns header row name
            office_columns_headers_row = office_df.columns.ravel()
            office_result_data = pd.DataFrame(office_df,
                                              columns=['Node', 'Office Direction Name', 'TG name', 'OPC', 'DPC',
                                                       'Start CIC',
                                                       'End CIC', 'SLC', 'MGW', 'MGW port (f-s-p)'])

            signalling_columns_headers_row = signalling_df.columns.ravel()
            signalling_result_data = pd.DataFrame(signalling_df,
                                                  columns=['Node', 'TG name', 'Link Name', 'Frame-Slot-Port', 'E1 no',
                                                           'TS'])

            cic_columns_headers_row = cic_df.columns.ravel()
            cic_result_data = pd.DataFrame(cic_df,
                                           columns=['Node', 'Office direction name', 'Trunk group name', 'OPC', 'DPC',
                                                    'Start CIC', 'End CIC.', 'Start TID.', 'End TID.'])

            ckt_columns_headers_row = ckt_df.columns.ravel()
            ckt_result_data = pd.DataFrame(ckt_df,
                                           columns=['Node', 'TG name', 'Circuit Selection Mode'])

            office_target_header = ['Node', 'Office Direction Name', 'TG name', 'OPC', 'DPC', 'Start CIC', 'End CIC',
                                    'SLC',
                                    'MGW', 'MGW port (f-s-p)']

            signalling_target_header = ['Node', 'TG name', 'Link Name', 'Frame-Slot-Port', 'E1 no', 'TS']

            cic_target_header = ['Node', 'Office direction name', 'Trunk group name', 'OPC', 'DPC',
                                 'Start CIC', 'End CIC.', 'Start TID.', 'End TID.']

            ckt_target_header = ['Node', 'TG name', 'Circuit Selection Mode']

            if all(item in office_columns_headers_row for item in office_target_header) and all(
                    item in signalling_columns_headers_row for item in signalling_target_header) and all(
                item in cic_columns_headers_row for item in cic_target_header) and all(
                item in ckt_columns_headers_row for item in ckt_target_header):
                return office_result_data.values, signalling_result_data.values, cic_result_data.values, ckt_result_data.values
            else:
                exit('plan not matched')
        except Exception as e:
            print("Plan format file  read not matched")
