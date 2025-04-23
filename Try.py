import os, platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    import tata
