
# noinspection PyUnusedLocal
# skus = unicode string
"""
@param skus: unicode string, non space separated letters, no numbers

We perform operations in the following order:
1. Apply all specials and BOGO style deals first
2. Apply bundle deals
3. Evaluate single item purchase prices
"""
def checkout(skus):
    prices = {"A": 50, "B": 30, "C":20, "D":15, "E":40, "F":10}
    deals = {"A": [(5,200), (3, 130)], "B": [(2, 45)]}
    specials = {"E": {"B": (2,1)}, "F":{"F": (2,1)}}
    total_cost = 0
    goods_purchased = {}
  
    # build map of item to amount purchased
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
                if freebie_sbu in goods_purchased:
                    # special gives you another item for free
                    if freebie_sbu != sbu: 
                        sku_count, freebie_count = specials[sku][freebie_sbu]
                        goods_purchased[freebie_sbu] -= (count // sku_count) * freebie_count
                        if goods_purchased[freebie_sbu] < 0: goods_purchased[freebie_sbu] = 0
                    # special BOGO style deal
                    else: 
                        sku_count, freebie_count = specials[sku][freebie_sbu]
                        if count >= sku_count + freebie_count: 
                            times_applied = count // (sku_count + freebie_count) 
                            total_cost += times_applied * sku_count * prices[sku]
                            goods_purchased[sku] -= times_applied * (sku_count + freebie_count) 

    for sku in goods_purchased: 
        count = goods_purchased[sku]
        # apply possible deals with current count of item
        if sku in deals: 
            current_deal = find_next_compatible_deal(count, deals[sku])
            if current_deal != -1: 
                deal_count, deal_price = deals[sku][current_deal]
                while count >= deal_count: 
                    count -= deal_count
                    total_cost += deal_price
                    if count < deal_count and current_deal<len(deals[sku])-1:
                        current_deal +=1 
                        deal_count, deal_price = deals[sku][current_deal]
        # add remainder using single item pricing 
        total_cost += count * prices[sku]
    return total_cost


def find_next_compatible_deal(count, sku_deals): 
    for i in range(len(sku_deals)):
        deal_count, _ = sku_deals[i]
        if deal_count <= count: 
            return i 
    return -1 




