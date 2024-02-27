

# noinspection PyUnusedLocal
# skus = unicode string
"""
@param skus: unicode string, non space separated letters, no numbers
"""
def checkout(skus):
    prices = {"A": 50, "B": 30, "C":20, "D":15}
    #deals = {"A": {3: 130}, "B": {2:45}}
    deals =  {"3A": 130, "2B": 45}
    total = 0
    for token in skus.split():
        if token in prices: 
            total+= prices[token]  
        elif token in deals:
            total+=deals[token]
        else:
            return -1
    return total
