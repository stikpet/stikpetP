import pandas as pd

def tab_frequency(data, order=None):
    '''
    Frequency Table
    ---------------
    
    A frequency table is defined as "a table showing (1) all of the values for a variable in a dataset, and (2) the 
    frequency of each of those responses. Some frequency tables also show a cumulative frequency and proportions of 
    responses" (Warne, 2017, p. 512). 
    
    A frequency table can help to get impression of your survey data of a binary, nominal, or ordinal variable. It 
    could also help with a scale variable, provided there are not too many options. If, for example, you have asked 
    for age, a list going from 1 to 90 with different ages and frequencies, will probably not be so helpful.
    
    If you have many options in the scale variable, the data is often binned (e.g. 0 < 10, 10 < 20, etc.), which 
    creates then an ordinal variable, of which a frequency table can then be helpful. See binning for more 
    information on this. A frequency table can show different types of frequencies. Various options are discussed in the details.
    
    A YouTube video with explanation on this test is available [here](https://youtu.be/DPmwWxYYCp4)
    
    Parameters
    ----------
    data : list or pandas data series
    order : list or dictionary, optional 
        specify the order of the categories
    
    Returns 
    -------
    Dataframe with the folowing columns:
    
    * *data*, the categories
    * *Frequency*, the absolute count
    * *Percent*, the percentage based on the total including missing values
    * *Valid Percent*, the percentage based on the total excluding missing values, only if missing values are present
    * Cumulative Percent*, the cumulative percentages
    
    Notes
    -----
    The column **Frequency** shows how many respondents answered each option. We can tell that 100 people in this survey 
    chose the option 'very scientific'. This is also known as the **absolute frequency** and defined as “the number of 
    occurrences of a particular phenomenon” (Zedeck, “Frequency”, 2014, p. 144).
    
    The **Percent** column shows the percentages, based on the grand total, so including the missing values. Percentages 
    can be defined as “a way of expressing ratios in terms of whole numbers. A ratio or fraction is converted to a 
    percentage by multiplying by 100 and appending a "percentage sign" %” (Weisstein, 2002, p. 2200).
    
    The **Valid Percent** shows the percentage, based on the valid total, so excluding the missing values. Most often 
    the ‘Percent’ shown in reports are actually Valid Percent, but the word ‘Valid’ is then simply left out.
    
    Percentages show the number of cases that could be expected if there would be 100 cases in total, hence per-cent which means 
    'per 100'. If your sample size is very small, be careful about using percentages. If it is less than 100, it means that you 
    are 'blowing up' your differences, while percentages are more commonly used to 'scale down'.
    
    The term **relative frequency** is also sometimes used. This is the frequency divided by the total number of cases. 
    Note that this should then always produce a decimal value between 0 and 1 (inclusive). Multiply this by 100 and you 
    get the percentage, multiply it by 1000 and you get permille (‰), multiply it by 360 and you get the degrees of a circle, etc.
    
    In general the formula for a percentage is:
    $$PR_i = \\frac{F_i}{n}\\times 100$$
    
    *Symbols used:*
    
    * \\(PR_i\\) the percentage of category i
    * \\(F_i\\) the (absolute) frequency of category i
    * \\(n\\) the sample size, i.e. the sum of all frequencies (either including or excluding the missing values)
    
    The **cumulative frequency** (not shown in table) can be defined as: “the total (absolute) frequency up to the upper boundary 
    of that class” (Kenney, 1939, p. 16). This would only be useful if there is an order to the categories, so we can say that 
    for example 299 respondents found accounting pretty scientific or even more. Which is why these cumulative frequencies 
    will not have a meaningful interpretation for a nominal variable (e.g. 28 students study business or less?).
    
    The **Cumulative Percent** is the running total of the Valid Percent, it is the addition of all previous and the current 
    category’s valid percentages.
    
    The cumulative frequency can be calculated using:
    $$CF_i = \\sum_{j=1}^i F_j$$
    Or using recursion:
    $$CF_i = F_i + CF_{i-1}$$
    
    For the cumulative percent the same formulas as for cumulative frequency can be used, but replacing \\(F_i\\) with \\(PR_i\\). 
    It can also be determined using the cumulative frequency:
    $$CPR_i = \\frac{CF_i}{n}$$
    
    When the categories are ranges of values (bins), the frequency density could become helpful. It can be defined as: “the 
    number of occurrences of an event divided by the bin size…” (Zedeck, 2014, pp. 144–145). See the binned tables for more information about this.
    
    References
    ----------
    Kenney, J. F. (1939). *Mathematics of statistics; Part one*. Chapman & Hall.
    
    Warne, R. T. (2017). *Statistics for the social sciences: A general linear model approach*. Cambridge University Press.
    
    Weisstein, E. W. (2002). *CRC concise encyclopedia of mathematics* (2nd ed.). Chapman & Hall/CRC.
    
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
    >>> tab_frequency(ex1)
                   Frequency    Percent  Valid Percent  Cumulative Percent
    DIVORCED             314  15.906788      16.177228           16.177228
    MARRIED              972  49.240122      50.077280           66.254508
    NEVER MARRIED        395  20.010132      20.350335           86.604843
    SEPARATED             79   4.002026       4.070067           90.674910
    WIDOWED              181   9.169200       9.325090          100.000000
    
    Example 2: Text data with specified order
    >>> tab_frequency(df1['mar1'], order=["MARRIED", "DIVORCED", "NEVER MARRIED", "SEPARATED", "WIDOWED"])
                   Frequency    Percent  Valid Percent  Cumulative Percent
    MARRIED              972  49.240122      50.077280           50.077280
    DIVORCED             314  15.906788      16.177228           66.254508
    NEVER MARRIED        395  20.010132      20.350335           86.604843
    SEPARATED             79   4.002026       4.070067           90.674910
    WIDOWED              181   9.169200       9.325090          100.000000
    
    Example 3: Numeric data
    >>> ex3 = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5]
    >>> tab_frequency(ex3)
       Frequency    Percent  Valid Percent  Cumulative Percent
    1          2  16.666667      16.666667           16.666667
    2          3  25.000000      25.000000           41.666667
    3          2  16.666667      16.666667           58.333333
    4          3  25.000000      25.000000           83.333333
    5          2  16.666667      16.666667          100.000000
    
    Example 4: Ordinal data
    >>> ex4a = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, "NaN"]
    >>> order = {"fully disagree":1, "disagree":2, "neutral":3, "agree":4, "fully agree":5}
    >>> tab_frequency(ex4a, order=order)
                    Frequency    Percent  Valid Percent  Cumulative Percent
    fully disagree          2  15.384615      16.666667           16.666667
    disagree                3  23.076923      25.000000           41.666667
    neutral                 2  15.384615      16.666667           58.333333
    agree                   3  23.076923      25.000000           83.333333
    fully agree             2  15.384615      16.666667          100.000000
    
    >>> ex4b = df1['accntsci']
    >>> tab_frequency(ex4b, order=["Not scientific at all", "Not too scientific", "Pretty scientific", "Very scientific"])
                           Frequency    Percent  Valid Percent  Cumulative Percent
    Not scientific at all        307  15.552178      32.180294           32.180294
    Not too scientific           348  17.629179      36.477987           68.658281
    Pretty scientific            199  10.081054      20.859539           89.517820
    Very scientific              100   5.065856      10.482180          100.000000
    
    '''
    
    if type(data) is list:
        data = pd.Series(data)
    
    if order is not None:
        if type(order) is dict:
            order2 = {y: x for x, y in order.items()}
            data = data.replace(order2)
            
        data = pd.Categorical(data, categories=order, ordered=True)
    
    data = data.sort_values()
    
    freq = data.value_counts().sort_index()
    perc = freq/sum(data.value_counts(dropna = False))*100
    vperc = freq/sum(freq)*100
    cperc = vperc.cumsum()
    tab = pd.DataFrame(list(zip(freq, perc, vperc, cperc)), columns = ["Frequency", "Percent", "Valid Percent", "Cumulative Percent"], index=freq.index)
    return tab