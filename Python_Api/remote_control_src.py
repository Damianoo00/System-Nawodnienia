import snap7
from net_address import IP, RACK, SLOT
from db_details import DB_NUMBER, R0, R1, R2, R3

def display_interface_db(DB_NUMBER):
    db = plc.db_read(DB_NUMBER, 0, 9)

    R0 = bool(db[0])
    print(f'Remote Start [bool]: {R0}')

    R1 = int.from_bytes(db[2:4], byteorder='big')
    print(f'(I) Time of watering [s]: {R1}')

    R2 = int.from_bytes(db[4:6], byteorder='big')
    print(f'(II) Time of watering [s]: {R2}')

    R3 = int.from_bytes(db[6:8], byteorder='big')
    print(f'(III) Time of watering [s]: {R3}')

def display_state_of_programm(DB_NUMBER):
    db = plc.db_read(DB_NUMBER, 8, 2)

    R4 = int.from_bytes(db[0:2], byteorder='big')
    
    return R4
    
def remote_DB_control_bool(plc, DB_NUMBER, Value, start_byte):
    plc.db_write(DB_NUMBER, start_byte, bool.to_bytes(Value,1,byteorder='big'))

def remote_DB_control_int(plc, DB_NUMBER, Value, start_byte):
    plc.db_write(DB_NUMBER, start_byte, int.to_bytes(Value, 2, byteorder='big'))

plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)

#plc.db_write(DB_NUMBER, 6, int.to_bytes(96, 2, byteorder='big'))

#plc.db_write(DB_NUMBER, 0, bool.to_bytes(True,1,byteorder='big'))
#plc.db_write(DB_NUMBER, 2, int.to_bytes(10, 2, byteorder='big'))
#plc.db_write(DB_NUMBER, 4, int.to_bytes(2, 2, byteorder='big'))
#plc.db_write(DB_NUMBER, 6, int.to_bytes(10, 2, byteorder='big'))

#remote_DB_control_bool(plc, DB_NUMBER, True, R0)
#remote_DB_control_int(plc, DB_NUMBER, 3, R1)
#remote_DB_control_int(plc, DB_NUMBER, 4, R2)
#remote_DB_control_int(plc, DB_NUMBER, 5, R3)
#display_interface_db(DB_NUMBER)






