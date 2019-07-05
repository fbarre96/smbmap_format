# SMBMAP formating

This script reformats the output of the great smb mapping tool from ShawnDEvans
 https://github.com/ShawnDEvans/smbmap

The smbmap tool is great and I use it often but it's output can be quiet confusing 
as it splits the info across multiple lines.

The output generated with this tool gather all the info on one line.

```
\\172.16.0.10:445\IPC$\lsass    r--r--r--       4 Mon Jan  1 00:09:21 1601

\\SERVER\SHARE\PATH\TO\FILE	Permissions	size DATE
```

# Run it

Install python 3 if not installed already, and just run it with

```
python3 smbformat.py <smbmap_output.txt> <formated_output.txt>

```
