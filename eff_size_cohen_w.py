import pandas as pd

def es_cohen_w(chi2, n):
    '''
    Cohen's w
     
    An effect size measure that could be used with a chi-square test. It has no upper limit, but can be compared to Cohen's rules-of-thumb. 
    
    Parameters
    ----------
    chi2 : the chi-square test statistic
    n : the sample size
        
    Returns
    -------
    w : value of Cohen's w
   
    Notes
    -----
    The formula used is (Cohen, 1988, p. 216):
    $$w = \sqrt\frac{\chi_{GoF}^{2}}{n}$$
    
    *Symbols used*:
    * \(\chi_{GoF}^{2}\) the Pearson chi-square goodness-of-fit value 
    * \(n\) the sample size, i.e. the sum of all frequencies
    
    The chi-square value could for example be obtained using the **ts_pearson_gof()** function.
    
    For a classification using some rule-of-thumb run **th_cohen_w()**.
    
    References 
    ----------
    Cohen, J. (1988). Statistical power analysis for the behavioral sciences (2nd ed.). L. Erlbaum Associates.

    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    Examples
    --------
    >>> chi2 = 3.105263
    >>> n = 19
    >>> es_cohen_w(chi2, n)

    '''
    
    w = (chi2 / n)**0.5
    
    return w
