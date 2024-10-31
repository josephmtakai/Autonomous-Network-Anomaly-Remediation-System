import subprocess
import smtplib
from email.mime.text import MIMEText

def remediate_action(severity, src_ip):
    if severity == "high":
        # Block IP in firewall
        subprocess.run(["iptables", "-A", "INPUT", "-s", src_ip, "-j", "DROP"])
        notify_admin(f"High severity anomaly detected. IP {src_ip} has been blocked.")
    elif severity == "medium":
        # Re-route traffic from this IP
        subprocess.run(["route", "add", src_ip, "gw", "alternative_gateway"])
        notify_admin(f"Medium severity anomaly: Traffic from IP {src_ip} has been re-routed.")
    elif severity == "low":
        # Just log the event
        print(f"Low severity anomaly detected for IP {src_ip}. No action taken.")
    else:
        print("Unknown severity level")

def notify_admin(message):
    sender = "alert@networksystem.com"
    recipient = "admin@yourdomain.com"
    msg = MIMEText(message)
    msg["Subject"] = "Network Anomaly Alert"
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP("smtp.yourdomain.com") as server:
        server.sendmail(sender, recipient, msg.as_string())
