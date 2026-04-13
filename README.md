# Network Scanning Automation

##  Project Description

This project automates basic network scanning tools using Python. It includes:

* **Ping Scanner** – Checks host availability and response time
* **ARP Scanner** – Displays IP-MAC address mappings
* **Nmap Scanner** – Performs network scans like port scanning and host discovery


##  Requirements

* Python 3.6 or higher
* Nmap installed


##  Installation

### Install Python

```bash
python --version
```

### Install Nmap

Download from: https://nmap.org/download.html

Verify:

```bash
nmap -v
```


Enter choice: 2
## Project Structure 

network-scanning-tools/
│
├── ping_scanner.py
├── arp_scanner.py
├── nmap_scanner.py
│
├── arp_results.txt
├── nmap_results.txt
│
├── screenshots/
│   ├── ping_output 1.jpeg
│   ├── ping_output 2.jpeg
│   ├── arp_output.jpeg
│   ├── nmap_output 1.jpeg
│   ├── nmap_output 2.jpeg
│   ├── nmap_output 3.jpeg
│
└── README.md


##  How to Run

### Ping Scanner

```bash
python ping_scanner.py
```

### ARP Scanner

```bash
python arp_scanner.py
```

### Nmap Scanner

```bash
python nmap_scanner.py
```


##  Example Usage

### Ping Scanner

Single Host:

```
Ping multiple hosts? n
Enter hostname or IP: google.com
```

Multiple Hosts:

```
Ping multiple hosts? y
Enter hosts: google.com, 8.8.8.8, 127.0.0.1
```


### ARP Scanner

```
python arp_scanner.py
Save results to file? y
```


### Nmap Scanner

Port Scan:

```
Enter target IP: 127.0.0.1
Enter choice: 2
```


##  Output Files

Screenshots included:

* ping_output 1.jpeg
* ping_output 2.jpeg
* arp_output.jpeg
* nmap_output 1.jpeg
* nmap_output 2.jpeg
* nmap_output 3.jpeg

Text outputs:

* arp_results.txt
* nmap_results.txt


##  Features

### Ping Scanner

* Single and multiple host scanning
* Response time extraction
* Cross-platform support

### ARP Scanner

* ARP table retrieval
* IP-MAC parsing
* Formatted display
* Save results to file

### Nmap Scanner

* Nmap installation check
* Host discovery
* Port scanning
* Multiple scan types
* Save results to file


##  Security Note

Only scan networks you own or have permission to scan. Unauthorized scanning is illegal.


## Author

Darshan S


##  Conclusion

This project demonstrates automation of network scanning tools using Python and provides practical exposure to cybersecurity concepts.
