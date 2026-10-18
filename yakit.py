def yakit_gostergesi(yakit : int,tuketim : int):
    """Her adimda tuketim miktarini duserek kalan yakiti uretir."""
    while yakit > 0 :
        yakit = max(yakit-tuketim,0)
        yield yakit 
    return 


