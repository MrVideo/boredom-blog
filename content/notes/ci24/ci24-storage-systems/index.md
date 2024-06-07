---
title: 'Storage systems'
date: 2024-06-06T10:30:00+02:00
draft: false
type: 'page'
toc: true
---

---

## Download as PDF

You can download this note as a PDF by clicking [here](storage-systems.pdf).

---

There are three main types of storage solutions for data centres:

- **Direct Attached Storage** (DAS): a storage system that is directly attached to a server or workstation. The operating system sees the disks in the DAS as disks attached to the system.
- **Network Attached Storage** (NAS): a computer connected to a network that provides file-based data storage services, such as FTP, NFS ans SAMBA, to other devices on the network. The operating system of a server or workstation sees a NAS as a file server.
- **Storage Area Network** (SAN): a remote storage unit that is connected to a server using specific networking technology and is visible as disks directly attached to the server by its OS.

![](images/Pasted%20image%2020240606100727.png)

## Direct Attached Storage (DAS)

A Direct Attached Storage is a storage system that is directly attached to a server or workstation. The term is used to differentiate non-networked storage from other storage systems, like NAS or SAN.

![](images/Pasted%20image%2020240606102945.png)

When speaking of Direct Attached Storage, we don’t necessarily mean internal drives inside a server or workstation: all external disks connected with a point-to-point protocol to a PC can be considered DAS.

Direct Attached Storage has some problems:

- It scalability is limited
- It management can be complex
- In order to read files on other machines, the OS’s file sharing protocol must be enabled

## Network Attached Storage (NAS)

A Network Attached Storage unit is a computer connected to a network that provides only file-based data storage services to other devices on the network. NAS systems contain one or more hard disks, often organised in a RAID configuration, and provide file-access services to the hosts connected to it via a TCP/IP network through different protocols, like FTP, NFS or SAMBA.

![](images/Pasted%20image%2020240606103034.png)

Each NAS unit has its own IP address on the network, which makes scalability more flexible: in order to increase storage capacity, one could either add disks to a single NAS or add another NAS entirely.

The key difference between a NAS and a DAS unit is that while a DAS is simply an extension of an existing server, a NAS is designed as a self-contained solution for sharing files over the network.

One key issue with NAS systems is that the performance of a NAS mainly depends on the speed and congestion of the network the system is in.

## Storage Area Network (SAN)

Storage Area Networks are remote storage units that are connected to a server or workstation using a specific networking technology, like fibre optics.

SANs usually employ a special network to access their storage devices. This means that while the SANs communicate via TCP/IP with other devices, they use a dedicated network just to read and write data. This provides great scalability, since to increase storage capacity it’s sufficient to increase the number of disks attached to the SAN.

![](images/Pasted%20image%2020240606103106.png)

The main difference between NAS and SAN is that, while a NAS also provides a file system, disks available through SAN appear as normal, directly attached disks to its users.

Traditionally, NAS systems are used for low-volume access to a large amount of storage by many users, while SAN system are a solution for petabytes of storage and multiple, simultaneous access to files, such audio and video streaming.

## Summing up

Below is a table condensing the main information about the three storage solutions seen above.

| Storage solution | Application domain                                               | Advantages                                                                      | Disadvantages                                                                |
| ---------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| DAS              | When a simple and cost-effective solution is required            | Easy setup, low cost, high performance                                          | Limited accessibility, limited scalability, no central management and backup |
| NAS              | When it is necessary to store and share a large quantity of data | Scalable, very accessible, good performance on a fast network                   | Increased LAN traffic, transfer speeds are limited by the network            |
| SAN              | Mainly used for virtualised environments and DBMSs               | Very good performance, great scalability, improved availability compared to NAS | High costs, complex setup and maintenance                                    | 
