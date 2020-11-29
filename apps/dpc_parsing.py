from workflow import config


class DPCParsing:

    def __init__(self):
        self.result_file_path = f'{config.result_file_path}'
        self.dsp_output_file_path = f'{config.dsp_output_file_path}'
        self.mscn_values = config.mscn_values

    # MGW Command
    def check_link_name_mgw_command(self):
        result_data = open(f"{self.result_file_path}", "r")
        result_data = result_data.read().splitlines()
        found_command = False
        first_link_name = False
        second_link_name = False
        for row in range(len(result_data)):
            if 'MML Command-----LST MTP2LNK:;' in result_data[row]:
                found_command = True
            elif found_command and 'G512NXCWT01_00' in result_data[row]:
                first_link_name = True
            elif found_command and 'G512NXCWT01_01' in result_data[row]:
                second_link_name = True
            elif first_link_name and second_link_name:
                break
            elif '(Number of results' in result_data[row] or '---    END' in result_data[row]:
                break
        return first_link_name and second_link_name

    def get_linkset_name_for_dpc1(self, mgw):
        try:
            result_data = open(f"{self.result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            link_name_list = []
            command = f'MML Command-----LST M2LKS:SGNM="{mgw}",LTP=LOCAL;'
            for row in range(len(result_data)):
                if command in result_data[row]:
                    found_command = 1
                if found_command == 1 and 'Linkset name' in result_data[row]:
                    start = row + 2
                    while '(Number of results ' not in result_data[start]:
                        link_name_line = result_data[start].split(' ')
                        flag = 0
                        for link_name in link_name_line:
                            if not link_name == '':
                                flag = flag + 1
                            if flag == 2:
                                link_name_list.append(link_name)
                                break
                        start = start + 1
                    return link_name_list
        except Exception as ex:
            print("false" + ex)

    def get_interface_id_list_dpc1(self):
        try:
            result_data = open(f"{self.result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            interface_id_list = []
            for row in range(len(result_data)):
                if 'MML Command-----LST N7LNK:LTP=LOCAL;' in result_data[row]:
                    found_command = 1
                elif found_command == 1 and 'Integer interface ID' in result_data[row]:
                    pos = result_data[row].index('Integer interface ID')
                    start = row + 2
                    flag = 0
                    while True:
                        if '---    END' in result_data[start] and 'To be continued...' not in result_data[start - 1]:
                            break
                        if '(Number of results' in result_data[start] or result_data[start].strip() == '':
                            flag = 1
                        elif flag == 1 and 'Integer interface ID' in result_data[start]:
                            start = start + 1
                            flag = 0
                        elif flag == 0:
                            line = result_data[start]
                            interface_id_list.append(int(line[pos:(pos + 4)].strip()))
                        start = start + 1
                    return interface_id_list

        except Exception as ex:
            print("false" + ex)

    def get_interface_id_dpc1(self):
        id_list = self.get_interface_id_list_dpc1()
        for i in range(1000, 10000):
            if i not in id_list:
                return i

    def get_mscn(self, ne_key):
        return "K'" + config.mscn_values[ne_key]

    def get_bill_office_num_list_dpc4(self):
        result_data = open(f"{self.result_file_path}", "r")
        result_data = result_data.read().splitlines()
        found_command = 0
        office_num_list = []
        for row in range(len(result_data)):
            if 'MML Command-----LST OFC:OFCTYPE=ALL,SMD=NO,SSR=NO,SADPC=NO,CLRDSP=NO,BOFFICEPARADSP=NO,OFFICECODECDSP=NO;' in \
                    result_data[row]:
                found_command = 1
            elif found_command == 1 and 'Bill office number' in result_data[row]:
                pos = result_data[row].index('Bill office number')
                start = row + 2
                flag = 0
                while True:
                    if '---    END' in result_data[start] and 'To be continued...' not in result_data[start - 1]:
                        break
                    if '(Number of results' in result_data[start] or result_data[start].strip() == '':
                        flag = 1
                    elif flag == 1 and 'Bill office number' in result_data[start]:
                        start = start + 1
                        flag = 0
                    elif flag == 0:
                        line = result_data[start]
                        office_num_list.append(int(line[pos:(pos + 4)].strip()))
                    start = start + 1
                return office_num_list

    def get_bill_office_num_dpc4(self):
        id_list = self.get_bill_office_num_list_dpc4()
        for i in range(0, 10000):
            if i not in id_list:
                return i

    def get_trunk_group_num_list_dpc5(self):
        result_data = open(f"{self.result_file_path}", "r")
        result_data = result_data.read().splitlines()
        found_command = 0
        office_num_list = []
        for row in range(len(result_data)):
            if 'LST N7TG:QR=LOCAL,SSR=NO,SRT=NO,SOF=NO,SL=NO,SC=NO,SS=NO,SOT=NO,CLRDSP=NO;' in result_data[row]:
                found_command = 1
            elif found_command == 1 and 'Trunk group number' in result_data[row]:
                pos = result_data[row].index('Trunk group number')
                start = row + 2
                flag = 0
                while True:
                    if '---    END' in result_data[start] and 'To be continued...' not in result_data[start - 1]:
                        break
                    if '(Number of results' in result_data[start] or result_data[start].strip() == '':
                        flag = 1
                    elif flag == 1 and 'Trunk group number' in result_data[start]:
                        start = start + 1
                        flag = 0
                    elif flag == 0:
                        line = result_data[start]
                        office_num_list.append(int(line[pos:(pos + 4)].strip()))
                    start = start + 1
                return office_num_list

    def get_trunk_group_num_dpc5(self):
        id_list = self.get_trunk_group_num_list_dpc5()
        for i in range(0, 10000):
            if i not in id_list:
                return i

    def get_link_no_list_dpc6(self):
        result_data = open(f"{self.result_file_path}", "r")
        result_data = result_data.read().splitlines()
        found_command = 0
        office_num_list = []
        for row in range(len(result_data)):
            if 'MML Command-----LST MTP2LNK:;' in result_data[row]:
                found_command = 1
            elif found_command == 1 and 'Link No.' in result_data[row]:
                pos = result_data[row].index('Link No.')
                start = row + 2
                flag = 0
                while True:
                    if '---    END' in result_data[start] and 'To be continued...' not in result_data[start - 1]:
                        break
                    if '(Number of results' in result_data[start] or result_data[start].strip() == '':
                        flag = 1
                    elif flag == 1 and 'Link No.' in result_data[start]:
                        start = start + 1
                        flag = 0
                    elif flag == 0:
                        line = result_data[start]
                        office_num_list.append(int(line[pos:(pos + 4)].strip()))
                    start = start + 1
                return office_num_list

    def get_link_no_dpc6(self):
        id_list = self.get_link_no_list_dpc6()
        for i in range(0, 10000):
            if i not in id_list:
                return i

    def get_ifbt_for_dpc6(self, fn, sn):
        result_data = open(f"{self.result_file_path}", "r")
        result_data = result_data.read().splitlines()
        found_command = 0
        key = 'Board type = '
        command = f'MML Command-----LST BRD:LM=FNSN,FN={fn},SN={sn},BP=BACK;'
        for row in range(len(result_data)):
            if command in result_data[row]:
                found_command = 1
            elif found_command == 1 and key in result_data[row]:
                pos = result_data[row].index(key)
                pos = pos + len(key)
                value = result_data[row]
                value = str(value[pos:]).strip()
                return value
            elif found_command == 1 and '---    END' in result_data[row]:
                break

    def get_ifbn_for_dpc6(self, fn, sn):
        result_data = open(f"{self.result_file_path}", "r")
        result_data = result_data.read().splitlines()
        found_command = 0
        key = 'Board No. '
        command = f'MML Command-----LST BRD:LM=FNSN,FN={fn},SN={sn},BP=BACK;'
        for row in range(len(result_data)):
            if command in result_data[row]:
                found_command = 1
            elif found_command == 1 and key in result_data[row]:
                pos = result_data[row].index(key)
                pos = pos + len(key)
                value = result_data[row]
                value = str(value[pos:]).strip()
                return value
            elif found_command == 1 and '---    END' in result_data[row]:
                break

    def get_bn_list(self):
        try:
            result_data = open(f"{self.dsp_output_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            bn_list = []
            for row in range(len(result_data)):
                if 'MML Command-----DSP CPUR:QM=BTBN,BT=SPF;' in result_data[row]:
                    found_command = 1
                elif '----------------------' in result_data[row + 1] and 'CPU ratio query result' in result_data[row]:
                    found_command = 2
                elif found_command == 2 and 'BN' in result_data[row]:
                    pos = result_data[row].index('BN')
                    start = row + 2
                    flag = 0
                    while True:
                        if '---    END' in result_data[start] or '(Number of results' in result_data[start] or \
                                result_data[start].strip() == '':
                            break
                        value = str(result_data[start])[pos:]
                        bn = ''
                        for v in value:
                            if v == ' ':
                                break
                            bn = bn + v
                        bn_list.append(bn.strip())
                        start = start + 1
                    return bn_list

        except Exception as ex:
            print("false" + ex)

    def get_spfbn_sbbn_for_dpc(self):
        bn_list = self.get_bn_list()
        for bn in bn_list:
            try:
                result_data = open(f"{self.dsp_output_file_path}", "r")
                result_data = result_data.read().splitlines()
                found_command = 0
                command = f'MML Command-----DSP SPFSUBRD:SPFBN={bn};'
                spf_bn_key = 'SPF board No.'
                sbbn_key = 'Sub-board No.'
                status_key = 'Status'
                for row in range(len(result_data)):
                    if command in result_data[row]:
                        found_command = 1
                    elif found_command == 1 and status_key in result_data[row]:
                        pos_sbbn = result_data[row].index(sbbn_key)
                        pos_status = result_data[row].index(status_key)
                        start = row + 2
                        while True:
                            if '---    END' in result_data[start] or '(Number of results' in result_data[start] or \
                                    result_data[start].strip() == '':
                                break
                            st = str(result_data[start])[pos_status:]
                            if st.lower() == 'normal':
                                value = str(result_data[start])[pos_sbbn:]
                                sbbn = ''
                                for v in value:
                                    if v == ' ':
                                        break
                                    sbbn = sbbn + v
                                return bn, sbbn
                            start = start + 1
            except Exception as ex:
                print("false" + ex)

    def get_lks_for_dpc6(self):
        result_data = open(f"{self.result_file_path}", "r")
        result_data = result_data.read().splitlines()
        found_command = 0
        command = f'LST L2UALKS:;'
        key = 'Linkset Name'
        link_no_list = []
        for row in range(len(result_data)):
            if command in result_data[row]:
                found_command = 1
            elif found_command == 1 and key in result_data[row]:
                pos = result_data[row].index(key)
                row = row + 2
                found_command = 2
            elif found_command == 1 and ('---    END' in result_data[row] or '(Number of results' in result_data[row]):
                break
            if found_command == 2:
                value = str(result_data[row])[pos:]
                link_no = ''
                for v in value:
                    if v == ' ':
                        break
                    link_no = link_no + v
                link_no_list.append(link_no)
        return link_no_list

    def get_ofc_no_dcp8(self, ofc_name):
        result_data = open(f"{self.result_file_path}", "r")
        result_data = result_data.read().splitlines()
        found_command = 0
        command = 'MML Command-----LST OFCNAME:;'
        for row in range(len(result_data)):
            if command in result_data[row]:
                found_command = 1
            elif found_command == 1 and ofc_name in result_data[row]:
                line = str(result_data[row]).split(' ')
                for l in line:
                    if l != '':
                        return l.strip()
            elif found_command == 1 and '---    END' in result_data[row]:
                break
