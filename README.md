# Frameworks for Vulnerability management based on Data science  

## Intro: 

Vulnerability management is not just patching, but gathering, analyzing, managing data and calculating risks based on it.

 In increasingly complex environments and increasingly frequent cyber attacks, vulnerability management is becoming an increasingly important and difficult task. I have seen many companies that could be saved from attack by implementing proper vulnerability management. Vulnerability management involves analyzing data from many sources. Thanks to this data, we can optimize our activities and identify our gaps.

 No single tool can address all these challenges alone. Many companies already use multiple vulnerability scanners and multiple vulnerability management software. This also requires knowledge and a developed standard of operation.
 
 In his project, I will try to gather all this knowledge in one place and propose standards ready to use including data science. Also will prepare ready solutions to make it easier to understand the vulnerability management process and to be used by companies that cannot afford expensive software.

 Vulnerability management relies on data, so appropriate actions need to be taken, such as data cleaning, grouping, and others. For this, I will use the same process as in Data science. Data quality and security are the most important when managing vulnerabilities and they occur frequently in it errors that accumulate later. therefore, data must be approached in a systematic and proven way

 The main goal of this project is to define a framework for Vulnerability management based on Data Science. It includes:
* Propose of Vulnerability management process description
* Propose of maturity level
* framework in Jupyter Notebook free for use.
  
I encourage Everyone to collaboration to build more standardised and usefulness frameworks for different use cases for Vulnerability management.
##  Process: 

Process is based on Data Science process: 
![Process](https://lh3.googleusercontent.com/pw/ADCreHf53bFBVWybp_M10SDVGECA013VpJjo6IIT25UsqNDLa6bQ0_aIDn7G0Us_JenCIpbY4cIzyvoJZrSnaBuJgg13cXqr9Tv__lPZNSVY366QHLrGbQwaVPOpEVd0-a8LKMPxlOCgmFeSHbwrbRoJ5GnUQg=w1338-h324-s-no-gm?authuser=0)
### Data collection: 

It can be scanning or collecting data from different sources:
* Scanning without authorisation
* Scanning with high privileges authorization
* Scanning local system by installed agent
* Passive scanning of capture traffic
* Gathering application versions by SCCM or other tools.
* Other sources like proxy servers capture information about version browsers and system versions.
* Analysing protocols on a network like If the device is responding with only SMBv1 version it means that it’s quite old and vulnerable.



###  Data Discovery:

First fast analytics: 

* Checking summary numbers: Total numbers of vulnerabilities, hosts.  

* Number of duplicated entries in CVE or hosts.  

* Top CVE, per software name or detection source. Top hosts per os and name 

Most issues found in that step: 

* Small numbers of detected vulnerabilities or small numbers of detected hosts - issue with data sources or connector 

* Multiple duplications – issue with connector 

### Data cleansing  

Semi manual analysis: 

* Checking if numbers are correct with number of hosts with other sources like Active Directory, clients using proxy, Firewalls  

* Checking if detected vulnerabilities could be false positives 

* Tree map to visualise distribution CVE per application.  It can provide information about disproportion of your data for example discover only vulnerability related with one application, lack vulnerability for local installed applications 

 

### Data structuring  

* Adding tags with corresponding to the owners of sites, applications, hosts 

### Data transformation and enrichment(in Progress): 
* Adding information about host criticality, expose ,  role 

* Adding information from company Threat intel  like  if CVe is currently exploiting  
* All data required by CVSS 4.0 Scoring Calculation https://www.first.org/cvss/v4-0/
* Mapping MITRE ATT&CK® to CVEs for Impact  https://github.com/center-for-threat-informed-defense/attack_to_cve
* https://nucleussec.com/guide-to-CISA-KEV-Enrichment/
* https://github.com/jgamblin/CISA_Enrichment
* https://www.first.org/epss/
 

### Data validation 

* Prepare reports and visualisation 

* Presenting finding to correct BU and investigate  

## Vulnerability management Maturity level 

* https://www.sans.org/blog/vulnerability-management-maturity-model/
* https://www.sans.org/blog/vulnerability-management-maturity-model-part-ii/
* https://github.com/jonathanristo
* https://www.sans.org/blog/vmmm-self-assessment-tool/
* http://docs.media.bitpipe.com/io_12x/io_120436/item_1066724/TVM%20Maturity%20Model%20WP%202014-10.pdf
* https://learn.cisecurity.org/cis-controls-download

## Links for free  tools 

### Assets discovery:

* https://nmap.org/
* https://www.pingcastle.com/

###  Vulnerability scanning

* https://github.com/scipag/vulscan
* https://www.openvas.org/

### Enrichment

* https://nucleussec.com/

## Project status :
#### Phase 1 
- Vulnerability management knowlage base - In progress
- Basic  AmongItems  notebook -  In progress
- Basic  OverTime  notebook - In progress
- Vulnerability management Maturity level - In progress
- Basic RiskCalculation notebook- not started
- CEO Dashboard with targets - not started

