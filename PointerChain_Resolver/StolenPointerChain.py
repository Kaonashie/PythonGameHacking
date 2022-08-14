class PointerChain:
    def __init__(self, offsets: Sequence[int]):
        self._offsets_ = offsets
 
    def resolve(self, pm: Pymem, base) -> int:
        try:
            addr = base
            for offset in self._offsets_[:-1]:
                addr = pm.read_int(addr + offset)
            return addr + self._offsets_[-1]
        except:
            return None
 
pPlayerControlStatic = PointerChain([0x5c, 0])
addr = pPlayerControlStatic.resolve(self._pm_, self._PlayerControl_class_)