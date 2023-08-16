## Requirements

* Python 3.7 or higher
* The latest Google Chrome and Chromedriver installed to the PATH (see [Installing Chrome and Chromedriver on Linux](#installing-chrome-and-chromedriver) or visit the Google Chrome and Chromedriver websites for instructions on installing these on other operating systems)
* The following Python libraries:
    * [ruamel.yaml](https://yaml.readthedocs.io/en/latest/index.html)
    * [Requests](https://2.python-requests.org/en/master/)
    * [openpyxl](https://pypi.org/project/openpyxl/)
    * [rich](https://pypi.org/project/rich/)
    * [selenium](https://pypi.org/project/selenium/)
    * [colorama](https://pypi.org/project/colorama/)
    * If you want to have these libraries automatically installed, you will need Python's [setuptools](https://pypi.org/project/setuptools/)
* Highly recommended: A Linux-based operating system (e.g. Ubuntu, Debian, Fedora, etc.)

## Installing SiteWatch

Installation involves three steps:

1. cloning the SiteWatch Github repo
2. running `setup.py` to install the required Python libraries (listed above)

### Step 1: Cloning the SiteWatch Repo

In a terminal, run:

`git clone https://github.com/digitalutsc/site_watch.git`

This will create a directory named `site_watch` where you will run the `./sitewatch` command. Change into this directory:
```bash
cd site_watch
```
and run the following command to make the `./sitewatch` and `./setupwizard` commands executable:
```bash
chmod +x sitewatch setupwizard
```

### Step 2: Running setup.py to Install the Required Python Libraries

For most users, the preferred place to install Python libraries is in the user directory. To do this, change into the "site_watch" directory created by cloning the repo, and run the following command:

`python3 setup.py install --user`

A less common mehtod is to install the required Python libraries into your computer's central Python environment. To do this, omit the `--user` (note: you must have administrator privileges on the computer to do this):

`sudo python3 setup.py install`

## Updating SiteWatch

Since SiteWatch is under development, you will want to update it often. To do this, within the `site_watch` directory, run the following `git` command:

`git pull origin main`

After you pull in the latest changes using `git`, it's a good idea to rerun the setup tools in case new Python libraries have been added since you last ran the setup tools (same command as above):

`python3 setup.py install --user`

or if you originally installed the required Python libraries centrally, without the `--user` option (again, you will need administrator privileges on the machine):

`sudo python3 setup.py install`

## Installing Google Chrome and Chromedriver on Linux

SiteWatch uses Google Chrome and Chromedriver to run tests. You will need to install both of these on the machine where you will be running SiteWatch. 


To install them, run the following in a terminal:

```bash
sudo apt-get update -y
sudo apt-get install unzip -y
sudo apt-get install curl -y
sudo apt install wget -y

latest_version=$(curl -sL https://chromedriver.chromium.org/downloads | grep -oP 'ChromeDriver \K([0-9]+.[0-9]+.[0-9]+.[0-9]+)' | head -n 1)

chromedriver_download_url="https://chromedriver.storage.googleapis.com/$latest_version/chromedriver_linux64.zip"
temp_dir=$(mktemp -d)
sudo curl -sL "$download_url" -o "$temp_dir/chromedriver.zip"
sudo unzip "$temp_dir/chromedriver.zip" -d "$temp_dir"
sudo mv "$temp_dir/chromedriver" /usr/local/bin/
sudo rm -rf "$temp_dir"

chrome_download_url=https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_"$latest_version"-1_amd64.deb
sudo wget $chrome_download_url
sudo dpkg -i google-chrome-stable_"$latest_version"-1_amd64.deb
sudo apt -f install
sudo rm google-chrome-stable_"$latest_version"-1_amd64.deb
```

!!! warning
    The script above downloads up to v114 of Google Chrome. Later versions require Chrome for Testing. Please see the following links:
    1. Chrome Testing Dashboard: https://googlechromelabs.github.io/chrome-for-testing/
    2. Chrome for Testing: reliable downloads for browser automation https://developer.chrome.com/blog/chrome-for-testing/#versioned-browser-binaries

!!! note
    You need not install the latest version of Google Chrome. To select a specific version of Google Chrome and Chromedriver, please refer to the following links
    1. All Versions of Chrome: https://chromedriver.storage.googleapis.com/index.html
    2. All Versions of Chromedriver: https://chromedriver.chromium.org/downloads