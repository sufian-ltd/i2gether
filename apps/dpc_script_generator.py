import pandas as pd
from apps.dpc_parsing import DPCParsing
from workflow import config


class DPCScriptGenerator:

    def __init__(self):
        self.dpc_parsing_obj = DPCParsing()

    def add_script_dpc1(self, office_plan_data, signalling_plan_data, scripts):

        for signaling_row in range(len(signalling_plan_data)):
            link_name = signalling_plan_data[signaling_row][2]
            for office_row in range(len(office_plan_data)):
                node = office_plan_data[office_row][0]
                device_code = config.command_code[node]
                tg_name = office_plan_data[office_row][2]
                mgd = office_plan_data[office_row][8]
                slc_col = str(office_plan_data[office_row][7]).split(':')
                slc = slc_col[0]
                slc = slc[len(slc) - 1:]
                linkset_name_list = self.dpc_parsing_obj.get_linkset_name_for_dpc1(mgd)
                for linkset_name in linkset_name_list:
                    binifid = self.dpc_parsing_obj.get_interface_id_dpc1()
                    scripts.append(
                        f"""ADD N7LNK:LNKNM="{link_name}",LSNM="{tg_name}",LNKTYPE=M2UA0,M2LSNM="{linkset_name}",BINIFID={binifid},SLC={slc},SLCS={slc},PRI=0,LCT=70,MCT=80,HCT=90,CET=60,TC="AA",TCLEN=10,PSLTM=YES,HLTHD=40,LLTHD=20,MOG="PUBLIC";{device_code}""")

        return scripts

    def add_script_dpc2(self, office_plan_data, signalling_plan_data, scripts):
        for signaling_row in range(len(signalling_plan_data)):
            link_name = signalling_plan_data[signaling_row][2]
            for office_row in range(len(office_plan_data)):
                node = office_plan_data[office_row][0]
                device_code = config.command_code[node]
                tg_name = office_plan_data[office_row][2]
                mgd = office_plan_data[office_row][8]
                slc_col = str(office_plan_data[office_row][7]).split('\n')
                slc_col = slc_col[1]
                slc_col = str(slc_col).split(':')
                slc_col = slc_col[0]
                slc = slc_col[len(slc_col) - 1:]
                slc = slc[len(slc) - 1:]
                linkset_name_list = self.dpc_parsing_obj.get_linkset_name_for_dpc1(mgd)
                for linkset_name in linkset_name_list:
                    binifid = self.dpc_parsing_obj.get_interface_id_dpc1()
                    scripts.append(
                        f"""ADD N7LNK:LNKNM="{link_name}",LSNM="{tg_name}",LNKTYPE=M2UA0,M2LSNM="{linkset_name}",BINIFID={binifid},SLC={slc},SLCS={slc},PRI=0,LCT=70,MCT=80,HCT=90,CET=60,TC="AA",TCLEN=10,PSLTM=YES,HLTHD=40,LLTHD=20,MOG="PUBLIC";{device_code}""")

        return scripts

    def add_script_dpc3(self, office_plan_data,signalling_plan_data, scripts):
        for office_row in range(len(office_plan_data)):
            node = office_plan_data[office_row][0]
            device_code = config.command_code[node]
            tg_name = office_plan_data[office_row][2]
            mscn = config.mscn_values[node]
            scripts.append(
                f"""ADD CALLSRC:CSCNAME="{tg_name}",RSSN="0",FSN="0",PRDN=1,P=0,ISADRDSG=NON,INNAME="INVALID",DRNT=0,MSCN={mscn},NPANXX="FFFFFF",EAFLAG=NO,MOG="PUBLIC",RSVLANG=YES,LANGKIND=255,CSCG="INVALID";{device_code}""")

        return scripts

    def add_script_dpc4(self, office_plan_data,signalling_plan_data, scripts):
        for office_row in range(len(office_plan_data)):
            node = office_plan_data[office_row][0]
            device_code = config.command_code[node]
            office_direction_name = office_plan_data[office_row][1]
            dpc = office_plan_data[office_row][4]
            bofcno = self.dpc_parsing_obj.get_bill_office_num_dpc4()
            scripts.append(
                f"""ADD OFC: ON="{office_direction_name}", OOFFICT=GMSC, DOL=HIGH, DOA=MSC, BOFCNO={bofcno}, OFCTYPE=COM, SIG=NONBICC/NONSIP, NI=NAT, DPC1="{dpc}", ASET=0, CLDST=YES, CLRST=NO, OCLDST=NO, FWNST=NO, OFWNST=NO, RELST=NO, ADJUSTPO=NO, FSET=NO, RM=SUS, FALLBACK=YES, IPD=0, ISUPSENDMSK=64, ISUPRECEIVMSK=64, MAXLEN=255, SVP=YES, SUPPORTACC=NO, ACC2THRESHOLD=80, BOFFICEPARA=TFO-0&G711-0&APM2-0&SETOMZERO-0&MSGLEN4096-0&DELUSI5-0&CODECMODRENEGO-0&COCK-0&BICCFORBIDTONE-0&PLAYTONEACMWITHCAUSE-0&DELBCUID-0&NOTSUPPORTCUGPARA-0&TRANSFERITC-0&CPGEVENTIND-0&OFCCODECINT-0&TRANSPROGIND-0&CAPABILITYIND-0&PRACONV32ISDNBC-0&SETG.711A-0&SUPPORTTTY-0&SUPPORTTRACE-0&POFCSUPIPRET-0&CTL1907ALM-0&OFP8-0&POI-0&PRIBCUIDFMT-0&OFP4-0&OFP3-0&TS61-0&OFP1-0&OFP0-0, BOFFICEEXTRAPARA=SUPPORTGCR-0&OVERRIDDENGCR-0&NUMRSTRTSND-0&OMCONTROLFLAG-0&SIP183RING-0&ARI-0&CPG2CONNECT-0&VIG-0&SVR8-0&SVR9-0&OOBTCNOTSENDRENEG-0&SVR11-0&SVR12-0&SIP200CARRIESMGWCODEC-0&SVR14-0&SPTMRBT-0&PREFIX2PLUS-0&SVR17-0&PRAPARA1-0&HOCHR-0&GTS-0&AMROCTETALIGN-0&SVR22-0&SVR23-0&SVR24-0&SVR25-0&SVR26-0&SVR27-0&RETDEAVIDEOSTREAM-0&SVR29-0&FAXUSET38-0&SVR31-0, BOFFICEEXTRAPARA2=FORCESETINOFFCODEC-0&SVR6-0&SVR7-0&SVR8-0&SVR9-0&SVR10-0&SVR11-0&SVR12-0&SVR13-0&SVR14-0&SVR15-0&SVR16-0&SVR17-0&SVR18-0&SVR19-0&SVR20-0&SVR21-0&SVR22-0&SVR23-0&SVR24-0&SVR25-0&SVR26-0&SVR27-0&SVR28-0&SVR29-0&SVR30-0&SVR31-0, CONRATE=100, ISEACM=FALSE, EACM=0, SVQE=NO, RESTRICTFORWARD=YES, ARRCFGNAME="INVALID", ISDP=YES, DISGRP=65535, IMTGRP=65535, SUPPORTWPS=NO, CLLI="INVALID", CICL=BIT12, ACTIVATEPSS=NO, EMLPP=NO, ANSINP=NO, MOG="PUBLIC", QENUM=NO;{device_code}""")

        return scripts

    def add_script_dpc5(self, office_plan_data, signalling_plan_data,ckt_plan_data, scripts):
        for office_row in range(len(office_plan_data)):
            node = office_plan_data[office_row][0]
            device_code = config.command_code[node]
            tg_name = office_plan_data[office_row][2]
            opc = office_plan_data[office_row][3]
            dpc = office_plan_data[office_row][4]
            mgd = office_plan_data[office_row][8]
            btg = self.dpc_parsing_obj.get_trunk_group_num_dpc5()
            for ckt_row in range(len(ckt_plan_data)):
                circuit_selection_mode = str(ckt_plan_data[ckt_row][2]).lower()
                csm = 'MIN' if circuit_selection_mode == 'minimum' else 'MAX'
                scripts.append(
                    f"""ADD N7TG:TGN="{tg_name}",MGWNAME="{mgd}",CT=ISUP,SRN="{tg_name}",G=INOUT,BTG={btg},BTGN="INVALID",SOPC="{opc}",SDPC="{dpc}",PCM=E1,CSCNAME="{tg_name}",CSM={csm},RCN=0,CNSF=NO,ICR=LCO-1&LC-1&LCT-1&NTT-1&ITT-1,OCR=LCO-1&LC-1&LCT-1&NTT-1&ITT-1,DOD2=NO,CRF=B0-0&B1-0,IT=NO,ABT=YES,RCHS=255,OTCS=255,UPF=NO,CD=NO,CAMA=NO,NIF=YES,IPM=NPR,DI=K'88888888,DINAI=NOIND,DINPI=NOIND,CBGRP=65535,HT=0,LT=0,CC=NO,DV=0,GTS=YES,TC=AUDIO-1&NLDIG-1&LDIG-1&AUD31-1&SNLD-1&VIDEO-1&FAX3-1,TM=PACK-1&S64K-1&S128K-1&S384K-1&S1530K-1&S1920K-1&MULTI-1,CCT=NOC,CCV=0,UL=255,SVRCTRL=WAC-0&NRR-0&CTL1907ALM-0&SSSB-0&TFCI-0&CLDPLANIND-0&BCPRIORITYCPC-0&SVR7-0&SVR8-0&SVR9-0&SV10R-0&DELCPNIFNIINC-0&TRANNIIFNIINC-0&SETNITOINC-0&DELCPNIFPIANV-0&MODSIIFPIANV-0,EXSVRCTRL=SVR0-0&ISUPPREIND-0&SETBCIBYFCI-0&SETECDI-0&SVR4-0&SVR5-0&SVR6-0&SVR7-0&SVR8-0&SVR9-0&SVR10-0&SVR11-0&SVR12-0&SVR13-0&SVR14-0&SVR15-0&SVR16-0&SVR17-0&SVR18-0&SVR19-0&SVR20-0&SVR21-0&SVR22-0&SVR23-0&SVR24-0&SVR25-0&SVR26-0&SVR27-0&SVR28-0&SVR29-0&SVR30-0&SVR31-0,EXSVRCTRL2=FUNC0-0&FUNC1-0&FUNC2-0&FUNC3-0&FUNC4-0&FUNC5-0&FUNC6-0&FUNC7-0&FUNC8-0&FUNC9-0&FUNC10-0&FUNC11-0&FUNC12-0&FUNC13-0&FUNC14-0&FUNC15-0,EXSVRCTRL3=FUNC0-0&FUNC1-0&FUNC2-0&FUNC3-0&FUNC4-0&FUNC5-0&FUNC6-0&FUNC7-0&FUNC8-0&FUNC9-0&FUNC10-0&FUNC11-0&FUNC12-0&FUNC13-0&FUNC14-0&FUNC15-0&FUNC16-0&FUNC17-0&FUNC18-0&FUNC19-0&FUNC20-0&FUNC21-0&FUNC22-0&FUNC23-0&FUNC24-0&FUNC25-0&FUNC26-0&FUNC27-0&FUNC28-0&FUNC29-0&FUNC30-0&FUNC31-0,NMSRC=65535,LCIC=0,HCIC=0,ISBF=NO,ISDP=YES,ISCLR=NO,ISPCLD=NO,NPCLR=YES,NPCLD=YES,DISGRP=0,OLPCLD=YES,CPN=255,ECMD=EC_OFF,BO=NO,ISVIRTG=NO,LOCNAME="INVALID",TRSMODE=FIB-0&COAXCABL-0&SIMMWAVE-0&DIGWAVE-0&SITTRAS-0&COMTRAS-0&OTHERTRAS-0,AN="DG05",RELRED=NO,NCBF=NO_BLOCK,INCALLDTMF=YES,OUTCALLDTMF=YES,HCF=FALSE,HCV=31,PEERNETTYPE=UNKNOWN,SIGTP=ITUS,PVSOISRI=NP,NIR="FFF",SUPTRICK=NO,SEGMODE=NOSEG,AOC99=NO,RESTONE=NO,SUPGISUP=NO,SIISUP=NO,TRN="INVALID",TRCIC=0,SWTGID="FFFFFF",PBXID="INVALID",MOG="PUBLIC";{device_code}""")

        return scripts

    def add_script_dpc6_7(self, office_plan_data, signalling_plan_data, scripts):
        device_code = config.command_code['DG08_MGW12']
        link_no_list = self.dpc_parsing_obj.get_lks_for_dpc6()
        for signaling_row in range(len(signalling_plan_data)):
            link_name = signalling_plan_data[signaling_row][2]
            frame_slot_port = signalling_plan_data[signaling_row][3]
            if not frame_slot_port or frame_slot_port == '' or pd.isnull(frame_slot_port):
                frame_slot_port = signalling_plan_data[signaling_row - 1][3]
            frame_slot_port = str(frame_slot_port).split('-')
            fn = frame_slot_port[0]
            sn = frame_slot_port[1]
            opn = frame_slot_port[2]
            link_no = self.dpc_parsing_obj.get_link_no_dpc6()
            ifbt = self.dpc_parsing_obj.get_ifbt_for_dpc6(fn, sn)
            ifbn = self.dpc_parsing_obj.get_ifbn_for_dpc6(fn, sn)
            spfbn, sbbn = self.dpc_parsing_obj.get_spfbn_sbbn_for_dpc()
            lks = link_no_list[signaling_row]
            binifid = self.dpc_parsing_obj.get_interface_id_dpc1()
            scripts.append(
                f"""ADD MTP2LNK: LNKNO={link_no}, LNKNAME="{link_name}", IFBT={ifbt}, IFBN={ifbn}, OPN={opn}, E1T1N=0, STRTTS=16, ENDTS=16, SPFBN={spfbn}, SUBBN={sbbn}, LNKTYPE=M2UA64K, LKS={lks}, BINIFID={binifid};{device_code}""")

        return scripts

    def add_script_dpc8(self, office_plan_data,signalling_plan_data, scripts):
        for office_row in range(len(office_plan_data)):
            node = office_plan_data[office_row][0]
            device_code = config.command_code['DG08_MGW12']
            tg_name = office_plan_data[office_row][2]
            ofcinfo = self.dpc_parsing_obj.get_ofc_no_dcp8(tg_name)
            scripts.append(f"""ADD OFCNAME: OFCNO={ofcinfo}, OFCINFO="{tg_name}";{device_code}""")

        return scripts

    def add_script_dpc9(self, office_plan_data, signalling_plan_data, scripts):
        for office_row in range(len(office_plan_data)):
            tg_name = office_plan_data[office_row][2]
            ofc = self.dpc_parsing_obj.get_ofc_no_dcp8(tg_name)
            device_code = config.command_code['DG08_MGW12']
            for signaling_row in range(len(signalling_plan_data)):
                frame_slot_port = signalling_plan_data[signaling_row][3]
                if not frame_slot_port or frame_slot_port == '' or pd.isnull(frame_slot_port):
                    break
                else:
                    frame_slot_port = str(signalling_plan_data[signaling_row][3]).split('-')
                    frame_slot_port = str(signalling_plan_data[0][3]).split('-')
                    fn = frame_slot_port[0]
                    sn = frame_slot_port[1]
                    pn = frame_slot_port[2]
                    bt = self.dpc_parsing_obj.get_ifbt_for_dpc6(fn, sn)
                    bn = self.dpc_parsing_obj.get_ifbn_for_dpc6(fn, sn)
                    scripts.append(f"""ADD OFCTKC: OFC={ofc}, BT={bt}, BN={bn}, PN={pn};{device_code}""")

        return scripts

    def set_script_dpc10_to_dpc14(self, office_plan_data, signalling_plan_data, scripts):
        device_code = config.command_code['DG08_MGW12']
        frame_slot_port = str(signalling_plan_data[0][3]).split('-')
        fn = frame_slot_port[0]
        sn = frame_slot_port[1]
        pn = frame_slot_port[2]
        bt = self.dpc_parsing_obj.get_ifbt_for_dpc6(fn, sn)
        bn = self.dpc_parsing_obj.get_ifbn_for_dpc6(fn, sn)

        scripts.append(f"""SET OPTALM: BT={bt},BN={bn}, PN={pn}, SW= ENABLE;{device_code}""")
        scripts.append(f"""SET OPTALM: BT={bt},BN={bn}, PN={pn},ALM=RSTIM, SW=DISABLE;{device_code}""")
        scripts.append(f"""SET OPTALM: BT={bt},BN={bn}, PN={pn},ALM=HPTIM, SW=DISABLE;{device_code}""")
        scripts.append(f"""SET OPTALM: BT={bt},BN={bn}, PN={pn},ALM=LPTIM, SW=DISABLE;{device_code} """)
        scripts.append(f"""SET OPTALM: BT={bt},BN={bn}, PN={pn},ALM=HPSD,  SW=DISABLE;{device_code}""")

        return scripts