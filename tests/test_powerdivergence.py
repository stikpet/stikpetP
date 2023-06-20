import pandas as pd
import numpy as np
from scipy.stats import chi2

def ts_powerdivergence(var1, var2=None, expCounts=None, lambd=2/3, corr=None):
    '''
    Power Divergence Tests
    A test that can be used with a single nominal variable, to test if the probabilities in all the categories are equal (the null hypothesis), or with two nominal variables to test if they are independent.
    
    There are quite a few tests that can do this. Perhaps the most commonly used is the Pearson chi-square test (\(\\chi^2\)), but also an exact multinomial, G-test (\(G^2}), Freeman-Tukey (\(T^2\)), Neyman (\(NM^2\)), Mod-Log Likelihood (\(GM^2\)), and Freeman-Tukey-Read test are possible.
    
    Cressie and Read (1984, p. 463) noticed how the \(\\chi^2\), \(G^2\), \(T^2\), \(NM^2\) and \(GM^2\) can all be captured with one general formula. The additional variable lambda (\(\\lambda\)) was then investigated, and they settled on a \(\\lambda\) of 2/3.
    
    By setting \(\\lambda\) to different values, we get the different tests:
    * *\(\\lambda = 1\)*, Pearson chi-square
    * *\(\\lambda = 0\)*, G/Wilks/Likelihood-Ratio
    * *\(\\lambda = -\\frac{1}{2}\)*, Freeman-Tukey
    * *\(\\lambda = -1\)*, Mod-Log-Likelihood
    * *\(\\lambda = -2\)*, Neyman
    * *\(\\lambda = \\frac{2}{3}\)*, Cressie-Read
    
    Parameters
    ----------
    var1 : a list or pandas data series with the data
    var2 : optional list or pandas data series with the data for tests of independence 
    expCounts : optional counts according to null hypothesis
    lambd : optional either name of test or specific value. Default is "cressie-read" i.e. lambda of 2/3
    corr Optional correction to be used.
    
    Returns 
    --------
    testResults : Pandas dataframe with:
    
    * *statistic*, the chi-square statistic
    * *df*, the degrees of freedom
    * *pValue*, two-sided p-value
    * *minExp*, the minimum expected count
    * *propBelow5*, the proportion of expected counts below 5
    * *testUsed*, a description of the test used
    
    Notes
    -----
    The formula used is (Cressie & Read, 1984, p. 442):
    $$\\chi_{C}^{2} = \\begin{cases} 2\\times\\sum_{i=1}^{r}\\sum_{j=1}^c\\left(F_{i,j}\\times ln\\left(\\frac{F_{i,j}}{E_{i,j}}\\right)\\right) & \\text{ if } \\lambda=0 \\\ 2\\times\\sum_{i=1}^{r}\\sum_{j=1}^c\\left(E_{i,j}\\times ln\\left(\\frac{E_{i,j}}{F_{i,j}}\\right)\\right) & \\text{ if } \\lambda=-1 \\\ \\frac{2}{\\lambda\\times\\left(\\lambda + 1\\right)} \\times \\sum_{i=1}^{r}\\sum_{j=1}^{c} F_{i,j}\\times\\left(\\left(\\frac{F_{i,j}}{E_{i,j}}\\right)^{\\lambda} - 1\\right) & \\text{ else } \\end{cases}$$
    $$df = \\left(r - 1\\right)\\times\\left(c - 1\\right)$$
    $$sig. = 1 - \\chi^2\\left(\\chi_{C}^{2},df\\right)$$
    
    With:
    $$n = \\sum_{i=1}^r \\sum_{j=1}^c F_{i,j}$$
    $$E_{i,j} = \\frac{R_i\\times C_j}{n}$$
    $$R_i = \\sum_{j=1}^c F_{i,j}$$
    $$C_j = \\sum_{i=1}^r F_{i,j}$$
    
    *Symbols used:*
    
    * \(r\) the number of categories in the first variable (the number of rows)
    * \(c\) the number of categories in the second variable (the number of columns)
    * \(F_{i,j}\) the observed count in row i and column j
    * \(E_{i,j}\) the expected count in row i and column j
    * \(R_i\) the i-th row total
    * \(C_j\) the j-th column total
    * \(n\) the sum of all counts
    * \(\\chi^2\\left(\\dots\\right)\) the chi-square cumulative density function
    
    Cressie and Read (1984, p. 463) suggest to use \(\\lambda = \\frac{2}{3}\),  which is therefor the default in this function.
    
    The **Pearson chi-square statistic** can be obtained by setting \(\\lambda = 1\). Pearson's original formula is (Pearson, 1900, p. 165):
    $$\\chi_{P}^2 = \\sum_{i=1}^r \\sum_{j=1}^c \\frac{\\left(F_{i,j} - E_{i,j}\\right)^2}{E_{i,j}}$$
    
    The **Freeman-Tukey test** has as a formula (Bishop et al., 2007, p. 513):
    $$T^2 = 4\\times\\sum_{i=1}^r \\sum_{j=1}^c \\left(\\sqrt{F_{i,j}} - \\sqrt{E_{i,j}}\\right)^2$$
    
    This will be same as setting lambda to \(-\\frac{1}{2}\). Note that the source for the formula is often quoted to be from Freeman and Tukey (1950) but couldn't really find it in that article.
    
    **Neyman test** formula was very similar to Pearson's, but the observed and expected counts swapped (Neyman, 1949, p. 250):
    $$\\chi_{N}^2 = \\sum_{i=1}^r \\sum_{j=1}^c \\frac{\\left(E_{i,j} - F_{i,j}\\right)^2}{F_{i,j}}$$
    
    This will be same as setting lambda to \(-2\).
    
    The Yates correction (yates) is calculated using (Yates, 1934, p. 222):
    Use instead of \(F_{i,j}\) the adjusted version defined by:
    $$F_{i,j}^\\ast = \\begin{cases} F_{i,j} - 0.5 & \\text{ if } F_{i,j}>E_{i,j}  \\\ F_{i,j} & \\text{ if } F_{i,j}= E_{i,j}\\\ F_{i,j} + 0.5 & \\text{ if } F_{i,j}<E_{i,j} \\end{cases}$$
    
    The Pearson correction (pearson) is calculated using (E.S. Pearson, 1947, p. 157):
    $$\\chi_{PP}^2 = \\chi_{P}^{2}\\times\\frac{n - 1}{n}$$
    
    The Williams correction (williams) is calculated using (Williams, 1976, p. 36):
    $$\\chi_{PW}^2 = \\frac{\\chi_{P}^2}{q}$$
    
    With:
    $$q = 1 + \\frac{\\left(n\\times\\left(\\sum_{i=1}^r \\frac{1}{R_i}\\right)-1\\right) \\times \\left(n\\times\\left(\\sum_{j=1}^c \\frac{1}{C_j}\\right)-1\\right)}{6\\times n\\times df}$$
    
    References 
    ----------
    Bishop, Y. M. M., Fienberg, S. E., & Holland, P. W. (2007). *Discrete multivariate analysis*. Springer.
    
    Cressie, N., & Read, T. R. C. (1984). Multinomial goodness-of-fit tests. *Journal of the Royal Statistical Society: Series B (Methodological), 46*(3), 440–464. https://doi.org/10.1111/j.2517-6161.1984.tb01318.x
    
    Freeman, M. F., & Tukey, J. W. (1950). Transformations related to the angular and the square root. *The Annals of Mathematical Statistics, 21*(4), 607–611. https://doi.org/10.1214/aoms/1177729756
    
    Neyman, J. (1949). Contribution to the theory of the chi-square test. Berkeley Symposium on Math. Stat, and Prob, 239–273. https://doi.org/10.1525/9780520327016-030
    
    Pearson, E. S. (1947). The choice of statistical tests illustrated on the Interpretation of data classed in a 2 × 2 table. *Biometrika, 34*(1/2), 139–167. https://doi.org/10.2307/2332518
    
    Pearson, K. (1900). On the criterion that a given system of deviations from the probable in the case of a correlated system of variables is such that it can be reasonably supposed to have arisen from random sampling. *Philosophical Magazine Series 5, 50*(302), 157–175. https://doi.org/10.1080/14786440009463897
    
    Wilks, S. S. (1938). The large-sample distribution of the likelihood ratio for testing composite hypotheses. *The Annals of Mathematical Statistics, 9*(1), 60–62. https://doi.org/10.1214/aoms/1177732360
    
    Williams, D. A. (1976). Improved likelihood ratio tests for complete contingency tables. *Biometrika, 63*(1), 33–37. https://doi.org/10.2307/2335081
    
    Yates, F. (1934). Contingency tables involving small numbers and the chi square test. *Supplement to the Journal of the Royal Statistical Society, 1*(2), 217–235. https://doi.org/10.2307/2983604
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    '''
    #Set correction factor to 1 (no correction)
    corFactor = 1
    
    #Test Used
    if lambd == 2/3 or lambd == "cressie-read":
        lambd = 2/3
        testUsed = "Cressie-Read"
    
    elif lambd==0 or lambd == "likelihood ratio":
        lambd=0
        testUsed = "likelihood-ratio"
        
    elif lambd==-1 or lambd == "mod-log":
        lambd=-1
        testUsed = "mod-log likelihood ratio"
        
    elif lambd==1 or lambd=="pearson":
        lambd=1
        testUsed = "Pearson chi-square"
    
    elif lambd==-0.5 or lambd=="freeman-tukey":
        lambd=-0.5
        testUsed = "Freeman-Tukey"
    elif lambd==-2 or lambd=="neyman":
        lambd=-2
        testUsed = "Neyman"
    else:
        testUsed = "power divergence with lambda = " + str(lambd)
        
        
    #The test itself
    
    if (var2 is None):
        #only one variable, so goodness-of-fit version
        
        freqs = var1.value_counts()
        k = len(freqs)
        
        #Determine expected counts if not provided
        if expCounts is None:
            expCounts = [sum(freqs)/len(freqs)]* k
            expCounts = pd.Series(expCounts, index=list(freqs.index.values))
        
        n = sum(freqs)
        df = k - 1
        
        #set williams correction factor
        if corr=="williams":
            corFactor = 1/(1 + (k**2 - 1)/(6*n*df))
            testUsed = testUsed + ", and Williams correction"
        
    else:
        #two variables, so use test of independence
        
        #create a cross table
        myCrosstable = pd.crosstab(var1, var2)
        colTotals = myCrosstable.sum()
        rowTotals = myCrosstable.sum(axis=1)
        n = sum(colTotals)
        r = len(rowTotals)
        c = len(colTotals)
        
        #Determine expected counts if not provided
        if expCounts is None:
            expCounts = myCrosstable.copy()
            for i in range(0, r):
                for j in range(0, c):
                    expCounts.iloc[i,j] = rowTotals[i]*colTotals[j]/n

            #convert the expected counts in the cross table to one long pandas series
            expCountsList = list(expCounts.iloc[:,0])
            for j in range(1,c):
                expCountsList = expCountsList + list(expCounts.iloc[:,j])
            expCounts = pd.Series(expCountsList) 
        
        #convert the frequencies in the cross table to one long pandas series
        freqsList = list(myCrosstable.iloc[:,0])
        for j in range(1,c):
            freqsList = freqsList + list(myCrosstable.iloc[:,j])
        freqs = pd.Series(freqsList) 
        
        df = (r - 1)*(c - 1)
        
        #set williams correction factor
        if corr=="williams":
            corFactor = 1/(1 + (n*sum(1/rowTotals) - 1)*(n*sum(1/colTotals) - 1)/(6*n*(r - 1)*(c - 1)))
            testUsed = testUsed + ", and Williams correction"
    
    #adjust frequencies if Yates correction is requested
    if corr=="yates":
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
    if lambd==0:
        ts = 2*sum(freqs*np.log(freqs/expCounts))
    elif lambd==-1:
        ts = 2*sum(expCounts*np.log(expCounts/freqs))
    else:
        ts = 2*sum(freqs*((freqs/expCounts)**(lambd) - 1))/(lambd*(lambd + 1))
    
    #set E.S. Pearson correction
    if corr=="pearson":
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