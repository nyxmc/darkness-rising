import os
import shutil

from zipfile import ZipFile


def create_tmp_dir(name):
    try:
        os.mkdir(name)
    except Exception as ignored:
        try:
            shutil.rmtree(name)
            os.mkdir(name)
        except Exception as ignored:
            print("Could not remove build dir. Please remove it manually.")
            sys.exit(1)

def delete_tmp_dir(name):
    try:
        shutil.rmtree(name)
    except Exception as ignored:
        print(f"Could not remove {name} dir. Please remove it manually.")
        sys.exit(1)

def zip(name, dirs, extra_files=[]):
    try:
        os.mkdir("build")
        os.remove("build/" + name)
    except Exception as ignored:
        pass

    with ZipFile("build/" + name, mode="w") as archive:
        for dir in dirs:
            for root, directories, files in os.walk(dir):
                for filename in files:
                    filepath = os.path.join(root, filename)
                    archive.write(filepath)
        for file in extra_files:
            archive.write(file)

def bytes_to_long(bytes):
    assert len(bytes) == 8
    return sum((b << (k * 8) for k, b in enumerate(bytes)))

def murmur64(data, seed = 19820125):

    m = 0xc6a4a7935bd1e995
    r = 47

    MASK = 2 ** 64 - 1

    data_as_bytes = bytearray(data)

    h = seed ^ ((m * len(data_as_bytes)) & MASK)

    off = len(data_as_bytes)/8*8
    for ll in range(0, off, 8):
        k = bytes_to_long(data_as_bytes[ll:ll + 8])
        k = (k * m) & MASK
        k = k ^ ((k >> r) & MASK)
        k = (k * m) & MASK
        h = (h ^ k)
        h = (h * m) & MASK

    l = len(data_as_bytes) & 7

    if l >= 7:
        h = (h ^ (data_as_bytes[off+6] << 48))

    if l >= 6:
        h = (h ^ (data_as_bytes[off+5] << 40))

    if l >= 5:
        h = (h ^ (data_as_bytes[off+4] << 32))

    if l >= 4:
        h = (h ^ (data_as_bytes[off+3] << 24))

    if l >= 3:
        h = (h ^ (data_as_bytes[off+2] << 16))

    if l >= 2:
        h = (h ^ (data_as_bytes[off+1] << 8))

    if l >= 1:
        h = (h ^ data_as_bytes[off])
        h = (h * m) & MASK

    h = h ^ ((h >> r) & MASK)
    h = (h * m) & MASK
    h = h ^ ((h >> r) & MASK)

    return h
