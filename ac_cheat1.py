from pymem import Pymem

pm = Pymem('ac_client.exe')
baseAddr = pm.base_address
offsets = [0x17E0A8, 0x140]

def pointer_chain(baseAddr, listOffset) :
    pointer = pm.read_int(baseAddr + listOffset[0])
    pointer2 = pointer + listOffset[1]
    return pointer2                


c = pointer_chain(baseAddr, offsets)

b = pm.read_int(c)
pm.write_int(c, b + 100)


