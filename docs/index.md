## Overview

[SiteWatch](https://github.com/digitalutsc/site_watch) is a command-line tool that allows for the monitoring of Islandora websites using tests specified in a CSV (or similar) file. The tool can be run manually through the command line or can be scheduled to run automatically using a cron job. Additionally, SiteWatch can be configured to send email notifications to multiple emails when a monitored website is down or when certain test cases fail. 

## Features

* Monitor Islandora websites using tests specified in a CSV file
* Run tests manually or automatically using a cron job
* Send email notifications to multiple emails when a monitored website is down or when certain test cases fail
* Intuitive, easy-to-use command-line interface
* Open source and free to use

## Usage

Within the `site_watch` directory, run the following command, providing the name of your configuration file ("config.yml" in this example):

`./site_watch config.yml`

!!! note
    If you're on Windows, you will likely need to run SiteWatch by explicitly invoking Python, e.g. `./site_watch config.yml` instead of using `./sitewatch` as illustrated above.


If your configuration file is not in the same directory as the `sitewatch` script, use its absolute path, e.g.:

`./site_watch /path/to/config.yml`

SiteWatch will run every test in the input data file referenced in the configuration file, displaying a progress bar and the results of each test as it runs.

## Contributing

Contributions to this documentation are welcome. If you have a suggestion, please open an issue on the SiteWatch [issues page](https://github.com/digitalutsc/site_watch/issues) and tag your issue "documentation".