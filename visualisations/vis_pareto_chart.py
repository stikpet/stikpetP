import matplotlib.pyplot as plt
import pandas as pd

def vi_pareto_chart(data, varname=None):
    '''
    Pareto Chart
    
    The Pareto Chart gets its name from the Pareto Principle, which is named after Vilfredo Pareto. This principle states that roughly 80% of consequencies come from 20% of causes (Pareto, 1896).
    
    Unfortunately, there is no general agreed upon definition of a Pareto diagram. The most general description I’ve found was by Kemp and Kemp (2004) who mention it is a name for a bar chart if the order of the bars have no meaning (i.e. for a nominal variable), and they only mention that often the bars are then placed in decreasing order. 
    
    According to some authors a Pareto diagram is any diagram with the bars in order of size (Joiner, 1995; WhatIs.com, n.d.), while others suggest that a line representing the cumulative relative frequencies should also be included (Weisstein, 2002). Upton and Cook (2014) also add that the bars should not have any gaps, but many other authors ignore this.
    
    The following definition by the author is used: a bar chart where the bars are placed in descending order of frequency. Usually an ogive is added in the chart as well. An ogive (oh-jive) is: "the graphs of cumulative frequencies" (Kenney, 1939).
    
    A video on Pareto charts is available [here](https://youtu.be/kDp5zPfK-Po).
    
    Parameters
    ----------
    data the data from which to create a Pareto chart
    varname a name for the data, if not provided the name of the data variable is used
    
    Returns
    -------
    a Pareto chart
    
    Notes
    -----
    Uses matplotlib pyplot
    
    References 
    ----------
    Joiner. (1995). Pareto charts: Plain & simple. Joiner Associates.
    
    Kemp, S. M., & Kemp, S. (2004). *Business statistics demystified*. McGraw-Hill.
    
    Kenney, J. F. (1939). *Mathematics of statistics; Part one*. Chapman & Hall.
    
    Pareto, V. (1896). *Cours d’économie politique* (Vol. 1). Lausanne.
    
    Upton, G. J. G., & Cook, I. (2014). *Dictionary of statistics* (3rd ed.). Oxford University Press.
    
    Weisstein, E. W. (2002). *CRC concise encyclopedia of mathematics* (2nd ed.). Chapman & Hall/CRC.
    
    WhatIs.com. (n.d.). What is Pareto chart (Pareto distribution diagram)? - Definition from WhatIs.com. Retrieved April 20, 2014, from http://whatis.techtarget.com/definition/Pareto-chart-Pareto-distribution-diagram
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    Examples
    --------
    >>> data = ["MARRIED", "DIVORCED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "NEVER MARRIED", "MARRIED", "MARRIED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "MARRIED"]
    >>> vi_pareto_chart(data)
    
    '''
    
    if type(data) == list:
        data = pd.Series(data)
        
        
    freq = data.value_counts()
    myKeys = freq.keys()
    myVals = freq.values

    myFreqTable = pd.DataFrame({'category': myKeys, 'Frequency': myVals})

    myFreqTable['Percent'] = myFreqTable['Frequency']/myFreqTable['Frequency'].sum()*100
    myFreqTable = myFreqTable.sort_values(by=['Frequency'], ascending=False)
    myFreqTable = myFreqTable.reset_index(drop=True)
    myFreqTable['Cumulative Percent'] = myFreqTable['Frequency'].cumsum() / myFreqTable['Frequency'].sum() * 100
    fig,ax=plt.subplots()
    ax.set_xlabel(varname)
    ax.bar('category', 'Frequency', data = myFreqTable)
    ax.set_ylabel("percent")
    ax.set_ylim(ymin=0)

    ax2=ax.twinx()
    ax2.plot('category', 'Cumulative Percent', data = myFreqTable, marker='o', color='red')
    ax2.set_ylabel("cumulative percent")
    ax2.set_ylim(ymin=0)    
    
    return plt