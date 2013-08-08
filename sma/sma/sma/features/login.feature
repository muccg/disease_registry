Feature: Login

    Scenario: You are on login page
        Given I go to "http://localhost:8000/admin"
        Then I should see "Spinal Muscular Atrophy"
    
    Scenario: Login successful as admin
        Given I go to "http://localhost:8000/admin"
        Then I log in as "admin" with "admin" password expects "Site administration"
        And I click "Log out"

    Scenario: Login successful as curator
        Given I go to "http://localhost:8000/admin"
        Then I log in as "curator" with "curator" password expects "Site administration"
        And I click "Log out"

    Scenario: Login failed as curator
        Given I go to "http://localhost:8000/admin"
        Then I log in as "curator" with "1234567890" password expects "Please enter the correct username and password"
