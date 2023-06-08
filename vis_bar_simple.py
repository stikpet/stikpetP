import matplotlib.pyplot as plt
import pandas as pd

def vi_bar_simple(data, varname=None, height="count"):
    '''
    Simple Bar Chart
    
    A bar-chart is defined as “a graph in which bars of varying height with spaces between them are  used to display data for variables defined by qualities or categories” (Zedeck, 2014, p. 20). 
    
    A [YouTube](https://youtu.be/zT52FTyC6P8) video on pie charts.
    
    Parameters
    ----------
    data : list or Pandas data series with the data
    varname : optional name for the variable
    height : optional to indicate what the height should represent
    
    Returns
    -------
    plt : a pyplot diagram
    
    Notes
    -----
    The function uses the *pyplot* library *plot* function.
    
    As a guideline for the size of the bar there is a rule of thumb known as the 'three quarter high rule' (Pitts, 1971). It means that the height of the vertical axis should be 3/4 of the length of the horizontal axis. So if the horizontal axis is 20 cm long, the vertical axis should be 3/4 * 20 = 15 cm high.
    
    According to Singh (2009) vertical bars (instead of horizontal bars) are preferred since they are easier on the eye. However if you have long category names some names might become unreadable. A bar chart with the bars placed horizontally might then be preferred. 
    
    One of the earliest found bar-charts from William Playfair (1786) has the bars placed horizontally. There is an earlier bar chart by Oresme (1486), but that is used more for a theoretical concept, than for descriptive statistics.
    
    References
    ----------
    Oresme, N. (1486). *Tractatus de latitudinibus formarum*. (B. Pelacani da Parma, Ed.). Mathaeus Cerdonis.
    
    Pitts, C. E. (1971). *Introduction to educational psychology: An operant conditioning approach*. Crowell.
    
    Playfair, W. (1786). *The commercial and political atlas*. Debrett; Robinson; and Sewell.
    
    Singh, G. (2009). *Map work and practical geography* (4th ed). Vikas Publishing House Pvt Ltd.
    
    Zedeck, S. (Ed.). (2014). *APA dictionary of statistics and research methods*. American Psychological Association.
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    Examples
    --------
    >>> data = ["MARRIED", "DIVORCED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "NEVER MARRIED", "MARRIED", "MARRIED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "MARRIED"]
    >>> vi_bar_simple(data) 
    >>> vi_bar_simple(data, varname="marital")
    >>> vi_bar_simple(data, varname="marital", height="percent")
    
    
    '''
    
    if type(data) == list:
        data = pd.Series(data)
    
    fr = data.value_counts()
    
    if height=="count":
        fr.plot(kind='bar')
        plt.ylabel('Frequency')
    
    elif height=="percent":
        perc = fr/sum(fr) * 100    
        perc.plot(kind='bar')
        plt.ylabel('Percent')
    
    plt.xlabel(varname)
    plt.xticks(rotation=45)
        
    return plt