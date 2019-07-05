import re
import sys
import os
regex_only_match_serv = re.compile(r"^\[\+\] IP: (\S+)")
regex_only_match_share_header = re.compile(r"^\t(\S+)\s+([A-Z ,]+)$") # group 1 = SHARE NAME group 2 = PERMISSIONS
regex_only_match_dir = re.compile(r"^\t(\S+)$") # group 1 = directory full path
regex_only_match_files = re.compile(r"^\s+([d-])([xrw-]{9})\s+([^\t]+)\t(.+)$") # group 1 = d ou -, group 2 = permissions, group 3 = date, group 4 = filename

if len(sys.argv) != 3:
    print("Usage: python3 smbformat.py <smboutput.txt> <formated_outpout.txt>")
    sys.exit(0)
with open(sys.argv[2], "w") as fout:
    with open(sys.argv[1]) as f:
        current_serv = ""
        current_share = ""
        current_dir = ""
        for line in f:
            result = regex_only_match_serv.match(line)
            if result is not None:
                ip = str(result.group(1))
                current_serv = ip
                continue
            result = regex_only_match_share_header.match(line)
            if result is not None:
                share_name = str(result.group(1))
                permissions = str(result.group(2))
                current_share = share_name
                continue
            result = regex_only_match_dir.match(line)
            if result is not None:
                dir_path = str(result.group(1))
                current_dir = dir_path
                continue
            result = regex_only_match_files.match(line)
            if result is not None:
                isDirectory = (str(result.group(1)) == "d")
                permissions = str(result.group(2))
                date = str(result.group(3))
                file_name = str(result.group(4))
                fullpath = "\\\\"+current_serv+"\\"+current_share+current_dir[1:]+file_name
                fout.write(fullpath+"\t"+permissions+"\t"+date+"\n")
                continue