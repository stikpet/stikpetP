import pandas as pd
from scipy.stats import chi2

def ts_pearson_gof(data, expCount=None, cc=None):
    '''
    Pearson Chi-Square Goodness-of-Fit Test
     
    A test that can be used with a single nominal variable, to test if the probabilities in all the categories are equal (the null hypothesis). If the test has a p-value below a pre-defined threshold (usually 0.05) the assumption they are all equal in the population will be rejected. 
    
    There are quite a few tests that can do this. Perhaps the most commonly used is this Pearson chi-square test, but also an exact multinomial, G-test, Freeman-Tukey, Neyman, Mod-Log Likelihood and Cressie-Read test are possible.
    
    The test compares the observed counts with the expected counts. It is often recommended not to use it if the expected count is at least 5 (Peck & Devore, 2012, p. 593).
    
    A YouTube video with explanation on this test is available at https://youtu.be/NVR5dZhp4vY
    
    Parameters
    ----------
    data : list or Pandas data series with the data
    expCount : Optional Pandas data frame with categories and expected counts
    cc : Optional which continuity correction to use, either None (default), "yates", "pearson", or "williams"
        
    Returns
    -------
    testResults : Pandas dataframe with the test statistic, degrees of freedom, significance (p-value) and test used
   
    Notes
    -----
    It uses chi2 from scipy's stats library
    
    The formula used is (Pearson, 1900):
    $$\\chi_{P}^{2}=\\sum_{i=1}^{k}\\frac{\\left(O_{i}-E_{i}\\right)^{2}}{E_{i}}$$
    $$df = k - 1$$
    $$sig. = 1 - \\chi^2\\left(\\chi_{P}^{2},df\\right)$$
    
    With:
    $$n = \\sum_{i=1}^k F_i$$
    
    If no expected counts provided:
    $$E_i = \\frac{n}{k}$$
    else:
    $$E_i = n\\times\\frac{E_{p_i}}{n_p}$$
    $$n_p = \\sum_{i=1}^k E_{p_i}$$
    
    *Symbols used:*
    * \(k\) the number of categories
    * \(F_i\) the (absolute) frequency of category i
    * \(E_i\) the expected frequency of category i
    * \(E_{p_i}\) the provided expected frequency of category i
    * \(n\) the sample size, i.e. the sum of all frequencies
    * \(n_p\) the sum of all provided expected counts
    * \(\\chi^2\\left(\\dots\\right)\)	the chi-square cumulative density function
    
    The Yates correction (yates) is calculated using (Yates, 1934, p. 222):
    $$\\chi_{PY}^2 = \\sum_{i=1}^k \\frac{\\left(\\left|F_i - E_i\\right| - 0.5\\right)^2}{E_i}$$
    
    The Pearson correction (pearson) is calculated using (E.S. Pearson, 1947, p. 157):
    $$\\chi_{PP}^2 = \\chi_{P}^{2}\\times\\frac{n - 1}{n}$$
    
    The Williams correction (williams) is calculated using (Williams, 1976, p. 36):
    $$\\chi_{PW}^2 = \\frac{\\chi_{P}^2}{q}$$
    With:
    $$q = 1 + \\frac{k^2 - 1}{6\\times n\\times df}$$
    
    The formula is also used by McDonald (2014, p. 87)
    
    Example
    -------
    >>> data = pd.DataFrame(["MARRIED", "DIVORCED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "NEVER MARRIED", "MARRIED", "MARRIED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "MARRIED"], columns=["marital"])
    
    >>> ts_pearson_gof(datadata['marital'])
    >>> eCounts = pd.DataFrame({'category' : ["MARRIED", "DIVORCED", "NEVER MARRIED", "SEPARATED"], 'count' : [5,5,5,5]})
    >>> ts_pearson_gof(data['marital'], eCounts)
    >>> ts_pearson_gof(data['marital'], cc="pearson")
    
    References 
    ----------
    McDonald, J. H. (2014). *Handbook of biological statistics* (3rd ed.). Sparky House Publishing.
    
    Pearson, E. S. (1947). The choice of statistical tests illustrated on the Interpretation of data classed in a 2 × 2 table. *Biometrika, 34*(1/2), 139–167. https://doi.org/10.2307/2332518
    
    Pearson, K. (1900). On the criterion that a given system of deviations from the probable in the case of a correlated system of variables is such that it can be reasonably supposed to have arisen from random sampling. *Philosophical Magazine Series 5, 50*(302), 157–175. https://doi.org/10.1080/14786440009463897
    
    Peck, R., & Devore, J. L. (2012). *Statistics: The exploration and analysis of data* (7th ed). Brooks/Cole.
    
    Williams, D. A. (1976). Improved likelihood ratio tests for complete contingency tables. *Biometrika, 63*(1), 33–37. https://doi.org/10.2307/2335081
    
    Yates, F. (1934). Contingency tables involving small numbers and the chi square test. *Supplement to the Journal of the Royal Statistical Society, 1*(2), 217–235. https://doi.org/10.2307/2983604

    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    '''
    if type(data) == list:
        data = pd.Series(data)
    
    #the sample size n
    n = len(data)
    
    #determine the observed counts
    
    if expCount is None:
        #generate frequency table
        freq = data.value_counts()
        n = sum(freq)
        freq = freq.rename_axis('category').reset_index(name='count')
        
        #number of categories to use (k)
        k = len(freq)
        
        #number of expected counts is simply sample size
        nE = n
    else:
        #if expected counts are given
        
        #number of categories to use (k)
        k = len(expCount)
        
        freq = pd.DataFrame(columns = ["category", "count"])
        for i in range(0, k):
            nk = data[data==expCount.iloc[i, 0]].count()
            lk = expCount.iloc[i, 0]
            freq = pd.concat([freq, pd.DataFrame([{"category": lk, "count": nk}])])
        nE = sum(expCount.iloc[:,1])
            
        freq = freq.reset_index(drop=True)
    
    n = sum(freq["count"])
    
    #the degrees of freedom
    df = k - 1
    
    #the true expected counts
    if expCount is None:
        #assume all to be equal
        expC = [n/k] * k
        
    else:
        #check if categories match
        expC = []
        for i in range(0,k):
            expC.append(expCount.iloc[i, 1]/nE*n)
            
    #calculate the chi-square value
    chiVal = 0
    if cc is None or cc == "pearson" or cc == "williams":
        for i in range(0, k):
            chiVal = chiVal + ((freq.iloc[i, 1]) - expC[i])**2 / expC[i]

        if not (cc is None) and cc == "pearson":
            chiVal = (n - 1) / n * chiVal
        elif not (cc is None) and cc == "williams":
            chiVal = chiVal / (1 + (k ^ 2 - 1) / (6 * n * (k - 1)))
        
    elif not (cc is None) and cc == "yates":
        for i in range(0, k):
            chiVal = chiVal + (abs((freq.iloc[i, 1]) - expC[i]) - 0.5)**2 / expC[i]
    
    pVal = chi2.sf(chiVal, df)
    
    minExp = min(expC)
    propBelow5 = sum(1 if x < 5 else 0 for x in expC)/k
    
    #Which test was used
    testUsed = "Pearson chi-square test of goodness-of-fit"
    if not (cc is None) and cc == "pearson":
        testUsed = testUsed + ", with E. Pearson continuity correction"
    elif not (cc is None) and cc == "williams":
        testUsed = testUsed + ", with Williams continuity correction"
    elif not (cc is None) and cc == "yates":
        testUsed = testUsed + ", with Yates continuity correction"
    
    testResults = pd.DataFrame([[chiVal, df, pVal, minExp, propBelow5, testUsed]], columns=["statistic", "df", "p-value", "minExp", "propBelow5", "test"])
    pd.set_option('display.max_colwidth', None)
    
    return testResults
