import pandas as pd
import numpy as np

def me_mode(data, allEq="none"):
    '''
    Mode
    ----
    
    The mode is a measure of central tendency and defined as “the abscissa corresponding to the ordinate of maximum 
    frequency” (Pearson, 1895, p. 345). A more modern definition would be “the most common value obtained in a set 
    of observations” (Weisstein, 2002). 
    
    The word mode might even come from the French word 'mode' which means fashion. Fashion is what most people wear, 
    so the mode is the option most people chose.
    
    If one category has the highest frequency this category will be the modal category and if two or more categories 
    have the same highest frequency each of them will be the mode. If there is only one mode the set is sometimes 
    called unimodal, if there are two it is called bimodal, with three trimodal, etc. For two or more, thse term 
    multimodal can also be used.
    
    An advantage of the mode over many other measures of central tendency (like the median and mean), is that it can 
    be determined for already nominal data types. 
    
    A video on the mode is available [here](https://youtu.be/oPpTE8qt2go).
    
    Parameters
    ----------
    data : list or pandas series 
        the scores to determine the mode from
    allEq : {"none", "all"}, optional 
        indicator on what to do if maximum frequency is equal for more than one category. Default is "none".
    
    Returns
    -------
    A dataframe with:
    
    * *mode*, the mode(s)
    * *mode freq.*, frequency of the mode
    
    Notes
    -----
    One small controversy exists if all categories have the same frequency. In this case none of them has a higher 
    occurence than the others, so none of them would be the mode (see for example Spiegel & Stephens, 2008, p. 64, 
    Larson & Farber, 2014, p. 69). This is used when *allEq="none"* and the default.
    
    On a rare occasion someone might argue that if all categories have the same frequency, then all categories are 
    part of the mode since they all have the highest frequency. This is used when *allEq="all"*.
    
    See Also
    --------
    stikpetP.measures.meas_mode_bin.me_mode_bin : to determine the mode with binned data
    
    References
    ----------
    Larson, R., & Farber, E. (2014). *Elementary statistics: Picturing the world* (6th ed.). Pearson.
    
    Pearson, K. (1895). Contributions to the mathematical theory of evolution. II. Skew variation in homogeneous material. *Philosophical Transactions of the Royal Society of London. (A.), 186*, 343–414. https://doi.org/10.1098/rsta.1895.0010
    
    Spiegel, M. R., & Stephens, L. J. (2008). *Schaum’s outline of theory and problems of statistics* (4th ed.). McGraw-Hill.
    
    Weisstein, E. W. (2002). *CRC concise encyclopedia of mathematics* (2nd ed.). Chapman & Hall/CRC.
    
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
    >>> me_mode(ex1)
            mode  mode freq.
    0  [MARRIED]         972
    
    Example 2: a list
    >>> ex2 = ["MARRIED", "DIVORCED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "NEVER MARRIED", "MARRIED", "MARRIED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "MARRIED"]
    >>> me_mode(ex2)
             mode  mode freq.
    0  [DIVORCED]           7
    
    Example 3: Multi-Mode
    >>> ex3a = [1, 1, 2, 3, 3, 4, 5, 6, 6]
    >>> me_mode(ex3a)
                  mode  mode freq.
    0  [1.0, 3.0, 6.0]           2
    >>> ex3b = ["MARRIED", "DIVORCED", "MARRIED", "DIVORCED", "DIVORCED", "NEVER MARRIED", "MARRIED"]
    >>> me_mode(ex3b)
                      mode  mode freq.
    0  [MARRIED, DIVORCED]           3

    Example 4: All Equal
    >>> ex4a = [1, 1, 2, 2, 3, 3, 6, 6]
    >>> me_mode(ex4a)
            mode mode freq.
    0  [no mode]         na
    >>> ex4b = [1, 1, 2, 2, 3, 3, 6, 6]
    >>> me_mode(ex4b, allEq="all")
                       mode  mode freq.
    0  [1.0, 2.0, 3.0, 6.0]           2
        
    '''
    
    if type(data) == list:
        data = pd.Series(data)
    
    freq = data.value_counts()
    maxCount = freq.max()
    modes = []
    for i in range(len(freq)):
        if freq.values[i]==maxCount:
            modes = np.append(modes, freq.index[i])
    
    if len(modes)==len(freq) and allEq=="none":
        modes = ['no mode']
        maxCount = "na"
    
    res = pd.DataFrame(list([[modes, maxCount]]), columns = ["mode", "mode freq."])
        
    return res