import pandas as pd
from .meas_quartiles import me_quartiles

def me_quartile_range(data, levels=None, measure="iqr", method="cdf"):
    '''
    Interquartile Range, Semi-Interquartile Range and Mid-Quartile Range
    --------------------------------------------------------------------
    
    Three different ranges that can be used with quartiles. The Interquartile Range (IQR) is simply the third minus the first quartile.
    
    The Semi-Interquartile range (a.k.a. Quartile Deviation) divides the IQR by 2.
    
    The Mid-Quartile Range adds the two quartiles and then divides by 2.
    
    A special case is the H-spread, which is if Hinges are used the IQR. This can be obtained by setting *method="tukey"*.
    
    The function uses the *me_quartiles* function and any of the methods from that function can be used.
    
    Parameters
    ----------
    data : list or pandas series 
        the scores as numbers, or if text also provide levels
    levels : dictionary, optional 
        levels in order
    measure : {"iqr", "siqr", "qd", "mqr"}, optional 
        the specific measure to determine. Default is "iqr"
    method : string, optional 
        the method to use to determine the quartiles. See me_quartiles for options
    
    Returns
    -------
    A dataframe with:
    
    * *Q1*, the first (lower) quartile
    * *Q3*, the third (upper/higher) quartile
    * *range*, the measure determined
    
    Notes
    -----
    The formula used for the Interquartile Range is:
    $$IQR = Q_3 - Q_1$$
    
    This can be obtained by setting *range="iqr"*.
    
    The IQR is mentioned in Galton (1881, p. 245) and the H-spread in Tukey (1977, p. 44).
    
    The H-spread can be obtained by setting *range="iqr"* and *method="tukey"*.
    
    The formula used for the Semi-Interquartile Range (Quartile Deviation) is (Yule, 1911, p. 147):
    $$SIQR = \\frac{Q_3 - Q_1}{2}$$
    
    This can be obtained by setting *range="siqr"* or *range="qd"*.
    
    The formula for the mid-quartile range used is:
    $$MQR = \\frac{Q_3 + Q_1}{2}$$
    
    This can be obtained by setting *range="mqr"*.
    This formula can be found in Parzen (1980, p. 19), but there are probably older references.
    
    See Also
    --------
    stikpetP.measures.meas_quartiles.me_quartiles : calculating quartiles
    
    References 
    ----------
    Galton, F. (1881). Report of the anthropometric committee. Report of the British Association for the Advancement of Science, 51, 225–272.
    
    Parzen, E. (1980). *Data modeling using quantile and density-quantile functions*. Institute of Statistics, Texas A&M University.
    
    Tukey, J. W. (1977). *Exploratory data analysis*. Addison-Wesley Pub. Co.
    
    Yule, G. U. (1911). *An introduction to the theory of statistics*. Charles Griffin.
    
    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    --------
    Example 1: Text Pandas Series
    >>> import pandas as pd
    >>> df2 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/StudentStatistics.csv', sep=';', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> ex1 = df2['Teach_Motivate']
    >>> order = {"Fully Disagree":1, "Disagree":2, "Neither disagree nor agree":3, "Agree":4, "Fully agree":5}
    >>> me_quartile_range(ex1, levels=order)
       Q1  Q3  IQR
    0   1   3    2

    Example 2: Numeric data
    >>> ex2 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    >>> me_quartile_range(ex2)
       Q1  Q3  IQR
    0   2   5    3
    
    
    '''
    
    qs = me_quartiles(data, levels=levels, method=method)
    q1 = qs.iloc[0,0]
    q3 = qs.iloc[0,1]
    
    if (measure=="iqr"):
        r = q3 - q1
        if (method in ["inclusive", "tukey", "vining", "hinges"]):
            rName = "Hspread"
        else:
            rName = "IQR"
    elif (measure=="siqr" or measure=="qd"):
        r = (q3 - q1)/2
        rName = "SIQR"
        
    elif (measure=="mqr"):
        r = (q3 + q1)/2
        rName = "MQR"
        
    res = pd.DataFrame([[q1, q3, r]], columns=["Q1", "Q3", rName])
        
    return res