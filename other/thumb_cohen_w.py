import pandas as pd

def th_cohen_w(w, qual="cohen"):
    '''
    Rule of thumb for Cohen w
    
    Simple function to use a rule-of-thumb for the Cohen w effect size.
    
    Parameters
    ----------
    w : the Cohen w value
    qual : optional indication which set of rule-of-thumb to use. Currently only "cohen"
    
    Returns
    -------
    results : Pandas dataframe with the classification and source used
    
    Notes
    -----
    Cohen's rule of thumb for Cohen h (1988, p. 227):
    
    |\|w\|| Interpretation|
    |---|----------|
    |0.00 < 0.10 | negligible |
    |0.10 < 0.30 | small |
    |0.30 < 0.50 | medium |
    |0.50 or more | large |
    
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
    >>> w = 0.24
    >>> th_cohen_w(w)
    
    
    '''
    
    if (qual=="cohen"):
        ref = "Cohen (1988, p. 227)"
        if (abs(w)<0.1):
            qual = "negligible"
        elif (abs(w)<0.3):
            qual = "small"
        elif (abs(w)<0.5):
            qual = "medium"
        else:
            qual = "large"
            
    results = pd.DataFrame([[qual, ref]], columns=["classification", "reference"])
    
    return(results)