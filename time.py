import re
import subprocess
from datetime import datetime, timedelta

def get_kernel_event():
    powershell_cmd = 'Get-WinEvent -ProviderName Microsoft-Windows-Kernel-General | Where-Object {$_.Id -eq 12} | Select-Object -First 1 | Format-Table -Property TimeCreated -AutoSize'
    result = subprocess.run(['powershell', '-Command', powershell_cmd], capture_output=True, text=True)
    return result.stdout.strip()

def extract_datetime(output_string):
    pattern = r'(\d{2}/\d{2}/\d{4} \d{1,2}:\d{2}:\d{2} [ap]m)'
    match = re.search(pattern, output_string)
    if match:
        return match.group(0)
    else:
        return None

def calculate_time_difference(datetime_str):
    event_time = datetime.strptime(datetime_str, '%d/%m/%Y %I:%M:%S %p')
    current_time = datetime.now()
    time_difference = (current_time - event_time).total_seconds() / 60
    return time_difference

if __name__ == "__main__":
    output_string = get_kernel_event()
    datetime_str = extract_datetime(output_string)
    if datetime_str:
        difference_in_minutes = calculate_time_difference(datetime_str)
        if difference_in_minutes > 10:
            print("Success")
        else:
            print("Error")
            minutes_remaining = 10 - difference_in_minutes
            print(f"Minutes remaining before 10 minutes: {minutes_remaining:.2f} minutes")
    else:
        print("Failed to extract datetime from output.")
