import time
import pyfiglet

def figlet_date(format = "%Y %d %b, %A", font = "graceful"):
    return pyfiglet.figlet_format(time.strftime(format), font=font)