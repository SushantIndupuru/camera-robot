import subprocess
import time
import sys
while True:
    try:
        subprocess.run(['/opt/vc/bin/vcgencmd', 'measure_temp'])
        time.sleep(0.5)
    except:
        sys.exit()