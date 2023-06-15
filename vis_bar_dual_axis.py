import pandas as pd
import matplotlib.pyplot as plt

def vi_bar_dual_axis(data, varname=None):
    '''
    Dual-Axis Bar Chart
    
    A dual axis bar-chart is a bar-chart with two vertical axis. In this function it will show both the count and cumulative proportion. 
    
    This chart could be used with a single ordinal variable.
    
    Parameters
    ----------
    data : a pandas series with the data
    varname : optional string for the horizontal axis (default is series name)
    
    Returns
    -------
    plt : pyplot with the chart
    
    Notes
    -----
    Uses pyplot **bar()** for the chart
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet


    '''
    
    field = data.name
    myFreq = data.value_counts().sort_index()
    myKeys = myFreq.keys()
    myVals = myFreq.values
    myFreqTable = pd.DataFrame({field: myKeys, 'Frequency': myVals})
    myFreqTable['Percent'] = myFreqTable['Frequency']/myFreqTable['Frequency'].sum()*100
    myFreqTable['Cumulative Percent'] = myFreqTable['Frequency'].cumsum() / myFreqTable['Frequency'].sum() * 100
    
    if varname is None:
        xlab = field
    else:
        xlab = varname
    
    fig,ax=plt.subplots()
    ax.set_xlabel(xlab)
    ax.bar(field, 'Frequency', data = myFreqTable)
    ax.set_ylabel("frequency")
    ax.set_ylim(ymin=0)

    ax2=ax.twinx()
    ax2.plot(field, 'Cumulative Percent', data = myFreqTable, marker='o', color='red')
    ax2.set_ylabel("cumulative percent")
    ax2.set_ylim(ymin=0)
    
    return plt