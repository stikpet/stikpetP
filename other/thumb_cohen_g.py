import pandas as pd

def th_cohen_g(g, qual="cohen"):
    '''
    Rule of thumb for Cohen g
    --------------------------
    
    Simple function to use a rule-of-thumb for the Cohen g effect size.
    
    Parameters
    ----------
    g : float
        the Cohen g value
    qual : {"cohen"}, optional 
        indication which set of rule-of-thumb to use. Currently only "cohen" (default)
    
    Returns
    -------
    results : a pandas dataframe with.
    
    * *classification*, the qualification of the effect size
    * *reference*, a reference for the rule of thumb used
    
    Notes
    -----
    Cohen's rule of thumb for Cohen g (1988, pp. 147-149):
    
    |\\|g\\|| Interpretation|
    |---|----------|
    |0.00 < 0.05 | negligible |
    |0.05 < 0.15 | small |
    |0.15 < 0.25 | medium |
    |0.25 or more | large |
    
    See Also
    --------
    stikpetP.effect_sizes.eff_size_cohen_g.es_cohen_g : to determine a Cohen g
    
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
    >>> th_cohen_g(es)
      classification                  reference
    0          large  Cohen (1988, pp. 147-149)
    
    
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