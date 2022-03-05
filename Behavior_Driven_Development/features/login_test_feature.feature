Feature: Login to ORANGE HRM
  Scenario: Login to ORANGE HRM With Valid Data
    Given I launched Chrome Browser
    When I Open ORANGE HRM Homepage
    And I enter Username
    And I enter Password
    And I Click Login
    Then User Suceesfully Logged in.