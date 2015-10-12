Feature: Report Links

    Scenario: [SMA] Admin should see NMD report links
        Given I go to "/admin"
        When I log in as "admin" with "admin" password
        Then I should see "Site administration"
        Then I should see "NMD Report Australia"
        And I click "Log out"
        
    Scenario: [SMA] Curator should not see NMD report links
        Given I go to "/admin"
        When I log in as "curator" with "curator" password
        Then I should see "Site administration"
        Then I should not see "NMD Report Australia"
        And I click "Log out"