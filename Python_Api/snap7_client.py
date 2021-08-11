import snap7

IP = '192.168.0.1'
RACK = 0
SLOT = 1

DB_NUMBER = 1
START_ADDRESS = 1
SIZE = 260


plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)

#plc_info = plc.get_cpu_info()
#print(f'Module Type: {plc_info.ModuleTypeName}')

state = plc.get_cpu_state()
print(f'Sate:  {state}')

#db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)

#product_name = db[1:256].decode('UTF-8').strip('\x00')
#print(f'Product Name: {product_name}')

#product_value = int.from_bytes(db[256:258], byteorder='big')
#print(f'Product Value: {product_value}')

#product_status = bool(db[258])
#print(f'Product Status: {product_status}')

plc.db_write(DB_NUMBER ,START_ADDRESS, b'xSnap7 App to PLC')
