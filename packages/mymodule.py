def top_n(items,n):
    """
    Return the top n items in an array,in desc order.

    Args:
        items(array): list or array-like object
        n (int) :number of items to return
    
    Return:
        array: top n items in desc order

   Egs:
        >>> top_n([8,7,2,3,7,4],3)
        [8,7,4]
    
    """


    for i in range(n):
        for j in range(len(items)-i-1):
            if items[i] > items[j+1]:
                items[i],items[j+1] = item[j+1],item[i]


   # Get last two items
   top_n = items[-n:]
   return top_n[:: -1]

