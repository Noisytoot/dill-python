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
    compress-lzo [filename]: compress file using lzo""")

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
elif command == "read-zlib":
    with open(filename, "rb") as f:
        card = toml.loads(zlib.decompress(f.read()).decode("utf-8"))
elif command == "compress-zlib":
    ufile = open(filename, "r")
    cdata = zlib.compress(ufile.read().encode("utf-8"))
    ufile.close()
    with open(f"{filename}.zlib", "wb") as cfile:
        cfile.write(cdata)
elif command == "read-lz4":
    with open(filename, "rb") as f:
        card = toml.loads(lz4.frame.decompress(f.read()).decode("utf-8"))
elif command == "compress-lz4":
    ufile = open(filename, "r")
    cdata = lz4.frame.compress(ufile.read().encode("utf-8"))
    ufile.close()
    with open(f"{filename}.lz4", "wb") as cfile:
        cfile.write(cdata)
elif command == "read-gz":
    with open(filename, "rb") as f:
        card = toml.loads(gzip.decompress(f.read()).decode("utf-8"))
elif command == "compress-gz":
    ufile = open(filename, "r")
    cdata = gzip.compress(ufile.read().encode("utf-8"))
    ufile.close()
    with open(f"{filename}.gz", "wb") as cfile:
        cfile.write(cdata)
elif command == "read-bz2":
    with open(filename, "rb") as f:
        card = toml.loads(bz2.decompress(f.read()).decode("utf-8"))
elif command == "compress-bz2":
    ufile = open(filename, "r")
    cdata = bz2.compress(ufile.read().encode("utf-8"))
    ufile.close()
    with open(f"{filename}.bz2", "wb") as cfile:
        cfile.write(cdata)
elif command == "read-xz":
    with open(filename, "rb") as f:
        card = toml.loads(lzma.decompress(f.read()).decode("utf-8"))
elif command == "compress-xz":
    ufile = open(filename, "r")
    cdata = lzma.compress(ufile.read().encode("utf-8"))
    ufile.close()
    with open(f"{filename}.xz", "wb") as cfile:
        cfile.write(cdata)
elif command == "read-br":
    with open(filename, "rb") as f:
        card = toml.loads(brotli.decompress(f.read()).decode("utf-8"))
elif command == "compress-br":
    ufile = open(filename, "r")
    cdata = brotli.compress(ufile.read().encode("utf-8"))
    ufile.close()
    with open(f"{filename}.br", "wb") as cfile:
        cfile.write(cdata)
elif command == "read-zstd":
    with open(filename, "rb") as f:
        decompressor = zstd.ZstdDecompressor()
        card = toml.loads(decompressor.decompress(f.read()).decode("utf-8"))
elif command == "compress-zstd":
    ufile = open(filename, "r")
    compressor = zstd.ZstdCompressor()
    cdata = compressor.compress(ufile.read().encode("utf-8"))
    ufile.close()
    with open(f"{filename}.zst", "wb") as cfile:
        cfile.write(cdata)
elif command == "read-sz":
    with open(filename, "rb") as f:
        card = toml.loads(snappy.decompress(f.read()).decode("utf-8"))
elif command == "compress-sz":
    ufile = open(filename, "r")
    cdata = snappy.compress(ufile.read().encode("utf-8"))
    ufile.close()
    with open(f"{filename}.sz", "wb") as cfile:
        cfile.write(cdata)
elif command == "read-lzo":
    with open(filename, "rb") as f:
        card = toml.loads(lzo.decompress(f.read()).decode("utf-8"))
elif command == "compress-lzo":
    ufile = open(filename, "r")
    cdata = lzo.compress(ufile.read().encode("utf-8"))
    ufile.close()
    with open(f"{filename}.lzo", "wb") as cfile:
        cfile.write(cdata)


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
        warning("the format if not specified in the document")
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
