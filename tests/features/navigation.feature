Feature: Navigation

    Background:
        Given 사용자가 홈페이지에 있다

    Scenario: 홈에서 로그인 페이지로 리디렉션
        When 로그인 버튼을 클릭한다
        Then 로그인 페이지로 이동한다

    Scenario: 홈에서 Products 페이지로 리디렉션
        When Products 버튼을 클릭한다
        Then Products 페이지로 이동한다

    Scenario: 홈에서 Cart 페이지로 리디렉션
        When Cart 버튼을 클릭한다
        Then Cart 페이지로 이동한다
