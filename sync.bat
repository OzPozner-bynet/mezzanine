@echo off
@echo changing dir
cd F:\bynet\Sites\mezzanine
@echo copy db
scp -i "f:\bynet\id_rsa" F:\bynet\Sites\mezzanine\cloudhome\cloudhome.db ozpoz@ec2-18-200-245-127.eu-west-1.compute.amazonaws.com:/home/ozpoz/sites/mezzanine/cloudhome/cloudhome.db
scp -i "f:\bynet\id_rsa" F:\bynet\Sites\mezzanine\cloudhome\cloudhome\settings.py ozpoz@ec2-18-200-245-127.eu-west-1.compute.amazonaws.com:/home/ozpoz/sites/mezzanine/cloudhome/cloudhome/settings.py