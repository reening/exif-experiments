from enum import IntEnum
from io import SEEK_CUR

from bytestream import BE, LE


BYTE_ORDER_BE = b'II'
BYTE_ORDER_LE = b'MM'

MAGIC = 42


class IFDEntryType(IntEnum):
    BYTE = 1
    ASCII = 2
    SHORT = 3
    LONG = 4
    RATIONAL = 5
    SBYTE = 6
    UNDEFINED = 7
    SSHORT = 8
    SLONG = 9
    SRATIONAL = 10
    FLOAT = 11
    DOUBLE = 12


class IFDTag(IntEnum):
    # Baseline
    Artist = 315
    BitsPerSample = 258
    CellLength = 265
    CellWidth = 264
    ColorMap = 320
    Compression = 259
    Copyright = 33432
    DateTime = 306
    ExtraSamples = 338
    FillOrder = 266
    FreeByteCounts = 289
    FreeOffsets = 288
    GrayResponseCurve = 291
    GrayResponseUnit = 290
    HostComputer = 316
    ImageDescription = 270
    ImageLength = 257
    ImageWidth = 256
    Make = 271
    MaxSampleValue = 281
    MinSampleValue = 280
    Model = 272
    NewSubfileType = 254
    Orientation = 274
    PhotometricInterpretation = 262
    PlanarConfiguration = 284
    ResolutionUnit = 296
    RowsPerStrip = 278
    SamplesPerPixel = 277
    Software = 305
    StripByteCounts = 279
    StripOffsets = 273
    SubfileType = 255
    Thresholding = 263
    XResolution = 282
    YResolution = 283

    # JPEG
    JPEGProc = 512
    JPEGInterchangeFormat = 513
    JPEGInterchangeFormatLength = 514
    JPEGRestartInterval = 515
    JPEGLosslessPredictors = 517
    JPEGPointTransforms = 518
    JPEGQTables = 519
    JPEGDCTables = 520
    JPEGACTables = 521

    # YCbCr Images
    YCbCrCoefficients = 529
    YCbCrSubSampling = 530
    YCbCrPositioning = 531

    # Private tags
    Exif = 34665
    GPSInfo = 34853
    

class TIFFDecoder:
    @staticmethod
    def decode_ifd(bs):
        fields = bs.read_short()

        print(f'IFD with {fields} fields')

        for i in range(fields):
            tag = IFDTag(bs.read_short())
            type = IFDEntryType(bs.read_short())
            count = bs.read_long()
            value_offset = bs.read_long()
        
            print('IFD Entry', tag, type, count, value_offset)

        next_offset = bs.read_long()

        return None, next_offset

    @staticmethod
    def decode(bs):
        bo = bs.read(2)
        if bo == BYTE_ORDER_BE:
            bs.endianness = BE
        elif bo == BYTE_ORDER_LE:
            bs.endianness = LE
        else:
            raise Exception('Unknown byte order, not a TIFF file')

        magic = bs.read_short()

        if magic != MAGIC:
            raise Exception('Unknown magic number, not a TIFF file')

        offset = bs.read_long()
        print('HDR', bo.decode('ascii'), magic, offset)

        while offset != 0:
            bs.seek(offset)
            ifd, offset = TIFFDecoder.decode_ifd(bs)
