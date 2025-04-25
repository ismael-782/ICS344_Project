# ICS344_Project

## Team

| Name           | ID        |
|----------------|-----------|
| Ismael Arqsosi | 202182150 |
| Taha Ali       | 202045620 |
| Saad Alharbi   | 201935590 |


# Phase 1: Exploitation

In this phase, we set up the attacker (Kali Linux) and victim (Metasploitable3) environments and conducted a successful attack using Metasploit, as well as a custom brute-force Python script.

### Tasks Performed
- Built Metasploitable3 VM with vulnerable services
- Configured Kali Linux as attacker
- Scanned target with Nmap to detect SMB port (445)
- Used EternalBlue exploit via Metasploit to gain access
- Wrote custom Python script using `smbclient` to brute-force SMB login

### Key Exploit Used
- `ms17_010_eternalblue`
- Target: SMB port 445 on Metasploitable3

### Successful Access Info
- Gained Meterpreter session via Metasploit
- Discovered working credentials: `administrator:vagrant`

### Evidence Screenshots
- `nmap_smb_scan.png`
- `smb_exploit_session.png`
- `smb_script_result.png`
- `smb_script_code.png`

### Files Included
- `smb_brute.py`

# Phase 2: SIEM Log Analysis (Splunk)

In this phase, logs were collected from the victim machine and imported into Splunk for analysis. Dashboards were created to visualize attacker activity.

### SIEM Used
- Splunk Enterprise (installed on Windows host)

### Logs Collected
- `security.evtx`
- `system.evtx`

### Analysis Performed
- Searched login-related Event IDs (4624, 4625)
- Searched system service logs (7036)
- Created dashboards for visualizing login activity and system events

### Screenshots Captured
- `splunk_login.png`
- `event_viewer.png`
- `add_data.png`
- `system_add_data.png`
- `search_results.png`
- `system_event_results.png`
- `dashboard_final.png`

### Note
Due to internal issues with Kali Linux, logs from the attacker machine could not be collected.


# Phase 3: Defense and Remediation

In this final phase, cleanup and hardening steps were performed on the victim machine (Metasploitable3) to remove traces of the attack and prevent future compromise.

### Trace Removal
- Checked open ports with `netstat`


### System Hardening
- Enabled Windows Firewall
- Enforced password complexity policy
- Disabled SMBv1 protocol using CMD

### Simulated Pre-Defense State
- Because the attack session was closed before screenshots were taken, a simulation was conducted to reproduce the vulnerable state

### we included a sub-folder called SCREENSHOTS containing all the screenshots and evidences required 
