# Update and upgrade
sudo apt-get update -y
sudo apt-get upgrade -y

# Install wget
sudo apt install wget -y

# Install Unzip
sudo apt-get install unzip -y

# Install Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt -f install
rm google-chrome-stable_current_amd64.deb

# Install ChromeDriver
latest_version=$(curl -sL https://chromedriver.chromium.org/downloads | grep -oP 'ChromeDriver \K([0-9]+.[0-9]+.[0-9]+.[0-9]+)' | head -n 1) # Retrieve the latest version of ChromeDriver from the website
download_url="https://chromedriver.storage.googleapis.com/$latest_version/chromedriver_linux64.zip" # Construct the download URL based on the latest version
temp_dir=$(mktemp -d) # Create a temporary directory to store the downloaded archive
curl -sL "$download_url" -o "$temp_dir/chromedriver.zip" # Download ChromeDriver
unzip "$temp_dir/chromedriver.zip" -d "$temp_dir" # Extract the archive
sudo mv "$temp_dir/chromedriver" /usr/local/bin/ # Move the chromedriver executable to a directory in PATH
rm -rf "$temp_dir" # Clean up by removing the temporary directory