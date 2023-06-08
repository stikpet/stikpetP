from math import log
import pandas as pd
from scipy.stats import chi2

def ts_g_gof(data, expCount=None, cc=None):
    '''
    G (Likelihood Ratio) Goodness-of-Fit Test
     
    A test that can be used with a single nominal variable, to test if the probabilities in all the categories are equal (the null hypothesis). If the test has a p-value below a pre-defined threshold (usually 0.05) the assumption they are all equal in the population will be rejected. 
    
    There are quite a few tests that can do this. Perhaps the most commonly used is the Pearson chi-square test, but also an exact multinomial, Freeman-Tukey, Neyman, Mod-Log Likelihood and Cressie-Read test are possible.
    
    Parameters
    ----------
    data : list or Pandas data series with the data
    expCount : Optional Pandas data frame with categories and expected counts
    cc : Optional which continuity correction to use, either None (default), "yates", "pearson", or "williams"
        
    Returns
    -------
    Pandas Dataframe with:
    
    * *statistic*, the chi-square statistic
    * *df*, the degrees of freedom
    * *pValue*, two-sided p-value
    * *minExp*, the minimum expected count
    * *propBelow5*, the proportion of expected counts below 5
    * *testUsed*, a description of the test used
   
    Notes
    -----
    It uses chi2 from scipy's stats library for the chi-square distribution
    
    The formula used (Wilks, 1938, p. 62):
    $$G=2\\times\\sum_{i=1}^{k}\\left(F_{i}\\times ln\\left(\\frac{F_{i}}{E_{i}}\\right)\\right)$$
    $$df = k - 1$$
    $$sig. = 1 - \\chi^2\\left(G,df\\right)$$
    
    With:
    $$n = \\sum_{i=1}^k F_i$$
    
    If no expected counts provided:
    $$E_i = \\frac{n}{k}$$
    else:
    $$E_i = n\\times\\frac{E_{p_i}}{n_p}$$
    $$n_p = \\sum_{i=1}^k E_{p_i}$$
    
    *Symbols used*:
    * \(k\) the number of categories
    * \(F_i\) the (absolute) frequency of category i
    * \(E_i\) the expected frequency of category i
    * \(E_{p_i}\) the provided expected frequency of category i
    * \(n\) the sample size, i.e. the sum of all frequencies
    * \(n_p\) the sum of all provided expected counts
    * \(\\chi^2\\left(\\dots\\right)\) the chi-square cumulative density function
    
    The term ‘Likelihood Ratio Goodness-of-Fit’ can for example be found in an article from Quine and Robinson (1985), the term ‘Wilks’s likelihood ratio test’ can also be found in Li and Babu (2019, p. 331), while the term G-test is found in Hoey (2012, p. 4)
    
    The Yates continuity correction (cc="yates") is calculated using (Yates, 1934, p. 222):
    $$F_i^\\ast  = \\begin{cases} F_i - 0.5 & \\text{ if } F_i > E_i \\\ F_i + 0.5 & \\text{ if } F_i < E_i \\\ F_i & \\text{ if } F_i = E_i \\end{cases}$$
    $$G_Y=2\\times\\sum_{i=1}^{k}\\left(F_i^\\ast\\times ln\\left(\\frac{F_i^\\ast}{E_{i}}\\right)\\right)$$
    
    Where if \(F_i^\\ast = 0\) then \(F_i^\\ast\\times \\ln\\left(\\frac{F_i^\\ast}{E_{i}}\\right) = 0\)
    
    The Pearson correction (cc="pearson") is calculated using (E.S. Pearson, 1947, p. 157):
    $$G_{P} = G\\times\\frac{n - 1}{n}$$
    
    The Williams correction (cc="williams") is calculated using (Williams, 1976, p. 36):
    $$G_{W} = \\frac{G}{q}$$
    With:
    $$q = 1 + \\frac{k^2 - 1}{6\\times n\\times df}$$
    
    The formula is also used by McDonald (2014, p. 87)
    
    References 
    ----------
    Hoey, J. (2012). The two-way likelihood ratio (G) test and comparison to two-way chi squared test. 1–6. https://doi.org/10.48550/ARXIV.1206.4881
    
    Li, B., & Babu, G. J. (2019). *A graduate course on statistical inference*. Springer.
    
    McDonald, J. H. (2014). *Handbook of biological statistics* (3rd ed.). Sparky House Publishing.
    
    Pearson, E. S. (1947). The choice of statistical tests illustrated on the Interpretation of data classed in a 2 × 2 table. *Biometrika, 34*(1/2), 139–167. https://doi.org/10.2307/2332518
    
    Quine, M. P., & Robinson, J. (1985). Efficiencies of chi-square and likelihood Ratio goodness-of-fit tests. *The Annals of Statistics, 13*(2), 727–742. https://doi.org/10.1214/aos/1176349550
    
    Wilks, S. S. (1938). The large-sample distribution of the likelihood ratio for testing composite hypotheses. *The Annals of Mathematical Statistics, 9*(1), 60–62. https://doi.org/10.1214/aoms/1177732360
    
    Williams, D. A. (1976). Improved likelihood ratio tests for complete contingency tables. *Biometrika, 63*(1), 33–37. https://doi.org/10.2307/2335081
    
    Yates, F. (1934). Contingency tables involving small numbers and the chi square test. *Supplement to the Journal of the Royal Statistical Society, 1*(2), 217–235. https://doi.org/10.2307/2983604
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    Examples
    --------
    >>> data = pd.DataFrame(["MARRIED", "DIVORCED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "NEVER MARRIED", "MARRIED", "MARRIED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "MARRIED"], columns=["marital"])
    >>> ts_g_gof(data)
    >>> eCounts = pd.DataFrame({'category' : ["MARRIED", "DIVORCED", "NEVER MARRIED", "SEPARATED"], 'count' : [5,5,5,5]})
    >>> ts_g_gof(data, eCounts)
    >>> ts_g_gof(data, cc="pearson")
    
    '''
    
    if type(data) == list:
        data = pd.Series(data)
    
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
            nk = data[data==expCount.iloc[i, 0]].count()[0]
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
    
    #adjust observed counts if Yates continuity correction is used
    if not (cc is None) and cc == "yates":
        for i in range(k):
            if freq.iloc[i, 1]>expC[i]:
                freq.iloc[i, 1] = freq.iloc[i, 1] - 0.5
            elif freq.iloc[i, 1]<expC[i]:
                freq.iloc[i, 1] = freq.iloc[i, 1] + 0.5
        
    for i in range(k):
        chiVal = chiVal + freq.iloc[i, 1]*log(freq.iloc[i, 1]/expC[i])

    chiVal = 2*chiVal
    
    if not (cc is None) and cc == "pearson":
        chiVal = (n - 1) / n * chiVal
    elif not (cc is None) and cc == "williams":
        chiVal = chiVal / (1 + (k ^ 2 - 1) / (6 * n * (k - 1)))
    
    pVal = chi2.sf(chiVal, df)
    
    minExp = min(expC)
    propBelow5 = sum(1 if x < 5 else 0 for x in expC)/k
    
    #Which test was used
    testUsed = "G test of goodness-of-fit"
    if not (cc is None) and cc == "pearson":
        testUsed = testUsed + ", with E. Pearson continuity correction"
    elif not (cc is None) and cc == "williams":
        testUsed = testUsed + ", with Williams continuity correction"
    elif not (cc is None) and cc == "yates":
        testUsed = testUsed + ", with Yates continuity correction"
    
    testResults = pd.DataFrame([[chiVal, df, pVal, minExp, propBelow5, testUsed]], columns=["statistic", "df", "p-value", "minExp", "propBelow5", "test"])
    pd.set_option('display.max_colwidth', None)
    
    return testResults

#