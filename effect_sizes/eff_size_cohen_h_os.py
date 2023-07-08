import math
import pandas as pd

def es_cohen_h_os(data, codes=None, p0=0.5):
    '''
    Cohen's h'
    ----------
     
    An adaptation of Cohen h for a one-sample case. It is an effect size measure that could be accompanying a one-sample binomial, score or Wald test.
    
    See also https://youtu.be/ddWe94VKX_8, a video on Cohen h'.
    
    Parameters
    ----------
    data : list or pandas data series 
        the data
    codes : list, optional 
        list with the two codes to use
    p0 : float, optional 
        probability for first category (the default is 0.5)
        
    Returns
    -------
    h2 : float
        Cohen's h' value.
   
    Notes
    -----
    Formula used (Cohen, 1988, p. 202):
    $$h'=\\phi_{1}-\\phi_{h_0}$$
    
    With:
    $$\\phi_{i}=2\\times\\text{arcsin}\\sqrt{p_{i}}$$
    $$p_i = \\frac{F_i}{n}$$
    $$n = \\sum_{i=1}^k F_i$$
    
    *Symbols used*:
    
    * \\(F_i\\) is the (absolute) frequency (count) of category i
    * \\(n\\) is the sample size, i.e. the sum of all frequencies
    * \\(p_i\\) the proportion of cases in category i
    * \\(p_{h_0}\\) the expected proportion (i.e. the proportion according to the null hypothesis)
    
    See Also
    --------
    stikpetP.effect_sizes.convert_es.es_convert : to convert Cohen h' to Cohen h, use fr="cohenhos" and to=cohenh
    stikpetP.other.thumb_cohen_h.th_cohen_h : rules-of-thumb for Cohen g
    
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
    >>> es_cohen_h_os(ex1)
    0.2526802551420786
    >>> es_cohen_h_os(ex1, p0=0.3)
    0.6641971012095669
    
    Example 2: pandas Series
    >>> import pandas as pd
    >>> df1 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/GSS2012a.csv', sep=',', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> es_cohen_h_os(df1['sex'])
    0.10250973241574934
    >>> es_cohen_h_os(df1['mar1'], codes=["DIVORCED", "NEVER MARRIED"])
    -0.11449540934184599
    
    '''
    
    if type(data) is list:
        data = pd.Series(data)
        
    if codes is None:
        freq = data.value_counts()
        n1 = freq.values[0]        
        n = sum(freq.values)
        n2 = n - n1
    else:
        #Determine number of successes
        n1 = sum(data==codes[0])
        n2 = sum(data==codes[1])
        n = n1 + n2
        
    p1 = n1/n
    
    phi1 = 2 * math.asin(p1**0.5)
    phic = 2 * math.asin(p0**0.5)
    
    h2 = phi1 - phic
    
    return (h2)