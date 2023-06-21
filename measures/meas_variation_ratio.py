import pandas as pd

def me_variation_ratio(data):
    '''
    Variation Ratio
    
    the Variation Ratio (VR) (Freeman, 1965) is simply the proportion that does not belong to the modal category (Zedeck, 2014, p.406). 
    
    It is a measure of dispersion for categorical data. There are many other measures of dispersion for categorical data. 
    A good start for more info on other measures could be an article from Kader and Perry (2007).
    
    Parameters
    ----------
    data : the scores from which to determine the variation ratio
    
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
    
    * \(n\) the total sample size
    * \(k_m\) the number of categories with a frequency equal to \eqn{F_{mode}}
    * \(F_{m}\) the frequency (count) of the modal category (categories)
    
    References 
    ----------
    Freeman, L. C. (1965). *Elementary applied statistics: For students in behavioral science*. Wiley.
    
    Zedeck, S. (Ed.). (2014). *APA dictionary of statistics and research methods*. American Psychological Association.
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    Examples
    --------
    >>> data = pd.DataFrame(["MARRIED", "DIVORCED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "NEVER MARRIED", "MARRIED", "MARRIED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "MARRIED"], columns=["marital"])
    >>> me_variation_ratio(data['marital'])    
    
    '''
    freq = data.value_counts()
    maxFreq = freq.max()
    n = freq.sum()
    maxCount = sum(freq.values==maxFreq)
    
    if maxCount==len(freq):
        VR = "no mode, so no vr"
    else:
        VR = 1 - maxCount*maxFreq / n
        
    return VR