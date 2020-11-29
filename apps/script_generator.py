import pandas as pd
from workflow import config
from apps.dpc_parsing import DPCParsing
from apps.dpc_script_generator import DPCScriptGenerator


class ScriptGenerator:
    def __init__(self):
        pass

    def lst_script_generation(self, office_plan_data, signalling_plan_data, location, file_name):

        stm_lst_scripts = []
        for row in range(len(office_plan_data)):
            node = office_plan_data[row][0]
            device_code = config.command_code[node]
            office_direction_name = office_plan_data[row][1]
            tg_name = office_plan_data[row][2]
            opc = office_plan_data[row][3]
            dpc = office_plan_data[row][4]
            dpc = ''.join(filter(lambda i: i.isdigit(), dpc))

            stm_lst_scripts.append(
                f"""LST N7DSP:DPNM="{tg_name}",SHLINK=FALSE,SHOFC=FALSE,LTP=LOCAL,SICFGDSP=NO;{device_code}""")
            stm_lst_scripts.append(
                f"""LST N7DSP:DPC="{dpc}",SHLINK=FALSE,SHOFC=FALSE,LTP=LOCAL,SICFGDSP=NO;{device_code}""")
            stm_lst_scripts.append(f"""LST N7LKS:LSNM="{tg_name}",LTP=LOCAL;{device_code}""")
            stm_lst_scripts.append(f"""LST N7LKS:LSNM="{tg_name}",ASPNM="G512NXCWT01",LTP=LOCAL;{device_code}""")
            stm_lst_scripts.append(f"""LST N7RT:RTNM="{tg_name}",LTP=LOCAL;{device_code}""")
            stm_lst_scripts.append(f"""LST N7RT:RTNM="{tg_name}",DPNM="{tg_name}",LTP=LOCAL;{device_code}""")
            stm_lst_scripts.append(f"""LST N7RT:RTNM="{tg_name}",LSNM="{tg_name}",LTP=LOCAL;{device_code}""")
            stm_lst_scripts.append(f"""LST N7LNK:LNKNM="{tg_name}",LTP=LOCAL;{device_code}""")
            stm_lst_scripts.append(f"""LST N7LNK:LSNM="{tg_name}",LTP=LOCAL;{device_code}""")
            stm_lst_scripts.append(f"""LST CALLSRC:CSCNAME="{tg_name}",QR=LOCAL;{device_code}""")
            stm_lst_scripts.append(f"""LST CLDPREANA:CSCNAME="{tg_name}",QR=LOCAL;{device_code}""")
            stm_lst_scripts.append(
                f"""LST CLDPREANA:CSCNAME="{tg_name}",PFX=K'018,MINCLDLEN=11,QR=LOCAL;{device_code}""")
            stm_lst_scripts.append(
                f"""LST CLDPREANA:CSCNAME="{tg_name}",PFX=K'0180,MINCLDLEN=11,QR=LOCAL;{device_code}""")
            stm_lst_scripts.append(
                f"""LST CLDPREANA:CSCNAME="{tg_name}",PFX=K'016,MINCLDLEN=11,QR=LOCAL;{device_code}""")
            stm_lst_scripts.append(
                f"""LST CLDPREANA:CSCNAME="{tg_name}",PFX=K'0160,MINCLDLEN=11,QR=LOCAL;{device_code}""")
            stm_lst_scripts.append(
                f"""LST CLDPREANA:CSCNAME="{tg_name}",PFX=K'EEEEEEEE,MINCLDLEN=1,QR=LOCAL;{device_code}""")

            stm_lst_scripts.append(
                f"""LST OFC:ON="{office_direction_name}",OFCTYPE=ALL,SMD=NO,SSR=NO,SADPC=NO,CLRDSP=NO,BOFFICEPARADSP=NO,OFFICECODECDSP=NO;{device_code}""")
            stm_lst_scripts.append(
                f"""LST OFC:OFCTYPE=ALL,SMD=NO,SSR=NO,SADPC=NO,CLRDSP=NO,DPC="{dpc}",BOFFICEPARADSP=NO,OFFICECODECDSP=NO;{device_code}""")

            stm_lst_scripts.append(f"""LST BILLCTRL:OFFICENAME="{office_direction_name}";{device_code}""")
            stm_lst_scripts.append(f"""LST SRT:SRN="{tg_name}",QR=LOCAL,SRT=NO,ST=NO;{device_code}""")
            stm_lst_scripts.append(
                f"""LST RT:RN="{tg_name}",SSR=NO,SRA=NO,SOFC=NO,SPFX=NO,SDSRT=NO,QR=LOCAL;{device_code}""")
            stm_lst_scripts.append(f"""LST RTANA:RSN="{tg_name}",SRT=NO,SPFX=NO,QR=LOCAL;{device_code}""")
            stm_lst_scripts.append(
                f"""LST N7TG:TGN="{tg_name}",QR=LOCAL,SSR=NO,SRT=NO,SOF=NO,SL=NO,SC=NO,SS=NO,SOT=NO,CLRDSP=NO;{device_code}""")
            stm_lst_scripts.append(
                f"""LST N7TG:QR=LOCAL,SOPC="{opc}",SDPC="{dpc}",SSR=NO,SRT=NO,SOF=NO,SL=NO,SC=NO,SS=NO,SOT=NO,CLRDSP=NO;{device_code}""")
            stm_lst_scripts.append(f"""LST OUTNUMPREPRO:TGN="{tg_name}",QR=LOCAL;{device_code}""")
            stm_lst_scripts.append(
                f"""LST N7TKC:TGN="{tg_name}",QR=LOCAL,SO=NO,ST=NO,SSR=NO,SRT=NO,SOF=NO;{device_code}""")

        device_code = config.command_code['DG05']
        for row in range(len(signalling_plan_data)):
            node = signalling_plan_data[row][0]
            link_name = signalling_plan_data[row][2]
            stm_lst_scripts.append(f"""LST N7LNK:LNKNM="{link_name}",LTP=LOCAL;{device_code}""")

        stm_lst_scripts.append(f"""LST MTP2LNK:;{device_code}""")

        try:
            file_handle = open(f"{location}{file_name}", 'w')
            for value in stm_lst_scripts:
                file_handle.write(value + '\n')
            file_handle.close()
        except Exception as e:
            print(f'{e}')

    def add_script_generation_for_ipc(self, office_plan_data, cic_plan_data, location, file_name):
        stm_add_scripts = []
        for row in range(len(office_plan_data)):
            node = office_plan_data[row][0]
            device_code = config.command_code[node]
            office_direction_name = office_plan_data[row][1]
            tg_name = office_plan_data[row][2]
            opc = office_plan_data[row][3]
            dpc = office_plan_data[row][4]
            mgd = office_plan_data[row][8]

            # IPC1-IPC19
            stm_add_scripts.append(
                f"""ADD N7DSP:DPNM="{tg_name}",NI=NAT,DPC="{dpc}",OPC="{opc}",STPF=FALSE,ADJF=TRUE,SLSSM=B1111,PRT=ITU,EXNI=NAT,SICFG=SCCP-1&TUP-1&ISUP-1&SI06-0&SI07-0&SI08-0&SI09-0&SI0A-0&SI0B-0&SI0C-0&BICC-1&H248-0&SI0F-0,SCRMSG=NO,MOG="PUBLIC";{device_code}""")
            stm_add_scripts.append(
                f"""ADD N7LKS:LSNM="{tg_name}",ASPNM="{tg_name}",SLSM=B1111,MOG="PUBLIC",LKSDIR=NULL,EMGF=FALSE;{device_code}""")
            stm_add_scripts.append(
                f"""ADD N7RT:RTNM="{tg_name}",DPNM="{tg_name}",LSNM="{tg_name}",PRI=0,MOG="PUBLIC";{device_code}""")
            stm_add_scripts.append(
                f"""ADD N7DSP:DPNM="{tg_name}",NI=NAT,DPC="{dpc}",OPC="{opc}",STPF=FALSE,ADJF=TRUE,SLSSM=B1111,PRT=ITU,EXNI=NAT,SICFG=SCCP-1&TUP-1&ISUP-1&SI06-0&SI07-0&SI08-0&SI09-0&SI0A-0&SI0B-0&SI0C-0&BICC-1&H248-0&SI0F-0,SCRMSG=NO,MOG="PUBLIC";{device_code}""")
            stm_add_scripts.append(
                f"""ADD N7LKS:LSNM="{tg_name}",ASPNM="{tg_name}",SLSM=B1111,MOG="PUBLIC",LKSDIR=NULL,EMGF=FALSE;{device_code}""")
            stm_add_scripts.append(
                f"""ADD N7RT:RTNM="{tg_name}",DPNM="{tg_name}",LSNM="{tg_name}",PRI=0,MOG="PUBLIC";{device_code}""")
            stm_add_scripts.append(
                f"""MOD OFC:ON="{office_direction_name}",OFCTYPE=COM,SIG=NONBICC/NONSIP,MST=NO,LOCNAME="INVALID";{device_code}""")
            stm_add_scripts.append(
                f"""ADD BILLCTRL:OFFICENAME="{office_direction_name}",OOFFICT=OTHERNET,GWIGENERATE=YES,GWOGENERATE=YES,GWICLDFILL=INCOMINGIAMCLD,GWOCLDFILL=FILLASNORMAL,SN="{node}",TZDSTNAME="INVALID",OFFICEINDICATOR=UNKNOWN,BILLGENERATE=NO;{device_code}""")
            stm_add_scripts.append(
                f"""ADD SRT: SN="{node}", SRN="{tg_name}", ON="{office_direction_name}", SCMN=YES, TSM=CYC, MOG="PUBLIC";{device_code}""")
            stm_add_scripts.append(
                f"""ADD RT: RN="{tg_name}", SRSM=SEQ, SR1N="{tg_name}", CLDNCN="DEFAULT", SN="{node}";{device_code}""")
            stm_add_scripts.append(
                f"""ADD RTANA: RSN="{tg_name}", RSSN="ALL", CC=CAT254, ADI=ALL, TP=ALL, ORT=ALL, TSN="DEFAULT", RTSM=SEQ, RN="{tg_name}", ISUP=ISUP_F, MOG="PUBLIC";{device_code}""")
            stm_add_scripts.append(
                f"""ADD CLDPREANA:CSCNAME="{tg_name}",CS=ISUP,PFX=K'018,MINCLDLEN=11,CDADDR=ALL,CRP=ALL,CLDNCN="DEFAULT",NP=255,PT=DONTPROC,CLISRVCAT=HOT_BILL-0&IN-0&SMMO_FILTER1-0&SMMO_FILTER2-0&SMMO_BKLST1-0&SMMO_BKLST2-0&SMMT_BKLST1-0&SMMT_BKLST2-0&MO_BKLST-0&MT_BKLST-0&SMCS_ALLOW1-0&SMCS_ALLOW2-0&ODB1_ALLOW-0&SERVICE12-0&SERVICE13-0&SMMO_ODBBAOC_B_ALLOW_LIST-0&OSS1-0&OSS3-0&VIDEOPHONE-0&RESTR_CRBT-0&CFPHSERVICE-0&SERVICE20-0&COLLECTCALL-0&SERVICE22-0&OCSIPROTECT-0&TCSIPROTECT-0&SERVICE25-0&SMMO_SMC-0&OTHERPLMNSUB-0&UNLOCAL_USER-0&SERVICE29-0&SERVICE30-0&SUPPRESS_ANNOUNCEMENT-0&WPS-0&SERVICE33-0&SERVICE34-0&SRI_VER-0&RESTR_HOLD-0&RESTR_MPTY-0&RESTR_ECT-0&PFPHSERVICE-0&SERVICE40-0&CANCEL_CLDANA_TIMES-0&SERVICE42-0&SERVICE43-0&SERVICE44-0&SERVICE45-0&SERVICE46-0&SERVICE47-0&SERVICE48-0&SERVICE49-0&SERVICE50-0&SERVICE51-0&SERVICE52-0&SERVICE53-0&SERVICE54-0&SERVICE55-0&SERVICE56-0&SERVICE57-0&SERVICE58-0&SERVICE59-0&SERVICE60-0&SERVICE61-0&SERVICE62-0&SERVICE63-0&SERVICE64-0&SERVICE65-0&SERVICE66-0&SERVICE67-0&SERVICE68-0&SERVICE69-0&SERVICE70-0&SERVICE71-0&SERVICE72-0&SERVICE73-0&SERVICE74-0&SERVICE75-0&SERVICE76-0&SERVICE77-0&RCF-0&SUPPRESS_TCSI-0&SERVICE80-0&SERVICE81-0&SERVICE82-0&SERVICE83-0&SERVICE84-0&SERVICE85-0&SERVICE86-0&SERVICE87-0&SERVICE88-0&SERVICE89-0&SERVICE90-0&SERVICE91-0&SERVICE92-0&SERVICE93-0&SERVICE94-0&SERVICE95-0&SERVICE96-0&SERVICE97-0&SERVICE98-0&SERVICE99-0&SERVICE100-0&FOLLOW_ME-0&SERVICE102-0,OCSICV=NO,NOOCSICV=NO,MOG="PUBLIC";{device_code}""")
            stm_add_scripts.append(
                f"""ADD CLDPREANA:CSCNAME="{tg_name}",CS=ISUP,PFX=K'0180,MINCLDLEN=11,CDADDR=ALL,CRP=ALL,CLDNCN="DEFAULT",NP=255,PT=FAILPROC,FCC=CV45,CLISRVCAT=HOT_BILL-0&IN-0&SMMO_FILTER1-0&SMMO_FILTER2-0&SMMO_BKLST1-0&SMMO_BKLST2-0&SMMT_BKLST1-0&SMMT_BKLST2-0&MO_BKLST-0&MT_BKLST-0&SMCS_ALLOW1-0&SMCS_ALLOW2-0&ODB1_ALLOW-0&SERVICE12-0&SERVICE13-0&SMMO_ODBBAOC_B_ALLOW_LIST-0&OSS1-0&OSS3-0&VIDEOPHONE-0&RESTR_CRBT-0&CFPHSERVICE-0&SERVICE20-0&COLLECTCALL-0&SERVICE22-0&OCSIPROTECT-0&TCSIPROTECT-0&SERVICE25-0&SMMO_SMC-0&OTHERPLMNSUB-0&UNLOCAL_USER-0&SERVICE29-0&SERVICE30-0&SUPPRESS_ANNOUNCEMENT-0&WPS-0&SERVICE33-0&SERVICE34-0&SRI_VER-0&RESTR_HOLD-0&RESTR_MPTY-0&RESTR_ECT-0&PFPHSERVICE-0&SERVICE40-0&CANCEL_CLDANA_TIMES-0&SERVICE42-0&SERVICE43-0&SERVICE44-0&SERVICE45-0&SERVICE46-0&SERVICE47-0&SERVICE48-0&SERVICE49-0&SERVICE50-0&SERVICE51-0&SERVICE52-0&SERVICE53-0&SERVICE54-0&SERVICE55-0&SERVICE56-0&SERVICE57-0&SERVICE58-0&SERVICE59-0&SERVICE60-0&SERVICE61-0&SERVICE62-0&SERVICE63-0&SERVICE64-0&SERVICE65-0&SERVICE66-0&SERVICE67-0&SERVICE68-0&SERVICE69-0&SERVICE70-0&SERVICE71-0&SERVICE72-0&SERVICE73-0&SERVICE74-0&SERVICE75-0&SERVICE76-0&SERVICE77-0&RCF-0&SUPPRESS_TCSI-0&SERVICE80-0&SERVICE81-0&SERVICE82-0&SERVICE83-0&SERVICE84-0&SERVICE85-0&SERVICE86-0&SERVICE87-0&SERVICE88-0&SERVICE89-0&SERVICE90-0&SERVICE91-0&SERVICE92-0&SERVICE93-0&SERVICE94-0&SERVICE95-0&SERVICE96-0&SERVICE97-0&SERVICE98-0&SERVICE99-0&SERVICE100-0&FOLLOW_ME-0&SERVICE102-0,OCSICV=NO,NOOCSICV=NO,MOG="PUBLIC";{device_code}""")
            stm_add_scripts.append(
                f"""ADD CLDPREANA:CSCNAME="{tg_name}",CS=ISUP,PFX=K'016,MINCLDLEN=11,CDADDR=ALL,CRP=ALL,CLDNCN="DEFAULT",NP=255,PT=DONTPROC,CLISRVCAT=HOT_BILL-0&IN-0&SMMO_FILTER1-0&SMMO_FILTER2-0&SMMO_BKLST1-0&SMMO_BKLST2-0&SMMT_BKLST1-0&SMMT_BKLST2-0&MO_BKLST-0&MT_BKLST-0&SMCS_ALLOW1-0&SMCS_ALLOW2-0&ODB1_ALLOW-0&SERVICE12-0&SERVICE13-0&SMMO_ODBBAOC_B_ALLOW_LIST-0&OSS1-0&OSS3-0&VIDEOPHONE-0&RESTR_CRBT-0&CFPHSERVICE-0&SERVICE20-0&COLLECTCALL-0&SERVICE22-0&OCSIPROTECT-0&TCSIPROTECT-0&SERVICE25-0&SMMO_SMC-0&OTHERPLMNSUB-0&UNLOCAL_USER-0&SERVICE29-0&SERVICE30-0&SUPPRESS_ANNOUNCEMENT-0&WPS-0&SERVICE33-0&SERVICE34-0&SRI_VER-0&RESTR_HOLD-0&RESTR_MPTY-0&RESTR_ECT-0&PFPHSERVICE-0&SERVICE40-0&CANCEL_CLDANA_TIMES-0&SERVICE42-0&SERVICE43-0&SERVICE44-0&SERVICE45-0&SERVICE46-0&SERVICE47-0&SERVICE48-0&SERVICE49-0&SERVICE50-0&SERVICE51-0&SERVICE52-0&SERVICE53-0&SERVICE54-0&SERVICE55-0&SERVICE56-0&SERVICE57-0&SERVICE58-0&SERVICE59-0&SERVICE60-0&SERVICE61-0&SERVICE62-0&SERVICE63-0&SERVICE64-0&SERVICE65-0&SERVICE66-0&SERVICE67-0&SERVICE68-0&SERVICE69-0&SERVICE70-0&SERVICE71-0&SERVICE72-0&SERVICE73-0&SERVICE74-0&SERVICE75-0&SERVICE76-0&SERVICE77-0&RCF-0&SUPPRESS_TCSI-0&SERVICE80-0&SERVICE81-0&SERVICE82-0&SERVICE83-0&SERVICE84-0&SERVICE85-0&SERVICE86-0&SERVICE87-0&SERVICE88-0&SERVICE89-0&SERVICE90-0&SERVICE91-0&SERVICE92-0&SERVICE93-0&SERVICE94-0&SERVICE95-0&SERVICE96-0&SERVICE97-0&SERVICE98-0&SERVICE99-0&SERVICE100-0&FOLLOW_ME-0&SERVICE102-0,OCSICV=NO,NOOCSICV=NO,MOG="PUBLIC";{device_code}""")
            stm_add_scripts.append(
                f"""ADD CLDPREANA:CSCNAME="{tg_name}",CS=ISUP,PFX=K'0160,MINCLDLEN=11,CDADDR=ALL,CRP=ALL,CLDNCN="DEFAULT",NP=255,PT=FAILPROC,FCC=CV45,CLISRVCAT=HOT_BILL-0&IN-0&SMMO_FILTER1-0&SMMO_FILTER2-0&SMMO_BKLST1-0&SMMO_BKLST2-0&SMMT_BKLST1-0&SMMT_BKLST2-0&MO_BKLST-0&MT_BKLST-0&SMCS_ALLOW1-0&SMCS_ALLOW2-0&ODB1_ALLOW-0&SERVICE12-0&SERVICE13-0&SMMO_ODBBAOC_B_ALLOW_LIST-0&OSS1-0&OSS3-0&VIDEOPHONE-0&RESTR_CRBT-0&CFPHSERVICE-0&SERVICE20-0&COLLECTCALL-0&SERVICE22-0&OCSIPROTECT-0&TCSIPROTECT-0&SERVICE25-0&SMMO_SMC-0&OTHERPLMNSUB-0&UNLOCAL_USER-0&SERVICE29-0&SERVICE30-0&SUPPRESS_ANNOUNCEMENT-0&WPS-0&SERVICE33-0&SERVICE34-0&SRI_VER-0&RESTR_HOLD-0&RESTR_MPTY-0&RESTR_ECT-0&PFPHSERVICE-0&SERVICE40-0&CANCEL_CLDANA_TIMES-0&SERVICE42-0&SERVICE43-0&SERVICE44-0&SERVICE45-0&SERVICE46-0&SERVICE47-0&SERVICE48-0&SERVICE49-0&SERVICE50-0&SERVICE51-0&SERVICE52-0&SERVICE53-0&SERVICE54-0&SERVICE55-0&SERVICE56-0&SERVICE57-0&SERVICE58-0&SERVICE59-0&SERVICE60-0&SERVICE61-0&SERVICE62-0&SERVICE63-0&SERVICE64-0&SERVICE65-0&SERVICE66-0&SERVICE67-0&SERVICE68-0&SERVICE69-0&SERVICE70-0&SERVICE71-0&SERVICE72-0&SERVICE73-0&SERVICE74-0&SERVICE75-0&SERVICE76-0&SERVICE77-0&RCF-0&SUPPRESS_TCSI-0&SERVICE80-0&SERVICE81-0&SERVICE82-0&SERVICE83-0&SERVICE84-0&SERVICE85-0&SERVICE86-0&SERVICE87-0&SERVICE88-0&SERVICE89-0&SERVICE90-0&SERVICE91-0&SERVICE92-0&SERVICE93-0&SERVICE94-0&SERVICE95-0&SERVICE96-0&SERVICE97-0&SERVICE98-0&SERVICE99-0&SERVICE100-0&FOLLOW_ME-0&SERVICE102-0,OCSICV=NO,NOOCSICV=NO,MOG="PUBLIC";{device_code}""")
            stm_add_scripts.append(
                f"""ADD CLDPREANA:CSCNAME="{tg_name}",CS=ISUP,PFX=K'EEEEEEEE,MINCLDLEN=1, CDADDR=ALL,CRP=ALL,CLDNCN="DEFAULT",NP=255,PT=FAILPROC,FCC=CV45,CLISRVCAT=HOT_BILL-0&IN-0&SMMO_FILTER1-0&SMMO_FILTER2-0&SMMO_BKLST1-0&SMMO_BKLST2-0&SMMT_BKLST1-0&SMMT_BKLST2-0&MO_BKLST-0&MT_BKLST-0&SMCS_ALLOW1-0&SMCS_ALLOW2-0&ODB1_ALLOW-0&SERVICE12-0&SERVICE13-0&SMMO_ODBBAOC_B_ALLOW_LIST-0&OSS1-0&OSS3-0&VIDEOPHONE-0&RESTR_CRBT-0&CFPHSERVICE-0&SERVICE20-0&COLLECTCALL-0&SERVICE22-0&OCSIPROTECT-0&TCSIPROTECT-0&SERVICE25-0&SMMO_SMC-0&OTHERPLMNSUB-0&UNLOCAL_USER-0&SERVICE29-0&SERVICE30-0&SUPPRESS_ANNOUNCEMENT-0&WPS-0&SERVICE33-0&SERVICE34-0&SRI_VER-0&RESTR_HOLD-0&RESTR_MPTY-0&RESTR_ECT-0&PFPHSERVICE-0&SERVICE40-0&CANCEL_CLDANA_TIMES-0&SERVICE42-0&SERVICE43-0&SERVICE44-0&SERVICE45-0&SERVICE46-0&SERVICE47-0&SERVICE48-0&SERVICE49-0&SERVICE50-0&SERVICE51-0&SERVICE52-0&SERVICE53-0&SERVICE54-0&SERVICE55-0&SERVICE56-0&SERVICE57-0&SERVICE58-0&SERVICE59-0&SERVICE60-0&SERVICE61-0&SERVICE62-0&SERVICE63-0&SERVICE64-0&SERVICE65-0&SERVICE66-0&SERVICE67-0&SERVICE68-0&SERVICE69-0&SERVICE70-0&SERVICE71-0&SERVICE72-0&SERVICE73-0&SERVICE74-0&SERVICE75-0&SERVICE76-0&SERVICE77-0&RCF-0&SUPPRESS_TCSI-0&SERVICE80-0&SERVICE81-0&SERVICE82-0&SERVICE83-0&SERVICE84-0&SERVICE85-0&SERVICE86-0&SERVICE87-0&SERVICE88-0&SERVICE89-0&SERVICE90-0&SERVICE91-0&SERVICE92-0&SERVICE93-0&SERVICE94-0&SERVICE95-0&SERVICE96-0&SERVICE97-0&SERVICE98-0&SERVICE99-0&SERVICE100-0&FOLLOW_ME-0&SERVICE102-0,OCSICV=NO,NOOCSICV=NO,MOG="PUBLIC";{device_code}""")
            stm_add_scripts.append(
                f"""MOD TG:TGN="{tg_name}",TRSMODE=FIB-0&COAXCABL-0&SIMMWAVE-0&DIGWAVE-0&SITTRAS-0&COMTRAS-0&OTHERTRAS-0,OOFFICT=OTHERS,MOG="PUBLIC";{device_code}""")
            stm_add_scripts.append(f"""MOD N7TG: TGN="{tg_name}", NPCLR=NO;{device_code}""")
            stm_add_scripts.append(
                f"""ADD OUTNUMPREPRO:CSCNAME="ALL",TGN="{tg_name}",P=0,PFX=K'EEEEEEEE,CS=ALL,CLDADDR=ALL,MAXLEN=32,CIDN="MNP_ADD_RN",ODIDN="MNP_ORG_REDR_NUMBER",CLRFT=UNKNOW,CDN="DEFAULT",CLDFT=UNKNOW,DDN="NDN_FORMAT",ORICLDFT=UNKNOW,ODDN="DEFAULT",RDFT=UNKNOW,RDDN="DEFAULT",GENFT=UNKNOW,GENNCN="DEFAULT",DCF=NO,FCCLI=NO,MOG="PUBLIC";{device_code}""")
            # IPC17
            for cic_row in range(len(cic_plan_data)):
                cic_node = cic_plan_data[cic_row][0]
                if cic_node == node:
                    start_cic = cic_plan_data[cic_row][5]
                    end_cic = cic_plan_data[cic_row][6]
                    start_tid = cic_plan_data[cic_row][7]
                    while True:
                        if (start_cic + 31) >= end_cic:
                            length_start = len(str(start_cic))
                            start = (4 - length_start) * '0' + str(start_cic)
                            length_end = len(str(end_cic))
                            end = (4 - length_end) * '0' + str(end_cic)
                            stm_add_scripts.append(
                                f"""ADD N7TKC:TGN="{tg_name}", SCIC={start}, ECIC={end}, TID= {start_tid};{device_code}""")
                            break
                        elif (start_cic + 31) < end_cic:
                            length_start = len(str(start_cic))
                            start = (4 - length_start) * '0' + str(start_cic)
                            end = start_cic + 31
                            start_cic = end + 1
                            length_end = len(str(end))
                            end = (4 - length_end) * '0' + str(end)
                            stm_add_scripts.append(
                                f"""ADD N7TKC:TGN="{tg_name}", SCIC={start}, ECIC={end}, TID= {start_tid};{device_code}""")

            stm_add_scripts.append(f"""MOD N7TKC: TGN=" {tg_name}", SCIC=16, ECIC=16, CS=UNU;{device_code}""")
            stm_add_scripts.append(f"""MOD N7TKC: TGN=" {tg_name}", SCIC=48, ECIC=48, CS=UNU;{device_code}""")

        try:
            file_handle = open(f"{location}{file_name}", 'w')
            for value in stm_add_scripts:
                file_handle.write(value + '\n')
            file_handle.close()
        except Exception as e:
            print(f'{e}')

    def lst_script_generation_for_dpc(self, office_plan_data, signalling_plan_data, location, file_name):
        stm_lst_scripts = []
        for row in range(len(office_plan_data)):
            node = office_plan_data[row][0]
            device_code = config.command_code[node]
            mgd = office_plan_data[row][8]
            stm_lst_scripts.append(f"""LST M2LKS:SGNM="{mgd}",LTP=LOCAL;{device_code}""")

        node = office_plan_data[0][0]
        device_code = config.command_code[node]
        device_code_2 = config.command_code['DG08_MGW12']
        stm_lst_scripts.append(f"""LST N7LNK:LTP=LOCAL;{device_code}""")
        stm_lst_scripts.append(
            f"""LST OFC:OFCTYPE=ALL,SMD=NO,SSR=NO,SADPC=NO,CLRDSP=NO,BOFFICEPARADSP=NO,OFFICECODECDSP=NO;{device_code}""")
        stm_lst_scripts.append(
            f"""LST N7TG:QR=LOCAL,SSR=NO,SRT=NO,SOF=NO,SL=NO,SC=NO,SS=NO,SOT=NO,CLRDSP=NO;{device_code}""")
        stm_lst_scripts.append(f"""LST MTP2LNK:;{device_code_2}""")

        for row in range(len(signalling_plan_data)):
            fnsn = signalling_plan_data[row][3]
            if not fnsn or fnsn == '' or pd.isnull(fnsn):
                break
            else:
                fnsn = fnsn.split('-')
                fn = fnsn[0]
                sn = fnsn[1]
                stm_lst_scripts.append(f"""LST BRD:LM=FNSN,FN={fn},SN={sn},BP=BACK;{device_code_2}""")

        stm_lst_scripts.append(f"""DSP CPUR:QM=BTBN,BT=SPF;{device_code_2}""")

        dpc_parsing_obj = DPCParsing()
        bn_list = dpc_parsing_obj.get_bn_list()
        for bn in bn_list:
            stm_lst_scripts.append(f"""DSP SPFSUBRD:SPFBN={bn};{device_code_2}""")

        stm_lst_scripts.append(f"""LST L2UALKS:;{device_code_2}""")
        stm_lst_scripts.append(f"""LST OFCNAME:;{device_code_2}""")

        try:
            file_handle = open(f"{location}{file_name}", 'w')
            for value in stm_lst_scripts:
                file_handle.write(value + '\n')
            file_handle.close()
        except Exception as e:
            print(f'{e}')

    def dpc_add_script_generate(self, office_plan_data, signalling_plan_data, ckt_plan_data, location, file_name):

        dpc_script_generator_obj = DPCScriptGenerator()
        scripts = []
        scripts = dpc_script_generator_obj.add_script_dpc1(office_plan_data, signalling_plan_data, scripts)
        scripts = dpc_script_generator_obj.add_script_dpc2(office_plan_data, signalling_plan_data, scripts)
        scripts = dpc_script_generator_obj.add_script_dpc3(office_plan_data, signalling_plan_data, scripts)
        scripts = dpc_script_generator_obj.add_script_dpc4(office_plan_data, signalling_plan_data, scripts)
        scripts = dpc_script_generator_obj.add_script_dpc5(office_plan_data, signalling_plan_data, ckt_plan_data,
                                                           scripts)
        scripts = dpc_script_generator_obj.add_script_dpc6_7(office_plan_data, signalling_plan_data, scripts)
        scripts = dpc_script_generator_obj.add_script_dpc8(office_plan_data, signalling_plan_data, scripts)
        scripts = dpc_script_generator_obj.add_script_dpc9(office_plan_data, signalling_plan_data, scripts)
        scripts = dpc_script_generator_obj.set_script_dpc10_to_dpc14(office_plan_data, signalling_plan_data, scripts)

        try:
            file_handle = open(f"{location}{file_name}", 'w')
            for value in scripts:
                file_handle.write(value + '\n')
            file_handle.close()
        except Exception as e:
            print(f'{e}')

    def consistency_list_script_generate(self, office_plan_data, signalling_plan_data, location, file_name):
        scripts = []
        for row in range(len(office_plan_data)):
            node = office_plan_data[row][0]
            device_code = config.command_code[node]
            office_direction_name = office_plan_data[row][1]
            tg_name = office_plan_data[row][2]
            opc = office_plan_data[row][3]
            dpc = office_plan_data[row][4]
            dpc1 = ''.join(filter(lambda i: i.isdigit(), dpc))

            scripts.append(
                f"""LST N7DSP:DPNM="{tg_name}",SHLINK=FALSE,SHOFC=FALSE,LTP=LOCAL,SICFGDSP=NO;{device_code}""")
            scripts.append(f"""LST N7LKS:LSNM="{tg_name}",LTP=LOCAL;{device_code}""")
            scripts.append(f"""LST N7RT:RTNM="{tg_name}",LTP=LOCAL;{device_code}""")
            scripts.append(f"""LST CALLSRC:CSCNAME="{tg_name}",QR=LOCAL;{device_code}""")
            scripts.append(f"""LST CLDPREANA:CSCNAME="{tg_name}",PFX=K'018,MINCLDLEN=11,QR=LOCAL;{device_code}""")
            scripts.append(f"""CLDPREANA:CSCNAME="{tg_name}",PFX=K'0180,MINCLDLEN=11,QR=LOCAL;{device_code}""")
            scripts.append(f"""LST CLDPREANA:CSCNAME="{tg_name}",PFX=K'016,MINCLDLEN=11,QR=LOCAL;{device_code}""")
            scripts.append(f"""LST CLDPREANA:CSCNAME="{tg_name}",PFX=K'0160,MINCLDLEN=11,QR=LOCAL;{device_code}""")
            scripts.append(
                f"""LST CLDPREANA:CSCNAME="{tg_name}",PFX=K'EEEEEEEE,MINCLDLEN=1,QR=LOCAL;{device_code}""")
            scripts.append(
                f"""LST OFC:ON="{office_direction_name}",OFCTYPE=ALL,SMD=NO,SSR=NO,SADPC=NO,CLRDSP=NO,DPC="{dpc1}",BOFFICEPARADSP=NO,OFFICECODECDSP=NO;{device_code}""")
            scripts.append(f"""LST BILLCTRL:OFFICENAME="{office_direction_name}";{device_code}""")
            scripts.append(f"""LST SRT:SRN="{office_direction_name}",QR=LOCAL,SRT=NO,ST=NO;{device_code}""")
            scripts.append(
                f"""LST RT:RN="{tg_name}",SSR=NO,SRA=NO,SOFC=NO,SPFX=NO,SDSRT=NO,QR=LOCAL;{device_code}""")
            scripts.append(f"""LST RTANA:RSN="{tg_name}",SRT=NO,SPFX=NO,QR=LOCAL;{device_code}""")
            scripts.append(
                f"""LST N7TG:TGN="{tg_name}",QR=LOCAL,MGWNAME="DG05_MGW12_KHL",SRN="G512NXCWT01",CSCNAME="G512NXCWT01",SOPC="H’002157",SDPC="H’002172",SSR=NO,SRT=NO,SOF=NO,SL=NO,SC=NO,SS=NO,SOT=NO,CLRDSP=NO;{device_code}""")
            scripts.append(f"""LST OUTNUMPREPRO:TGN="{tg_name}",QR=LOCAL;{device_code}""")
            scripts.append(f"""DSP TGTK:TGN="{tg_name}";{device_code}""")

        for row in range(len(signalling_plan_data)):
            device_code = config.command_code['DG05']
            link_name = signalling_plan_data[row][2]
            scripts.append(f"""LST N7LNK:LNKNM="{link_name}",LTP=LOCAL;{device_code}""")

        try:
            file_handle = open(f"{location}{file_name}", 'w')
            for value in scripts:
                file_handle.write(value + '\n')
            file_handle.close()
        except Exception as e:
            print(f'{e}')
