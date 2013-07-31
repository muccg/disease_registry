Feature: User

    Scenario: Add User
        Given I go to "http://localhost:8000/admin"
        When I fill in "username" with "admin"
        When I fill in "password" with "admin"
        And I press "Log in"
        Then I should see "Site administration"
        Given I go to "http://localhost:8000/admin/groups/user/add/"
        Then I should see "Add user"
        When I fill in "username" with "pumpernickel"
        When I fill in "password" with "password"
        When I fill in "confirm_password" with "password"
        When I fill in "first_name" with "John Michael"
        When I fill in "last_name" with "Pumpernickel"
        When I fill in "email_address" with "email@address.com"
        When I fill in "title" with "Tester"
        When I select "Working Group Curators" from "groups"
        When I select "Western Australia" from "working_group"
        And I press "Save"
        Then I should see "Select user to change"

    Scenario: Verify Django user created
        Given I go to "http://localhost:8000/admin/auth/user/"
        Then I should see "pumpernickel"
    
    Scenario: Delete Django and RDR user
        Given I go to "http://localhost:8000/admin/auth/user/"
        When I click "pumpernickel"
        Then I should see "Change user" within 1 seconds
        When I click "Delete"
        Then I should see "Are you sure?"
        When I press "Yes, I'm sure"
        Then I should see "was deleted successfully"