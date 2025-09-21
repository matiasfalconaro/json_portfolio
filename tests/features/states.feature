Feature: State management for modals

  Scenario: Toggle general modal
    Given I have a fresh state
    When I toggle the general modal
    Then the modal should be shown
    When I toggle the general modal again
    Then the modal should be hidden

  Scenario: Toggle code modal
    Given I have a fresh state
    When I toggle the code modal
    Then the code modal should be shown
    When I toggle the code modal again
    Then the code modal should be hidden
    