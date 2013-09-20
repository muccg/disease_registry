Feature: Patient

    Scenario: [DM1] Add Patient
        Given I go to "http://localhost/dm1/admin"
        And I log in as "admin" with "admin" password
        Given I go to "http://localhost/dm1/admin/patients/patient/add/"
        Then I should see "Add patient" within 3 seconds
        When I check "consent"
        When I select "Western Australia" from "working_group"
        When I fill in "family_name" with random text
        When I fill in "given_names" with random text
        When I fill in "date_of_birth_year" with "1990" year
        When I select "Male" from "sex"
        When I fill in "address" with "123 Nowhere Street"
        When I fill in "suburb" with "Perth"
        When I select "Western Australia" from "state"
        When I fill in "postcode" with "6666"
        And I press "Save"
        Then I should see "was added successfully" within 3 seconds
        And I click "Log out"
    
    #TODO
    Scenario: [DM1] Can't Add Duplicate Patient
        Given I go to "http://localhost/dm1/admin"
        And I log in as "admin" with "admin" password
        Given I go to "http://localhost/dm1/admin/patients/patient/add/"
        And I click "Log out"