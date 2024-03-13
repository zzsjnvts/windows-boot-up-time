from datetime import datetime

def get_boot_time():
    boot_time_str = "13/03/2024 7:37:01 pm"
    boot_time = datetime.strptime(boot_time_str, "%d/%m/%Y %I:%M:%S %p")
    return boot_time

def main():
    boot_time = get_boot_time()
    current_time = datetime.now()
    time_difference = (current_time - boot_time).total_seconds() / 60
    if time_difference <= 10:
        time_remaining = 10 - time_difference
        print("Error: Boot-up time less than 10 minutes ago.")
        print("Time remaining until success: {:.2f} minutes".format(time_remaining))
    else:
        print("Success: Boot-up time more than 10 minutes ago.")

if __name__ == "__main__":
    main()
