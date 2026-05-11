Feature: Cart

    Scenario: 단일 상품 - 카트에 추가 확인
        Given 사용자가 Products 페이지에 있다
        When add to cart 버튼을 눌러 상품을 카트에 추가한다
        Then 카트에 해당 상품이 들어있다

    Scenario: 단일 상품 - 카트에서 삭제 확인
        Given 카트에 상품이 담겨있다
        When 삭제 버튼을 클릭한다
        Then 해당 상품이 카트에서 삭제된다

    Scenario: 여러 상품 - 카트에 추가 확인
        Given 사용자가 Products 페이지에 있다
        When add to cart 버튼을 눌러 여러 상품을 카트에 추가한다
        Then 카트에 해당 상품들이 모두 들어있다