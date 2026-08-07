Feature: Database connection and operations

  Scenario: Database connection is established
    Given the database client is configured
    When I check the database connection
    Then the connection should be active

  Scenario: Collections are initialized
    Given the database is empty
    When I initialize collections
    Then all required collections should exist

  Scenario: Indexes are created on collections
    Given a collection exists
    When I ensure an index on a field
    Then the index should be created
    And subsequent index creation should be idempotent

  Scenario: Database connection failure
    Given invalid database credentials
    When I attempt to connect to the database
    Then a connection error should be raised

  Scenario: Collection initialization is idempotent
    Given collections already exist
    When I initialize collections again
    Then no errors should occur
    And existing collections should remain unchanged
