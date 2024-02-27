
# noinspection PyUnusedLocal
# skus = unicode string
"""
@param skus: unicode string, non space separated letters, no numbers

We perform operations in the following order:
1. Apply all group bundles
2. Apply all specials and BOGO style deals first
3. Apply bundle deals
4. Evaluate single item purchase prices
"""
def checkout(skus):
    prices = {"A": 50, "B": 30, "C":20, "D":15, "E":40, "F":10, "G": 20, "H": 10, "I": 35, "J": 60, "K":70, "L":90, "M":15, "N":40, "O":10, "P":50, "Q":30, "R":50, "S":20, "T":20,"U":40,"V":50, "W":20,"X":17, "Y":20, "Z":21}
    deals = {"A": [(5,200), (3, 130)], "B": [(2, 45)], "H":[(10,80),(5,45)], "K":[(2,150)], "P":[(5,200)], "Q":[(3,80)], "V": [(3,130), (2,90)]} # lists must be sorted in decreasing sku count 
    specials = {"E": {"B": (2,1)}, "F":{"F": (2,1)}, "N":{"M":(3,1)},"R":{"Q":(3,1)}, "U":{"U":(3,1)}}
    group_bundle_price_ordered = {"ZSTYX":(3,45)} # IMPORTANT: the key in this dictionary is in sorted single price order, meaning the single price of Z >= S >= T...
    bundle_sku_count = {"ZSTYX": 0}
    total_cost = 0
    goods_purchased = {sku:0 for sku in prices}
  
    # build map of item to amount purchased
    for sku in skus:
        if sku not in prices: 
            return -1 
        if sku in "ZSTYX": # this would be a for loop, if numerous bundles 
            bundle_sku_count["ZSTYX"] +=1
        if sku not in goods_purchased: 
            goods_purchased[sku] = 1
        else: 
            goods_purchased[sku] +=1

    # apply group bundles first
    for bundle in group_bundle_price_ordered: 
        total_item_count = bundle_sku_count[bundle]
        deal_count, deal_price = group_bundle_price_ordered[bundle]
        while total_item_count >= deal_count: 
            remaining_items = deal_count
            for sku in bundle: 
                if goods_purchased[sku] >= remaining_items:
                    goods_purchased[sku] -= remaining_items 
                    total_cost += deal_price
                    total_item_count -= remaining_items
                    break 
                elif goods_purchased[sku] < remaining_items and goods_purchased[sku] > 0 and total_item_count>=remaining_items: 
                    remaining_items -= goods_purchased[sku]
                    goods_purchased[sku] = 0
                    total_item_count -= remaining_items
                
  
    # apply specials and BOGO deals 
    for sku in goods_purchased: 
        count = goods_purchased[sku]
        if sku in specials: 
            for freebie_sbu in specials[sku]: 
                if freebie_sbu in goods_purchased:
                    # special gives you another item for free
                    if freebie_sbu != sku: 
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

    # apply possible deals with current count of item
    for sku in goods_purchased: 
        count = goods_purchased[sku]
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

