import pandas as pd

def th_cohen_h(h, qual="cohen"):
    '''
    Rule of thumb for Cohen h
    
    Simple function to use a rule-of-thumb for the Cohen h effect size.
    
    Parameters
    ----------
    h : the Cohen h value
    qual : optional indication which set of rule-of-thumb to use. Currently only "cohen"
    
    Returns
    -------
    results : Pandas dataframe with the classification and source used
    
    Notes
    -----
    Cohen's rule of thumb for Cohen h (1988, p. 198):
    
    |\|h\|| Interpretation|
    |---|----------|
    |0.00 < 0.20 | negligible |
    |0.20 < 0.50 | small |
    |0.50 < 0.80 | medium |
    |0.80 or more | large |
    
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
    
    #Cohen (1988, pp. 184-185)
    if (qual=="cohen"):
        ref = "Cohen (1988, p. 198)"
        if (abs(h)<0.2):
            qual = "negligible"
        elif (abs(h)<0.5):
            qual = "small"
        elif (abs(h)<0.8):
            qual = "medium"
        else:
            qual = "large"
            
    results = pd.DataFrame([[qual, ref]], columns=["classification", "reference"])
    
    return(results)