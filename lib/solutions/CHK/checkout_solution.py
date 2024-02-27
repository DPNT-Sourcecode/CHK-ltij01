
# noinspection PyUnusedLocal
# skus = unicode string
"""
@param skus: unicode string, non space separated letters, no numbers
"""
def checkout(skus):
    prices = {"A": 50, "B": 30, "C":20, "D":15}
    deals = {"A": (3, 130), "B": (2, 45)}
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
        if sku in deals: 
            deal_count, deal_price = deals[sku]
            total_cost += (count//deal_count) * deal_price 
            count = count % deal_count
        total_cost += count * prices[sku]
    return total_cost




