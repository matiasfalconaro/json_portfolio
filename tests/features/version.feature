Feature: Version management

  Scenario: Get version from version file
    Given I have a version file with content "2.0.0"
    When I call get_version
    Then it should return "2.0.0"

  Scenario: Get version when file is missing
    Given I am in a directory without version file
    When I call get_version
    Then it should return "dev"
    