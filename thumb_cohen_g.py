import pandas as pd

def th_cohen_g(g, qual="cohen"):
    '''
    Rule of thumb for Cohen g
    
    Simple function to use a rule-of-thumb for the Cohen g effect size.
    
    Parameters
    ----------
    g : the Cohen g value
    qual : optional indication which set of rule-of-thumb to use. Currently only "cohen"
    
    Returns
    -------
    results : Pandas dataframe with the classification and source used
    
    Notes
    -----
    Cohen's rule of thumb for Cohen g (1988, pp. 147-149):
    
    |\|g\|| Interpretation|
    |---|----------|
    |0.00 < 0.05 | negligible |
    |0.05 < 0.15 | small |
    |0.15 < 0.25 | medium |
    |0.25 or more | large |
    
    References
    ----------
    Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). L. Erlbaum Associates.
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    Examples
    -------
    >>> g = 0.24
    >>> th_cohen_g(g)
    
    
    '''
    
    if (qual=="cohen"):
        ref = "Cohen (1988, pp. 147-149)"
    
    if (abs(g)<0.05):
        qual = "negligible"
    elif (abs(g)<0.15):
        qual = "small"
    elif (abs(g)<0.25):
        qual = "medium"
    else:
        qual = "large"
        
    results = pd.DataFrame([[qual, ref]], columns=["classification", "reference"])
    
    return(results)