import pandas as pd
import matplotlib.pyplot as plt

def vi_bar_stacked_single(data, catCoding = None, orientation = "h"):    
    '''
    Single Stacked Bar-Chart
    
    A regular bar-chart but with the bars on top of each other, instead of next to each other. This is called a compound bar chart, stacked bar chart (Wilkinson, 2005, p. 157) or component bar chart (Zedeck, 2014, p. 54). 
    
    It can be defined as: “a bar chart showing multiple bars stacked at each x-axis category, each representing a value of the stacking variable” (Upton & Cook, 2014, p. 88).
    
    Parameters
    ----------
    data : pandas series with the data
    catCoding : optional dictionary with the coding to use
    orientation : optional to indicate horizontal or vertical chart, "h" (default) or "v"
    
    Returns
    -------
    pyplot chart
    
    Notes
    -----
    This function uses the **barh()** function from pyplot
    
    References 
    ----------
    Upton, G. J. G., & Cook, I. (2014). *Dictionary of statistics* (3rd ed.). Oxford University Press.
    
    Wilkinson, L. (2005). *The grammar of graphics* (2nd ed). Springer.
    
    Zedeck, S. (Ed.). (2014). *APA dictionary of statistics and research methods*. American Psychological Association.
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    '''
    
    if catCoding is not None:
        data = data.replace(catCoding)
        categories = catCoding.keys()
    myFreq = data.value_counts()
    myFreq = myFreq.sort_index()
    
    if catCoding is None:
        categories = myFreq.index
    
    myPerc = myFreq/myFreq.sum()*100
    cf = myPerc.cumsum()
    myLabels= myFreq.index.tolist()
    
    if orientation=="v":
        plt.figure(figsize=(2, 5))
        plt.bar(0, myPerc.values[0], edgecolor='white', width = 0.2)
        for i in range(1, len(myFreq)):
            plt.bar(0, myPerc.values[i], bottom=cf.values[i-1], edgecolor='white', width = 0.2)
        plt.legend(categories, bbox_to_anchor=(1.05, 1))
        plt.ylabel('percent')
        frame1 = plt.gca()
        frame1.axes.get_xaxis().set_visible(False)
    else:
        plt.figure(figsize=(5, 2))
        plt.barh(0, myPerc.values[0], edgecolor='white', height = 0.2)
        for i in range(1, len(myFreq)):
            plt.barh(0, myPerc.values[i], left=cf.values[i-1], edgecolor='white', height = 0.2)
        plt.legend(categories, bbox_to_anchor=(1.05, 1))
        plt.xlabel('percent')
        frame1 = plt.gca()
        frame1.axes.get_yaxis().set_visible(False)
        
    return plt