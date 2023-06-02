# Update and upgrade
sudo apt-get update -y
sudo apt-get upgrade -y

# Install wget
sudo apt install wget -y

# Install Unzip
sudo apt-get install unzip -y

# Install Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb  # Download the latest version of Google Chrome
yes | sudo dpkg -i google-chrome-stable_current_amd64.deb  # Install Google Chrome; say yes to all prompts
sudo apt-get install -f -y  # Install dependencies
rm google-chrome-stable_current_amd64.deb  # Clean up by removing the downloaded deb file

# Install ChromeDriver
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip  # Check the latest version from https://sites.google.com/a/chromium.org/chromedriver/downloads
unzip chromedriver_linux64.zip  # Unzip the chromedriver_linux64.zip file
sudo mv chromedriver /usr/bin/chromedriver  # Move the chromedriver executable to /usr/bin/ so that it is in the PATH
sudo chown root:root /usr/bin/chromedriver  # Set the owner and group of the executable to root
sudo chmod +x /usr/bin/chromedriver  # Set the executable permission
rm chromedriver_linux64.zip  # Clean up by removing the downloaded zip file

# Install Mozilla Firefox
sudo apt-get install firefox -y

# Install GeckoDriver
latest_version=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")') # Get the latest release version from GitHub API
download_url="https://github.com/mozilla/geckodriver/releases/download/$latest_version/geckodriver-$latest_version-linux64.tar.gz" # Set the download URL based on the latest version
curl -sL "$download_url" -o geckodriver.tar.gz # Download GeckoDriver
tar -xvzf geckodriver.tar.gz # Extract the archive
sudo mv geckodriver /usr/local/bin/ # Move the GeckoDriver executable to /usr/local/bin/ so that it is in the PATH
rm geckodriver.tar.gz # Clean up by removing the downloaded archive
