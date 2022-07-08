Feature: To check whether the file used for processing any NULL values exist
  Scenario: The file exist in the folder to chec NULL values
    Given Open the file from the given location
    When The file is opened and read
    Then Check if NULL values exist
