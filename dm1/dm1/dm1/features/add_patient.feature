Feature: Patient

    Scenario: Add Patient
        Given I go to "http://localhost:8000/admin"
        When I fill log in as "admin" with "admin" password
        Given I go to "http://localhost:8000/admin/patients/patient/add/"
        Then I should see "Add patient"
        When I check "consent"
        When I select "Western Australia" from "working_group"
        When I fill in "family_name" with "Doe"
        When I fill in "given_names" with "John"
        When I fill in "date_of_birth_year" with "1990" year
        When I select "Male" from "sex"
        When I fill in "address" with "123 Nowhere Street"
        When I fill in "suburb" with "Perth"
        When I select "Western Australia" from "state"
        When I fill in "postcode" with "6666"
        And I press "Save"
        Then I should see "Select patient to change"
        And I should see "DOE John"
        And I click "Log out"
        
        
        
        