Feature: Login

    Scenario: [DM1] You are on login page
        Given I go to "http://localhost/dm1/admin"
        Then I should see "Myotonic Dystrophy"
    
    Scenario: [DM1] Login successful
        Given I go to "http://localhost/dm1/admin"
        Then I log in as "admin" with "admin" password
        And I click "Log out"