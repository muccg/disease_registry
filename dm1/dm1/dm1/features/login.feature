Feature: Login page

    Scenario: You are on login page
        Given I go to "http://192.168.251.183:8080/admin"
        Then I should see "Australian Myotonic Dystrophy"
    
    Scenario: Login successful
        Given I go to "http://192.168.251.183:8080/admin"
        When I fill in "username" with "admin"
        When I fill in "password" with "admin"
        And I press "Log in"
        Then I should see "Site administration"