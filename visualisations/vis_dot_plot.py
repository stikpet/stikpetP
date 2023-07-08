import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def vi_dot_plot(data, dotSize = 1):
    '''
    Dot Plot
    --------
    
    The Oxford Dictionary of Statistics defines a dot plot as "an alternative to a bar chart or line graph when there are very few data values. Each value is recorded as a dot, so that the frequencies for each value can easily be counted" (Upton & Cook, 2014, p. 129). 
    
    This function uses matplotlib.pyplot scatter() to create a simple dot plot.
    
    A [YouTube](https://youtu.be/qs1nh0CMiIY) video on dot plots.
    
    Parameters
    ----------
    data : list or pandas series
    dotSize : float, optional
        indicator for how big the dots need to be. Default is 1
    
    Notes
    -----
    In the definition a *bar chart* is mentioned. A bar chart can be defined as “a graph in which bars of varying height with spaces between them are used to display data for variables defined by qualities or categories” (Zedeck, 2014, p. 20). Together this indicates that a dot plot is used for categorical data.
    
    However, Zedeck sees the dot plot as an alternative name for a scatterplot, which is for continuous data. A third version comes from the Cambridge Dictionary of Statistics: "A more effective display than a number of other methods, for example, pie charts and bar charts, for displaying quantitative data which are labelled" (Everitt, 2004, p. 123). They also show an example where we see a categorical variable on one axis, and a continuous variable on another.
    
    This function was only for the original definition for categorical data.
    
    References 
    ----------
    Everitt, B. (2004). *The Cambridge dictionary of statistics* (2nd ed). Cambridge University Press.
    
    Upton, G. J. G., & Cook, I. (2014). *Dictionary of statistics* (3rd ed.). Oxford University Press.
    
    Zedeck, S. (Ed.). (2014). *APA dictionary of statistics and research methods*. American Psychological Association.
    
    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    --------
    Example 1: pandas series
    >>> df1 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/GSS2012a.csv', sep=',', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> ex1 = df1['mar1']
    >>> vi_dot_plot(ex1);
    >>> vi_dot_plot(ex1, dotSize=50);
    
    Example 2: a list
    >>> ex2 = ["MARRIED", "DIVORCED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "NEVER MARRIED", "MARRIED", "MARRIED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "MARRIED"]
    >>> vi_dot_plot(ex2);

    '''
    if type(data) == list:
        data = pd.Series(data)
    
    freq = data.value_counts()
    
    # divide if needed by number of dots each should represent
    n_dots = (freq/dotSize).astype(np.int64)
    
    # create an array for each categorie that has the label, and 
    # a consecutive number going from the first to the last case in that category
    a = []
    for i in range(len(n_dots)):
        a.append(np.vstack((np.full(n_dots.values[i], n_dots.keys()[i]), np.arange(1,n_dots.values[i]+1))).T)
    
    # now combine all the arrays from the categories
    my_data = np.concatenate((a[0],a[1]),axis=0)
    for i in range(2, len(n_dots)):
        my_data = np.concatenate((my_data,a[i]),axis=0)
    
    plt.scatter(x=my_data[:,0], y=my_data[:,1])
    plt.ylabel("x " + str(dotSize))
    plt.show()
    
    return