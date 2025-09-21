Feature: Portfolio page components validation

  Scenario: Index page components are Reflex components
    Given I have the portfolio page components
    When I check each component type
    Then all components should be valid Reflex components

  Scenario: Footer contains copyright text
    Given I have the footer component
    When I render the footer
    Then it should contain the copyright text "© 2025 Matias Falconaro."
