#!/usr/bin/env python3
import toml, sys, datetime, zlib, lz4.frame, gzip, bz2, brotli, lzma, snappy, lzo
import zstandard as zstd
from contextlib import suppress
from colorama import init, deinit, Fore, Style

init()

def dillhelp():
    print("""\
Commands:
    read [filename]: read uncompressed dill file
    read-zlib [filename]: read zlib compressed file
    read-lz4 [filename]: read lz4 compressed file
    read-gz [filename]: read gzip compressed file
    read-bz2 [filename]: read bzip2 compressed file
    read-br [filename]: read brotli compressed file
    read-xz [filename]: read xz compressed file
    read-sz [filename]: read snappy compressed file
    read-lzo [filename]: read lzo compressed file
    compress-zlib [filename]: compress file using zlib
    compress-lz4 [filename]: compress file using lz4
    compress-gz [filename]: compress file using gzip
    compress-bz2 [filename]: compress file using bzip2
    compress-br [filename]: compress file using brotli
    compress-xz [filename]: compress file using xz
    compress-sz [filename]: compress file using snappy
    compress-lzo [filename]: compress file using lzo
    decompress-zlib [filename]: decompress file using zlib
    decompress-lz4 [filename]: decompress file using lz4
    decompress-gz [filename]: decompress file using gzip
    decompress-bz2 [filename]: decompress file using bzip2
    decompress-br [filename]: decompress file using brotli
    decompress-xz [filename]: decompress file using xz
    decompress-sz [filename]: decompress file using snappy
    decompress-lzo [filename]: decompress file using lzo""")

if len(sys.argv) < 2:
    dillhelp()
    exit(0)

command = sys.argv[1]
if len(sys.argv) > 2:
    filename = sys.argv[2]

if command == "help":
    dillhelp()
    exit(0)
elif command == "read":
    card = toml.load(filename)

# Zlib
elif command == "read-zlib":
    with open(filename, "rb") as f:
        card = toml.loads(zlib.decompress(f.read()).decode("utf-8"))
elif command == "compress-zlib":
    with open(filename, "r") as f:
        cdata = zlib.compress(f.read().encode("utf-8"))
    sys.stdout.buffer.write(cdata)
elif command == "decompress-zlib":
    with open(filename, "rb") as f:
        udata = zlib.decompress(f.read()).decode("utf-8")
    sys.stdout.write(udata)

# LZ4
elif command == "read-lz4":
    with open(filename, "rb") as f:
        card = toml.loads(lz4.frame.decompress(f.read()).decode("utf-8"))
elif command == "compress-lz4":
    with open(filename, "r") as f:
        cdata = lz4.frame.compress(f.read().encode("utf-8"))
    sys.stdout.buffer.write(cdata)
elif command == "decompress-lz4":
    with open(filename, "rb") as f:
        udata = lz4.frame.decompress(f.read()).decode("utf-8")
    sys.stdout.write(udata)

# Gzip
elif command == "read-gz":
    with open(filename, "rb") as f:
        card = toml.loads(gzip.decompress(f.read()).decode("utf-8"))
elif command == "compress-gz":
    with open(filename, "r") as f:
        cdata = gzip.compress(f.read().encode("utf-8"))
    sys.stdout.buffer.write(cdata)
elif command == "decompress-gz":
    with open(filename, "rb") as f:
        udata = gzip.decompress(f.read()).decode("utf-8")
    sys.stdout.write(udata)

# Bzip2
elif command == "read-bz2":
    with open(filename, "rb") as f:
        card = toml.loads(bz2.decompress(f.read()).decode("utf-8"))
elif command == "compress-bz2":
    with open(filename, "r") as f:
        cdata = bz2.compress(f.read().encode("utf-8"))
    sys.stdout.buffer.write(cdata)
elif command == "decompress-bz2":
    with open(filename, "rb") as f:
        udata = bz2.decompress(f.read()).decode("utf-8")
    sys.stdout.write(udata)

# XZ
elif command == "read-xz":
    with open(filename, "rb") as f:
        card = toml.loads(lzma.decompress(f.read()).decode("utf-8"))
elif command == "compress-xz":
    with open(filename, "r") as f:
        cdata = lzma.compress(f.read().encode("utf-8"))
    sys.stdout.buffer.write(cdata)
elif command == "decompress-xz":
    with open(filename, "rb") as f:
        udata = lzma.decompress(f.read()).decode("utf-8")
    sys.stdout.write(udata)

# Brotli
elif command == "read-br":
    with open(filename, "rb") as f:
        card = toml.loads(brotli.decompress(f.read()).decode("utf-8"))
elif command == "compress-br":
    with open(filename, "r") as f:
        cdata = brotli.compress(f.read().encode("utf-8"))
    sys.stdout.buffer.write(cdata)
elif command == "decompress-br":
    with open(filename, "rb") as f:
        udata = brotli.decompress(f.read()).decode("utf-8")
    sys.stdout.write(udata)

# Zstandard
elif command == "read-zstd":
    with open(filename, "rb") as f:
        decompressor = zstd.ZstdDecompressor()
        card = toml.loads(decompressor.decompress(f.read()).decode("utf-8"))
elif command == "compress-zstd":
    with open(filename, "r") as f:
        compressor = zstd.ZstdCompressor()
        cdata = compressor.compress(ufile.read().encode("utf-8"))
    sys.stdout.buffer.write(cdata)
elif command == "decompress-zstd":
    with open(filename, "rb") as f:
        decompressor = zstd.ZstdDecompressor()
        udata = decompressor.decompress(f.read()).decode("utf-8")
    sys.stdout.write(udata)

# Snappy
elif command == "read-sz":
    with open(filename, "rb") as f:
        card = toml.loads(snappy.decompress(f.read()).decode("utf-8"))
elif command == "compress-sz":
    with open(filename, "r") as f:
        cdata = snappy.compress(f.read().encode("utf-8"))
    sys.stdout.buffer.write(cdata)
elif command == "decompress-sz":
    with open(filename, "rb") as f:
        udata = snappy.decompress(f.read()).decode("utf-8")
    sys.stdout.write(udata)

# LZO
elif command == "read-lzo":
    with open(filename, "rb") as f:
        card = toml.loads(lzo.decompress(f.read()).decode("utf-8"))
elif command == "compress-lzo":
    with open(filename, "r") as f:
        cdata = lzo.compress(f.read().encode("utf-8"))
    sys.stdout.buffer.write(cdata)
elif command == "decompress-lzo":
    with open(filename, "rb") as f:
        udata = lzo.decompress(f.read()).decode("utf-8")
    sys.stdout.write(udata)

def warning(text):
    print(f"{Fore.YELLOW}{Style.BRIGHT}Warning: {text}{Style.RESET_ALL}")

# def isLeapYear(year):
#     if year % 100 == 0:
#         if year % 400 == 0 and year % 4 == 0:
#             return True
#         return False
#     elif year % 4 == 0:
#         return True
#     return False

def read():
    if "format" not in card["meta"]:
        warning("the format is not specified in the document")
    if ("format" in card["meta"]) and (card["meta"]["format"].lower() != "dill"):
        warning("the format specified in the in document is not Dill")
    with suppress(Exception):
        print("First name: " + card["data"]["name"]["first"])
    with suppress(Exception):
        print("Middle name: " + card["data"]["name"]["middle"])
    with suppress(Exception):
        print("Last name: " + card["data"]["name"]["last"])
    with suppress(Exception):
        print("Birthdate: " + str(card["data"]["birthdate"]))
    # h = datetime.date.today() - card["data"]["birthdate"]
    # year = int(card["data"]["birthdate"].year())
    # while year != int(datetime.date.today().year())
    # if isLeapYear(year) == True:
    # print(h.days / 365 + 1/4)
    # else:
    #     print(h.days / 365)
    # print(isLeapYear(2000))
    with suppress(Exception):
        for which, pluscode in card["data"]["location"]["pluscode"].items():
            print(f"{which} plus code: {pluscode}")
    with suppress(Exception):
        for which, address in card["data"]["location"]["address"].items():
            print(f"{which} address: {address}")
    with suppress(Exception):
        for which, postcode in card["data"]["location"]["postcode"].items():
            print(f"{which} post code: {postcode}")
    with suppress(Exception):
        for which, latlong in card["data"]["location"]["latlong"].items():
            print(f"{which} latitude: {latlong[0]}")
    with suppress(Exception):        
        for which, latlong in card["data"]["location"]["latlong"].items():
            print(f"{which} longitude: {latlong[1]}")
    with suppress(Exception):
        for which, phone in card["data"]["contact"]["phone"].items():
            print(f"{which} phone number: {phone}")
    with suppress(Exception):
        for which, email in card["data"]["contact"]["email"].items():
            print(f"{which} email address: {email}")
    with suppress(Exception):
        for app, username in card["data"]["contact"]["username"].items():
            print(app + " username: " + username)
    with suppress(Exception):
        print("Organization: " + card["data"]["organization"])
    with suppress(Exception):
        for citizenship in card["data"]["citizenship"]:
            print("Citizenship: " + citizenship)
    with suppress(Exception):
        print("Website: " + card["data"]["website"])
    with suppress(Exception):
        print("Description: " + card["data"]["description"])
    with suppress(Exception):
        for language in card["data"]["languages"]["fluent"]:
            print("Fluent language: " + language)
    with suppress(Exception):
        print("Job: " + card["data"]["job"])
    with suppress(Exception):
        for key, value in card["data"]["custom"].items():
            if key in card["define"]:
                print(card["define"][key] + ": " + value)
            else:
                print(f"{key}: {value}")
    with suppress(Exception):
        print("Gender: " + card["data"]["gender"])

if (command == "read"
    or command == "read-zlib"
    or command == "read-lz4"
    or command == "read-gz"
    or command == "read-bz2"
    or command == "read-xz"
    or command == "read-br"
    or command == "read-zstd"
    or command == "read-sz"
    or command == "read-lzo"):
    read()

deinit()
