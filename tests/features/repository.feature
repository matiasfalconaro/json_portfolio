Feature: Repository data retrieval

  Scenario: Retrieve basics information
    Given basics data exists in the database
    When I call get_basics
    Then it should return a Basics model instance
    And the basics should contain name and email

  Scenario: Retrieve work experience list
    Given multiple work items exist in the database
    When I call get_work
    Then it should return a list of Work models
    And each work item should have required fields

  Scenario: Retrieve education records
    Given education data exists in the database
    When I call get_education
    Then it should return a list of Education models
    And each education record should have institution and area

  Scenario: Retrieve projects
    Given project data exists in the database
    When I call get_projects
    Then it should return a list of Project models
    And each project should have name and description

  Scenario: Handle empty collections
    Given the work collection is empty
    When I call get_work
    Then it should return an empty list
    And no errors should occur

  Scenario: Handle invalid data in database
    Given the work collection contains invalid data
    When I call get_work
    Then a ValidationError should be raised

  Scenario: Handle database connection failure
    Given the database is unavailable
    When I call get_basics
    Then a database connection error should be raised

  Scenario: Retrieve certificates
    Given certificate data exists in the database
    When I call get_certificates
    Then it should return a list of Certificate models
    And each certificate should have a name and issuer

  Scenario: Handle malformed URLs in data
    Given work data contains invalid URLs
    When I call get_work
    Then a ValidationError should be raised
