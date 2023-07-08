import pandas as pd

def es_cramer_v_gof(chi2, n, k, bergsma=False):
    '''
    Cramer's V for Goodness-of-Fit
    ------------------------------
     
    Cramér's V is one possible effect size when using a chi-square test. This measure is actually designed for the chi-square test for independence but can be adjusted for the goodness-of-fit test (Kelley & Preacher, 2012, p. 145; Mangiafico, 2016, p. 474). 
    
    It gives an estimate of how well the data then fits the expected values, where 0 would indicate that they are exactly equal. If you use the equal distributed expected values the maximum value would be 1, otherwise it could actually also exceed 1.
    
    As for a classification Cramér's V can be converted to Cohen w, for which Cohen provides rules of thumb.
    
    A Bergsma correction is also possible.
    
    Parameters
    ----------
    chi2 : float
        the chi-square test statistic
    n : int
        the sample size
    k : int
        the number of categories
    bergsma : boolean, optional 
        to indicate the use of the Bergsma correction (default is False)
        
    Returns
    -------
    v : float
        Cramer's V value
   
    Notes
    -----
    The formula used is:
    $$V=\\sqrt\\frac{\\chi_{GoF}^{2}}{n\\times \\left(k - 1\\right)}$$
    
    *Symbols used*:
    
    * \\(k\\) the number of categories
    * \\(n\\) the sample size, i.e. the sum of all frequencies
    * \\(\\chi_{GoF}^{2}\\) the chi-square value of a Goodness-of-Fit test
    
    The Bergsma correction uses a different formula.
    $$\\tilde{V} = \\sqrt{\\frac{\\tilde{\\varphi}^2}{\\tilde{k} - 1}}$$
    
    With:
    $$\\tilde{\\varphi}^2 = max\\left(0,\\varphi^2 - \\frac{k - 1}{n - 1}\\right)$$
    $$\\tilde{k} = k - \\frac{\\left(k - 1\\right)^2}{n - 1}$$
    $$\\varphi^2 = \\frac{\\chi_{GoF}^{2}}{n}$$
    
    Cramér described V (1946, p. 282) for use with a test of independence. Others (e.g. K. Kelley & Preacher, 2012, p. 145; Mangiafico, 2016a, p. 474) added that this can also be use for goodness-of-fit tests.
    
    For the Bergsma (2013, pp. 324-325) correction the same thing applies
    
    See Also
    --------
    stikpetP.effect_sizes.convert_es.es_convert : to convert Cramér's V (GoF) to Cohen w, use fr="cramervgof" and to="cohenw"
    stikpetP.other.thumb_cohen_w.th_cohen_w : rules-of-thumb for Cohen w
    
    References
    ----------
    Bergsma, W. (2013). A bias-correction for Cramér’s and Tschuprow’s. *Journal of the Korean Statistical Society, 42*(3), 323–328. https://doi.org/10.1016/j.jkss.2012.10.002
    
    Cramér, H. (1946). *Mathematical methods of statistics*. Princeton University Press.
    
    Kelley, K., & Preacher, K. J. (2012). On effect size. *Psychological Methods, 17*(2), 137–152. https://doi.org/10.1037/a0028086
    
    Mangiafico, S. S. (2016). *Summary and analysis of extension program evaluation in R* (1.13.5). Rutger Cooperative Extension.

    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    --------
    >>> chi2Value = 3.106
    >>> n = 19
    >>> k = 3
    >>> es_cramer_v_gof(chi2Value, n, k)
    0.2858965584005221
    >>> es_cramer_v_gof(chi2Value, n, k, bergsma=True)
    0.17162152361641894
    
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