import pandas as pd
import matplotlib.pyplot as plt

def vi_cleveland_dot_plot(data):
    
    '''
    Simple Bar Chart
    
    A Cleveland dot plot (Cleveland & McGill, 1987) is a bar chart where instead of bars a dot is placed at the center of the top of the bar (and then the bars removed). It is a dot plot only showing the top dot.This requires less ink. 
    
    The function simply uses the scatter() function from the matplotlib pyplot library.
    
    A video on (Cleveland) dot plots is available [here](https://youtu.be/qs1nh0CMiIY).
    
    Parameters
    ----------
    data : list or Pandas data series with the data
    
    Returns
    -------
    plt : a pyplot diagram
    
    Notes
    -----
    The function uses the *pyplot* library *plot* function.
    
    References
    ----------
    Cleveland, W. S., & McGill, R. (1984). Graphical perception: Theory, experimentation, and application to the development of graphical methods. *Journal of the American Statistical Association, 79*(387), 531–554. https://doi.org/10.2307/2288400 
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    Examples
    --------
    >>> data = ["MARRIED", "DIVORCED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "NEVER MARRIED", "MARRIED", "MARRIED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "MARRIED"]
    >>> vi_cleveland_dot_plot(data) 
    
    '''
    
    if type(data) == list:
        data = pd.Series(data)
        
    freq = data.value_counts()
    
    plt.scatter(x=freq.keys(), y=freq.values)
    plt.ylabel('Frequency')
    
    return plt