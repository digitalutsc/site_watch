# Output In SiteWatch
Sitewatch has the capability to convey the results of its tests in a variety of ways:
* To the console (stdout)
* To a log file
* To a CSV file
* To email addresses

The first three of these are by default enabled, and the last is up to the user to enable. The following sections describe each of these in detail.

## Console Output
SiteWatch provides a nice, human-readable summary of its results to the console. Here is an example of what that looks like:
```text
   _________.__  __         __      __         __         .__     
 /   _____/|__|/  |_  ____/  \    /  \_____ _/  |_  ____ |  |__  
 \_____  \ |  \   __\/ __ \   \/\/   /\__  \\   __\/ ___\|  |  \ 
 /        \|  ||  | \  ___/\        /  / __ \|  | \  \___|   Y  \
/_______  /|__||__|  \___  >\__/\  /  (____  /__|  \___  >___|  /
        \/               \/      \/        \/          \/     \/  
 SiteWatch has started.
 The output CSV will be written to output_csvs/site_watch-2023-06-14-13-02-23.csv
 The log file will be written to logs/site_watch-2023-06-14-13-02-23.log
Verifying CSV File... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
 CSV file is valid.
 Site Availability Test passed on row 2.
 Facet Load Test passed on row 3.
 Collection Count Test passed on row 4.
 OpenSeaDragon Load Test passed on row 5.
 Mirador Load Test passed on row 6.
 AblePlayer Transcript Load Test passed on row 7.
 Mirador Load Test passed on row 8.
 Mirador Page Count Test failed on row 9. Please see log for more details.
Running Tests... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:17
 All tests have finished running.
 Results have been written to output_csvs/site_watch-2023-06-14-13-02-23.csv
 ```

## Log File
SiteWatch writes a log file to the `logs` directory. The name of the file is time-stamped to be unique. The name of the log file is the same as the name of the output CSV file (see below), but with a `.log` extension. For example, if the output CSV file is named `site_watch-2023-06-14-13-02-23.csv`, the log file will be named `site_watch-2023-06-14-13-02-23.log`. The log file serves to report important information about the results of tests and, if they failed, why they failed. Here is an example of what the log file for the above console output might look like:
```text
INFO:root:SiteWatch has started.
INFO:utils.csv_utils:CSV file is valid.
INFO:test_suites.test_controller:Site Availability Test passed on row 2.
INFO:test_suites.test_controller:Facet Load Test passed on row 3.
INFO:test_suites.test_controller:Collection Count Test passed on row 4.
INFO:test_suites.test_controller:OpenSeaDragon Load Test passed on row 5.
INFO:test_suites.test_controller:Mirador Load Test passed on row 6.
INFO:test_suites.test_controller:AblePlayer Transcript Load Test passed on row 7.
INFO:test_suites.test_controller:Mirador Load Test passed on row 8.
ERROR:test_suites.test_controller:Mirador Page Count Test failed on row 9. Mirador viewer does not have the expected number of thumbnails. Expected 1032, got 1034.
INFO:root:All tests have finished running.
INFO:root:Results have been written to output_csvs/site_watch-2023-06-14-13-02-23.csv
```

## Output CSV
SiteWatch writes a CSV file to the `output_csvs` directory. The name of the file is time-stamped to be unique. The name of the output CSV file is the same as the name of the log file (see above), but with a `.csv` extension. For example, if the log file is named `site_watch-2023-06-14-13-02-23.log`, the output CSV file will be named `site_watch-2023-06-14-13-02-23.csv`. The output CSV is a copy of the input test data file, but with two columns appended: 
* `test_result`: The result of the test. This will be either `Passed` or `Failed`.
* `total_time`: The total time it took to run the test, in seconds.
For example, if the original input data file looked like
```text
url,test_type,description,test_input
https://memory.digital.utsc.utoronto.ca/collection/33463,facet_load_test,test_subject_fact_exists,subject
```
the output CSV file would look like
```text
url,test_type,description,test_input,test_result,total_time
https://memory.digital.utsc.utoronto.ca/collection/33463,facet_load_test,test_subject_fact_exists,subject,Passed,0.39168238639831543
```

## Email
SiteWatch has the capability to send an email to one or more email addresses when it finishes running, only in the event of error or failed test case. This is useful for notifying people when a test has failed. The email sent will contain a copy of the log and output CSV files. To enable this feature, see [Email Settings](configuration.md#email-settings).

