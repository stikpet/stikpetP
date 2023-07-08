import pandas as pd

def me_mode_bin(data, bins, allEq="none", value="none"):
    '''
    Mode for Binned Data
    --------------------
    
    The mode is a measure of central tendency and defined as “the abscissa corresponding to the ordinate of maximum frequency” (Pearson, 1895, p. 345). A more modern definition would be “the most common value obtained in a set of observations” (Weisstein, 2002).

    For binned data the mode is the bin with the highest frequency density. This will have the same result as using the highest frequency if all bins are of equal size. A frequency density is the frequency divided by the bin size (Zedeck, 2014, pp. 144-145). Different methods exist to narrow this down to a single value. See the notes for more info on this.

    The word mode might even come from the French word 'mode' which means fashion. Fashion is what most people wear, so the mode is the option most people chose.

    If one category has the highest frequency this category will be the modal category and if two or more categories have the same highest frequency each of them will be the mode. If there is only one mode the set is sometimes called unimodal, if there are two it is called bimodal, with three trimodal, etc. For two or more, thse term multimodal can also be used.

    An advantage of the mode over many other measures of central tendency (like the median and mean), is that it can be determined for already nominal data types.

    Parameters
    ----------
    data : list or pandas data series
    bins : list 
        a list with tuples, each a lower and upper bound
    allEq : {"none", "all"}, optional 
        indicator on what to do if maximum frequency is equal for more than one category. Default is "none"
    value : {"none", "midpoint", "quadratic"} 
        optional which value to show in the output. Default is "none"

    Returns
    -------
    A pandas dataframe with:

    * *mode*, the mode(s)
    * *mode fd*, frequency density of the mode

    Notes
    -----
    **Value to return**

    If *value="midpoint"* is used the modal bin(s) midpoints are shown, using:
    $$MP_m = \\frac{UB_m + LB_m}{2}$$
    Where \\(UB_m\\) is the upper bound of the modal bin, and \\(LB_m\\) the lower bound.

    If *value="quadratic"* is used a quadratic curve is made from the midpoint of the bin prior to the modal bin, to 
    the midpoint of the bin after the modal bin. This is done using:
    $$M = LB_{m} + \\frac{d_1}{d_1 + d_2}\\times\\left(UB_m - LB_m\\right)$$
    With:
    $$d_1 = FD_m - FD_{m -1}$$
    $$d_2 = FD_m - FD_{m + 1}$$

    Where \\(FD_m\\) is the frequency density of the modal category.

    **Multimode**

    One small controversy exists if all categories have the same frequency. In this case none of them has a higher 
    occurence than the others, so none of them would be the mode (see for example Spiegel & Stephens, 2008, p. 64, 
    Larson & Farber, 2014, p. 69). This is used when *allEq="none"* and the default.

    On a rare occasion someone might argue that if all categories have the same frequency, then all categories are 
    part of the mode since they all have the highest frequency. This is used when *allEq="all"*.

    The function can return the bins that are the modal bins, by setting *value="none"*.

    References
    ----------
    Larson, R., & Farber, E. (2014). *Elementary statistics: Picturing the world* (6th ed.). Pearson.

    Pearson, K. (1895). Contributions to the mathematical theory of evolution. II. Skew variation in homogeneous material. *Philosophical Transactions of the Royal Society of London. (A.), 186*, 343–414. https://doi.org/10.1098/rsta.1895.0010

    Spiegel, M. R., & Stephens, L. J. (2008). *Schaum’s outline of theory and problems of statistics* (4th ed.). McGraw-Hill.

    Weisstein, E. W. (2002). *CRC concise encyclopedia of mathematics* (2nd ed.). Chapman & Hall/CRC.

    Zedeck, S. (Ed.). (2014). *APA dictionary of statistics and research methods*. American Psychological Association.

    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    --------
    >>> import pandas as pd
    >>> df1 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/GSS2012a.csv', sep=',', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> ex1 = df1['age']
    >>> ex1 = ex1.replace({'89 OR OLDER': 89})
    >>> ex1 = pd.to_numeric(ex1)
    >>> bins = [(0, 20), (20, 50), (50, 70), (70, 90)]
    >>> me_mode_bin(ex1, bins=bins)
          mode   mode fd.
    0  20 < 50  34.833333
    
    '''
    if type(data) is list:
        data = pd.Series(data)
        
    freq = pd.DataFrame(columns=["lb", "ub", "f", "fd"])
    for i in bins:
        f = len(data[((data < i[1]) * (data >= i[0]))])
        fd = f/(i[1] - i[0])
        freq = pd.concat([freq, pd.DataFrame([{"lb": i[0], "ub": i[1], "f": f, "fd": fd}])])
        
    modeFD = max(freq['fd'])
    nModes = sum(freq['fd']==modeFD)
    k = len(freq)
    
    if nModes==k and allEq=="none":
        mode = "none"
        modeFD = "none"
    else:
        if value=="midpoint":
            ff = 0
            for i in range(0,k):
                if freq.iloc[i, 3] == modeFD:
                    newMode = (freq.iloc[i, 1] + freq.iloc[i, 0])/2
                    if ff==0:
                        mode = newMode
                        ff = ff + 1
                    else:
                        mode = str(mode) + ", " + str(newMode)
        elif value=="quadratic":
            ff = 0
            for i in range(0,k):
                if freq.iloc[i, 3] == modeFD:
                    if i==0:
                        d1 = modeFD
                    elif i==(k-1):
                        d2 = modeFD
                    else:
                        d1 = modeFD - freq.iloc[i-1, 3]
                        d2 = modeFD - freq.iloc[i+1, 3]
                
                    newMode = freq.iloc[i, 0] + d1/(d1 + d2) * (freq.iloc[i, 1] - freq.iloc[i, 0])
                    
                    if ff==0:
                        mode = newMode
                        ff = ff + 1
                    else:
                        mode = str(mode) + ", " + str(newMode) 
                        
        elif value == "none":
            ff = 0
            for i in range(0,k):
                if freq.iloc[i, 3] == modeFD:
                    newMode = str(freq.iloc[i, 0]) + " < " + str(freq.iloc[i, 1])
                    if ff==0:
                        mode = newMode
                        ff = ff + 1
                    else:
                        mode = str(mode) + ", " + str(newMode)
                    
    res = pd.DataFrame(list([[mode, modeFD]]), columns = ["mode", "mode fd."])
    
    return (res)