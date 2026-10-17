def yakit_gostergesi(yakit : int,tuketim : int):
    while yakit > 0 :
        yakit = max(yakit-tuketim,0)
        yield yakit 
    return 


