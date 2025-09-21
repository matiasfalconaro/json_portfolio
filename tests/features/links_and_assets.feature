Feature: Links and assets validation

  Scenario: Local asset files exist
    Given I have a list of required asset files
    When I check each file path
    Then all local asset files should exist

  Scenario: External URLs are reachable
    Given I have a list of external URLs to test
    When I check each URL
    Then all external URLs should be accessible

  Scenario: Certificate URLs are valid
    Given I have certificate data from portfolio
    When I check each certificate URL
    Then all certificate URLs should be accessible
