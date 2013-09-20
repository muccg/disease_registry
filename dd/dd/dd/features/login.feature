Feature: Login

    Scenario: [DD] You are on login page
        Given I go to "http://localhost/dd/admin"
        Then I should see "Demyelinating Diseases Registry"
    
    Scenario: [DD] Login successful as admin
        Given I go to "http://localhost/dd/admin"
        Then I log in as "admin" with "admin" password
        Then I should see "Site administration" within 3 seconds
        And I click "Log out"

    Scenario: [DD] Login successful as curator
        Given I go to "http://localhost/dd/admin"
        Then I log in as "curator" with "curator" password
        Then I should see "Site administration" within 3 seconds
        And I click "Log out"

    Scenario: [DD] Login failed as curator
        Given I go to "http://localhost/dd/admin"
        Then I log in as "curator" with "1234567890" password expects "Please enter the correct username and password"
