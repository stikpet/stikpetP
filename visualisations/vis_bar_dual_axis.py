import pandas as pd
import matplotlib.pyplot as plt
from ..other.table_frequency import tab_frequency

def vi_bar_dual_axis(data, varname=None, order=None):
    '''
    Dual-Axis Bar Chart
    -------------------
    
    A dual axis bar-chart is a bar-chart with two vertical axis. In this function it will show both the count and cumulative proportion. 
    
    This chart could be used with a single ordinal variable.
    
    Parameters
    ----------
    data : list or pandas series 
        the data
    varname : string, optional 
        label for the horizontal axis. Default is series name
    order : list or dictionary, optional 
        the order of the categories
    
    Returns
    -------
    plt : pyplot with the chart
    
    Notes
    -----
    Uses pyplot **bar()** for the chart
    
    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076

    Examples
    --------
    >>> df1 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/GSS2012a.csv', sep=',', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> ex1 = df1['mar1']
    >>> vi_bar_dual_axis(ex1);
    >>> vi_bar_dual_axis(ex1, varname="marital status");

    '''
    
    field = data.name
    
    myFreqTable = tab_frequency(data=data, order=order)
    
    if varname is None:
        xlab = field
    else:
        xlab = varname

    fig,ax=plt.subplots()
    ax.set_xlabel(xlab)
    ax.bar(myFreqTable.index, 'Frequency', data = myFreqTable)
    ax.set_ylabel("frequency")
    ax.set_ylim(ymin=0)

    ax2=ax.twinx()
    ax2.plot(myFreqTable.index, 'Cumulative Percent', data = myFreqTable, marker='o', color='red')
    ax2.set_ylabel("cumulative percent")
    ax2.set_ylim(ymin=0)
    
    plt.show()
    
    return