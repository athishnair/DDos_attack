🔐 IoT Security System with Traffic Simulation & ID Verification
This project is an IoT-based cybersecurity simulation using an ESP32 microcontroller. It includes real-time DDoS attack simulation, ID verification, and adaptive response logic using Python and Arduino.

📁 Project Structure
Attack_Simulations.py: Python script to simulate normal, moderate, DDoS, and gradual network traffic against the ESP32 device.

verified_id.ino: Arduino sketch that verifies trusted IDs and responds accordingly.

unverified_id.ino: Arduino sketch that handles unknown/unverified IDs, triggering alerts or restrictive measures.

🚀 How to Use
1. Set Up Your ESP32
Flash either verified_id.ino or unverified_id.ino to your ESP32 using the Arduino IDE.

verified_id.ino: Accepts and logs verified IDs (e.g., from RFID or keypad input).

unverified_id.ino: Responds to unauthorized access attempts (could trigger buzzer, LED, etc.).

Connect your ESP32 to the same network as your PC (or in AP mode with IP 192.168.4.x).

2. Install Python Requirements
Make sure you have requests installed for the simulation script:

bash
Copy
Edit
pip install requests
3. Run Attack Simulations
Use the terminal to run simulated traffic patterns to the ESP32:

bash
Copy
Edit
python Attack_Simulations.py --ip 192.168.4.110 --type ddos --duration 120 --delay 0.05
Available Traffic Modes:

normal: Light traffic with minimal errors

moderate: Medium traffic with some errors

ddos: High traffic, high error rate (simulating attack)

gradual: Escalates from normal to DDoS over time

You can stop it anytime using Ctrl+C.

⚙️ Hardware Used
ESP32 Dev Board

Sensors (optional): RFID, Keypad, LED, Buzzer

USB cable, Wi-Fi network

✅ Applications
IoT device security simulation

Cybersecurity training and analysis

Load testing and fault tolerance for embedded web servers
