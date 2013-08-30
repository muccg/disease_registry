Feature: Questionnaire

    Scenario: Access to Australian questionnaire
        Given I go to "http://localhost:8000/questionnaire/au"
        I should see "Australia Myotonic Dystrophy Registry"

    Scenario: Submit incomplete Australian questionnaire
        Given I go to "http://localhost:8000/questionnaire/au"
        I should see "Australia Myotonic Dystrophy Registry"
        When I press "Continue"
        I should see "Please correct the errors in the form below!"

    Scenario: Submit Australian questionnaire
        Given I go to "http://localhost:8000/questionnaire/au"
        I should see "Australia Myotonic Dystrophy Registry"
        When I choose "id_q1" radio
        When I choose "id_q2_1" radio
        When I choose "id_q3_1" radio
        When I choose "id_q4" radio
        When I choose "id_q5" radio
        When I choose "id_q6" radio
        When I choose "id_q7" radio
        When I fill in "firstname" with random text
        When I fill in "lastname" with random text
        When I fill in "consentdate" with "23/05/2013"
        And I press "Continue"
        I should see "Personal Details"
        And The browser's URL should contain "personal"
        When I fill in "date_of_birth_year" with "1990" year
        When I fill in "address" with "Elm Street"
        When I fill in "suburb" with "Neverland"
        When I select "Western Australia" from "state"
        When I select "Australia" from "country"
        When I fill in "postcode" with "6666"
        And I press "Continue"
        I should see "Diagnosis"
        And The browser's URL should contain "clinical"
        When I press "Submit"
        I should see "Thank you for your submission."
        And The browser's URL should contain "thanks"


    Scenario: Access to New Zealand questionnaire
        Given I go to "http://localhost:8000/questionnaire/nz"
        I should see "New Zealand Myotonic Dystrophy Registry"

    Scenario: Submit New Zealand questionnaire
        Given I go to "http://localhost:8000/questionnaire/nz"
        I should see "New Zealand Myotonic Dystrophy Registry"
        When I choose "id_q8" radio
        When I choose "id_q9" radio
        When I choose "id_q10" radio
        When I choose "id_q1" radio
        When I choose "id_q2_1" radio
        When I choose "id_q3_1" radio
        When I choose "id_q4" radio
        When I choose "id_q5" radio
        When I choose "id_q6" radio
        When I choose "id_q7" radio
        When I fill in "firstname" with random text
        When I fill in "lastname" with random text
        When I fill in "consentdate" with "23/05/2013"
        And I press "Continue"
        I should see "Personal Details"
        And The browser's URL should contain "personal"
        When I fill in "date_of_birth_year" with "1990" year
        When I fill in "address" with "Elm Street"
        When I fill in "suburb" with "Neverland"
        When I select "Western Australia" from "state"
        When I select "Australia" from "country"
        When I fill in "postcode" with "6666"
        And I press "Continue"
        I should see "Diagnosis"
        And The browser's URL should contain "clinical"
        When I press "Submit"
        I should see "Thank you for your submission."
        And The browser's URL should contain "thanks"

    Scenario: Submit incomplete New Zealand questionnaire
        Given I go to "http://localhost:8000/questionnaire/nz"
        I should see "New Zealand Myotonic Dystrophy Registry"
        When I press "Continue"
        I should see "Please correct the errors in the form below!"