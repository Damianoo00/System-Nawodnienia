from db_details import R5
import snap7
from remote_control_src import remote_DB_control_bool, bitlist2int

IP = '192.168.0.99'
RACK = 0
SLOT = 1

DB_NUMBER = 1
START_ADDRESS = 0
SIZE = 21


plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)

#plc_info = plc.get_cpu_info()
#print(f'Module Type: {plc_info.ModuleTypeName}')

#state = plc.get_cpu_state()
#print(f'Sate:  {state}')

#db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)


#print([int(x) for x in list('{0:0b}'.format(db[10]))])

#bit_list = [1,1,1,0,1,1,0]
#bit_list_2 = [0,0,0,0,0,0,0,1]



#remote_DB_control_bool(plc, DB_NUMBER, bitlist2int(bit_list), 11)
#remote_DB_control_bool(plc, DB_NUMBER, bitlist2int(bit_list), 10)


#product_name = db[1:256].decode('UTF-8').strip('\x00')
#print(f'Product Name: {product_name}')

#product_value = int.from_bytes(db[256:258], byteorder='big')
#print(f'Product Value: {product_value}')

#product_status = bool(db[258])
#print(f'Product Status: {product_status}')

#plc.db_write(DB_NUMBER ,START_ADDRESS, b'xSnap7 App to PLC')
