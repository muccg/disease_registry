Feature: Questionnaire

    Scenario: Access to Australian questionnaire
        Given I go to "http://localhost:8000/questionnaire/au"
        I should see "Australia Myotonic Dystrophy Registry"


    Scenario: Access to New Zealand questionnaire
        Given I go to "http://localhost:8000/questionnaire/nz"
        I should see "New Zealand Myotonic Dystrophy Registry"