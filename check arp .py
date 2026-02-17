import subprocess

def get_connected_devices():
    result = subprocess.check_output("arp -a", shell=True)
    try:
        result = result.decode("utf-8")
    except UnicodeDecodeError:
        result = result.decode("cp866")  # fallback для Windows
    devices = [line for line in result.splitlines() if "динамический" in line.lower()]
    for d in devices:
        print(d)

get_connected_devices()
