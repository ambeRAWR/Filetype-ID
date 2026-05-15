#!/usr/bin/env python3

import os
import sys
from pathlib import Path

MAGIC_DATABASE = [ #database of filetype's recognised binary headers
    (b'\xFF\xD8\xFF',          0, 'JPEG Image',          ['.jpg', '.jpeg']),
    (b'\x89PNG\r\n\x1a\n',     0, 'PNG Image',           ['.png']),
    (b'%PDF',                  0, 'PDF Document',        ['.pdf']),
    (b'PK\x03\x04',            0, 'ZIP / Office Open XML',['.zip', '.docx', '.xlsx', '.pptx', '.jar', '.apk']),
    (b'\x1f\x8b',              0, 'GZIP Archive',        ['.gz', '.tgz']),
    (b'MZ',                    0, 'Windows Executable',  ['.exe', '.dll']),
    (b'\x7fELF',               0, 'ELF Executable',      ['.elf', '.so', '']),
    (b'GIF87a',                0, 'GIF Image',           ['.gif']),
    (b'GIF89a',                0, 'GIF Image',           ['.gif']),
    (b'\x42\x4D',              0, 'BMP Image',           ['.bmp']),
    (b'RIFF',                  0, 'RIFF Container',      ['.wav', '.avi']),
    (b'\xD0\xCF\x11\xE0',      0, 'OLE2 (Legacy Office)',['.doc', '.xls', '.ppt']),
    (b'\xef\xbb\xbf',          0, 'UTF-8 BOM Text',      ['.txt']),
    (b'\x00\x00\x01\xBA',      0, 'MPEG Video Stream',   ['.mpg', '.mpeg']),
    (b'\x00\x00\x00\x20ftyp',  0, 'MP4 Video',           ['.mp4', '.m4v']),
    (b'ID3',                   0, 'MP3 Audio',           ['.mp3']),
    (b'\x52\x61\x72\x21',      0, 'RAR Archive',         ['.rar']),
    (b'\x37\x7A\xBC\xAF',      0, '7-Zip Archive',       ['.7z']),
    (b'BZh',                   0, 'BZip2 Archive',       ['.bz2']),
]

def read_header(filepath, num_bytes=32): #pulls file header from file
    with open(filepath, 'rb') as f:
        return f.read(num_bytes)

def identify_file(filepath): #checks file header by database above ^^
    path = Path(filepath)
    actual_extension = path.suffix.lower()
    header = read_header(filepath, num_bytes=32)

    detected_type = None
    valid_extensions = []

    for magic, offset, type_name, exts in MAGIC_DATABASE:
        if header[offset : offset + len(magic)] == magic:
            detected_type = type_name
            valid_extensions = exts
            break

    return {
        'filepath':        str(path),
        'extension':       actual_extension,
        'detected_type':   detected_type,
        'valid_extensions': valid_extensions,
        'header_hex':      header.hex(' '),
    }

def analyse_file(filepath): #returns result of database-match check
    result = identify_file(filepath)

    ext       = result['extension']
    valid     = result['valid_extensions']
    detected  = result['detected_type']

    print(f"\n{'═'*54}")
    print(f"  File      : {result['filepath']}")
    print(f"  Extension : {ext or '(none)'}")
    print(f"  Detected  : {detected or 'Unrecognised format'}")
    print(f"  Header    : {result['header_hex'][:47]}...")

    print()
    if detected is None:
        print("Unknown — signature not in database")
    elif not ext:
        print(f"No extension detected — content is {detected}")
    elif ext not in valid:
        print(f"Mismatch  — '{ext}' does not match detected type")
        print(f"     Expected extensions: {valid}")
    else:
        print(f"okay! — extension matches detected type :]")

    return result


def main(): #executes functions
    if len(sys.argv) < 2:
        print("Usage: python3 filetypeID.py <file1> [file2] ...")
        sys.exit(1)

    for filepath in sys.argv[1:]:
        if not os.path.exists(filepath):
            print(f"\n  ✗ File not found: {filepath}")
            continue
        try:
            analyse_file(filepath)
        except PermissionError:
            print(f"\n  ✗ Permission denied: {filepath}")
        except Exception as e:
            print(f"\n  ✗ Error reading {filepath}: {e}")

if __name__ == '__main__':
    main()
