#from pymeow import * | Not used yet. Want to make an overlay in the future
from pymem import *
#from PointerChain_Resolver import pointer_chain | Not used here

pm = Pymem('ac_client.exe')
# Getting handle of the process
baseAddr = pm.base_address
# Get base address of the process

class Pointers: 
    player_pointer = 0x17E0A8

class Offsets: 
    ammo_offset = 0x140
    name_offset = 0x205
    
player_addr = pm.read_int(baseAddr + Pointers.player_pointer)
# Getting local player address using the offsets

if __name__ == "__main__":
    print("Current Stats: ")
    print("Name : %s" % pm.read_string(player_addr + Offsets.name_offset))
    print("Ammo in clip : %s" % pm.read_int(player_addr + Offsets.ammo_offset))
    answer = input("Do you want to change the value?(Yes/No)")
    if "Yes" in answer:
        name = input("Change your name to : ")
        pm.write_string(player_addr + Offsets.name_offset, name)

        ammo = input("Change your ammo value to : ") 
        ammo = int(ammo)
        pm.write_int(player_addr + Offsets.ammo_offset, ammo)
    else: 
        print("GoodBye!")
 
    

    