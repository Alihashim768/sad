import os, platform, sys
import traceback

os.system('git pull')
sys.path.append('/sdcard')

bit = platform.architecture()[0]
print(f"System Architecture: {bit}")

if bit == '64bit':
    try:
        import tata
        print("Imported tata module successfully.")
    except Exception as e:
        print("Failed to import tata module.")
        traceback.print_exc()
