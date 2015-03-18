Feature: Test
	As someone new to testing
	So I can learn behavior driven development
	I want to write some scenarios
 
	Scenario: I can view the test page
		Given I am at "/quick-test/"
		Then I should see "Hello testing world!"
