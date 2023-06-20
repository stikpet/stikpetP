from statistics import mean, stdev
from ..other.thumb_cohen_d import th_cohen_d
import pandas as pd

def es_cohen_d_os(data, mu="none", qual="sawilowsky"):
    '''
    Cohen d'
     
    This function will calculate Cohen d' (one-sample)
    
    Parameters
    ----------
    data : pandas series with the numeric scores
    mu : optional parameter to set the hypothesized mean. If not used the midrange is used
    qual : rule of thumb to use for qualification. See th_cohen_d for more details.
        
    Returns
    -------
    testResults : Pandas dataframe with effect size and classification.
   
    Notes
    -----
    Requires the th_cohen_d function from thumb_cohen_d
    The Cohen d' is converted to the regular Cohen d, and those interpretations are then used.
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    '''
    
    #set hypothesized median to mid range if not provided
    if (mu=="none"):
        mu = (min(data) + max(data)) / 2
        
    xBar = mean(data)
    s = stdev(data)
    dos = abs(xBar - mu)/s
    
    #convert to regular Cohen d for qualification
    d = dos*(2)**0.5
    
    #use rule of thumb function
    qualification = th_cohen_d(d, qual)
    
    testResults = pd.DataFrame([[dos, qualification]], columns=["d'", "Classification"])
        
    pd.set_option('display.max_colwidth', None)
    
    return testResults