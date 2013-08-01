Feature: Login

    Scenario: You are on login page
        Given I go to "http://localhost:8080/admin"
        Then I should see "Myotonic Dystrophy"
    
    Scenario: Login successful
        Given I go to "http://localhost:8080/admin"
        Then I log in as "admin" with "admin" password
        And I click "Log out"