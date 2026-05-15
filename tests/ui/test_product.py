from tests.ui.steps.products_steps import *
from tests.ui.steps.cart_steps import *
from pytest_bdd import scenarios


scenarios("features/products.feature")
scenarios("features/cart.feature")