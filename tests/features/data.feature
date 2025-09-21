Feature: Portfolio data validation

  Scenario: Load portfolio data
    Given the portfolio data is loaded
    Then it should be a dictionary

  Scenario: Verify top-level keys in portfolio
    Given the portfolio data is loaded
    Then the data should contain the keys "basics", "work", "education", "projects", "certificates"

  Scenario: Validate project fields
    Given the portfolio data is loaded
    Then each project should have "name", "description" and "highlights" as a list

  Scenario: Check image assets exist
    Given the portfolio data is loaded
    Then the main image and logos should exist in the assets folder
