Feature: example of a simple test case

Scenario: we make a simple request to the api
  Given the api url
  When we make a request to the api
  Then json response is retrieved with status code 200