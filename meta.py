from io import SEEK_CUR

from bytestream import ByteStreamReader
from tiff import TIFFDecoder

filename = '/home/reening/Projects/JPEGReader/data.exif'
bs = ByteStreamReader.open(filename)

decoded = TIFFDecoder.decode(bs)

print(decoded)
