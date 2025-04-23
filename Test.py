import os, platform, sys

# Git pull (assuming this script is inside a git repo)
os.system('git pull')

# Add path where the .so file exists
sys.path.append('/sdcard')  # Change if the file is in a subfolder

# Check system architecture and import accordingly
bit = platform.architecture()[0]
if bit == '64bit':
    import tata
