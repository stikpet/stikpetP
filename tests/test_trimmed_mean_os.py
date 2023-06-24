import pandas as pd
import math
from scipy.stats import t

def ts_trimmed_mean_os(data, mu=None, trim=0.1, se="yuen"):
    '''
    One-Sample Trimmed Mean Test
    
    A variation on a one-sample Student t-test where the data is first trimmed, and the Winsorized variance is used.
    
    The assumption about the population for this test is that the mean in the population is equal to the provide mu value. The test will show the probability of the found test statistic, or more extreme, if this assumption would be true. If this is below a specific threshold (usually 0.05) the assumption is rejected.
    
    Paramaters
    ----------
    data : a pandas series with the data as numbers
    mu : optional hypothesized trimmed mean, otherwise the midrange will be used
    trim : optional proportion to trim in total. Default is 0.1 (e.g. 0.05 from each side)
    se : optional method to use to determine standard error. Either "yuen" (default) or "wilcox"
    
    Returns
    -------
    pandas dataframe with:
    
    * *trim. mean*, the sample trimmed mean
    * *mu*, hypothesized mean
    * *SE*, the standard error
    * *statistic*, the test statistic (t-value)
    * *df*, degrees of freedom
    * *p-value*, p-value (sig.)
    * *test used*, name of test used
    
    Notes
    -----
    The formula used is:
    $$\frac{\bar{x}_t - \mu_{H_0}}{SE}$$
    $$sig = 2\times\left(1 - T\left(\left|t\right|, df\right)\right)$$
    
    With:
    $$\bar{x}_t = \frac{\sum_{i=g+1}^{n - g}y_i}{}$$
    $$g = \lfloor n\times p_t\rfloor$$
    $$m = n - 2\times g$$
    $$SE = \sqrt{\frac{SSD_w}{m\times\left(m - 1\right)}}$$
    $$SSD_w = g\times\left(y_{g+1} - \bar{x}_w\right)^2 + g\times\left(y_{n-g} - \bar{x}_w\right)^2 + \sum_{i=g+1}^{n - g} \left(y_i - \bar{x}_w\right)^2$$
    $$\bar{x}_w = \frac{\bar{x}_t\times m + g\times\left(y_{g+1} + y_{n-g}\right)}{n}$$
    
    If *se="wilcox" is used, the formula for SE will be adjusted to:
    $$SE = \frac{\sqrt{SSD_w}}{\left(1 - 2\times p_t\right)\times\sqrt{n}}$$
    
    *Symbols used:*
    
    * \(x_t\) the trimmed mean of the scores
    * \(x_w\) The Winsorized mean
    * \(SSD_w\) the sum of squared deviations from the Winsorized mean
    * \(m\) the number of scores in the trimmed data set from category i
    * \(y_i\) the i-th score after the scores are sorted from low to high
    * \(p\) the proportion of trimming on each side, we can define
    
    The test is often also referred to as a Yuen test, or Yuen-Welch test.
    
    The standard error can either be calculated using the first SE, which for example can be found in Tukey and McLaughlin (1963, p. 342), and seems similar to the independent samples version of this test as proposed by Yuen (1974, p. 167)
    
    The second version is used in the other libraries from the software R, and can be found in Wilcox (2012, p. 157), or Peró-Cebollero and Guàrdia-Olmos (2013, p. 409).
    
    References 
    ----------
    Peró-Cebollero, M., & Guàrdia-Olmos, J. (2013). The adequacy of different robust statistical tests in comparing two independent groups. *Psicológica*, 34, 407–424.
    
    Tukey, J. W., & McLaughlin, D. H. (1963). Less vulnerable confidence and significance procedures for location based on a single sample: Trimming/Winsorization 1. *Sankhyā: The Indian Journal of Statistics, 25*(3), 331–352.
    
    Wilcox, R. R. (2012). *Introduction to robust estimation and hypothesis testing* (3rd ed.). Academic Press.
    
    Yuen, K. K. (1974). The two-sample trimmed t for unequal population variances. *Biometrika, 61*(1), 165–170. https://doi.org/10.1093/biomet/61.1.165
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    Examples
    --------
    >>> dataList = [1, 2, 5, 1, 1, 5, 3, 1, 5, 1, 1, 5, 1, 1, 3, 3, 3, 4, 2, 4]
    >>> data = pd.Series(dataList)
    >>> ts_trimmed_mean_os(data)
    
    '''
    
    data = data.dropna()
    data = pd.to_numeric(data)
    data = data.sort_values()
    data = data.reset_index(drop=True)
    
    if mu is None:
        mu = (max(data)+min(data))/2
    
    n = len(data)
    nt = n*trimProp/2
    nl = math.floor(nt)
    mt = data[nl:(n - nl)].mean()
    nat = n - 2*nl
    mw = (mt*nat + nl*(data[nl] + data[nl+nat-1]))/n
    ssdw = nl*(data[nl] - mw)**2 + nl*(data[nl+nat-1] - mw)**2 + sum((data[nl:(nl+nat)] - mw)**2)
    varw = ssdw/(n - 1)
    
    if se=="yuen":
        SE = (ssdw/(nat*(nat - 1)))**0.5
    elif se=="wilcox":
        SE = (varw)**0.5/((1 - trimProp)*(n**0.5))
    
    tValue = (mt - mu)/SE
    df = nat - 1
    pValue = 2 * (1 - t.cdf(abs(tValue), df))
    
    testUsed = "one-sample trimmed mean test"
    results = pd.DataFrame([[mt, mu, se, tValue, df, pValue, testUsed]], columns=["trim. mean", "mu", "SE", "statistic", "df", "p-value", "test used"])
    
    return (results)