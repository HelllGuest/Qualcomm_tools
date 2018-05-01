#!python3

''' BSD 3-Clause License — but if it was useful to you, you may tell me :)
Copyright (c) 2016-2017, Alexandre `Alex131089` Levavasseur
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the copyright holder nor the names of its
      contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import sys, io
from struct import unpack
from uuid import UUID

# Utils
try:
	# See https://gist.github.com/Alex131089/b3a23c9461e95433387f285f6e0860ca
	# and put guids.py in the same location
	from guids import guids
except:
	guids = {}
# https://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
def sizeof_fmt(num, suffix='B'):
	for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
		if abs(num) < 1024.0:
			return "%g %s%s" % (num, unit, suffix)
		num /= 1024.0
	return "%g %s%s" % (num, 'Yi', suffix)


# Help
if len(sys.argv) < 2:
	print('Usage: ./{} <gpt.bin>'.format(sys.argv[0]))
	exit(-1)

# Defines
# https://github.com/android-ia/vendor_intel_common/blob/master/gpt_bin/gpt_ini2bin.py
expected_magic = 0x6a8b0da1
header_len = 0xC # = 3*4 : A1 0D 8B 6A  00 00 00 00  0D 00 00 00
                 #         MAGIC        Start LBA    ENTRY COUNT
entry_len = 0x6C

# Now start
# http://www.devdungeon.com/content/working-binary-data-python
with open(sys.argv[1], "rb") as binary_file:
	# Read the whole file at once
	data = binary_file.read()

# https://stackoverflow.com/questions/18563018/how-to-remove-a-range-of-bytes-from-a-bytes-object-in-python
#del data[0:0xc]

# https://stackoverflow.com/questions/20024490/how-to-split-a-byte-string-into-separate-bytes-in-python
entries = [data[i:i+entry_len] for i in range(header_len, len(data)-header_len, entry_len)]
magic, start_lba, entries_count = unpack('<LLL', data[:header_len])

print('{:<16} = 0x{:x} ({})'.format('Magic', magic, ('valid' if magic == expected_magic else 'invalid, 0x{:x} expected'.format(expected_magic))))
print('{:<16} = {}'.format('Start LBA', start_lba))
print('{:<16} = {} (file size allows {} entries)'.format('Partition count', entries_count, len(entries)))
print()

print ('{:<36} {:<10} {:36}\t{}'.format('Partition name', 'Size', 'GPT Type GUID', 'Partition UUID'))
print ('{:-<36} {:-<10} {:-<36}\t{:-<36}'.format('', '', '', ''))
for entry in entries:
	# https://stackoverflow.com/questions/14859578/how-to-read-bytes-as-stream-in-python-3
	# https://docs.python.org/3/library/io.html
	entry = io.BytesIO(entry)
	
	# https://docs.python.org/3/library/struct.html
	size = unpack('<L', entry.read(4))[0]
	size_pp = sizeof_fmt(size*1024*1024)
	#print(size[0], 'MB')
	
	# https://docs.python.org/3/library/codecs.html#standard-encodings
	# https://stackoverflow.com/questions/1185524/how-to-trim-whitespace-including-tabs
	name = entry.read(0x48).decode('utf_16_le').strip('\0')
	#print(name)
	
	# https://docs.python.org/3.1/library/uuid.html
	guid = UUID(bytes_le=entry.read(0x10))
	guid_name = guids[guid] if guid in guids else str(guid)
	#print(guid)
	
	puid = UUID(bytes_le=entry.read(0x10))
	puid_name = guids[puid] if puid in guids else str(puid)
	#print(puid)
	
	print ('{:<36} {:<10} {:36}\t{}'.format(name, size_pp, guid_name, puid_name))
	
	end = entry.read()
	if len(end) > 0:
		print('Extra data:', end)

'''
--Sample outputs : 

PS D:\Dev\GPT> py -3 .\read.py .\gpt_dual.bin
Magic            = 0x6a8b0da1 (valid)
Start LBA        = 0
Partition count  = 13 (file size allows 13 entries)

Partition name                       Size       GPT Type GUID                           Partition UUID
------------------------------------ ---------- ------------------------------------    ------------------------------------
android_persistent                   7 MiB      Linux filesystem data                   Android-IA Persistent
android_config                       8 MiB      Linux filesystem data                   Android-IA Config
android_factory                      10 MiB     Linux filesystem data                   Android-IA Factory
android_misc                         6 MiB      Android-IA Misc                         Android-IA Misc
android_metadata                     16 MiB     Android-IA Metadata                     Android-IA Metadata
android_bk1                          16 MiB     Linux filesystem data                   Linux filesystem data
android_bootloader                   32 MiB     EFI System partition                    Android-IA Bootloader
android_bootloader2                  32 MiB     Windows Basic data partition            Android-IA Bootloader2
android_boot                         32 MiB     Android-IA Boot                         Android-IA Boot
android_recovery                     32 MiB     Android-IA Recovery                     Android-IA Recovery
android_system                       1.875 GiB  Linux filesystem data                   Android-IA System
android_cache                        256 MiB    Linux filesystem data                   Android-IA Cache
android_data                         12 GiB     Linux filesystem data                   Android-IA Data

PS D:\Dev\GPT> py -3 .\read.py .\gpt_miui.bin
Magic            = 0x6a8b0da1 (valid)
Start LBA        = 0
Partition count  = 13 (file size allows 13 entries)

Partition name                       Size       GPT Type GUID                           Partition UUID
------------------------------------ ---------- ------------------------------------    ------------------------------------
android_persistent                   7 MiB      Linux filesystem data                   Android-IA Persistent
android_config                       8 MiB      Linux filesystem data                   Android-IA Config
android_factory                      10 MiB     Linux filesystem data                   Android-IA Factory
android_misc                         6 MiB      Android-IA Misc                         Android-IA Misc
android_metadata                     16 MiB     Android-IA Metadata                     Android-IA Metadata
android_bk1                          16 MiB     Linux filesystem data                   Linux filesystem data
android_bootloader                   32 MiB     EFI System partition                    Android-IA Bootloader
android_bootloader2                  32 MiB     Windows Basic data partition            Android-IA Bootloader2
android_boot                         32 MiB     Android-IA Boot                         Android-IA Boot
android_recovery                     32 MiB     Android-IA Recovery                     Android-IA Recovery
android_system                       1.875 GiB  Linux filesystem data                   Android-IA System
android_cache                        256 MiB    Linux filesystem data                   Android-IA Cache
android_data                         4 PiB      Linux filesystem data                   Android-IA Data
'''