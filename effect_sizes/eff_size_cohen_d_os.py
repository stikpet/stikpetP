from statistics import mean, stdev
import pandas as pd

def es_cohen_d_os(data, mu=None):
    '''
    Cohen d'
    --------
     
    This function will calculate Cohen d' (one-sample). An effect size measure that can be used with a test for a single mean (for example a one-sample Student t-test).
    
    Parameters
    ----------
    data : list or pandas series 
        the numeric scores
    mu : float, optional 
        the hypothesized mean. If not used the midrange is used
        
    Returns
    -------
    dos : Cohen d' value
   
    Notes
    -----
    The formula used (Cohen, 1988, p. 46):
    $$d'=\\frac{\\bar{x}-\\mu_{H_{0}}}{s}$$
    With:
    $$s = \\sqrt{\\frac{\\sum_{i=1}^n \\left(x_i - \\bar{x}\\right)^2}{n - 1}}$$
    $$\\bar{x} = \\frac{\\sum_{i=1}^n x_i}{n}$$
    
    *Symbols used:*
    
    * \\(\\bar{x}\\) the sample mean
    * \\(\\mu_{H_0}\\) the hypothesized mean in the population
    * \\(n\\) the sample size (i.e. the number of scores)
    * \\(s\\) the unbiased sample standard deviation
    * \\(x_i\\) the i-th score
    
    Cohen d' can be converted to a 'regular' Cohen d and then rules of thumb for the interpertation 
    could be used. 
    
    See Also
    --------
    stikpetP.effect_sizes.convert_es.es_convert : to convert Cohen's d one-sample to Cohen d, use *fr = "cohendos"* and *to = "cohend"*
    stikpetP.other.thumb_cohen_d.th_cohen_d : rules-of-thumb for Cohen d
    
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
    Example 1: Numeric Pandas Series
    >>> import pandas as pd
    >>> df2 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/StudentStatistics.csv', sep=';', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> ex1 = df2['Gen_Age']
    >>> es_cohen_d_os(ex1)
    2.9082571798993557
    
    Example 2: Numeric list
    >>> ex2 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    >>> es_cohen_d_os(ex2)
    0.28127524771945256
    
    '''
    #data as a pandas series
    if type(data) is list:
        data = pd.Series(data)
    
    #remove missing values
    data = data.dropna()
    
    #set hypothesized median to mid range if not provided
    if (mu is None):
        mu = (min(data) + max(data)) / 2
        
    xBar = mean(data)
    s = stdev(data)
    dos = abs(xBar - mu)/s
    
    return dos