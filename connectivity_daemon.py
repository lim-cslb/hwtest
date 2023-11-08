import time
import subprocess

def check_internet_connection():
    try:
        subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == '__main__':
    while True:
        f = open("/tmp/led5", "w")
        if check_internet_connection():
            f.write("%s" % "00FF00")
        else:
            f.write("%s" % "FF0000")
        f.close()
        time.sleep(15)
