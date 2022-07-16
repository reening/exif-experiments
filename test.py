from io import SEEK_CUR

from bytestream import ByteStreamReader, BE, LE
from jpeg.marker import Marker
from jpeg.app import APP_EXIF, APP_XMP
from tiff import TIFFDecoder

filename = '/home/reening/Downloads/20220627184253_IMG_5096.JPG'
bs = ByteStreamReader.open(filename)

while True:
    marker_num = bs.read_short()
    marker = Marker(marker_num)
    print(marker)

    if marker == Marker.SOI:
        pass
    elif marker == Marker.EOI:
        break
    elif (marker & 0xFFF0) == Marker.APP0:
        length = bs.read_short()
        pos = bs.tell()
        data = bs.read(length - 2)

        app_type_marker = data.find(0x00)
        app_type = data[0:app_type_marker].decode('ascii')

        if app_type == APP_EXIF:
            bs.seek(pos + len(APP_EXIF) + 2)

            decoded = TIFFDecoder.decode(bs)
            print(decoded)

            bs.seek(pos + len(data))
        elif app_type == APP_XMP:
            app_data = data[app_type_marker + 1:]
            print(app_data.decode('utf8'))

    elif marker in (Marker.DQT, ):
        length = bs.read_short()
        bs.seek(length - 2, SEEK_CUR)
    elif marker == Marker.SOS:
        length = bs.read_short()
        bs.seek(length - 2, SEEK_CUR)

        # Skip to next marker
        while True:
            b = bs.read_byte()

            if b != 0xFF:
                continue

            nb = bs.read_byte()
            if nb == 0x00:
                continue

            bs.seek(-2, SEEK_CUR)
            break
    elif (marker & 0xFFF0) == Marker.SOF0:
        length = bs.read_short()
        bs.seek(length - 2, SEEK_CUR)
