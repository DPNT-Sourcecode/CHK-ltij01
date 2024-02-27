
# noinspection PyUnusedLocal
# skus = unicode string
"""
@param skus: unicode string, non space separated letters, no numbers
"""
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
            current_deal = 0 
            deal_count, deal_price = deals[sku][current_deal]
            while count >= deal_count: 
                count -= deal_count
                total_cost += goods_purchased
                if count < deal_count and current_deal<len(deals[sku])-1:
                    current_deal +=1 
                    deal_count, deal_price = deals[sku][current_deal]

        total_cost += count * prices[sku]
    return total_cost



