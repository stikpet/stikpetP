import pandas as pd

def me_median(data, levels=None, tieBreaker="between"):
    '''
    Median
    
    Function to determine the median of a set of data. The median can be defined as "the middle value in a distribution, below and above which lie values with equal total frequencies or probabilities" (Porkess, 1991, p. 134). This means that 50% of the respondents scored equal or higher to the median, and also 50% of the respondents scored lower or equal.
    
    Parameters
    ----------
    data : pandas series with the (at least ordinal) data
    levels : optional dictionary to indicate what values represent
    tieBreaker : optional which to return if median falls between two values, either "between" (default), "low" or "high"
    
    Returns
    -------
    medNum : numeric value of the median
    medText : string value of the median
    
    Notes
    -----
    The formula that is used, assuming the data has been sorted, is:
    $$\\tilde{x} = \\begin{cases} x_{MI} & \\text{ if } MI= \\left \\lfloor MI \\right \\rfloor \\\ \\frac{x_{MI-0.5} + x_{MI+0.5}}{2} & \\text{ if } MI\\neq \\left \\lfloor MI \\right \\rfloor \\end{cases}$$
    
    With:
    $$MI = \\frac{n + 1}{2}$$
    
    *Symbols used:*
    * \(n\) the sample size
    * \(x_i\) the i-th score of X, assuming X has been sorted.
    * \(MI\) the index of the median
    * \(\\tilde{x}\) the median
    
    If the number of scores is an odd number, and the median falls between two categories, the *tieBreaker* can be used. If this is set to *"between"*, the function will return the average of the two values, or "between x and y" if levels are used. If it is set to "tieBreaker="low"", the lower value is returned, and if set to "tiebreaker="high"" the upper value is returned.
    
    Some old references to the median are Pacioli (1523) in Italian, Cournot (1843, p. 120) in French, and Galton (1881, p. 246) in English.
    
    References
    ----------
    Cournot, A. A. (1843). *Exposition de la théorie des chances et des probabilités*. L. Hachette.
    
    Galton, F. (1881). Report of the anthropometric committee. *Report of the British Association for the Advancement of Science, 51*, 225–272.
    
    Pacioli, L. (1523). *Summa de arithmetica geometria proportioni: Et proportionalita*. Paganino de Paganini.
    
    Porkess, R. (1991). *The HarperCollins dictionary of statistics*. HarperPerennial.
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet

    '''
    
    # set myField
    data = data.dropna()
    
    # if no coding is used, all values must be numeric, so we can use the median functions:
    if levels==None:
        
        if tieBreaker=="low":
            medNum = data.median_low()
        elif tieBreaker=="high":
            medNum = data.median_high()
        else:
            medNum = data.median()
                
        medText = str(medNum)
        
    else:
        # make sure we get a full coding
        uniqueVals = data.unique()
        fullCoding = levels
        for i in uniqueVals:
            if i not in fullCoding:
                fullCoding[i] = float(i) 
        
        # replace the values in the field with the numeric codes
        data2 = data.replace(fullCoding)
        # make sure its numeric
        data3 = pd.to_numeric(data2)
        
        # now find the numeric value of the median
        medNum = data3.median()
                
        keys = list(fullCoding.keys())
        values = list(fullCoding.values())
        
        # in case the numeric median is not in the coding
        if values.count(medNum) == 0:
            adf = lambda list_value : abs(list_value - medNum)
            nearest_value = min(values, key=adf)
            if nearest_value < medNum:
                lower_value = nearest_value
                lower_index = values.index(lower_value)
            else:
                higher_value = nearest_value
                lower_index = values.index(higher_value)-1
                
            if tieBreaker=="low":
                medText = str(keys[lower_index])
            elif tieBreaker=="high":
                medText = str(keys[lower_index+1])
            else:
                medText = ('between ' + str(keys[lower_index]) + ' and ' + str(keys[lower_index+1]))
                
        # if it is in the coding
        else:
            medText = str(keys[values.index(medNum)])
    
    return medNum, medText