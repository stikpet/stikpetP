import pandas as pd
from .table_nbins import tab_nbins

def tab_frequency_bins(data, nbins="sturges", bins=None, incl_lower=True, adjust=1):
    '''
    Binned Frequency Table 
    ----------------------
    
    Bins data and creates a frequency table with frequency density.
    
    Parameters
    ----------
    data : list or pandas series
        the data
    nbins : int or string, optional
        either the number of bins to create, or a specific method from the *tab_nbins()* function. Default is "sturges"
    bins : list of tuples, optional
    incl_lower : boolean, optional
        to include the lower bound, otherwise the upper bound is included. Default is True
    adjust : float, optional
        value to add  or subtract to guarantee all scores will fit in a bin
        
    Returns
    -------
    tab : pandas dataframe with the following fields
    
    * *lower bound* 
    * *upper bound*
    * *frequency* 
    * *frequency density*
    
    See Also
    --------
    stikpetP.other.table_nbins.tab_nbins : to determine the number of bins
    
    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    --------
    Example 1: TNumeric Pandas Series
    >>> import pandas as pd
    >>> df2 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/StudentStatistics.csv', sep=';', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> ex1a = df2['Gen_Age']
    >>> tab_frequency_bins(ex1a)
       lower bound  upper bound  frequency  frequency density
    0    18.000000    32.571429       42.0           2.882353
    1    32.571429    47.142857        1.0           0.068627
    2    47.142857    61.714286        0.0           0.000000
    3    61.714286    76.285714        0.0           0.000000
    4    76.285714    90.857143        0.0           0.000000
    5    90.857143   105.428571        0.0           0.000000
    6   105.428571   120.000000        1.0           0.068627
    
    >>> ex1b = df2['Gen_Age']
    >>> myBins = [(0, 20), (20, 25), (25, 30), (30, 120)]
    >>> tab_frequency_bins(ex1b, bins=myBins)
       lower bound  upper bound  frequency  frequency density
    0          0.0         20.0       12.0           0.600000
    1         20.0         25.0       21.0           4.200000
    2         25.0         30.0        8.0           1.600000
    3         30.0        120.0        3.0           0.033333
    
    Example 2: Numeric list
    >>> ex2 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    >>> tab_frequency_bins(ex2, adjust=0.1)
       lower bound  upper bound  frequency  frequency density
    0     1.000000     1.683333        3.0           4.390244
    1     1.683333     2.366667        3.0           4.390244
    2     2.366667     3.050000        2.0           2.926829
    3     3.050000     3.733333        0.0           0.000000
    4     3.733333     4.416667        3.0           4.390244
    5     4.416667     5.100000        7.0          10.243902
    
    '''
    
    if type(data) is list:
        data = pd.Series(data)
    
    #remove missing values
    data = data.dropna()
    
    if bins is None:
        
        if isinstance(nbins, int):
            k = nbins
        else:
            k = tab_nbins(data, method=nbins)

        #determine minimum and maximum
        mx = max(data)
        mn = min(data)

        #increase maximimum if to include the lower bound
        if incl_lower:
            mx = mx + adjust
        #decrease minimum if to include the upper bound
        else:
            mn = mn - adjust

        #determine range and width
        r = mx - mn
        h = r/k

        #create the bins
    
        bins=[]
        i = 0
        while i < k:
            lb = mn + i*h
            ub = lb + h
            bins.append((lb, ub))
            i = i+1    
    
    tab = pd.DataFrame(columns = ["lower bound", "upper bound", "frequency", "frequency density"])
    
    for i in bins:
        lb = i[0]
        ub = i[1]
        if incl_lower:
            f = sum(data<ub) - sum(data<lb)
        else:
            sum(data<=ub) - sum(data<=lb)
        fd = f / (ub - lb)
        tab.loc[len(tab)] = [lb, ub, f, fd]
    
    return tab