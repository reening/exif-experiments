from io import SEEK_SET, SEEK_CUR, SEEK_END


BE = 1
LE = 2


class ByteStreamReader:
    def __init__(self, fh, endianness=LE):
        self.fh = fh
        self.endianness = endianness

    def read(self, size=-1):
        return self.fh.read(size)

    def read_byte(self):
        return self.read(1)[0]

    def read_short(self):
        b = self.read(2)

        if self.endianness == BE:
            b = b[::-1]

        return (b[0] << 8) + b[1]

    def read_long(self):
        b = self.read(4)

        if self.endianness == BE:
            b = b[::-1]

        return (b[0] << 24) + (b[1] << 16) + (b[2] << 8) + b[3]

    def seek(self, offset, whence=SEEK_SET):
        return self.fh.seek(offset, whence)

    def tell(self):
        return self.fh.tell()

    @staticmethod
    def open(file, endianness=LE, **kwargs):
        fh = open(file, mode='rb', **kwargs)
        return ByteStreamReader(fh)
