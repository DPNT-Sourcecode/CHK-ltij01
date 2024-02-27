import unittest

"""
@param skus: unicode string, non space separated letters, no numbers
"""
def checkout(skus):
    prices = {"A": 50, "B": 30, "C":20, "D":15, "E":40}
    deals = {"A": [(5,200), (3, 130)], "B": (2, 45)}
    specials = {"E": {"B": (2,1)}}
    total_cost = 0
    goods_purchased = {}
    for sku in skus:
        if sku not in prices: 
            return -1 
        if sku not in goods_purchased: 
            goods_purchased[sku] = 1
        else: 
            goods_purchased[sku] +=1
    for sku in goods_purchased: 
        count = goods_purchased[sku]
        if sku in specials: 
            for freebie_sbu in specials[sku]: 
                sku_count, freebie_count = specials[sku][freebie_sbu]
                goods_purchased[freebie_sbu] -= (count // sku_count) * freebie_count
                if goods_purchased[freebie_sbu] < 0: goods_purchased[freebie_sbu] = 0

    for sku in goods_purchased: 
        count = goods_purchased[sku]
        if sku in deals: 
            current_deal = 0 
            deal_count, deal_price = deals[sku][current_deal]
            while count >= deal_count: 
                count -= deal_count
                total_cost += goods_purchased
                if count < deal_count:
                    current_deal +=1 
                    deal_count, deal_price = deals[sku][current_deal]

        total_cost += count * prices[sku]
    return total_cost

class TestCheckout(unittest.TestCase): 
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
        assert checkout(skus) == 460


if __name__ == '__main__':
    unittest.main()



