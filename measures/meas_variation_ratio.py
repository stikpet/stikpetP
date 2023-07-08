import pandas as pd

def me_variation_ratio(data):
    '''
    Variation Ratio
    ---------------
    
    the Variation Ratio (VR) (Freeman, 1965) is simply the proportion that does not belong to the modal category (Zedeck, 2014, p.406). 
    
    It is a measure of dispersion for categorical data. There are many other measures of dispersion for categorical data. A good start for more info on other measures could be an article from Kader and Perry (2007).
    
    Parameters
    ----------
    data : list or pandas series
        the scores from which to determine the variation ratio
    
    Returns
    -------
    VR : the variation ratio value
    
    Notes
    -----
    The formula used is (Freeman, 1965, p. 41):
    $$VR = 1 - p_{m}$$
    
    With:
    $$p_{m} = \\frac{F_{m}}{n}$$
    
    *Symbols used:*
    
    * \\(n\\) the total sample size
    * \\(k_m\\) the number of categories with a frequency equal to \\(F_{mode}\\)
    * \\(F_{m}\\) the frequency (count) of the modal category (categories)
    
    References 
    ----------
    Freeman, L. C. (1965). *Elementary applied statistics: For students in behavioral science*. Wiley.
    
    Zedeck, S. (Ed.). (2014). *APA dictionary of statistics and research methods*. American Psychological Association.
    
    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    --------
    Example 1: pandas series
    >>> import pandas as pd
    >>> df1 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/GSS2012a.csv', sep=',', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'}) 
    >>> ex1 = df1['mar1']
    >>> me_variation_ratio(ex1)
    0.49922720247295205
    
    Example 2: a list
    >>> ex2 = ["MARRIED", "DIVORCED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "NEVER MARRIED", "MARRIED", "MARRIED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "MARRIED"]
    >>> me_variation_ratio(ex2)
    0.631578947368421
    
    '''
    
    if type(data) == list:
        data = pd.Series(data)
    
    freq = data.value_counts()
    maxFreq = freq.max()
    n = freq.sum()
    maxCount = sum(freq.values==maxFreq)
    
    if maxCount==len(freq):
        VR = "no mode, so no vr"
    else:
        VR = 1 - maxCount*maxFreq / n
        
    return VR