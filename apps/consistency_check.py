from workflow import config

class ConsistencyCheck:

    def __init__(self):
        pass

    def command1(self, result_file_path, office_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                node = office_plan_data[row_plan][0]
                tg_name = office_plan_data[row_plan][2]
                opc = office_plan_data[row_plan][3]
                dpc = office_plan_data[row_plan][4]
                command = f"""LST N7DSP:DPNM="{tg_name}",SHLINK=FALSE,SHOFC=FALSE,LTP=LOCAL,SICFGDSP=NO;"""
                found_command = 0
                key_opc = 'Originating point code  =  '
                key_dpc = 'National network DPC  =  '
                key_node = 'Server name  =  '
                result_count = 0
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_dpc in result_data[row_data]:
                        pos = result_data[row_data].index(key_dpc)
                        pos = pos + len(key_dpc)
                        value = result_data[row_data]
                        value = value[pos:]
                        if value == dpc:
                            result_count = result_count + 1
                    elif found_command == 1 and key_opc in result_data[row_data]:
                        pos = result_data[row_data].index(key_opc)
                        pos = pos + len(key_opc)
                        value = result_data[row_data]
                        value = value[pos:]
                        if value == opc:
                            result_count = result_count + 1
                    elif found_command == 1 and key_node in result_data[row_data]:
                        pos = result_data[row_data].index(key_node)
                        pos = pos + len(key_node)
                        value = result_data[row_data]
                        value = value[pos:]
                        if value == node:
                            result_count = result_count + 1
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break

                if result_count != 3:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    def command2(self, result_file_path, office_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                node = office_plan_data[row_plan][0]
                tg_name = office_plan_data[row_plan][2]
                opc = office_plan_data[row_plan][3]
                dpc = office_plan_data[row_plan][4]
                command = f"""LST N7LKS:LSNM="{tg_name}",LTP=LOCAL;"""
                found_command = 0
                key_opc = 'OPC  =  '
                key_dpc = 'National network DPC  =  '
                result_count = 0
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_dpc in result_data[row_data]:
                        pos = result_data[row_data].index(key_dpc)
                        pos = pos + len(key_dpc)
                        value = result_data[row_data]
                        value = value[pos:]
                        if value == dpc:
                            result_count = result_count + 1
                    elif found_command == 1 and key_opc in result_data[row_data]:
                        pos = result_data[row_data].index(key_opc)
                        pos = pos + len(key_opc)
                        value = result_data[row_data]
                        value = value[pos:]
                        if value == opc:
                            result_count = result_count + 1
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break

                if result_count != 2:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    def command3(self, result_file_path, office_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                node = office_plan_data[row_plan][0]
                tg_name = office_plan_data[row_plan][2]
                command = f"""LST N7RT:RTNM="{tg_name}",LTP=LOCAL;"""
                found_command = 0
                key_1 = 'Linkset name  =  '
                key_2 = 'DSP name  =  '
                result_count = 0
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_1 in result_data[row_data]:
                        pos = result_data[row_data].index(key_1)
                        pos = pos + len(key_1)
                        value = result_data[row_data]
                        value = value[pos:]
                        if value == tg_name:
                            result_count = result_count + 1
                    elif found_command == 1 and key_2 in result_data[row_data]:
                        pos = result_data[row_data].index(key_2)
                        pos = pos + len(key_2)
                        value = result_data[row_data]
                        value = value[pos:]
                        if value == tg_name:
                            result_count = result_count + 1
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break

                if result_count != 2:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    def command_4_5(self, result_file_path, office_plan_data, signalling_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(signalling_plan_data)):
                tg_name_signalling = signalling_plan_data[row_plan][1]
                link_name = signalling_plan_data[row_plan][2]
                command = f"""LST N7LNK:LNKNM="{link_name}",LTP=LOCAL;"""
                key_1 = 'Linkset name  =  '
                for row_office in range(len(office_plan_data)):
                    tg_name_office = office_plan_data[row_office][2]
                    if tg_name_signalling == tg_name_office:
                        found_command = 0
                        status = False
                        for row_data in range(len(result_data)):
                            if command in result_data[row_data]:
                                found_command = 1
                            elif found_command == 1 and key_1 in result_data[row_data]:
                                pos = result_data[row_data].index(key_1)
                                pos = pos + len(key_1)
                                value = result_data[row_data]
                                value = value[pos:]
                                if value == tg_name_office:
                                    status = True
                                    break
                            elif found_command == 1 and '---    END' in result_data[row_data]:
                                break
                        if not status:
                            return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    def command6(self, result_file_path, office_plan_data,mscn_values):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                node = office_plan_data[row_plan][0]
                tg_name = office_plan_data[row_plan][2]
                command = f"""LST CALLSRC:CSCNAME="{tg_name}",QR=LOCAL;"""
                found_command = 0
                key_1 = 'Local MSC number  =  '
                status = False
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_1 in result_data[row_data]:
                        pos = result_data[row_data].index(key_1)
                        pos = pos + len(key_1)
                        value = result_data[row_data]
                        value = value[pos:]
                        if value == config.mscn_values[node]:
                            status = True
                            break
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break
                if not status:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    def command7(self, result_file_path, office_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                tg_name = office_plan_data[row_plan][2]
                command = f"""LST CLDPREANA:CSCNAME="{tg_name}",PFX=K'018,MINCLDLEN=11,QR=LOCAL;"""
                found_command = 0
                key_1 = 'RETCODE = 0  Operation succeeded'
                status = False
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_1 in result_data[row_data]:
                        status = True
                        break
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break
                if not status:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    def command8(self, result_file_path, office_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                tg_name = office_plan_data[row_plan][2]
                command = f"""LST CLDPREANA:CSCNAME="{tg_name}",PFX=K'0180,MINCLDLEN=11,QR=LOCAL;"""
                found_command = 0
                key_1 = 'RETCODE = 0  Operation succeeded'
                status = False
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_1 in result_data[row_data]:
                        status = True
                        break
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break
                if not status:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    def command9(self, result_file_path, office_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                tg_name = office_plan_data[row_plan][2]
                command = f"""LST CLDPREANA:CSCNAME="{tg_name}",PFX=K'016,MINCLDLEN=11,QR=LOCAL;"""
                found_command = 0
                key_1 = 'RETCODE = 0  Operation succeeded'
                status = False
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_1 in result_data[row_data]:
                        status = True
                        break
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break
                if not status:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    def command10(self, result_file_path, office_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                tg_name = office_plan_data[row_plan][2]
                command = f"""LST CLDPREANA:CSCNAME="{tg_name}",PFX=K'0160,MINCLDLEN=11,QR=LOCAL;"""
                found_command = 0
                key_1 = 'RETCODE = 0  Operation succeeded'
                status = False
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_1 in result_data[row_data]:
                        status = True
                        break
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break
                if not status:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    def command11(self, result_file_path, office_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                tg_name = office_plan_data[row_plan][2]
                command = f"""CLDPREANA:CSCNAME="{tg_name}",PFX=K'EEEEEEEE,MINCLDLEN=1,QR=LOCAL;"""
                found_command = 0
                key_1 = 'RETCODE = 0  Operation succeeded'
                status = False
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_1 in result_data[row_data]:
                        status = True
                        break
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break
                if not status:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    def command12(self, result_file_path, office_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                office_direction_name = office_plan_data[row_plan][1]
                dpc = office_plan_data[row_plan][4]
                dpc = ''.join(filter(lambda i: i.isdigit(), dpc))
                command = f"""LST OFC:ON="{office_direction_name}",OFCTYPE=ALL,SMD=NO,SSR=NO,SADPC=NO,CLRDSP=NO,DPC="{dpc}",BOFFICEPARADSP=NO,OFFICECODECDSP=NO;"""
                found_command = 0
                key_1 = 'RETCODE = 0  Operation succeeded'
                status = False
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_1 in result_data[row_data]:
                        status = True
                        break
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break
                if not status:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    def command13(self, result_file_path, office_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                office_direction_name = office_plan_data[row_plan][1]
                command = f"""LST BILLCTRL:OFFICENAME="{office_direction_name}";"""
                found_command = 0
                key_1 = 'RETCODE = 0  Operation succeeded'
                status = False
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_1 in result_data[row_data]:
                        status = True
                        break
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break
                if not status:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    def command14(self, result_file_path, office_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                tg_name = office_plan_data[row_plan][2]
                command = f"""LST SRT:SRN="G512NXCWT01",QR=LOCAL,SRT=NO,ST=NO;"""
                found_command = 0
                key_1 = 'RETCODE = 0  Operation succeeded'
                status = False
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_1 in result_data[row_data]:
                        status = True
                        break
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break
                if not status:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    def command16(self, result_file_path, office_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                tg_name = office_plan_data[row_plan][2]
                command = f"""LST RTANA:RSN="{tg_name}",SRT=NO,SPFX=NO,QR=LOCAL;"""
                found_command = 0
                key_1 = 'RETCODE = 0  Operation succeeded'
                status = False
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_1 in result_data[row_data]:
                        status = True
                        break
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break
                if not status:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    def command17(self, result_file_path, office_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                tg_name = office_plan_data[row_plan][2]
                command = f"""LST N7TG:TGN="{tg_name}",QR=LOCAL,MGWNAME="DG05_MGW12_KHL",SRN="G512NXCWT01",CSCNAME="G512NXCWT01",SOPC="H’002157",SDPC="H’002172",SSR=NO,SRT=NO,SOF=NO,SL=NO,SC=NO,SS=NO,SOT=NO,CLRDSP=NO;"""
                found_command = 0
                key_1 = 'RETCODE = 0  Operation succeeded'
                status = False
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_1 in result_data[row_data]:
                        status = True
                        break
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break
                if not status:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    def command18(self, result_file_path, office_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                tg_name = office_plan_data[row_plan][2]
                command = f"""LST OUTNUMPREPRO:TGN="{tg_name}",QR=LOCAL;"""
                found_command = 0
                key_1 = 'RETCODE = 0  Operation succeeded'
                status = False
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_1 in result_data[row_data]:
                        status = True
                        break
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break
                if not status:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

    #nothing to check
    def command19(self, result_file_path, office_plan_data):
        try:
            result_data = open(f"{result_file_path}", "r")
            result_data = result_data.read().splitlines()
            found_command = 0
            for row_plan in range(len(office_plan_data)):
                tg_name = office_plan_data[row_plan][2]
                command = f"""DSP TGTK:TGN="{tg_name}";"""
                found_command = 0
                key_1 = 'RETCODE = 0  Operation succeeded'
                status = False
                for row_data in range(len(result_data)):
                    if command in result_data[row_data]:
                        found_command = 1
                    elif found_command == 1 and key_1 in result_data[row_data]:
                        status = True
                        break
                    elif found_command == 1 and '---    END' in result_data[row_data]:
                        break
                if not status:
                    return 'Reject'
            return 'Accept'

        except Exception as ex:
            print("false" + "ex")

