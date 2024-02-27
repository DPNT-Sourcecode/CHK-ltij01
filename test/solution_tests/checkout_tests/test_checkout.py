from solutions.CHK import checkout

class TestCheckout(): 
    def test_checkout_singles(): 
        skus = "ABC"
        assert checkout(skus) == 100
    def test_checkout_invalid():
        skus = "DEF"
        assert checkout(skus) == -1
    def test_checkout_deals(): 
        skus = "AAAAB"
        assert checkout(skus) == 210
    def test_checkout_specials():
        skus = "EEB"
        assert checkout(skus) == 80
    def test_checkout_specials_and_deals(): 
        skus = "AAAAAAAAAEEB"

