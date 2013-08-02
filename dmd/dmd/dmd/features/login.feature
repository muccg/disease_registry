Feature: Login

    Scenario: You are on login page
        Given I go to "http://localhost:8000/admin"
        Then I should see "Duchenne Muscular Dystrophy Registry"
    
    Scenario: Login successful
        Given I go to "http://localhost:8000/admin"
        Then I log in as "admin" with "admin" password
        And I click "Log out"