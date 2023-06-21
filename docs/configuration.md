# Configuration

## The Setup Wizard
Instead of creating your own configuration file, you can use the setup wizard to create one for you. To run the setup wizard, run the following command:
```bash
$ ./setupwizard
```
The setup wizard will ask you a series of questions, and then create a configuration file for you. You can then edit the configuration file to add any additional settings you need.


## The Configuration File

SiteWatch gets its first input from a configuration file whose path is passed to it as a command line argument. This file is a YAML file, and can be named anything you like, but it must have a `.yml` extension. For example, if your configuration file is named `my_config.yml`, you would run SiteWatch like this:
```bash
$ ./sitewatch my_config.yml
```
The configuration file contains all the information SiteWatch needs to run. It contains the location of the CSV-like file containing the tests that SiteWatch is to run, the email addresses of the people who are to receive the test results, and other information. For example, one of the the simplist configuration files might look like this:
```yaml
csv: /path/to/test/csv
```

## Required Configuration Settings

### Input Source

**Exactly one** of the following settings must be present in the configuration file to tell SiteWatch where to find the tests to run:
* `csv`: A path to a CSV file containing the tests to run.
* `excel`: A path to an Excel file containing the tests to run.
* `google_sheets`: A URL to a Google Sheets file containing the tests to run.

### Minimum Age of Output Files to Delete
SiteWatch produces output `.log` and `.csv` files (see [Output](./output.md)) for each test it runs. These files are stored in the `output` directory. By default, SiteWatch will delete these files if they are older than 30 days. To change this, add the following to your configuration file:
```yaml
delete_stale_files_after: <number of days>
```

## Optional Configuration Settings

### Email Settings

SiteWatch can send email notifications to one or more recipients when it finishes running. To enable this feature, the configuration file must include the following
```yaml
email:
  sender_name: <The name to appear on the emails>
  sender_email: <The email address to send from; must be an email this machine can send from>
  recipient_emails: 
    - <email address 1>
    - <email address 2>
```