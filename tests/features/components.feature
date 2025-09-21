Feature: Portfolio components

  Scenario: Navbar returns a Reflex Component
    When I render the navbar
    Then it should be a Reflex Component

  Scenario: Header, Work, Education, Project and Footer return components
    When I render all main sections
    Then each should be a Reflex Component

  Scenario: Modals return components when state flags are set
    Given a fresh state
    When I enable show_modal and show_code_modal
    Then contact_modal and code_info_modal should be Reflex Components
