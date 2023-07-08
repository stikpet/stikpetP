import pandas as pd

def th_cohen_w(w, qual="cohen"):
    '''
    Rule of thumb for Cohen w
    --------------------------
    
    Simple function to use a rule-of-thumb for the Cohen w effect size.
    
    Parameters
    ----------
    w : float
        the Cohen w value
    qual : {"cohen"}, optional 
        indication which set of rule-of-thumb to use. Currently only "cohen"
    
    Returns
    -------
    results : a pandas dataframe with.
    
    * *classification*, the qualification of the effect size
    * *reference*, a reference for the rule of thumb used
    
    Notes
    -----
    Cohen's rule of thumb for Cohen h (1988, p. 227):
    
    |\\|w\\|| Interpretation|
    |---|----------|
    |0.00 < 0.10 | negligible |
    |0.10 < 0.30 | small |
    |0.30 < 0.50 | medium |
    |0.50 or more | large |
    
    See Also
    --------
    stikpetP.effect_sizes.eff_size_cohen_w.es_cohen_w : to determine a Cohen w
    
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
    -------
    >>> es = 0.6
    >>> th_cohen_w(es)
      classification             reference
    0          large  Cohen (1988, p. 227)
    
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