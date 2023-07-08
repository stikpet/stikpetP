import pandas as pd

def es_cohen_w(chi2, n):
    '''
    Cohen's w
    ---------
     
    An effect size measure that could be used with a chi-square test. It has no upper limit, but can be compared to Cohen's rules-of-thumb. 
    
    Parameters
    ----------
    chi2 : float
        the chi-square test statistic
    n : int
        the sample size
        
    Returns
    -------
    w : float
        value of Cohen's w
   
    Notes
    -----
    The formula used is (Cohen, 1988, p. 216):
    $$w = \\sqrt\\frac{\\chi_{GoF}^{2}}{n}$$
    
    *Symbols used*:
    
    * \\(\\chi_{GoF}^{2}\\) the Pearson chi-square goodness-of-fit value 
    * \\(n\\) the sample size, i.e. the sum of all frequencies
    
    See Also
    --------
    stikpetP.tests.test_pearson_gof.ts_pearson_gof : to obtain a chi-square value
    stikpetP.other.thumb_cohen_w.th_cohen_w : rules-of-thumb for Cohen w
    
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
    >>> chi2 = 3.106
    >>> n = 19
    >>> es_cohen_w(chi2, n)
    0.40431879032581
    
    
    '''
    
    w = (chi2 / n)**0.5
    
    return w
