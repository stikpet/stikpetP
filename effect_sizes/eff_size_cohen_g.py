import pandas as pd

def es_cohen_g(data, codes=None):
    '''
    Cohen's g
     
    Cohen’s g (Cohen, 1988) is an effect size measure that could be accompanying a one-sample binomial (see Rosnow & Rosenthal, 2003), score or Wald test. It is simply the difference of the sample proportion with 0.5. 
    
    A video explanation of Cohen g can be found https://youtu.be/tPZMvB8QrM0
    
    Parameters
    ----------
    data : list or Pandas data series with the data
    codes : optional list with the two codes to use
        
    Returns
    -------
    testResults : Cohen's g value.
   
    Notes
    -----
    The formula used is (Cohen, 1988, p. 147):
    $$g=p-0.5$$
    
    *Symbols used*:
    
    * \(p\) is the sample proportion
    
    References
    ----------
    Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). L. Erlbaum Associates.
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    Examples
    --------
    >>> dataList = ["Female", "Male", "Male", "Female", "Male", "Male"]
    >>> data = pd.Series(dataList)
    >>> es_cohen_g(data)
    
    '''
    if codes is None:
        freq = data.value_counts()
        n = sum(freq.values)
        p1 = freq.values[0]/n
    
    else:
        #Determine number of successes
        n1 = sum(data==codes[0])
        n2 = sum(data==codes[1])
        n = n1 + n2
        p1 = n1/n
        
    g = p1 - 0.5
    
    return (g)