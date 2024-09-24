import subprocess

def get_wifi_passwords():
    # Run the command to list all saved WiFi networks
    command = "nmcli -t -f active,ssid dev wifi"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Parse the output to get SSIDs of connected networks
    ssids = [line.split(':')[1] for line in result.stdout.splitlines() if line.startswith('yes')]
    
    passwords = {}
    for ssid in ssids:
        # Run the command to get the password for each SSID
        command = f"nmcli -s -g 802-11-wireless-security.psk connection show {ssid}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # Store the password in a dictionary
        passwords[ssid] = result.stdout.strip()
    
    return passwords

print(get_wifi_passwords())