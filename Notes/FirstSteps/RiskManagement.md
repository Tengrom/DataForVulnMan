# Risk management - List of first steps

Prioritization in  [Maturity Assessment VMMM](https://github.com/jonathanristo/VMMM-self-assessment-tool)

AND

[CISv8](https://learn.cisecurity.org/cis-controls-download) on IG1 Level - 07 Continuous Vulnerability Management

* Divide vulnerabilities for 3 categories 

      - Lack   of  patching :  Easy to resolve by deploying patches

      - Configuration / Hardening:  Medium level  to resolve by implementing configuration/Hardening standards. Examples of weak configuration:
              - Open permisions
              - Unsecured privilage access
              - Errors ( how they are handled)
              - Unsecure protocols
              - Default settings
   
      - Cryptography :  Require cryptography policy and information what type of data is on hosts

* Prepare lists of security control  with could help  mitigate detected vulnerabilities 

* Start proritizing vulnerabilities with are using by malwares or with public exploit you can also  use CVSS calculator by adding supplemental and environmental scores  [CVSSv4 calculator](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:A/AC:H/AT:N/PR:N/UI:P/VC:N/VI:N/VA:N/SC:N/SI:N/SA:N) . Example :
        - https://www.youtube.com/watch?v=x3wAINJF7UE - How to  use CVSS 

