# Autonomous Network Anomaly Remediation System

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

**Autonomous Network Anomaly Remediation System** is an AI-powered tool designed to detect and automatically remediate network anomalies in real-time. Leveraging machine learning models, network automation, and a dashboard interface, this system predicts potential network anomalies based on historical data and real-time monitoring. Upon detection, it takes automated actions, like adjusting firewall rules, rerouting traffic, or alerting admins based on severity.

## Features

- **Real-Time Anomaly Detection**: Uses machine learning models to detect unusual network activity and identify threats in real-time.
- **Automated Remediation**: Executes remediation actions (firewall rule adjustment, traffic rerouting, account lockdown) based on the severity of detected anomalies.
- **Interactive Dashboard**: A Flask-based web dashboard for monitoring detected anomalies, displaying real-time data, and providing admin notifications.
- **Multi-Level Notification System**: Sends notifications (email, Slack, or SMS) to administrators based on anomaly severity.

---

## Architecture

The system consists of three primary components:

1. **Anomaly Detection Model**: A machine learning model (Isolation Forest or a custom TensorFlow model) trained on network traffic data to detect anomalies.
2. **Remediation Module**: Network automation scripts (powered by Nornir) that perform predefined remediation actions, such as firewall rule adjustments and traffic rerouting.
3. **Monitoring Dashboard**: A Flask-based interface displaying real-time data and anomaly alerts.

---

## Requirements

- **Programming Language**: Python 3.8+
- **Libraries**: 
  - `scikit-learn` or `TensorFlow` (for the anomaly detection model)
  - `Flask` (for the monitoring dashboard)
  - `Nornir` (for network automation tasks)
  - `Requests` (for handling notifications)
  - `pandas`, `numpy`, `matplotlib` (for data processing and visualization)
- **Other Tools**: 
  - `iptables` or `firewall-cmd` (for firewall rule configuration)
  - Network traffic simulator (optional: `Scapy` for testing traffic anomalies)

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/NetworkAnomalyRemediationSystem.git
    cd NetworkAnomalyRemediationSystem
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
    - Add your admin notification email or Slack webhook.
    - Configure firewall access permissions if testing with live firewall adjustments.
    - Example:
      ```bash
      export ADMIN_EMAIL="admin@example.com"
      export SLACK_WEBHOOK="https://hooks.slack.com/services/..."
      ```

---

## Usage

### 1. **Run the Anomaly Detection Model**

   Train and load the anomaly detection model with your historical network traffic data:
   ```bash
   python anomaly_detection.py --train <path/to/training_data.csv>

2. Start the Flask Dashboard
Launch the monitoring dashboard to visualize real-time anomaly detection data:
python app.py

Access the dashboard at http://localhost:5000.

3. Configure Remediation Rules
Define custom rules in the configuration file (config.yaml) to specify actions based on severity levels (low, medium, high).

Testing
Model Testing:

Use a labeled dataset with normal and anomalous data to test the model’s detection accuracy.
Run:
python anomaly_detection.py --test <path/to/test_data.csv>

Remediation Action Testing:

Test each remediation action individually using the provided functions.
Verify changes to firewall and routing configurations.
Simulate Traffic Anomalies:

Generate synthetic traffic anomalies with Scapy:
from scapy.all import *
def generate_high_traffic(src_ip, dest_ip, packet_size=1500, count=1000):
    for _ in range(count):
        send(IP(src=src_ip, dst=dest_ip)/Raw(b"X"*packet_size), verbose=0)
generate_high_traffic("192.168.1.10", "192.168.1.100")

Dashboard Testing:

Open the dashboard and ensure real-time updates appear as anomalies are simulated.
Confirm notifications are sent correctly for each severity level.

Project Structure:
NetworkAnomalyRemediationSystem/
├── README.md
├── app.py                 # Flask application for dashboard
├── anomaly_detection.py   # Anomaly detection model script
├── remediation.py         # Remediation action functions
├── config.yaml            # Configuration file for rules and notifications
├── requirements.txt       # Project dependencies
├── templates/             # HTML templates for Flask app
├── static/                # CSS/JS files for dashboard styling
└── tests/                 # Test cases and test data

Contributing
Contributions are welcome! Please follow these steps:

Fork the project.
Create a branch for your feature or bug fix (git checkout -b feature-name).
Commit your changes (git commit -m "Add feature-name").
Push to the branch (git push origin feature-name).
Open a Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
Feel free to reach out for any questions or suggestions:

Email: joseph.mtakai@outlook.com
Slack Channel: Link to Channel
--- 

This README provides a complete overview, installation guide, and instructions to get started with the **Autonomous Network Anomaly Remediation System** project.



