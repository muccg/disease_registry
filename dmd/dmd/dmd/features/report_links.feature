Feature: Report Links

    Scenario: Admin should see NMD report links
        Given I go to "http://localhost:8000/admin"
        When I log in as "admin" with "admin" password expects "Site administration"
        Then I should see "NMD Report Australia"
        And I click "Log out"
        
    Scenario: Curator should not see NMD report links
        Given I go to "http://localhost:8000/admin"
        When I log in as "curator" with "curator" password expects "Site administration"
        Then I should not see "NMD Report Australia"
        And I click "Log out"