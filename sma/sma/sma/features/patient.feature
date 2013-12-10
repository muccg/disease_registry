Feature: Patient

    Scenario: [SMA] Add Patient
        Given I go to "/admin"
        And I log in as "admin" with "admin" password expects "Site administration"
        Given I go to "/admin/patients/patient/add/"
        Then I should see "Add patient"
        When I check "consent"
        When I select "New Zealand" from "working_group"
        When I fill in "family_name" with random text
        When I fill in "given_names" with random text
        When I fill in "date_of_birth_year" with "1990" year
        When I select "Male" from "sex"
        When I fill in "address" with "123 Nowhere Street"
        When I fill in "suburb" with "Perth"
        When I select "Western Australia" from "state"
        When I fill in "postcode" with "6666"
        And I press "Save"
        Then I should see "was added successfully"
        And I click "Log out"
    
    #TODO
    Scenario: [SMA] Can't Add Duplicate Patient
        Given I go to "/admin"
        And I log in as "admin" with "admin" password
        Then I should see "Site administration"
        Given I go to "/admin/patients/patient/add/"
        And I click "Log out"