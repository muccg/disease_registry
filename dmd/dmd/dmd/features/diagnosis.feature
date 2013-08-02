Feature: Diagnosis

    Scenario: Add diagnosis page accessible by admin
        Given I go to "http://localhost:8000/admin"
        Then I log in as "admin" with "admin" password expects "Site administration"
        Given I go to "http://localhost:8000/admin/dmd/diagnosis/add/"
        Then I should see "Add clinical diagnosis"
        And I click "Log out"

    Scenario: Add diagnosis page accessible by curator
        Given I go to "http://localhost:8000/admin"
        Then I log in as "curator" with "curator" password expects "Site administration"
        Given I go to "http://localhost:8000/admin/dmd/diagnosis/add/"
        Then I should see "Add clinical diagnosis"
        And I click "Log out"