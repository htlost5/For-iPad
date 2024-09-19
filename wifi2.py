import subprocess

def get_wifi_passwords():
    command = "nmcli -t -f active,ssid dev wifi"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("Available SSIDs:", result.stdout)  # デバッグ用出力
    
    ssids = [line.split(':')[1] for line in result.stdout.splitlines() if line.startswith('yes')]
    
    passwords = {}
    for ssid in ssids:
        command = f"nmcli -s -g 802-11-wireless-security.psk connection show {ssid}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(f"Password for {ssid}:", result.stdout.strip())  # デバッグ用出力
        
        passwords[ssid] = result.stdout.strip()
    
    return passwords

print(get_wifi_passwords())