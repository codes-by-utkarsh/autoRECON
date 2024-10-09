import subprocess

def display_banner():
    banner = """
    \033[1;36m
============================================================================
    ---------------------AUTO RECONNAISSANCE---------------------------
============================================================================

============================================================================
    \033[1;97m
    """
    print(banner)
def run_nmap(target):
    print(f"Running Nmap on {target} for service enumeration")
    scan_command = f"sudo nmap -sV -p- {target}"  
    subprocess.run(scan_command, shell=True)

def run_vuln_scan(target):
    print(f"Running Vulnerability Scan on {target}")
    vuln_scan_command = f"sudo nmap --script vuln {target}" 
    subprocess.run(vuln_scan_command, shell=True)

def run_dnsenum(target):
    print(f"Running DNS Enumeration on {target}")
    dnsenum_command = f"sudo dnsenum {target}"
    try:
        result = subprocess.run(dnsenum_command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"DNS Enumeration failed for {target}. Domain doesn't Exist")

def find_subdomains(domain):
    print(f"Running Subdomain Enumeration on {domain}")
    sublist3r_command = f"sublist3r -d {domain}"
    subprocess.run(sublist3r_command, shell=True)

def run_nikto(target):
    print(f"Running Nikto for web vulnerability scanning on {target}")
    nikto_command = f"nikto -h {target}"
    subprocess.run(nikto_command, shell=True)

def scan_ip(target):
    run_nmap(target)
    run_vuln_scan(target)

def scan_website(target):
    find_subdomains(target)
    run_nikto(target)
    run_dnsenum(target)

def main():
    display_banner()
    print("Choose your target type:")
    print("1. IP Address Scan")
    print("2. Website Scanning")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        target = input("Enter the target IP address: ")
        scan_ip(target)
    elif choice == '2':
        target = input("Enter the target website domain: ")
        scan_website(target) 
    else:
        print("Invalid choice. Please choose either 1 or 2.")

if __name__ == "__main__":
    main()
