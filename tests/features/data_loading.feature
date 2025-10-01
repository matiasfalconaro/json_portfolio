Feature: Portfolio data loading and serialization

  Scenario: Load portfolio data from JSON
    Given the resume.json file exists
    When I call load_portfolio
    Then it should return a dictionary
    And the dictionary should contain all required keys

  Scenario: Serialize dictionary data
    Given I have a dictionary with nested data
    When I call serialize on the data
    Then it should return the same structure
    And all data types should be preserved

  Scenario: Serialize HttpUrl objects
    Given I have data containing HttpUrl objects
    When I call serialize on the data
    Then HttpUrl objects should be converted to strings
    And the URLs should be properly formatted

  Scenario: Serialize nested HttpUrl in lists
    Given I have a list containing HttpUrl objects
    When I call serialize on the list
    Then all HttpUrl objects should be converted to strings

  Scenario: Serialize None values
    Given I have data with None values
    When I call serialize on the data
    Then None values should be preserved

  Scenario: Main function inserts basics
    Given valid portfolio data exists
    When I run the main function
    Then basics data should be inserted into the database
    And the basics should be upserted (replace or insert)

  Scenario: Main function inserts work items
    Given portfolio data contains work experiences
    When I run the main function
    Then all work items should be inserted as a batch
    And each work item should be validated

  Scenario: Main function handles validation errors
    Given portfolio data contains invalid email
    When I run the main function
    Then a ValidationError should be raised
    And no data should be inserted

  Scenario: Handle missing resume.json file
    Given the resume.json file does not exist
    When the data module is imported
    Then a FileNotFoundError should be raised

  Scenario: Handle malformed JSON
    Given the resume.json file contains invalid JSON
    When the data module is imported
    Then a JSONDecodeError should be raised

  Scenario: Serialize complex nested structures
    Given I have complex nested data with HttpUrl objects
    When I call serialize on the data
    Then all nested HttpUrl objects should be converted
    And the structure should remain intact

  Scenario: Primitive types are unchanged
    Given I have primitive types (string, int, float, bool)
    When I call serialize on each type
    Then each type should be returned unchanged

  Scenario: Data variable is loaded on import
    Given the data module is imported
    Then the data variable should exist
    And it should be a dictionary
    And it should contain all required top-level keys
