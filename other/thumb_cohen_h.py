import pandas as pd

def th_cohen_h(h, qual="cohen"):
    '''
    Rule of thumb for Cohen h
    -------------------------
    
    Simple function to use a rule-of-thumb for the Cohen h effect size.
    
    Parameters
    ----------
    h : float
        the Cohen h value
    qual : {"cohen"}, optional 
        indication which set of rule-of-thumb to use. Currently only "cohen" (default)
    
    Returns
    -------
    results : a pandas dataframe with.
    
    * *classification*, the qualification of the effect size
    * *reference*, a reference for the rule of thumb used
    
    Notes
    -----
    Cohen's rule of thumb for Cohen h (1988, p. 198):
    
    |\\|h\\|| Interpretation|
    |---|----------|
    |0.00 < 0.20 | negligible |
    |0.20 < 0.50 | small |
    |0.50 < 0.80 | medium |
    |0.80 or more | large |
    
    See Also
    --------
    stikpetP.effect_sizes.eff_size_cohen_h_os.es_cohen_h_os : to determine a Cohen h' then use
    
    stikpetP.effect_sizes.convert_es.es_convert : to convert this to Cohen h
    
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
    >>> es = 0.6
    >>> th_cohen_h(es)
      classification             reference
    0         medium  Cohen (1988, p. 198)
    
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