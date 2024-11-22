import subprocess
import json
import networkx as nx
import matplotlib.pyplot as plt

def run_nmap(target):
    print(f"Running Nmap on {target} for service enumeration")
    scan_command = f"sudo nmap -sV -p 1-1024 {target}"
    result = subprocess.run(scan_command, shell=True, capture_output=True, text=True)
    return parse_nmap_output(result.stdout)

def parse_nmap_output(output):
    hosts = {}
    lines = output.splitlines()
    current_host = None

    for line in lines:
        if 'Nmap scan report for' in line:
            current_host = line.split()[-1]
            hosts[current_host] = {}
        elif '/tcp' in line:
            parts = line.split()
            port = parts[0].split('/')[0]
            state = parts[1]
            service = parts[2] if len(parts) > 2 else 'unknown'
            if current_host:
                if 'tcp' not in hosts[current_host]:
                    hosts[current_host]['tcp'] = {}
                hosts[current_host]['tcp'][int(port)] = {'state': state, 'name': service}
    return hosts

def run_vuln_scan(target):
    print(f"Running Vulnerability Scan on {target}")
    vuln_scan_command = f"sudo nmap --script vuln {target}"
    subprocess.run(vuln_scan_command, shell=True)

def detect_services(host_data):
    services = []
    for proto, ports in host_data.items():
        for port, info in ports.items():
            if info['state'] == 'open':
                services.append((port, info.get('name', 'unknown')))
    return services

def search_exploits(port, service, version):
    print(f"Searching for exploits for {service} on port {port} with version {version}")
    search_command = f"searchsploit {service} {version}"
    result = subprocess.run(search_command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        exploits = result.stdout.splitlines()
        return exploits
    else:
        print("Error occurred while searching for exploits.")
        return []

def generate_json_report(target, hosts_data):
    report = {"target": target, "hosts": []}

    for host, host_data in hosts_data.items():
        services = detect_services(host_data)
        host_report = {
            "host": host,
            "services": []
        }
        for port, service in services:
            version = "unknown" 
            host_report["services"].append({
                "port": f"{port}/tcp",
                "service": service,
                "vulnerabilities": search_exploits(port, service, version) 
            })
        report["hosts"].append(host_report)

    with open("network_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("\nReport saved as 'network_report.json'.")

def create_attack_graph(hosts_data):
    G = nx.Graph()
    for host, host_data in hosts_data.items():
        services = detect_services(host_data)
        for port, service in services:
            G.add_node(service, label=service)
            G.add_edge(service, "vulnerabilities")

    nx.draw(G, with_labels=True, font_size=8, node_size=2000, node_color='lightblue', font_weight='bold', edge_color='gray')
    plt.title("Network Attack Graph")
    plt.show()

def main():
    target = input("Enter target IP address: ")
    hosts_data = run_nmap(target)

    if not hosts_data:
        print("No hosts found.")
        return

    print("Open ports and services:")
    for host, data in hosts_data.items():
        print(f"Host: {host}")
        for proto, ports in data.items():
            for port, info in ports.items():
                print(f"  Port {port}: {info['state']} - {info.get('name', 'unknown')}")

    run_vuln_scan(target) 
    generate_json_report(target, hosts_data)
    create_attack_graph(hosts_data)

if __name__ == "__main__":
    main()
