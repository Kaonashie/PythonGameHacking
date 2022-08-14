from pymem import Pymem
from ctypes import *
from PointerChain_Resolver import pointer_chain
pm = Pymem('ac_client.exe')

player_ptr = pm.read_int(pm.base_address + 0x000DDE48)
ammo_offsets = [0x274, 0x2C, 0x90, 0x50, 0x78, 0x58, 0x140]

if __name__ == "__main__":
    count = 0
    ammoAddr = pointer_chain(player_ptr, ammo_offsets)
    while count < 5:
        ammoCurrValue = pm.read_int(ammoAddr)
        pm.write_int(ammoAddr, ammoCurrValue + 10)
        print("You just gave yourself + 10 ammo!")
        input("Press any key to continue...")
        count += 1




