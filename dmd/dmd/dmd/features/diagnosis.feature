Feature: Diagnosis

    Scenario: [DMD] Add diagnosis page accessible by admin
        Given I go to "/admin"
        Then I log in as "admin" with "admin" password expects "Site administration"
        Given I go to "/admin/dmd/diagnosis/add/"
        Then I should see "Add clinical diagnosis"
        And I click "Log out"
