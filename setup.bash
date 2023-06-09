# Update and upgrade
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Python Dependencies
pip3 install termcolor
pip3 install selenium
pip3 install rich
pip3 install ruamel.yaml
pip3 install gspread
pip3 install oauth2client

# Install Snap
sudo apt install snapd -y

# Install wget
sudo apt install wget -y

# Install Unzip
sudo apt-get install unzip -y

# Install Google Chrome
sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt -f install
sudo rm google-chrome-stable_current_amd64.deb

# Install ChromeDriver
latest_version=$(curl -sL https://chromedriver.chromium.org/downloads | grep -oP 'ChromeDriver \K([0-9]+.[0-9]+.[0-9]+.[0-9]+)' | head -n 1) # Retrieve the latest version of ChromeDriver from the website
download_url="https://chromedriver.storage.googleapis.com/$latest_version/chromedriver_linux64.zip" # Construct the download URL based on the latest version
temp_dir=$(mktemp -d) # Create a temporary directory to store the downloaded archive
sudo curl -sL "$download_url" -o "$temp_dir/chromedriver.zip" # Download ChromeDriver
sudo unzip "$temp_dir/chromedriver.zip" -d "$temp_dir" # Extract the archive
sudo mv "$temp_dir/chromedriver" /usr/local/bin/ # Move the chromedriver executable to a directory in PATH
sudo rm -rf "$temp_dir" # Clean up by removing the temporary directory

# # Install Firefox
# sudo apt-get install firefox

# # Install GeckoDriver
# latest_version=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")') # Get the latest release version from GitHub API
# download_url="https://github.com/mozilla/geckodriver/releases/download/$latest_version/geckodriver-$latest_version-linux64.tar.gz" # Set the download URL based on the latest version
# sudo curl -sL "$download_url" -o geckodriver.tar.gz # Download GeckoDriver
# sudo tar -xvzf geckodriver.tar.gz # Extract the archive
# sudo mv geckodriver /usr/local/bin/ # Move the geckodriver executable to a directory in PATH
# sudo rm geckodriver.tar.gz # Clean up by removing the downloaded archive