import pandas as pd

def es_cohen_g(data, codes=None):
    '''
    Cohen's g
    ---------
     
    Cohen’s g (Cohen, 1988) is an effect size measure that could be accompanying a one-sample binomial (see Rosnow & Rosenthal, 2003), score or Wald test. It is simply the difference of the sample proportion with 0.5. 
    
    A video explanation of Cohen g can be found at https://youtu.be/tPZMvB8QrM0
    
    Parameters
    ----------
    data : list or pandas data series 
        the data
    codes : list, optional 
        list with the two codes to use
        
    Returns
    -------
    g : float
        Cohen's g value.
   
    Notes
    -----
    The formula used is (Cohen, 1988, p. 147):
    $$g=p-0.5$$
    
    *Symbols used*:
    
    * \\(p\\) is the sample proportion
    
    See Also
    --------
    stikpetP.other.thumb_cohen_g.th_cohen_g : rules-of-thumb for Cohen g
    
    References
    ----------
    Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). L. Erlbaum Associates.
    
    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    --------
    Example 1: Numeric list
    >>> ex1 = [1, 1, 2, 1, 2, 1, 2, 1]
    >>> es_cohen_g(ex1)
    0.125
    
    Example 2: pandas Series
    >>> import pandas as pd
    >>> df1 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/GSS2012a.csv', sep=',', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> es_cohen_g(df1['sex'])
    0.05116514690982776
    >>> es_cohen_g(df1['mar1'], codes=["DIVORCED", "NEVER MARRIED"])
    -0.057122708039492265
    
    '''
    
    if type(data) is list:
        data = pd.Series(data)
        
    if codes is None:
        freq = data.value_counts()
        n = sum(freq.values)
        p1 = freq.values[0]/n
    
    else:
        #Determine number of successes
        n1 = sum(data==codes[0])
        n2 = sum(data==codes[1])
        n = n1 + n2
        p1 = n1/n
        
    g = p1 - 0.5
    
    return (g)