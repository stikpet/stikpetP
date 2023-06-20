import pandas as pd

def es_cramer_v_gof(chi2, n, k, bergsma=False):
    '''
    Cramer's V for Goodness-of-Fit
     
    Cramér's V is one possible effect size when using a chi-square test. This measure is actually designed for the chi-square test for independence but can be adjusted for the goodness-of-fit test (Kelley & Preacher, 2012, p. 145; Mangiafico, 2016, p. 474). 
    
    It gives an estimate of how well the data then fits the expected values, where 0 would indicate that they are exactly equal. If you use the equal distributed expected values the maximum value would be 1, otherwise it could actually also exceed 1.
    
    As for a classification Cramér's V can be converted to Cohen w, for which Cohen provides rules of thumb.
    
    A Bergsma correction is also possible.
    
    Parameters
    ----------
    chi2 : the chi-square test statistic
    n : the sample size
    k : the number of categories
    bergsma : optional boolean to indicate the use of the Bergsma correction (default is False)
        
    Returns
    -------
    v : Cramer's V value
   
    Notes
    -----
    The formula used is:
    $$V=\\sqrt\\frac{\\chi_{GoF}^{2}}{n\\times \\left(k - 1\\right)}$$
    
    *Symbols used*:
    * *\(k\) the number of categories
    * *\(n\) the sample size, i.e. the sum of all frequencies
    * *\(\\chi_{GoF}^{2}\) the chi-square value of a Goodness-of-Fit test
    
    The Bergsma correction uses a different formula.
    $$\\tilde{V} = \\sqrt{\\frac{\\tilde{\\varphi}^2}{\\tilde{k} - 1}}$$
    
    With:
    $$\\tilde{\\varphi}^2 = max\\left(0,\\varphi^2 - \\frac{k - 1}{n - 1}\\right)$$
    $$\\tilde{k} = k - \\frac{\\left(k - 1\\right)^2}{n - 1}$$
    $$\\varphi^2 = \\frac{\\chi_{GoF}^{2}}{n}$$
    
    Cramér described V (1946, p. 282) for use with a test of independence. Others (e.g. K. Kelley & Preacher, 2012, p. 145; Mangiafico, 2016a, p. 474) added that this can also be use for goodness-of-fit tests.
    
    For the Bergsma (2013, pp. 324-325) correction the same thing applies
    
    Cramér's V can be converted to Cohen's w using *es_convert(v, from="cramervgof", to = "cohenw", ex1 = df)*
    
    Rules-of-thumb for the interpretation can then be used, using *th_cohen_w(w)*
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    '''
    
    df = k - 1
    
    if bergsma:
        kAvg = k - df**2/(n - 1)
        phi2 = chi2/n
        phi2Avg = max(0, phi2 - df/(n - 1))
        v = (phi2Avg/(kAvg - 1))**0.5
    else:
        v = (chi2/(n * df))**0.5
    
    return v    