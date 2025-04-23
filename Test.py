import os, platform, sys
import traceback

# Update Git repo (optional)
os.system('git pull')

# Path jahan .so file rakhi hai
sys.path.append('/sdcard')

# System architecture check
bit = platform.architecture()[0]
print(f"System Architecture: {bit}")

try:
    if bit == '64bit':
        import tata  # For 64-bit .so file
        print("64-bit: Imported tata module successfully.")
    elif bit == '32bit':
        import tata  # If the 32-bit .so file is also named the same
        print("32-bit: Imported tata module successfully.")
    else:
        print("Unknown system architecture.")
except Exception as e:
    print("Failed to import tata module.")
    traceback.print_exc()
