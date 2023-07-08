import math
import pandas as pd

def es_hedges_g_os(data, mu=None, appr=None):
    '''
    Hedges g (one-sample)
    ---------------------
    
    This function will calculate Hedges g (one-sample). An effect size measure that can be used with a test for a single mean (for example a one-sample Student t-test).
    
    Hedges g is a correction for Cohen's d'. Actually Hedges (1981) didn't seem to have a one-sample version for Hedges g, and this correction is the one for Hedges g used for the independent samples.
    
    Parameters
    ----------
    data : list
        numeric list with numbers
    mu : float
        the hypothesized mean
    appr : {None, 'hedges', 'durlak', 'xue'}, optional
        approximation to use. Default is None 
    
    Returns
    -------
    results : pandas dataframe with:
    
    * *mu*, the hypothesized mean used
    * *g*, Hedges g for a one-sample
    * *version*, description of version used.
    
    Notes
    -----
    The formula used for the exact method (appr=NULL) (Hedges, 1981, p. 111):
    $$g = d' \\times\\frac{\\Gamma\\left(m\\right)}{\\Gamma\\left(m - \\frac{1}{2}\\right)\\times\\sqrt{m}}$$
    
    With:
    $$m = \\frac{df}{2}$$
    $$df = n - 1$$
    
    *Symbols used:*
    
    * \\(d'\\) Cohen’s d for one-sample
    * \\(df\\) the degrees of freedom
    * \\(n\\) the sample size (i.e. the number of scores)
    * \\(\\Gamma\\left(\\dots\\right)\\) the gamma function
    
    The formula used for the approximation from Hedges (1981, p. 114) (appr="hedges"):
    $$g = d' \\times\\left(1 - \\frac{3}{4\\times df - 1}\\right)$$
    
    The formula used for the approximation from Durlak (2009, p. 927) (appr="durlak"):
    $$g = d' \\times\\frac{n - 3}{n - 2.25} \\times\\sqrt{\\frac{n - 2}{n}}$$
    
    The formula used for the approximation from Xue (2020, p. 3) (appr="xue"):
    $$g = d' \\times \\sqrt[12]{1 - \\frac{9}{df} + \\frac{69}{2\\times df^2} - \\frac{72}{df^3} + \\frac{687}{8\\times df^4} - \\frac{441}{8\\times df^5} + \\frac{247}{16\\times df^6}}$$
    
    Since Hedges g is a correction for Cohen d', it can be converted to a 'regular' Cohen d and then rules of thumb for the interpertation could be used. 
    
    See Also
    --------
    stikpetP.effect_sizes.convert_es.es_convert : to convert Cohen d one-sample to Cohen d, use fr="cohendos" and to="cohend"
    stikpetP.other.thumb_cohen_d.th_cohen_d : rules-of-thumb for Cohen d
    
    References
    ----------
    Durlak, J. A. (2009). How to select, calculate, and interpret effect sizes. *Journal of Pediatric Psychology, 34*(9), 917–928. https://doi.org/10.1093/jpepsy/jsp004
    
    Hedges, L. V. (1981). Distribution Theory for Glass’s Estimator of Effect Size and Related Estimators. *Journal of Educational Statistics, 6*(2), 107–128. https://doi.org/10.2307/1164588
    
    Xue, X. (2020). Improved approximations of Hedges’ g*. https://doi.org/10.48550/arXiv.2003.06675
    
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
    >>> es_hedges_g_os(ex1)
         mu         g version
    0  68.5 -2.857185   exact
    
    Example 2: Numeric list
    >>> ex2 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    >>> es_hedges_g_os(ex2)
        mu         g version
    0  3.0  0.268649   exact
    
    '''
    #data as a pandas series
    if type(data) is list:
        data = pd.Series(data)
        
    #set hypothesized median to mid range if not provided
    if (mu is None):
        mu = (min(data) + max(data)) / 2
    
    #remove missing values
    data = data.dropna()
    
    # sample size and degrees of freedom
    n = len(data)
    df = n - 1
    
    # sample mean and standard deviation
    avg = sum(data)/n
    s = (sum((data-avg)**2)/df)**(1/2)
    
    # Cohen's d for one-sample
    d = (avg - mu) / s
    
    # helper variable m
    m = df/2
    
    if appr is None and m < 172:
        g = d*math.gamma(m)/(math.gamma(m-0.5)*m**(1/2))
        comment = "exact"
    elif appr=="hedges":
        g = d*(1 - 3/(4*df-1))
        comment = "Hedges approximation"
    elif appr=="durlak":
        g = d*(n-3)/(n-2.25)*((n-2)/n)**0.5
        comment = "Durlak approximation"
    else:
        g = d*(1-9/df+69/(2*df**2)-72/(df**3)+687/(8*df**4)-441/(8*df**5)+247/(16*df**6))**(1/12)
        comment = "Xue approximation"
    
    # print warning if exact was asked but couldn't be used
    if appr=="none" and m >= 172:
        print("WARNING: exact method could not be computed due to large sample size, Xue approximation used instead")
        comment = "Xue approximation"
    
    
    results = pd.DataFrame([[mu, g, comment]], columns=["mu", "g", "version"])
        
    pd.set_option('display.max_colwidth', None)
    
    return results
