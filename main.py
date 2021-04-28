from app.excel import *

if __name__ == "__main__":
    place = input("Place: ")
    ip_address = input("Ip_address: ") 
    excel = Excel(place, ip_address)
    excel.create_excel()