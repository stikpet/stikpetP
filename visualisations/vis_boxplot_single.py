import pandas as pd
import matplotlib.pyplot as plt


def vi_boxplot_single(data, varname=None):
    '''
    Box (and Whisker) Plot
    ----------------------
    
    A box plot is a little more complex visualisation than a histogram. It shows the five quartiles (e.g. minimum, 1st quartile, median, 3rd quartile, and maximum). It can also be adjusted to show so-called outliers.
    
    Parameters
    ----------
    data : list or pandas series 
        the numeric data
    varname : string, optional
        name to display on vertical axis
    
    Notes
    -----
    This was actually a 'range chart' (Spear, 1952, p. 166) but somehow it is these days referred to as a box-and-whisker plot as named by Tukey (1977, p. 39)
    
    The function uses the **boxplot()** function from the *pandas* library. If you want to modify more things (like colors etc.) you might want to use that function.
    
    References
    ----------
    Spear, M. E. (1952). *Charting statistics*. McGraw-Hill.
    
    Tukey, J. W. (1977). *Exploratory data analysis*. Addison-Wesley Pub. Co.
    
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
    >>> vi_boxplot_single(ex1);
    
    Example 2: Numeric list
    >>> ex2 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    >>> vi_boxplot_single(ex2);
    
    '''
    
    if type(data) == list:
        data = pd.Series(data)
        
    data = data.dropna()
    data = pd.to_numeric(data)
    
    plt.boxplot(data.dropna(), vert=False)
    plt.xlabel(varname)
    plt.yticks([1], " ")
    plt.show()
    
    return