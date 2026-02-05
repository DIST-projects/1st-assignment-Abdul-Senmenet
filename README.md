# Distributed Systems Assignment  
## RPC, RMI, and Peer-to-Peer File Sharing

**Student Name:** Abdullah  
**Register Number:** 2023115002  
**Course:** Cloud & Distributed Systems  
**Platform Used:** AWS EC2 (Ubuntu)

---

## Introduction

This project was done as part of the Distributed Systems coursework to understand how **remote communication** works in real-world systems.  

The assignment focuses on:
- Remote Procedure Call (RPC)
- Remote Method Invocation (RMI)
- Hosting services in a cloud environment
- Basic peer-to-peer (P2P) file sharing using torrents

All services were hosted on an **AWS EC2 cloud instance**, and clients were executed from a local machine.

---

## What This Project Demonstrates

- How a client can remotely access services from a server
- Differences between RPC and RMI
- How cloud deployment affects networking and security
- Basic idea of decentralized file sharing using BitTorrent

---

## Project Screenshots
AWS EC2 Setup:
<img width="1079" height="719" alt="Screenshot 2026-02-03 092147" src="https://github.com/user-attachments/assets/6e6fe57c-892d-4923-88b9-b624a635d24a" />
EC2 Instance details:
<img width="1079" height="719" alt="Screenshot 2026-02-03 092249" src="https://github.com/user-attachments/assets/382807fe-e46d-4287-b565-cff417733757" />
<img width="1067" height="719" alt="Screenshot 2026-02-03 092329" src="https://github.com/user-attachments/assets/4a395d5e-4ba7-4d27-b96f-8111978abb91" />


## Project Structure

```

ds_assignment/
├── rpc/
│   ├── rpc_server.py
│   └── rpc_client.py
│
├── rmi/
│   ├── Calculator.java
│   ├── CalculatorImpl.java
│   ├── RMIServer.java
│   └── RMIClient.java
│
├── torrent/
│   ├── sample_file.txt
│   ├── sample_file.torrent
│   └── screenshots/
│
└── README.md

````

---

## Cloud Setup

- **Cloud Provider:** AWS EC2 (Free Tier)
- **Operating System:** Ubuntu Server 24.04 LTS
- **Instance Type:** t2.micro
- **Region:** Europe (Stockholm)

### Security Group Configuration

The following inbound ports were enabled:

| Port | Usage |
|-----|------|
| 22 | SSH access |
| 8000 | Python RPC server |
| 1099 | Java RMI registry |
| 1100 | Java RMI remote object |

---

## Part 1: RPC Implementation (Python)

### Description
A simple RPC-based calculator service was implemented using Python’s XML-RPC library.  
The server exposes basic arithmetic operations, and the client invokes them remotely.

### How It Works
- The RPC server runs on the AWS EC2 instance.
- The client connects using the server’s public IP.
- Requests are processed remotely and results are returned to the client.

### How to Run

**On the AWS Server**
```bash
python3 rpc_server.py
````

**On the Local Client**

```bash
python rpc_client.py
```

### Sample Output

```
Addition: 15
Multiplication: 24
```

This confirms successful remote procedure execution.

---

## Part 2: RMI Implementation (Java)

### Description

A Java RMI application was developed to demonstrate remote method invocation using Java objects.

The application exposes a calculator service where methods are invoked remotely via the RMI registry.

### Components

* `Calculator.java` – Remote interface
* `CalculatorImpl.java` – Implementation of the remote object
* `RMIServer.java` – Registers the object with the RMI registry
* `RMIClient.java` – Invokes methods from the client side

### Important Configuration

* The RMI server hostname is set to the **public IP** of the AWS instance.
* A fixed port (1100) is used for the remote object to avoid firewall issues.

### How to Run

**On the AWS Server**

```bash
javac *.java
java RMIServer
```

**On the Local Client**

```bash
javac Calculator.java RMIClient.java
java RMIClient
```

### Sample Output

```
Addition: 15
Subtraction: 17
```

This confirms successful remote method invocation.

---

## Part 3: Peer-to-Peer File Sharing (Torrent)

### Description

This part demonstrates basic peer-to-peer file sharing using the BitTorrent protocol.

### Steps Performed

1. A non-copyrighted file was selected.
2. A `.torrent` file was created using qBittorrent.
3. A public tracker was configured.
4. One peer seeded the file.
5. Another peer downloaded the file.
6. File integrity was verified after download.

### Tools Used

* qBittorrent
* Public BitTorrent tracker

---

## Screenshots and Proof

The repository includes screenshots showing:

* AWS EC2 instance running
* RPC server and client output
* RMI server and client output
* Security group inbound rules
* Torrent seeding and downloading status

---

## Notes

* No cloud credentials or private keys are included.
* Only free-tier AWS resources were used.
* All cloud resources were terminated after completion.
* Non-copyrighted files were used for torrent sharing.

---

## Conclusion

This project helped in understanding how distributed systems work in practice, especially the challenges involved in cloud networking, security, and remote communication.

Both RPC and RMI were successfully implemented and tested in a real cloud environment, and peer-to-peer file sharing was demonstrated using BitTorrent.

---

## Output Screenshots
<img width="565" height="224" alt="Screenshot 2026-02-03 092452" src="https://github.com/user-attachments/assets/0c4caf6f-77f6-4024-95f3-d6dcd5a6a022" />
<img width="565" height="224" alt="Screenshot 2026-02-03 092452" src="https://github.com/user-attachments/assets/44e8a96e-3919-42a6-abe7-2df5ce85e591" />
<img width="563" height="317" alt="Screenshot 2026-02-03 092536" src="https://github.com/user-attachments/assets/8acad0a5-548c-4de6-809f-f625d4570e4a" />
<img width="508" height="79" alt="Screenshot 2026-02-03 092943" src="https://github.com/user-attachments/assets/d7891b45-2a9d-4785-b054-26dc88ee66c8" />
<img width="665" height="110" alt="Screenshot 2026-02-03 093119" src="https://github.com/user-attachments/assets/338f51cd-26f7-43a8-aecf-871927c04636" />
<img width="568" height="108" alt="Screenshot 2026-02-03 093255" src="https://github.com/user-attachments/assets/bb606f3d-e24e-464d-81ac-e4dc15e94286" />

