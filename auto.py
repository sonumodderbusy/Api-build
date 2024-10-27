import os
import time
from urllib.request import urlretrieve

important = b'Auto Setup Api '



# Prepare Node
os.system('clear')
print('Preparing Node')
time.sleep(1)

# Update system and install necessary packages
os.system('clear')
systemupdate = 'sudo apt update && sudo apt install -y python3-requests php screen apache2'
os.system(systemupdate)

# Move the API file to Apache's document root
os.system('sudo mv api.php /var/www/html')

# Allow HTTP and HTTPS traffic
os.system('sudo ufw allow Apache')
os.system('sudo ufw allow 443')

# Compile system
os.system('sudo apt install build-essential')
os.system('sudo a2enmod rewrite')
os.system('sudo service apache2 restart')

# Make sure SSH2 works
os.system('clear')
print('Making Sure SSH2 Works')
os.system('sudo apt install -y gcc make autoconf libc-dev pkg-config')
os.system('sudo apt install -y libssh2-1-dev')
os.system('sudo pecl install ssh2-1')
os.system('echo "extension=ssh2.so" | sudo tee /etc/php/8.1/cli/conf.d/20-ssh2.ini')

# Install Perl dependencies
os.system('sudo apt install -y cpanminus')
os.system('sudo cpanm Net::SSH2')
os.system('sudo cpanm Parallel::ForkManager')
os.system('sudo apt install php-ssh2')
os.system('sudo service apache2 restart')

os.system('clear')
print('Finished!')
input('Press ENTER to exit')
