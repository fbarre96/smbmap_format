# SMBMAP formateur

Ce script sert à formater les sorties textes de smbmap.
Une sortie de smbmap sur un sous-réseaux entier est complexe à analyser car les informations sont séparées de plusieurs dizaines/centaines de lignes.
L'utilisation du script se fait ainsi

```
python3 smbformat.py <Sortie_smbmap.txt> <Nom_fichier_sortie.txt>

```

Aucune dépendance requise.

La sortie finale du script doit ressembler à 

```
\\172.24.1.10:445\IPC$\lsass    r--r--r--       4 Mon Jan  1 00:09:21 1601

\\SERVER\SHARE\PATH\TO\FILE	Permissions	size DATE
```
