import pandas as pd
class Log:
    
    def get_arp_table(self, arp_log):
        structure = {"IP Address":[],"MAC":[], "VLAN":[]}
        with open(arp_log, 'r') as reader:
            lines = reader.readlines()
            for line in lines[2:]:
                data = line.split()
                try:
                    if(data[0] == "Internet"):
                        structure["IP Address"].append(data[1])
                        structure["MAC"].append(data[3])
                        structure["VLAN"].append(data[5])
                except:
                    pass
        return pd.DataFrame(data=structure)       
    