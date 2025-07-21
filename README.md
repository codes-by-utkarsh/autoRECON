# autoRECON
The AutoRecon tool is built for automating the reconnaissance phase in penetration testing. It collects essential information about a target by:  Enumerating open ports. Identifying services running on those ports. Conducting vulnerability scans. Conducting website reconnaissance, including subdomain discovery and vulnerability detection.

## Prerequisites

Before using autoRECON, ensure you meet the following requirements:

- You have a Linux machine.
- You have administrative privileges.
- Python 3 and Git are installed on your system.

## Installing Python 3

If Python 3 is not installed, follow these steps:

1. Update the package list:

   ```bash
   sudo apt update
   sudo apt install python3
   python3 --version
   ```
2. Install Git (if not installed):
   ```bash
   sudo apt install git
   ```

3. Clone the Repository:
    ```bash
   git clone https://github.com/codes-by-utkarsh/autoRECON.git
   ```
4. cd autoRECON
    
5. Install Dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```   
##Usage
Run the tool with:
   ```bash
   python3 autoRECON.py
   ```

Features
Port Scanning: Enumerates open ports and identifies services.
Vulnerability Scanning: Detects vulnerabilities in discovered services.
Exploit Search: Finds known exploits for identified vulnerabilities.
Website Testing: Discovers subdomains and analyzes website vulnerabilities.

License
This project is licensed under the MIT License. See the LICENSE file for details.
