import snap7
import time
from remote_control_src import remote_DB_control_int, remote_DB_control_bool, display_state_of_programm, display_outputs_state
from net_address import IP, RACK, SLOT
from db_details import DB_NUMBER, R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R20, R21, R22, R23

from remote_control_src import remote_DB_control_int
response = ""
time_I_pole = 0
time_II_pole = 0
time_III_pole = 0

falownik_delay = 1*1000     #s -> ms
pompa_delay = 1*1000
wylewanie_delay = 1*1000
obnizenie_cisnienia = 1*1000

response = input("Zaprogramuj podlewanie(y/n): ")
if response == "y":
    time_I_pole =  input("Ustaw czas podelwania I pola [min]: ")
    time_II_pole =  input("Ustaw czas podelwania II pola [min]: ")
    time_III_pole =  input("Ustaw czas podelwania III pola [min]: ")

    response = input("Czy chcesz uruchomić ten program? (y/n): ")
    if response == "y":
        try:
            plc = snap7.client.Client()
            plc.connect(IP, RACK, SLOT)
            
            remote_DB_control_int(plc, DB_NUMBER, int(time_I_pole)*1000, R1)
            remote_DB_control_int(plc, DB_NUMBER, int(time_II_pole)*1000, R2)
            remote_DB_control_int(plc, DB_NUMBER, int(time_III_pole)*1000, R3)
            remote_DB_control_int(plc, DB_NUMBER, int(falownik_delay), R20)
            remote_DB_control_int(plc, DB_NUMBER, int(pompa_delay), R21)
            remote_DB_control_int(plc, DB_NUMBER, int(wylewanie_delay), R22)
            remote_DB_control_int(plc, DB_NUMBER, int(obnizenie_cisnienia), R23)
            remote_DB_control_bool(plc, DB_NUMBER, True, R0)
            
            print("Właśnie trwa podlewanie...")
            progres = 0
            progres_1 = 0
            t_end = 0
            while(progres < 9):
                if (t_end < time.time()):
                    progres = display_state_of_programm(DB_NUMBER)
                    if progres > progres_1:
                        print("-------------------------------")
                        print(f'Procent wyknania programu: {int(progres/9*100)} %')
                        progres_1 = progres
                        display_outputs_state(DB_NUMBER, R5)

                    t_end = time.time() + 1
            print("-------------------------------")
            print("Wszystko poszło pomyślnie")
            print("Do zobaczenia wkrótce :)")
            print("-------------------------------")
        except:
            print("Coś poszło nie tak :(")
exit()
