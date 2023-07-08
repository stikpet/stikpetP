import pandas as pd

def th_cohen_d(d, qual="sawilowsky"):
    '''
    Rules of Thumb for Cohen d
    --------------------------
     
    This function will give a qualification (classification) for Cohen d
    
    Parameters
    ----------
    d : float
        the Cohen d value
    qual : {"sawilowsky", "cohen", "lovakov", "rosenthal"} optional 
        the rule of thumb to be used. Default is "sawilowsky"
        
    Returns
    -------
    results : a pandas dataframe with.
    
    * *classification*, the qualification of the effect size
    * *reference*, a reference for the rule of thumb used
   
    Notes
    -----
    The following rules-of-thumb can be used:
    
    *"cohen"* => Uses Cohen (1988, p. 40):
    
    |\\|d\\|| Interpretation|
    |---|----------|
    |0.00 < 0.20 | negligible |
    |0.20 < 0.50 | small |
    |0.50 < 0.80 | medium |
    |0.80 or more | large |
    
    *"lovakov"* => Lovakov and Agadullina (2021, p. 501):
    
    |\\|d\\|| Interpretation|
    |---|----------|
    |0.00 < 0.15 | negligible |
    |0.15 < 0.35 | small |
    |0.35 < 0.65 | medium |
    |0.65 or more | large |
    
    *"rosenthal"* => Rosenthal (1996, p. 45):
    
    |\\|d\\|| Interpretation|
    |---|----------|
    |0.00 < 0.20 | negligible |
    |0.20 < 0.50 | small |
    |0.50 < 0.80 | medium |
    |0.80 < 1.30 | large |
    |1.30 or more | very large |
    
    *"sawilowsky"* => Sawilowsky (2009, p. 599):
    
    |\\|d\\|| Interpretation|
    |---|----------|
    |0.00 < 0.01 | negligible |
    |0.01 < 0.20 | very small |
    |0.20 < 0.50 | small |
    |0.50 < 0.80 | medium |
    |0.80 < 1.20 | large |
    |1.20 < 2.00 | very large |
    |2.00 or more | huge |
    
    See Also
    --------
    stikpetP.effect_sizes.eff_size_cohen_d_os.es_cohen_d_os : to determine a Cohen d' then use
    
    stikpetP.effect_sizes.convert_es.es_convert : to convert this to Cohen d
    

    References
    ----------
    Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). L. Erlbaum Associates.
    
    Lovakov, A., & Agadullina, E. R. (2021). Empirically derived guidelines for effect size interpretation in social psychology. *European Journal of Social Psychology, 51*(3), 485–504. https://doi.org/10.1002/ejsp.2752
    
    Rosenthal, J. A. (1996). Qualitative descriptors of strength of association and effect size. *Journal of Social Service Research, 21*(4), 37–59. https://doi.org/10.1300/J079v21n04_02
    
    Sawilowsky, S. (2009). New effect size rules of thumb. *Journal of Modern Applied Statistical Methods, 8*(2). https://doi.org/10.22237/jmasm/1257035100
    
    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    --------
    >>> es = 0.6
    >>> th_cohen_d(es)
      classification                  reference
    0         medium  Sawilowsky (2009, p. 599)
    
    '''
            
    #Cohen (1988, p. 40).
    if (qual=="cohen"):
        ref = "Cohen (1988, p. 40)"
        if (abs(d) < 0.2):
            qual = "negligible"
        elif (abs(d) < 0.5):
            qual = "small"
        elif (abs(d) < 0.8):
            qual = "medium"
        else:
            qual = "large"
            
    #Lovakov and Agadullina (2021, p. 501).
    if (qual=="lovakov"):
        ref = "Lovakov and Agadullina (2021, p. 501)"
        if (abs(d) < 0.15):
            qual = "negligible"
        elif (abs(d) < 0.35):
            qual = "small"
        elif (abs(d) < 0.65):
            qual = "medium"
        else:
            qual = "large"
    
    #Rosenthal (1996, p. 45).
    elif (qual=="rosenthal"):
        ref = "Rosenthal (1996, p. 45)"
        if (abs(d) < 0.2):
            qual = "negligible"
        elif (abs(d) < 0.5):
            qual = "small"
        elif (abs(d) < 0.8):
            qual = "medium"
        elif (abs(d) < 1.3):
            qual = "large"
        else:
            qual = "very large"
            
    #Sawilowsky (2009, p. 599).
    elif (qual=="sawilowsky"):
        ref = "Sawilowsky (2009, p. 599)"
        if (abs(d) < 0.01):
            qual = "negligible"
        elif (abs(d) < 0.2):
            qual = "very small"
        elif (abs(d) < 0.5):
            qual = "small"
        elif (abs(d) < 0.8):
            qual = "medium"
        elif (abs(d) < 1.2):
            qual = "large"
        elif (abs(d) < 2.0):
            qual = "very large"        
        else:
            qual = "huge"
    
    results = pd.DataFrame([[qual, ref]], columns=["classification", "reference"])
    
    return results