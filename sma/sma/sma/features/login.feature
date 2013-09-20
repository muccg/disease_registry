Feature: Login

    Scenario: [SMA] You are on login page
        Given I go to "http://localhost/sma/admin"
        Then I should see "Spinal Muscular Atrophy" within 3 seconds
    
    Scenario: [SMA] Login successful as admin
        Given I go to "http://localhost/sma/admin"
        Then I log in as "admin" with "admin" password
        Then I should see "Site administration" within 3 seconds
        And I click "Log out"

    Scenario: [SMA] Login successful as curator
        Given I go to "http://localhost/sma/admin"
        Then I log in as "curator" with "curator" password
        Then I should see "Site administration" within 3 seconds
        And I click "Log out"

    Scenario: [SMA] Login failed as curator
        Given I go to "http://localhost/sma/admin"
        Then I log in as "curator" with "1234567890" password
        Then I should see "Please enter the correct username and password" within 3 seconds
