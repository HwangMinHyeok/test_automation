Feature: Cart

    Scenario: 단일 상품 카트 추가 확인
        Given 사용자가 Products 페이지에 있다
        When add to cart 버튼을 눌러 상품을 카트에 추가한다
        Then 카트에 해당 상품이 들어있다