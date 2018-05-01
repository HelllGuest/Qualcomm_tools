#!python3

from uuid import UUID
from datetime import date

# https://github.com/d-fence/frit/blob/master/frit/fritutils/fsprobe.py
# https://gist.github.com/sque/dc7a057e66371717e921
# https://en.wikipedia.org/wiki/GUID_Partition_Table
# https://github.com/n0fate/raw/blob/master/gpt_parser.py
# https://sourceforge.net/u/guikcd93/gptfdisk/ci/master/tree/parttypes.cc#l179
# http://gitweb.mageia.org/software/drakx/plain/perl-install/partition_table/gpt.pm
# https://github.com/caldwell/gdisk/blob/master/partition-type.c

# https://github.com/android-ia/device-androidia-mixins/blob/master/groups/boot-arch/android_ia/gpt.ini
# https://github.com/android-ia/device-androidia/blob/master/androidia_64/gpt.ini
# https://github.com/android-ia/vendor_intel_baytrail/blob/master/minnow_max/gpt.ini
# https://github.com/android-ia/platform_bootable_userfastboot/blob/master/gpt-sample.ini
# https://android.googlesource.com/platform/hardware/bsp/intel/+/e2ef91a5723be4c50e0bd93f82c329d262c2f366/soc/common/tools/gpt_ini2bin.py
# https://github.com/android-ia/platform_bootable_userfastboot/blob/master/libgpt/gpt.c
# https://github.com/android-ia/vendor_intel_common/blob/master/gpt_bin/gpt_ini2bin.py

guids = {
	UUID('00000000-0000-0000-0000-000000000000'): 'Unused entry',
	UUID('024DEE41-33E7-11D3-9D69-0008C781F39F'): 'MBR partition scheme',
	UUID('C12A7328-F81F-11D2-BA4B-00A0C93EC93B'): 'EFI System partition',
	UUID('21686148-6449-6E6F-744E-656564454649'): 'BIOS Boot partition',
	UUID('D3BFE2DE-3DAF-11DF-BA40-E3A556D89593'): 'Intel Fast Flash (iFFS) partition (for Intel Rapid Start technology)',
	UUID('F4019732-066E-4E12-8273-346C5641494F'): 'Sony boot partition',
	UUID('BFBFAFE7-A34F-448A-9A5B-6213EB736C22'): 'Lenovo boot partition',
	UUID('E3C9E316-0B5C-4DB8-817D-F92DF00215AE'): 'Microsoft Reserved Partition (MSR)',
	UUID('EBD0A0A2-B9E5-4433-87C0-68B6B72699C7'): 'Windows Basic data partition',
	UUID('5808C8AA-7E8F-42E0-85D2-E1E90434CFB3'): 'Windows Logical Disk Manager (LDM) metadata',
	UUID('AF9B60A0-1431-4F62-BC68-3311714A69AD'): 'Windows Logical Disk Manager data',
	UUID('DE94BBA4-06D1-4D40-A16A-BFD50179D6AC'): 'Windows Recovery Environment',
	UUID('37AFFC90-EF7D-4E96-91C3-2D7AE055B174'): 'Windows IBM General Parallel File System (GPFS)',
	UUID('E75CAF8F-F680-4CEE-AFA3-B001E56EFC2D'): 'Windows Storage Spaces partition',
	UUID('75894C1E-3AEB-11D3-B7C1-7B03A0000000'): 'HP-UX Data',
	UUID('E2A1E728-32E3-11D6-A682-7B03A0000000'): 'HP-UX Service',
	UUID('0FC63DAF-8483-4772-8E79-3D69D8477DE4'): 'Linux filesystem data',
	UUID('A19D880F-05FC-4D3B-A006-743F0F84911E'): 'Linux RAID',
	UUID('44479540-F297-41B2-9AF7-D131D5F0458A'): 'Linux Root (x86)',
	UUID('4F68BCE3-E8CD-4DB1-96E7-FBCAF984B709'): 'Linux Root (x86-64)',
	UUID('69DAD710-2CE4-4E3C-B16C-21A1D49ABED3'): 'Linux Root (32-bit ARM)',
	UUID('B921B045-1DF0-41C3-AF44-4C6F280D3FAE'): 'Linux Root (64-bit ARM/AArch64)',
	UUID('993D8D3D-F80E-4225-855A-9DAF8ED7EA97'): 'Linux Root (IA-64)',
	UUID('0657FD6D-A4AB-43C4-84E5-0933C84B4F4F'): 'Linux Swap',
	UUID('E6D6D379-F507-44C2-A23C-238F2A3DF928'): 'Linux Logical Volume Manager (LVM)',
	UUID('933AC7E1-2EB4-4F13-B844-0E14E2AEF915'): 'Linux /home',
	UUID('3B8F8425-20E0-4F3B-907F-1A25A76F98E8'): 'Linux /srv (server data)',
	UUID('7FFEC5C9-2D00-49B7-8941-3EA10A5586B7'): 'Linux Plain dm-crypt',
	UUID('CA7D7CCB-63ED-4C53-861C-1742536059CC'): 'Linux LUKS',
	UUID('8DA63339-0007-60C0-C436-083AC8230908'): 'Linux Reserved',
	UUID('83BD6B9D-7F41-11DC-BE0B-001560B84F0F'): 'FreeBSD Boot',
	UUID('516E7CB4-6ECF-11D6-8FF8-00022D09712B'): 'FreeBSD Data',
	UUID('516E7CB5-6ECF-11D6-8FF8-00022D09712B'): 'FreeBSD Swap',
	UUID('516E7CB6-6ECF-11D6-8FF8-00022D09712B'): 'FreeBSD Unix File System (UFS)',
	UUID('516E7CB8-6ECF-11D6-8FF8-00022D09712B'): 'FreeBSD Vinum volume manager',
	UUID('516E7CBA-6ECF-11D6-8FF8-00022D09712B'): 'FreeBSD ZFS',
	UUID('48465300-0000-11AA-AA11-00306543ECAC'): 'Apple Hierarchical File System Plus (HFS+)',
	UUID('55465300-0000-11AA-AA11-00306543ECAC'): 'Apple UFS',
	UUID('52414944-0000-11AA-AA11-00306543ECAC'): 'Apple RAID',
	UUID('52414944-5F4F-11AA-AA11-00306543ECAC'): 'Apple RAID (offline)',
	UUID('426F6F74-0000-11AA-AA11-00306543ECAC'): 'Apple Boot (Recovery HD)',
	UUID('4C616265-6C00-11AA-AA11-00306543ECAC'): 'Apple Label',
	UUID('5265636F-7665-11AA-AA11-00306543ECAC'): 'Apple TV Recovery',
	UUID('53746F72-6167-11AA-AA11-00306543ECAC'): 'Apple Core Storage (i.e. Lion FileVault)',
	UUID('6A82CB45-1DD2-11B2-99A6-080020736631'): 'Solaris Boot',
	UUID('6A85CF4D-1DD2-11B2-99A6-080020736631'): 'Solaris Root',
	UUID('6A87C46F-1DD2-11B2-99A6-080020736631'): 'Solaris Swap',
	UUID('6A8B642B-1DD2-11B2-99A6-080020736631'): 'Solaris Backup',
	UUID('6A898CC3-1DD2-11B2-99A6-080020736631'): 'Solaris /usr // Apple ZFS',
	UUID('6A8EF2E9-1DD2-11B2-99A6-080020736631'): 'Solaris /var',
	UUID('6A90BA39-1DD2-11B2-99A6-080020736631'): 'Solaris /home',
	UUID('6A9283A5-1DD2-11B2-99A6-080020736631'): 'Solaris Alternate sector',
	UUID('6A945A3B-1DD2-11B2-99A6-080020736631'): 'Solaris Reserved',
	UUID('6A9630D1-1DD2-11B2-99A6-080020736631'): 'Solaris Reserved',
	UUID('6A980767-1DD2-11B2-99A6-080020736631'): 'Solaris Reserved',
	UUID('6A96237F-1DD2-11B2-99A6-080020736631'): 'Solaris Reserved',
	UUID('6A8D2AC7-1DD2-11B2-99A6-080020736631'): 'Solaris Reserved',
	UUID('49F48D32-B10E-11DC-B99B-0019D1879648'): 'NetBSD Swap',
	UUID('49F48D5A-B10E-11DC-B99B-0019D1879648'): 'NetBSD FFS',
	UUID('49F48D82-B10E-11DC-B99B-0019D1879648'): 'NetBSD LFS',
	UUID('49F48DAA-B10E-11DC-B99B-0019D1879648'): 'NetBSD RAID',
	UUID('2DB519C4-B10F-11DC-B99B-0019D1879648'): 'NetBSD Concatenated partition', # libfdisk is wrong on this
	UUID('2DB519EC-B10F-11DC-B99B-0019D1879648'): 'NetBSD Encrypted partition', # libfdisk is wrong on this
	UUID('FE3A2A5D-4F32-41A7-B725-ACCC3285A309'): 'ChromeOS kernel',
	UUID('3CB8E202-3B7E-47DD-8A3C-7FF2A13CFCEC'): 'ChromeOS rootfs',
	UUID('2E0A753D-9E48-43B0-8337-B15192CB1B5E'): 'ChromeOS future use',
	UUID('42465331-3BA3-10F1-802A-4861696B7521'): 'Haiku BFS',
	UUID('85D5E45E-237C-11E1-B4B3-E89A8F7FC3A7'): 'MidnightBSD Boot',
	UUID('85D5E45A-237C-11E1-B4B3-E89A8F7FC3A7'): 'MidnightBSD Data',
	UUID('85D5E45B-237C-11E1-B4B3-E89A8F7FC3A7'): 'MidnightBSD Swap',
	UUID('0394EF8B-237E-11E1-B4B3-E89A8F7FC3A7'): 'MidnightBSD Unix File System (UFS)',
	UUID('85D5E45C-237C-11E1-B4B3-E89A8F7FC3A7'): 'MidnightBSD Vinum volume manager',
	UUID('85D5E45D-237C-11E1-B4B3-E89A8F7FC3A7'): 'MidnightBSD ZFS',
	UUID('45B0969E-9B03-4F30-B4C6-B4B80CEFF106'): 'Ceph Journal',
	UUID('45B0969E-9B03-4F30-B4C6-5EC00CEFF106'): 'Ceph dm-crypt Encrypted Journal',
	UUID('4FBD7E29-9D25-41B8-AFD0-062C0CEFF05D'): 'Ceph OSD',
	UUID('4FBD7E29-9D25-41B8-AFD0-5EC00CEFF05D'): 'Ceph dm-crypt OSD',
	UUID('89C57F98-2FE5-4DC0-89C1-F3AD0CEFF2BE'): 'Ceph disk in creation',
	UUID('89C57F98-2FE5-4DC0-89C1-5EC00CEFF2BE'): 'Ceph dm-crypt disk in creation',
	UUID('824CC7A0-36A8-11E3-890A-952519AD3F61'): 'OpenBSD Data partition',
	UUID('CEF5A9AD-73BC-4601-89F3-CDEEEEE321A1'): 'QNX Power-safe (QNX6) file system',
	UUID('C91818F9-8025-47AF-89D2-F030D7000C2C'): 'Plan 9 partition',
	UUID('9D275380-40AD-11DB-BF97-000C2911D1B8'): 'VMware ESX vmkcore (coredump)',
	UUID('AA31E02A-400F-11DB-9590-000C2911D1B8'): 'VMware ESX VMFS filesystem',
	UUID('9198EFFC-31C0-11DB-8F78-000C2911D1B8'): 'VMware ESX VMware Reserved',
	UUID('2568845D-2332-4675-BC39-8FA5A4748D15'): 'Android-IA Bootloader',
	UUID('114EAFFE-1552-4022-B26E-9B053604CF84'): 'Android-IA Bootloader2',
	UUID('49A4D17F-93A3-45C1-A0DE-F50B2EBE2599'): 'Android-IA Boot',
	UUID('4177C722-9E92-4AAB-8644-43502BFD5506'): 'Android-IA Recovery',
	UUID('EF32A33B-A409-486C-9141-9FFB711F6266'): 'Android-IA Misc',
	UUID('20AC26BE-20B7-11E3-84C5-6CFDB94711E9'): 'Android-IA Metadata',
	UUID('38F428E6-D326-425D-9140-6E0EA133647C'): 'Android-IA System',
	UUID('A893EF21-E428-470A-9E55-0668FD91A2D9'): 'Android-IA Cache',
	UUID('DC76DDA9-5AC1-491C-AF42-A82591580C0D'): 'Android-IA Data',
	UUID('EBC597D0-2053-4B15-8B64-E0AAC75F4DB1'): 'Android-IA Persistent',
	UUID('C5A0AEEC-13EA-11E5-A1B1-001E67CA0C3C'): 'Android-IA Vendor',
	UUID('BD59408B-4514-490D-BF12-9878D963F378'): 'Android-IA Config',
	UUID('8F68CC74-C5E5-48DA-BE91-A0C8C15E9C80'): 'Android-IA Factory',
	UUID('9FDAA6EF-4B3F-40D2-BA8D-BFF16BFB887B'): 'Android-IA Factory (alt)',
	UUID('767941D0-2085-11E3-AD3B-6CFDB94711E9'): 'Android-IA Fastboot / Tertiary',
	UUID('AC6D7924-EB71-4DF8-B48D-E267B27148FF'): 'Android-IA OEM',
	# Wiki DE
	UUID('7412F7D5-A156-4B13-81DC-867174929325'):'ONIE boot',
	UUID('D4E6E2CD-4469-46F3-B5CB-1BFF57AFC149'):'ONIE config',
	UUID('9E1A2D38-C612-4316-AA26-8B49521E5A8B'):'PowerPC PReP boot',
	UUID('BC13C2FF-59E6-4262-A352-B275FD6F7172'):'Freedesktop Extended Boot Partition',
}

#comp = {
#
#}
#diff = set(comp.keys()) - set(guids.keys())
#for i in diff:
#  print(i, comp[i])

count = len(guids) # 105
date = date(2017, 8, 29)
