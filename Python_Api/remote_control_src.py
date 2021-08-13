import snap7
from net_address import IP, RACK, SLOT
from db_details import DB_NUMBER, R0, R1, R2, R3

def bitlist2int(bit_list):
    r_bit_list = []
    while len(bit_list)<7:
        bit_list.append(0)
    
    r_bit_list.append(1)
    
    l = len(bit_list)
    for i in range(l):
        r_bit_list.append(bit_list[l-1-i])
    
    w = 0
    l = len(r_bit_list)
    for bit in r_bit_list:
        
        w = w+bit* 2**(l-1)
        l = l-1
    

    return w


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

def display_outputs_state(DB_NUMBER, bit_of_start):
    db = plc.db_read(DB_NUMBER, 10, 1)
    print([int(x) for x in list('{0:0b}'.format(db[0]))])

def display_state_of_programm(DB_NUMBER):
    db = plc.db_read(DB_NUMBER, 8, 2)

    R4 = int.from_bytes(db[0:2], byteorder='big')
    
    return R4
    
def remote_DB_control_bool(plc, DB_NUMBER, Value, start_byte):
    plc.db_write(DB_NUMBER, start_byte, bool.to_bytes(Value,1,byteorder='big'))

def remote_control_outputs(plc, DB_NUMBER, start_byte, bits_list):
    value = bitlist2int(bits_list)
    remote_DB_control_bool(plc, DB_NUMBER, value, start_byte)

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






