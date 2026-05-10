Feature: Products

    Scenario: 카트에 상품을 추가 가능
        Given 사용자가 Products 페이지에 있다
        When 상품에 마우스를 hover하고 add to cart 버튼을 클릭한다
        Then 상품 추가 확인 modal이 표시된다

    Scenario: 상품 추가 확인 modal - Continue Shopping 버튼 동작
        Given 상품 추가 확인 modal이 표시되어 있다
        When Continue Shopping 버튼을 클릭한다
        Then 상품 추가 확인 modal이 닫힌다

    Scenario: 상품 추가 확인 modal - View Cart 버튼 동작
        Given 상품 추가 확인 modal이 표시되어 있다
        When View Cart 버튼을 클릭한다
        Then View Cart 페이지로 이동한다