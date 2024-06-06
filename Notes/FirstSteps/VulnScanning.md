# Vulnerability  scanning - List of first steps

### Applied standards:

Automated Identification in  [Maturity Assessment VMMM](https://github.com/jonathanristo/VMMM-self-assessment-tool)

AND

[CISv8](https://learn.cisecurity.org/cis-controls-download) on IG1 Level - 07 Continuous Vulnerability Management

### Steps:

* NMAP scans with gathering banners and other safe  script and protocols  - like if something is smb1 it's  old and big chance to be  vulnerable

* Analisys of banners gathered results in CVE by software version

* Report all  finding more focusing on outdated components or vulnerabilities with critical  of importance

* Agree process and procedure  for managing outdated components and patching of application / devices. Don't forgot about network equipment also

* It's ok to use free tools like openvasp but do scans with authentication there will small amount of finding  without authentication to devices.

* Prepare first analysis of  vulnerability decide is't enough for now or  there is need to buy enterprise solutions .

* The best solution with less overwork and are  solutions with has agents with can be installed on hosts . Some antivirus has already this functionality  base  on that you can  already have results.

* Work on your  pathing process and responsibility of fixing it ,  Just very robust plan what can be done for now and so on what are the gaps .  No big  plans.

