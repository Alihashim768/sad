import os, platform, sys

os.system('git pull')
sys.path.append('/sdcard')

bit = platform.architecture()[0]
if bit == '64bit':
    try:
        import tata
        print("Imported tata module successfully.")
    except Exception as e:
        print("Failed to import tata:", e)
