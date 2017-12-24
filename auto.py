import os
import time
from time import sleep
class color:
    pink = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    cyan = '\033[36m'
    lightred = '\033[91m'


os.system("clear")


def centerr(text, width=-1):
    lines = text.split('\n')
    width = max(map(len, lines)) if width == -1 else width
    return '\n'.join(line.center(width) for line in lines)


def menu():
    print(color.lightred)
    print("*" * 30, "CONTENTS", "*" * 30)
    print()
    print("1. Install Recommended Packages")
    print("2. Secure This Server")
    print("3. Create Secure User")
    print("4. Database Selection (Redis/MySQL)")
    print(color.cyan, color.bold)
    print(" Made by T8M")
    print(color.lightred)
    print("*" * 70)
    sleep(2)
    os.system("clear")
    cachewipe()
    pass


def recommended():
    os.system("clear")
    print(color.red, "*" * 80, color.reset)
    print(color.yellow, color.bold, centerr("Recommended", 80))
    print(color.green, color.bold, "===> Downloading needed files", color.reset)
    print(color.pink, "  ---> sudo apt-get install software-properties-common python-software-properties make cmake")
    os.system("sudo apt-get -qq install software-properties-common python-software-properties -y")
    print(color.pink, "  ---> sudo add-apt-repository ppa:webupd8team/java")
    os.system("sudo add-apt-repository -qq ppa:webupd8team/java -y  > /dev/null 2>&1")
    print(color.pink, "  ---> Updating packages")
    os.system("sudo apt-get -qq update -y")
    print(color.pink, "  ---> sudo apt-get install oracle-java8-installer")
    os.system("sudo apt-get -qq install oracle-java8-installer -y")
    os.system("javac -version")
    print(color.green, color.bold, "Finished Installing Recommended Packages!")
    print(color.red, "*" * 80, color.reset)
    sleep(2)
    os.system("clear")
    cachewipe()
    pass


def secure():
    os.system("clear")
    print(color.red, "*" * 80, color.reset)
    print(color.yellow, color.bold, centerr("Secure This Server", 80))
    print(color.green, color.bold, "===> Adding a login banner (Legal Reasons)", color.reset)
    os.system("wget --quiet -O /root/.motd.banner https://gist.githubusercontent.com/Of/8d3e9b9de0a2d562522571b20ba85aa3/raw/67ec6774e609b9694e70a5248b6c06b7e0c91b45/motd.banner")
    os.system("echo 'Banner /root/.motd.banner' >> /etc/ssh/sshd_config")
    #################################################################################
    print(color.green, color.bold, "===> Removing un-needed packages", color.reset)
    print(color.pink, "  ---> apt-get --purge remove xinetd nis tftpd atftpd tftpd-hpa telnetd rsh-server rsh-redone-server")
    os.system("apt-get -qq -y --purge remove xinetd nis tftpd atftpd tftpd-hpa telnetd rsh-server rsh-redone-server")
    #################################################################################
    print(color.green, color.bold, "===> Installing security packages", color.reset)
    print(color.pink, "  ---> sudo apt-get install fail2ban")
    os.system("sudo apt-get -qq install fail2ban -y")
    print(color.pink, "  ---> sudo apt-get install auditd audispd-plugins")
    os.system("sudo apt-get -qq install auditd audispd-plugins -y")
    print(color.pink, "  ---> sudo apt-get install rssh")
    os.system("sudo apt-get -qq install rssh -y")
    ##############################################################################################
    print(color.green, color.bold, "===> Setting up Fail2Ban to block SSH BruteForce", color.reset)
    print(color.pink, "  ---> Backing up jail config")
    os.system("cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local")
    print(color.pink, "  ---> Stopping Fail2Ban")
    os.system("sudo service fail2ban stop")
    print(color.pink, "  ---> Removing Fail2Ban config")
    os.system("rm -f /etc/fail2ban/jail.conf")
    print(color.pink, "  ---> Downloading recommended Fail2Ban config")
    os.system("wget --quiet -O /etc/fail2ban/jail.conf https://gist.githubusercontent.com/Of/b3046e7661103237aa59218a1fdf591b/raw/efea812dbca0926c73842f7f7639095cf8847f3f/jail.conf")
    print(color.pink, "  ---> Starting Fail2Ban")
    os.system("sudo service fail2ban start")
    #################################################################################################################
    print(color.green, color.bold, "===> Setting up Audit Daemon", color.reset)
    print(color.pink, "  ---> Backing up Audit Rules")
    os.system("cp /etc/audit/audit.rules /etc/audit/audit.rules.old")
    print(color.pink, "  ---> Stopping the Audit Daemon")
    os.system("sudo service auditd stop")
    print(color.pink, "  ---> Removing Audit Rules")
    os.system("rm -f /etc/audit/audit.rules")
    print(color.pink, "  ---> Downloading Audit Rules")
    os.system("wget --quiet -O /etc/audit/audit.rules https://gist.githubusercontent.com/Of/5b9ad0816a6b36d1eec7cdb67a6507d3/raw/02ff17317c4755eed32e5e27f95eab28e3859351/audit.rules")
    print(color.pink, "  ---> Starting the Audit Daemon")
    os.system("sudo service auditd start")
    sleep(2)
    os.system("clear")
    cachewipe()
    pass


def users():
    os.system("clear")
    print(color.red, "*" * 80, color.reset)
    print(color.yellow, color.bold, centerr("Users", 80))
    print(color.green, color.bold, "===> Setting up required users", color.reset)
    os.system("ln -s /bin/bash /bin/rbash")
    print(color.pink, "  ---> Adding a user")
    user = str(input("Enter a username: "))
    os.system("useradd -m -d /home/" + user + " -s /bin/rbash " + user)
    print(color.pink, "  ---> Disabling all commands apart from screen and clean")
    os.system("mkdir /home/" + user + "/bin")
    os.system("ln -s /usr/bin/screen /home/" + user + "/bin/screen")
    os.system("ln -s /usr/bin/clear /home/" + user + "/bin/clear")
    os.system("echo 'PATH=$HOME/bin' >> /home/" + user + "/.bash_profile")
    os.system("echo 'PATH=$HOME/bin' >> /home/" + user + "/.bashrc")
    os.system("wget --quiet -O /home/" + user + "/.profile https://gist.githubusercontent.com/Of/383d8efdb210778114d3b8253ae5e089/raw/d0ec3ca7f19279c8988415e1d0378d6a21239f7a/.profile")
    os.system("cp -f /home/" + user + "/.profile /home/" + user + "/.bash_profile")
    os.system("sudo chown -R root:" + user + " /home/" + user + "/.bash_profile /home/" + user + "/.bashrc /home/" + user + "/.profile")
    os.system("sudo chmod 050 /home/" + user + "/.bash_profile /home/" + user + "/.bashrc /home/" + user + "/.profile")
    os.system("cat /etc/passwd | grep " + user)
    print()
    print(color.green, color.bold, "===> Secure user created!.")
    sleep(2)
    os.system("clear")
    cachewipe()
    pass


def cachewipe():
    print(color.yellow, color.bold, centerr("........CLEARING CACHE........", 80))
    print(color.yellow, color.bold, centerr("MAY LAG FOR A FEW SECONDS", 80))
    os.system("echo 3 > /proc/sys/vm/drop_caches")
    os.system("apt-get -qq clean")
    sleep(2)
    pass


start = time.time()
menu()
recommended()
secure()
users()
os.system("clear")
print(color.reset)
print("\nIt took", time.time() - start, "seconds.")
