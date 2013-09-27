Feature: Login

    Scenario: [DMD] You are on login page
        Given I go to "/admin"
        Then I should see "Duchenne Muscular Dystrophy Registry"
    
    Scenario: [DMD] Login successful as admin
        Given I go to "/admin"
        Then I log in as "admin" with "admin" password
        Then I should see "Site administration"
        And I click "Log out"

    Scenario: [DMD] Login successful as curator
        Given I go to "/admin"
        Then I log in as "curator" with "curator" password
        Then I should see "Site administration"
        And I click "Log out"

    Scenario: [DMD] Login failed as curator
        Given I go to "/admin"
        Then I log in as "curator" with "1234567890" password
        Then I should see "Please enter the correct username and password"
