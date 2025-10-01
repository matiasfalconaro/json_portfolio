Feature: Admin panel CRUD operations

  Background:
    Given the admin panel is loaded
    And I have a fresh admin state

  Scenario: Create a new work experience
    When I select the work collection
    And I click create new work item
    And I fill in work details:
      | field      | value              |
      | name       | Tech Company       |
      | position   | Software Developer |
      | startDate  | 2020-01            |
      | endDate    | 2023-01            |
      | summary    | Worked on projects |
    And I save the work item
    Then the work item should be created in the database
    And I should see the work item in the list

  Scenario: Edit an existing work experience
    Given a work item exists in the database
    When I select the work collection
    And I click edit on the first work item
    And I update the position to "Senior Developer"
    And I save the work item
    Then the work item should be updated in the database
    And the changes should be reflected in the list

  Scenario: Delete a work experience
    Given a work item exists in the database
    When I select the work collection
    And I delete the first work item
    Then the work item should be removed from the database
    And the item should not appear in the list

  Scenario: Create a new education entry
    When I select the education collection
    And I click create new education item
    And I fill in education details:
      | field       | value              |
      | institution | MIT                |
      | area        | Computer Science   |
      | studyType   | Bachelor           |
      | startDate   | 2015-09            |
      | endDate     | 2019-06            |
    And I save the education item
    Then the education item should be created in the database

  Scenario: Update education courses
    Given an education item exists
    When I edit the education item
    And I set courses to "Algorithms, Data Structures, Machine Learning"
    And I save the education item
    Then the courses should be saved as a list
    And the courses should contain 3 items

  Scenario: Create a new project
    When I select the projects collection
    And I click create new project
    And I fill in project details:
      | field       | value                    |
      | name        | Portfolio Website        |
      | role        | Full Stack Developer     |
      | description | Personal portfolio site  |
      | github      | https://github.com/test  |
      | isActive    | true                     |
    And I save the project
    Then the project should be created in the database

  Scenario: Cancel editing without saving
    Given a work item exists
    When I start editing the work item
    And I make changes to the fields
    And I click cancel
    Then the changes should not be saved
    And the original data should be preserved

  Scenario: Switch collections while editing
    Given I am editing a work item
    When I switch to the education collection
    Then the editing state should be reset
    And no unsaved changes should affect the new collection

  Scenario: Handle database save error
    Given I have created a new work item
    And the database connection fails
    When I try to save the work item
    Then an error should be displayed
    And the work item data should be preserved in the form
