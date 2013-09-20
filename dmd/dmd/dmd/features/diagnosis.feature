Feature: Diagnosis

    Scenario: [DMD] Add diagnosis page accessible by admin
        Given I go to "http://localhost/dmd/admin"
        Then I log in as "admin" with "admin" password expects "Site administration"
        Given I go to "http://localhost/dmd/admin/dmd/diagnosis/add/"
        Then I should see "Add clinical diagnosis" within 3 seconds
        And I click "Log out"

    Scenario: [DMD] Add diagnosis page accessible by curator
        Given I go to "http://localhost/dmd/admin"
        Then I log in as "curator" with "curator" password expects "Site administration"
        Given I go to "http://localhost/dmd/admin/dmd/diagnosis/add/"
        Then I should see "Add clinical diagnosis" within 3 seconds
        And I click "Log out"