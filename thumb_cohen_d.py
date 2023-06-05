def th_cohen_d(d, qual="sawilowsky"):
    '''
    Rules of Thumb for Cohen d
     
    This function will give a qualification (classification) to a given correlation coefficient
    
    Parameters
    ----------
    d : the Cohen d value
    qual : optional the rule of thumb to be used
        
    Returns
    -------
    qual : string with the qualification.
   
    Notes
    -----
    The following rules-of-thumb can be used:
    "cohen" => Cohen (1988, p. 40)
    "lovakov" => Lovakov and Agadullina (2021, p. 501)
    "rosenthal" => Rosenthal (1996, p. 45)
    "sawilowsky" => Sawilowsky (2009, p. 599)
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    '''
            
    #Cohen (1988, p. 40).
    if (qual=="cohen"):
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
        if (abs(d) < 0.10):
            qual = "negligible"
        elif (abs(d) < 0.1):
            qual = "very small"
        elif (abs(d) < 0.2):
            qual = "small"
        elif (abs(d) < 0.5):
            qual = "medium"
        elif (abs(d) < 0.8):
            qual = "large"
        elif (abs(d) < 1.2):
            qual = "very large"        
        else:
            qual = "huge"
            
    return qual