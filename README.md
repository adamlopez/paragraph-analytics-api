# paragraph-analytics-api

Flask Web API that returns various summary statistics about some text.

## Interface
<details>
 <summary><code>GET</code> <code><b>/word_frequency</b></code> <code>(Get a sorted frequency count of each alphanumeric word in the paragraph.)</code></summary>

##### Body

> | key       |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | paragraph |  required | string                  | The text paragraph that will be analyzed  |


##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`        | lexicographically sorted frequency map of all words in the paragraph. |
> | `400`         | `text/html;charset=UTF-8` |Error parsing paragraph from request body. body should be of the form:`{"paragraph": "your_paragraph_here"}`|

</details>

<details>
 <summary><code>GET</code> <code><b>/word_count</b></code> <code>(Get the total number of alphanumeric words in the paragraph.)</code></summary>

##### Body

> | key       |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | paragraph |  required | string                  | The text paragraph that will be analyzed  |


##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `text/html;charset=UTF-8`        | number of words in the paragraph. |
> | `400`         | `text/html;charset=UTF-8 |Error parsing paragraph from request body. body should be of the form:`{"paragraph": "your_paragraph_here"}`|

</details>

<details>
 <summary><code>GET</code> <code><b>/character_count</b></code> <code>(gets the total number of alphanumeric characters in the paragraph.)</code></summary>

 ##### Parameters

> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `exclude_spaces` |  optional | boolean   | Whether or not spaces should be excluded from the character count. The default behaviour is to include spaces in the count.|

  
##### Body

> | key       |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | paragraph |  required | string                  | The text paragraph that will be analyzed  |


##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `text/html; charset=utf-8`        |  Number of alphanumeric or punctuation characters in the paragraph. |
> | `400`         | `text/html;charset=UTF-8` |Error parsing paragraph from request body. body should be of the form:`{"paragraph": "your_paragraph_here"}`|
> | `400`         | `text/html;charset=UTF-8`|Error parsing `exclude_spaces` value from the request parameters.|

</details>

See postman collection for example requests to all endpoints.


## Development

To build the docker container, run
```
make build
```

After running `make build`,to start the docker container, run:
``` 
make start 
```
To run unit tests against the paragraph parsing engine, run:
```
make test
```
