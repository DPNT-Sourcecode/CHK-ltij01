import unittest

def checkout(skus):
    prices = {"A": 50, "B": 30, "C":20, "D":15, "E":40}
    deals = {"A": [(5,200), (3, 130)], "B": [(2, 45)]}
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
            current_deal = find_next_compatible_deal(count, deals[sku])
            if current_deal == -1: 
                continue
            deal_count, deal_price = deals[sku][current_deal]
            while count >= deal_count: 
                count -= deal_count
                total_cost += goods_purchased
                if count < deal_count and current_deal<len(deals[sku])-1:
                    current_deal +=1 
                    deal_count, deal_price = deals[sku][current_deal]

        total_cost += count * prices[sku]
    return total_cost


def find_next_compatible_deal(count, sku_deals): 
    current_deal = 0
    deal_count, deal_price = sku_deals[current_deal]
    while deal_count > count: 
        if current_deal<len(sku_deals)-1: 
            current_deal +=1
            deal_count, deal_price = sku_deals[current_deal]
        else:
            return -1
    return current_deal


class TestCheckout(unittest.TestCase): 
    def test_checkout_singles(self): 
        skus = "ABC"
        self.assertEqual(checkout(skus), 100)
    def test_checkout_invalid(self):
        skus = "DEF"
        self.assertEqual(checkout(skus), -1)
    def test_checkout_deals(self): 
        skus = "AAAAB"
        self.assertEqual(checkout(skus), 210)
    def test_checkout_specials(self):
        skus = "EEB"
        self.assertEqual(checkout(skus), 80)
    def test_checkout_specials_and_deals(self): 
        skus = "AAAAAAAAAEEB"
        self.assertEqual(checkout(skus), 460)


if __name__ == '__main__':
    unittest.main()

