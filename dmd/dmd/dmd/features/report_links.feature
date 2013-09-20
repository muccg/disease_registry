Feature: Report Links

    Scenario: [DMD] Admin should see NMD report links
        Given I go to "http://localhost:8000/admin"
        When I log in as "admin" with "admin" password
        Then I should see "Site administration" within 3 seconds
        Then I should see "NMD Report Australia"
        And I click "Log out"
        
    Scenario: [DMD] Curator should not see NMD report links
        Given I go to "http://localhost:8000/admin"
        When I log in as "curator" with "curator" password
        Then I should see "Site administration" within 3 seconds
        Then I should not see "NMD Report Australia"
        And I click "Log out"