Feature: Version management

  Scenario: Get version from version file
    Given I have a version file with content "1.4.2"
    When I call get_version
    Then it should return "1.4.2"

  Scenario: Get version when file is missing
    Given I am in a directory without version file
    When I call get_version
    Then it should return "dev"
    