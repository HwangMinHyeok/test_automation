Feature: Login

    Background: 
        Given 사용자가 로그인 페이지에 있다

    Scenario: 로그인 성공
        When 올바른 계정을 입력하고 로그인한다
        Then 로그인에 성공한다

    Scenario: 로그인 실패
        When 올바르지 않은 계정을 입력한다
        Then 로그인에 실패한다
