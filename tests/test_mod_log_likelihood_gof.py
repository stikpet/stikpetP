import pandas as pd
import numpy as np
from scipy.stats import chi2

def ts_mod_log_likelihood_gof(data, expCounts=None, cc=None):
    '''
    Mod-Log Likelihood Test of Goodness-of-Fit
    
    A test that can be used with a single nominal variable, to test if the probabilities in all the categories are equal (the null hypothesis). If the test has a p-value below a pre-defined threshold (usually 0.05) the assumption they are all equal in the population will be rejected.
    
    There are quite a few tests that can do this. Perhaps the most commonly used is the Pearson chi-square test, but also an exact multinomial, G-test, Neyman, Freeman-Tukey, Cressie-Read, and Freeman-Tukey-Read test are possible.
    
    Parameters
    ----------
    data :  list or Pandas data series with the data
    expCount : optional dataframe with the categories and expected counts 
    cc : ptional continuity correction None (default), "yates", "pearson", or "williams"
    
    Returns
    -------
    testResults : Pandas dataframe with:
    
    * *statistic*, the chi-square statistic
    * *df*, the degrees of freedom
    * *pValue*, two-sided p-value
    * *minExp*, the minimum expected count
    * *propBelow5*, the proportion of expected counts below 5
    * *testUsed*, a description of the test used
    
    Notes
    -----
    The formula used (Cressie & Read, 1984, p. 441):
    $$MG=2\\times\\sum_{i=1}^{k}\\left(F_{i}\\times \\ln\\left(\\frac{F_{i}}{E_{i}}\\right)\\right)$$
    $$df = k - 1$$
    $$sig. = 1 - \\chi^2\\left(MG,df\\right)$$
    
    With:
    $$n = \\sum_{i=1}^k F_i$$
    
    If no expected counts provided:
    $$E_i = \\frac{n}{k}$$
    else:
    $$E_i = n\\times\\frac{E_{p_i}}{n_p}$$
    $$n_p = \\sum_{i=1}^k E_{p_i}}
    
    *Symbols used:*
    * \(k\) the number of categories
    * \(F_i\) the (absolute) frequency of category i
    * \(E_i\) the expected frequency of category i
    * \(E_{p_i}\) the provided expected frequency of category i
    * \(n\) the sample size, i.e. the sum of all frequencies
    * \(n_p\) the sum of all provided expected counts
    * \(\\chi^2\\left(\\dots\\right)\) the chi-square cumulative density function
    
    Cressie and Read (1984) is not the original source, but the source where I found the formula.
    
    The Yates continuity correction (cc="yates") is calculated using (Yates, 1934, p. 222):
    $$F_i^\\ast  = \\begin{cases} F_i - 0.5 & \\text{ if } F_i > E_i \\\ F_i + 0.5 & \\text{ if } F_i < E_i \\\ F_i & \\text{ if } F_i = E_i \\end{cases}$$
    $$MG_Y=2\\times\\sum_{i=1}^{k}\\left(F_i^\\ast\\times ln\\left(\\frac{F_i^\\ast}{E_{i}}\\right)\\right)$$
    Where if \\(F_i^\\ast = 0\\) then \\(F_i^\\ast\\times ln\\left(\\frac{F_i^\\ast}{E_{i}}\\right) = 0\\).
    
    The Pearson correction (cc="pearson") is calculated using (E.S. Pearson, 1947, p. 157):
    $$\\chi_{PP}^2 = \\chi_{P}^{2}\\times\\frac{n - 1}{n}$$
    
    The Williams correction (cc="williams") is calculated using (Williams, 1976, p. 36):
    $$\\chi_{PW}^2 = \\frac{\\chi_{P}^2}{q}$$
    
    With:
    $$q = 1 + \\frac{k^2 - 1}{6\\times n\\times df}$$
    
    The formula is also used by McDonald (2014, p. 87)
    
    References
    ----------
    Cressie, N., & Read, T. R. C. (1984). Multinomial goodness-of-fit tests. *Journal of the Royal Statistical Society: Series B (Methodological), 46*(3), 440–464. https://doi.org/10.1111/j.2517-6161.1984.tb01318.x
    
    Pearson, E. S. (1947). The choice of statistical tests illustrated on the Interpretation of data classed in a 2 × 2 table. *Biometrika, 34*(1/2), 139–167. https://doi.org/10.2307/2332518
    
    Williams, D. A. (1976). Improved likelihood ratio tests for complete contingency tables. *Biometrika, 63*(1), 33–37. https://doi.org/10.2307/2335081
    
    Yates, F. (1934). Contingency tables involving small numbers and the chi square test. *Supplement to the Journal of the Royal Statistical Society, 1*(2), 217–235. https://doi.org/10.2307/2983604
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    Examples
    ---------
    >>> data = pd.DataFrame(["MARRIED", "DIVORCED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "NEVER MARRIED", "MARRIED", "MARRIED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "MARRIED"], columns=["marital"])
    >>> ts_mod_log_likelihood_gof(data)
    >>> eCounts = pd.DataFrame({'category' : ["MARRIED", "DIVORCED", "NEVER MARRIED", "SEPARATED"], 'count' : [5,5,5,5]})
    >>> ts_mod_log_likelihood_gof(data['marital'], eCounts)
    
    '''
    
    if type(data) == list:
        data = pd.Series(data)
        
    #Set correction factor to 1 (no correction)
    corFactor = 1    
    testUsed = "mod-log likelihood ratio"
    
    #The test itself        
    freqs = data.value_counts()
    k = len(freqs)

    #Determine expected counts if not provided
    if expCounts is None:
        expCounts = [sum(freqs)/len(freqs)]* k
        expCounts = pd.Series(expCounts, index=list(freqs.index.values))

    n = sum(freqs)
    df = k - 1

    #set williams correction factor
    if cc=="williams":
        corFactor = 1/(1 + (k**2 - 1)/(6*n*df))
        testUsed = testUsed + ", and Williams correction"
    
    #adjust frequencies if Yates correction is requested
    if cc=="yates":
        k = len(freqs)
        adjFreq = list(freqs).copy()
        for i in range(0, k):
            if adjFreq[i] > expCounts[i]:
                adjFreq[i] = adjFreq[i] - 0.5
            elif adjFreq[i] < expCounts[i]:
                adjFreq[i] = adjFreq[i] + 0.5

        freqs = pd.Series(adjFreq, index=list(freqs.index.values))
        testUsed = testUsed + ", and Yates correction"
    
    #determine the test statistic
    ts = 2*sum(expCounts*np.log(expCounts/freqs))
    
    #set E.S. Pearson correction
    if cc=="pearson":
        corFactor = (n - 1)/n
        testUsed = testUsed + ", and Pearson correction"
    
    #Adjust test statistic
    ts = ts*corFactor
    
    #Determine p-value
    pVal = chi2.sf(ts, df)
    
    #Check minimum expected counts
    #Cells with expected count less than 5
    nbelow = len([x for x in expCounts if x < 5])
    #Number of cells
    ncells = len(expCounts)
    #As proportion
    pBelow = nbelow/ncells
    #the minimum expected count
    minExp = min(expCounts)
    
    #prepare results
    testResults = pd.DataFrame([[ts, df, pVal, minExp, pBelow*100, testUsed]], columns=["statistic", "df", "p-value", "minExp", "percBelow5", "test used"])        
    pd.set_option('display.max_colwidth', None)
    
    return testResults