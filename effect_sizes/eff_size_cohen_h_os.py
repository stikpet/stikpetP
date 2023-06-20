import math
import pandas as pd

def es_cohen_h_os(data, codes=None, p0=0.5):
    '''
    Cohen's h' for one-sample
     
    An adaptation of Cohen h (\code{\link{es_cohen_h}}) for a one-sample case. It is an effect size measure that could be accompanying a one-sample binomial, score or Wald test.
    
    See also https://youtu.be/ddWe94VKX_8, a video on Cohen h'.
    
    Parameters
    ----------
    data : list or Pandas data series with the data
    codes : optional list with the two codes to use
    p0 : optional probability for first category
        
    Returns
    -------
    h2 : Cohen's h' value.
   
    Notes
    -----
    Formula used (Cohen, 1988, p. 202):
    $$h'=\\phi_{1}-\\phi_{h_0}$$
    
    With:
    $$\phi_{i}=2\\times\\textup{arcsin}\\sqrt{p_{i}}$$
    $$p_i = \\frac{F_i}{n}$$
    $$n = \\sum_{i=1}^k F_i$$
    
    *Symbols used*:
    
    * \(F_i\) is the (absolute) frequency (count) of category i
    * \(n\) is the sample size, i.e. the sum of all frequencies
    * \(p_i\) the proportion of cases in category i
    * \(p_{h_0}\) the expected proportion (i.e. the proportion according to the null hypothesis)
    
    For a rule of thumb a conversion to the 'regular' Cohen h can be made using **es_convert()**, then the interpretation with **th_cohen_h()**.
    
    References
    ----------
    Cohen, J. (1988). Statistical power analysis for the behavioral sciences (2nd ed.). L. Erlbaum Associates.
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    Examples
    --------
    >>> dataList = ["Female", "Male", "Male", "Female", "Male", "Male"]
    >>> data = pd.Series(dataList)
    >>> es_cohen_h2_os(data)
    
    '''
    if codes is None:
        freq = data.value_counts()
        n1 = freq.values[0]        
        n = sum(freq.values)
        n2 = n - n1
    else:
        #Determine number of successes
        n1 = sum(data==codes[0])
        n2 = sum(data==codes[1])
        n = n1 + n2
        
    p1 = n1/n
    
    phi1 = 2 * math.asin(p1**0.5)
    phic = 2 * math.asin(p0**0.5)
    
    h2 = phi1 - phic
    
    return (h2)