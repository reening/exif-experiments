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

    # Exif
    Exif = 34665
    GPSInfo = 34853


class InteroperabilityIFDTag(IntEnum):
    InteroperabilityIndex = 1
    InteroperabilityVersion = 2


class ExifIFDTag(IntEnum):
    Interoperability = 40965

    ExifVersion = 36864
    Flashpix = version = FlashpixVersion = 40960
    ColorSpace = 40961
    Gamma = 42240
    ComponentsConfiguration = 37121
    CompressedBitsPerPixel = 37122
    PixelXDimension = 40962
    PixelYDimension = 40963
    MakerNote = 37500
    UserComment = 37510
    RelatedSoundFile = 40964
    DateTimeOriginal = 36867
    DateTimeDigitized = 36868
    OffsetTime = 36880
    OffsetTimeOriginal = 36881
    OffsetTimeDigitized = 36882
    SubSecTime = 37520
    SubSecTimeOriginal = 37521
    SubSecTimeDigitized = 37522
    Temperature = 37888
    Humidity = 37889
    Pressure = 37890
    WaterDepth = 37891
    Acceleration = 37892
    CameraElevationAngle = 37893
    ImageUniqueID = 42016
    CameraOwnerName = 42032
    BodySerialNumber = 42033
    LensSpecification = 42034
    LensMake = 42035
    LensModel = 42036
    LensSerialNumber = 42037

    ExposureTime = 33434
    FNumber = 33437
    ExposureProgram = 34850
    SpectralSensitivity = 34852
    PhotographicSensitivity = 34855
    OECF = 34856
    SensitivityType = 34864
    StandardOutputSensitivity = 34865
    RecommendedExposureIndex = 34866
    ISOSpeed = 34867
    ISOSpeedLatitudeyyy = 34868
    ISOSpeedLatitudezzz = 34869
    ShutterSpeedValue = 37377
    ApertureValue = 37378
    BrightnessValue = 37379
    ExposureBiasValue = 37380
    MaxApertureValue = 37381
    SubjectDistance = 37382
    MeteringMode = 37383
    LightSource = 37384
    Flash = 37385
    FocalLength = 37386
    SubjectArea = 37396
    FlashEnergy = 41483
    SpatialFrequencyResponse = 41484
    FocalPlaneXResolution = 41486
    FocalPlaneYResolution = 41487
    FocalPlaneResolutionUnit = 41488
    SubjectLocation = 41492
    ExposureIndex = 41493
    SensingMethod = 41495
    FileSource = 41728
    SceneType = 41729
    CFAPattern = 41730
    CustomRendered = 41985
    ExposureMode = 41986
    WhiteBalance = 41987
    DigitalZoomRatio = 41988
    FocalLengthIn35mmFilm = 41989
    SceneCaptureType = 41990
    Gain = control = GainControl = 41991
    Contrast = 41992
    Saturation = 41993
    Sharpness = 41994
    DeviceSettingDescription = 41995
    SubjectDistanceRange = 41996
    CompositeImage = 42080
    SourceImageNumberOfCompositeImage = 42081
    SourseExposureTimesOfCompositeImage = 42082


class GPSIFDTag(IntEnum):
    GPSVersionID = 0
    GPSLatitudeRef = 1
    GPSLatitude = 2
    GPSLongitudeRef = 3
    GPSLongitude = 4
    GPSAltitudeRef = 5
    GPSAltitude = 6
    GPSTimeStamp = 7
    GPSSatellites = 8
    GPSStatus = 9
    GPSMeasureMode = 10
    GPSDOP = 11
    GPSSpeedRef = 12
    GPSSpeed = 13
    GPSTrackRef = 14
    GPSTrack = 15
    GPSImgDirectionRef = 16
    GPSImgDirection = 17
    GPSMapDatum = 18
    GPSDestLatitudeRef = 19
    GPSDestLatitude = 20
    GPSDestLongitudeRef = 21
    GPSDestLongitude = 22
    GPSDestBearingRef = 23
    GPSDestBearing = 24
    GPSDestDistanceRef = 25
    GPSDestDistance = 26
    GPSProcessingMethod = 27
    GPSAreaInformation = 28
    GPSDateStamp = 29
    GPSDifferential = 30
    GPSHPositioningError = 31


class CanonIFDTag(IntEnum):
    CameraSettings = 1
    FocalLength = 2
    ShotInfo = 4
    Panorama = 5
    ImageType = 6
    FirmwareVersion = 7
    FileNumber = 8
    OwnerName = 9
    CameraInfo = 13
    ModeIID = 16
    ThumbnailImageValidArea = 19


subifd_map = {
    IFDTag.Exif: ExifIFDTag,
    IFDTag.GPSInfo: GPSIFDTag,
    ExifIFDTag.Interoperability: InteroperabilityIFDTag,
    ExifIFDTag.MakerNote: CanonIFDTag,
}

class TIFFDecoder:
    @staticmethod
    def decode_ifd(bs, parent_tag=None):
        fields = bs.read_short()

        print(f'IFD with {fields} fields')

        for i in range(fields):
            tag_num = bs.read_short()
            type = IFDEntryType(bs.read_short())
            count = bs.read_long()
            value_offset = bs.read_long()

            tag_enum = subifd_map.get(parent_tag, IFDTag)

            try:
                tag = tag_enum(tag_num)
            except ValueError:
                print(f'Unknown Tag {tag_num} {str(type)} {count} {value_offset}')
                continue
        
            print('IFD Entry', tag, type, count, value_offset)

            if tag in subifd_map:
                pos = bs.tell()
                bs.seek(value_offset)

                TIFFDecoder.decode_ifd(bs, parent_tag=tag)

                bs.seek(pos)

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
