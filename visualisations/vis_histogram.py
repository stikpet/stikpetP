import pandas as pd
import matplotlib.pyplot as plt

def vi_histogram(data, xlbl=None, ylbl=None, **kwargs):
    '''
    Histogram
    ---------
    
    A histogram is a bit like a bar chart for a scale variable. You would create some bins, and then plot these as bars.
    
    Parameters
    ----------
    data : list or pandas series 
        the numeric scores
    xlbl : string, optional 
        label for the horizontal axis
    ylbl : string, optional 
        label for the vertical axis
    kwargs : other parameters for use in pyplot hist function
    
    Notes
    -----
    To set the bins, the *bins* argument can be used. This could be a pre-set number based on a calculation, a specific rule (e.g. bins="sturges"), or a list with the cut-off points.
    
    If your bins are of equal width, a true histogram than actually should show frequency densities (Pearson, 1895, p. 399). These are the frequencies divided by the bin-width. This can be done using *density=True* parameter.
    
    References
    ----------
    Pearson, K. (1895). Contributions to the mathematical theory of evolution. II. Skew variation in homogeneous material. *Philosophical Transactions of the Royal Society of London. (A.)*, 186, 343–414. doi:10.1098/rsta.1895.0010
    
    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    ---------    
    Example 1: pandas series
    >>> df2 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/StudentStatistics.csv', sep=';', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> ex1 = df2['Gen_Age']
    >>> vi_histogram(ex1);
    >>> vi_histogram(ex1, density=True);
    
    Example 2: Numeric list
    >>> ex2 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    >>> vi_histogram(ex2);
    
    '''
    
    plt.hist(data, **kwargs)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.show()
    
    return