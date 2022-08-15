from pymem import Pymem
pm = Pymem('ac_client.exe')
def pointer_chain(basePtr, listOffsets):
    newListOffsets = listOffsets[:-1]
    lenght = len(newListOffsets)
    count = 0
    while count < lenght :
        for i in newListOffsets:
            n = pm.read_int(basePtr + i)
            basePtr = n
            count += 1
    else:
        print(f"The base pointer is : {hex(basePtr)}")
        value = pm.read_int(basePtr + listOffsets[-1])
        print(f"The value of that address is:  {value}")
        address = basePtr + listOffsets[-1]
        print(f"The address of that value is : {hex(address)}")
        return address     
