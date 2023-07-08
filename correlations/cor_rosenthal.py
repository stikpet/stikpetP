import pandas as pd

def r_rosenthal(zVal, n):
    '''
    Rosenthal Correlation Coefficient
    ---------------------------------
     
    This function will calculate Rosenthal Correlation Coefficient. A simple correlation coefficient that divides a z-score by the square root of the sample size.
    
    Parameters
    ----------
    zVal : float
        the z-value of test
    n : int
        the sample size
        
    Returns
    -------
    r : float
        the Rosenthal correlation coefficient value.
   
    Notes
    -----
    The formula used (Rosenthal, 1991, p. 19):
    $$r = \\frac{z}{\\sqrt{n}}$$
    
    *Symbols used:*
    
    * \\(n\\) the sample size
    * \\(z\\) the calculated z-statistic value
    
    Rosenthal (1991) is the oldest reference I could find for this correlation coefficient. However, Cohen (1988, p. 275) actually has a measure 'f' that has the same equation.
    
    See Also
    --------
    stikpetP.other.thumb_pearson_r.th_pearson_r : rules of thumb for a Pearson correlation coefficient.
    
    References 
    ----------
    Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). L. Erlbaum Associates.
    
    Rosenthal, R. (1991). *Meta-analytic procedures for social research* (Rev. ed). Sage Publications.
    
    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    --------
    >>> z = 1.143943
    >>> n = 20
    >>> r_rosenthal(z, n)
    0.25579343103850416
    
    '''
    
    r = abs(zVal / (n**0.5))
    
    return (r)