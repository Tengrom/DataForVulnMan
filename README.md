# Frameworks for Vulnerability management based on Data science  

## Intro: 

 In increasingly complex environments and increasingly frequent of cyber attacks, vulnerability management is becoming an increasingly important and difficult task. I have seen many companies that could be saved from attack by implementing proper vulnerability management. Vulnerability management involves analyzing data from many sources. Thanks to this data, we can optimize our activities and identify our gaps.
 
 No single tool can address all these challenges alone.  Many companies already use multiple vulnerability scanners and multiple vulnerability management software. This also requires knowledge and a developed standard of operation.
 
 In his project I will try to gather  all this knowledge in one place and propose standards ready to use including data science.  Also will be prepared ready solution to make easier to understand vulnerability managemnt process and to be used by companies that cannot afford expensive software.
 
 Vulnerability management relies on data, so appropriate actions need to be taken, such as data cleaning, grouping, and others. For this I will use the same process as in Data science. Data quality and security are the most important when managing vulnerabilities and they occur frequently in it errors that accumulate later. therefore, data must be approached in a systematic and proven way

Main goal of this project is defining framework for Vulnerability management based on Data Science. It includes: 

* Propose of Vulnerability management process description 

* Propose of maturity level  

* framework in Jupyter notebook free for use.   

I encourage Everyone for collaboration to build more standardize and usefulness frameworks for different use cases for Vulnerability management.  

##  Process: 

Process is based on Data Science process: 
![Process](https://lh3.googleusercontent.com/pw/ADCreHf53bFBVWybp_M10SDVGECA013VpJjo6IIT25UsqNDLa6bQ0_aIDn7G0Us_JenCIpbY4cIzyvoJZrSnaBuJgg13cXqr9Tv__lPZNSVY366QHLrGbQwaVPOpEVd0-a8LKMPxlOCgmFeSHbwrbRoJ5GnUQg=w1338-h324-s-no-gm?authuser=0)
### Data collection: 

IT can be scanning or collecting data from different sources: 

* Scanning without authorisation 

* Scanning with high privileges authorization 

* Scanning local system by installed agent 

* Passive scanning of capture traffic  

* Gathering application version by SCCM or other tools.  

* Other sources like proxy server with capturing information about version browser and system versions.  

* Analysing protocols on network like If device is responding with only SMBv1 version it means that it’s quite old and vulnerable.   

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
* https://www.first.org/epss/
 

### Data validation 

* Prepare reports and visualisation 

* Presenting finding to correct BU and investigate  

## Vulnerability management Maturity level 

In  progress

## Project status :
#### Phase 1 
- Basic  AmongItems  notebook -  Done
- Basic  OverTime  notebook - In progress
- Vulnerability management Maturity level - not started
- Basic RiskCalculation notebook- not started
- CEO Dashboard with targets - not started

