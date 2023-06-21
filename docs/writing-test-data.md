# The Test File
SiteWatch gets its second input from a CSV-like file containing the tests that SiteWatch is to run. This file specifies the URLs to test, the type of test to be run, expected values, and other information. For example, a test file might look like this:
```csv
url,test_type,input_data
https://memory.digital.utsc.utoronto.ca/collection/33463,collection_count_test,23591
https://memory.digital.utsc.utoronto.ca/,site availability test,
```

## Required Test File Columns
While the test file can contain any number of columns (for example, a description column), it must contain the following columns:
* `url`: The URL to test.
* `test_type`: The type of test to run. See [Test Types](#test-types) below for a list of valid test types.
* `input_data`: For some test types, this column is required, and is used to provide more information about the tests. The format of this column depends on the test type. See [Test Types](#test-types) below for more information.

## Test Types
SiteWatch supports the following test types:

### `site_availability_test`:
This test type checks to see if the site is available. It does not require any input data. It performs a `GET` request to the URL, and checks to see if the response code is indicative of a successful request (i.e., a 2xx response code). Then, it double-checks by scanning the response body for a string that indicates the site is not available. Then, it triple-checks by actually visiting the site in a browser and checking to see if it is available. If any of these checks fail, the test fails. Here is a sample test row for this test type:
```csv
url,test_type,input_data
https://memory.digital.utsc.utoronto.ca/,site_availability_test,
```
As you can see, the `input_data` column is empty, as this test type does not require any input data.

### `facet_load_test`:
This test type checks to see if a specific facet loads on a collection page. It requires the facet name to be passed as input. The supported facets are

* Subject
* Genre
* Publication Date
* Related Archival Fonts

The test will then visit the page in a browser and check to see if the facet loads. Here is a sample test row for this test type that checks to see if the "Subject" facet loads on the page.
```csv
url,test_type,input_data
https://memory.digital.utsc.utoronto.ca/collection/33463,facet_load_test,Subject
```
By default, the test will check to see if the facet loads within 20 seconds.


### `collection_count_test`:
This test type checks to see if the number of items in a collection matches the expected number of items. It requires the expected number of items to be passed as input. The test will then visit the collection page in a browser and check to see if the number of items matches the expected number of items. Here is a sample test row for this test type that checks to see if the collection has 23,591 items.
```csv
url,test_type,input_data
https://memory.digital.utsc.utoronto.ca/collection/33463,collection_count_test,23591
```
By default, the test will check to see if the collection count matches the expected count within 20 seconds.

### `openseadragon_load_test`:
This test type checks to see if the OpenSeadragon viewer loads on an item page. It does not require any input data. The test will then visit the item page in a browser and check to see if the OpenSeadragon viewer loads. Here is a sample test row for this test type:
```csv
url,test_type,input_data
https://memory.digital.utsc.utoronto.ca/61220/utsc16185,openseadragon_load_test,
```
By default, the test will check to see if the OpenSeadragon viewer loads within 20 seconds.

### `mirador_viewer_load_test`:
This test type checks to see if the Mirador viewer loads on an item page. It does not require any input data. The test will then visit the item page in a browser and check to see if the Mirador viewer loads. Here is a sample test row for this test type:
```csv
url,test_type,input_data
https://memory.digital.utsc.utoronto.ca/61220/utsc11802,mirador_viewer_load_test,4
```
By default, the test will check to see if the Mirador viewer loads within 40 seconds.

### `mirador_page_count_test`:
This test type checks to see if the number of pages in a Mirador viewer matches the expected number of pages. It requires the expected number of pages to be passed as input. The test will then visit the item page in a browser and check to see if the number of pages matches the expected number of pages. Here is a sample test row for this test type that checks to see if the Mirador viewer has 1034 pages.
```csv
url,test_type,input_data
https://tamil.digital.utsc.utoronto.ca/61220/utsc34439,mirador_page_count_test,1034
```
By default, the test will check to see if the Mirador viewer has the expected number of pages within 40 seconds.

### `ableplayer_load_test`:
This test type checks to see if the AblePlayer viewer loads on an item page. It does not require any input data. The test will then visit the item page in a browser and check to see if the AblePlayer viewer loads. Here is a sample test row for this test type:
```csv
https://tamil.digital.utsc.utoronto.ca/61220/utsc34400,ableplayer_load_test,
```
By default, the test will check to see if the AblePlayer viewer loads within 20 seconds.

### `ableplayer_transcript_load_test`:
This test type checks to see if the AblePlayer transcript loads on an item page. It does not require any input data. The test will then visit the item page in a browser and check to see if the AblePlayer transcript loads. Here is a sample test row for this test type:
```csv
https://tamil.digital.utsc.utoronto.ca/61220/utsc34400,ableplayer_transcript_load_test,
```
By default, the test will check to see if the AblePlayer transcript loads within 20 seconds.

### `element_present_test`:
This test takes allows the checking of the presence of any element on a page. It requires two inputs: the method to search by, and the search term. The method can be one of the following:
* `id`: Search by element ID.
* `class`: Search by element class.
* `xpath`: Search by XPath.
* `css`: Search by CSS selector.

The search term is the value to search for. The two inputs must be provided in the CSV file "test_input" column and be separated by a subdelimeter "|" (pipe). Here is a sample test row for this test type:
```csv
url,test_type,test_input
https://tamil.digital.utsc.utoronto.ca/collection/2855,element_present_test,xpath|/html/body/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/aside/div[3]/h2
```

### `invalid_links_test`:
This test (non-recursively) tests all links present on the given URL to see if they are broken. It does not require any input data. Here is a sample test row for this test type:
```csv
url,test_type,input_data
https://digital.utsc.utoronto.ca/basic-page/systems-and-software,invalid_links_test,
```

### `permalink_redirect_test`:
This test checks to see if the ARK resolver correctly redirects the permalink on a collection page to the correct location. It requires the expected redirect URL to be passed as input. The test will then visit the collection page in a browser and check to see if the permalink redirects to the expected URL. Here is a sample test row for this test type:
```csv
url,test_type,input_data
https://ark.digital.utsc.utoronto.ca/ark:/61220/utsc11324,permalink_redirect_test,https://tamil.digital.utsc.utoronto.ca/61220/utsc11324
```

### `rest_oai_pmh_xml_validity_test`:
This test checks if the XML on the OAI-PMH endpoint is valid. It does not require any input data. Here is a sample test row for this test type:
```csv
url,test_type,input_data
https://memory.digital.utsc.utoronto.ca/oai/request?identifier=oai%3Amemory.digital.utsc.utoronto.ca%3Anode-10262&metadataPrefix=mods&verb=GetRecord,permalink_redirect_test,
```