from app.logs import *
import pandas as pd
from xlsxwriter import *

class Excel:

    def __init__(self, place_name, ip_address):
        self.place_name = place_name
        self.ip_address = ip_address
        self.log = Log()
        self.writer = pd.ExcelWriter("output/"+place_name+"_Assesment.xlsx", engine='xlsxwriter')
    def create_excel(self):
        arp_filename = "data/"+self.place_name+"/show-arp-"+self.ip_address+".log"
        arp_df = self.log.get_arp_table(arp_filename)
        arp_df.to_excel(self.writer, sheet_name="ARP_Table", index=False)
        self.writer.save()
        
