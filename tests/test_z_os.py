from statistics import NormalDist
import pandas as pd

def ts_z_os(data, mu=None, sigma=None):
    '''
    One-Sample Z Test
    -----------------
    
    This test is often used if there is a large sample size. For smaller sample sizes, a Student t-test
    is usually used.
    
    The assumption about the population (null hypothesis) for this test is a pre-defined mean, i.e. the 
    (arithmetic) mean that is expected in the population. If the p-value (significance) is then below a 
    pre-defined threhold (usually 0.05), the assumption is rejected.
    
    Parameters
    ----------
    data : list or pandas data series
        the data as numbers
    mu : float, optional
        hypothesized mean, otherwise the midrange will be used
    sigma : float, optional 
        population standard deviation, if not set the sample results will be used
    
    Returns
    -------
    A dataframe with:
    
    * *mu*, the hypothesized mean
    * *sample mean*, the sample mean
    * *statistic*, the test statistic (z-value)
    * *p-value*, the significance (p-value)
    * *test used*, name of test used
    
    Notes
    -----
    The formula used is:
    $$z = \\frac{\\bar{x} - \\mu_{H_0}}{SE}$$
    $$sig = 2\\times\\left(1 - \\Phi\\left(\\left|z\\right|\\right)\\right)$$
    
    With:
    $$SE = \\frac{\\sigma}{\\sqrt{n}}$$
    $$\\sigma \\approx s = \\sqrt{\\frac{\\sum_{i=1}^n\\left(x_i - \\bar{x}\\right)^2}{n - 1}}$$
    $$\\bar{x} = \\frac{\\sum_{i=1}^nx_i}{n}$$
    
    *Symbols used:*
    
    * \\(\\Phi\\left(\\dots\\right)\\) the cumulative distribution function of the standard normal distribution
    * \\(\\bar{x}\\) the sample mean
    * \\(\\mu_{H_0}\\) the hypothesized mean in the population
    * \\(SE\\) the standard error (i.e. the standard deviation of the sampling distribution)
    * \\(n\\) the sample size (i.e. the number of scores)
    * \\(s\\) the unbiased sample standard deviation
    * \\(x_i\\) the i-th score
    
    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    ---------
    >>> pd.set_option('display.width',1000)
    >>> pd.set_option('display.max_columns', 1000)
    
    Example 1: pandas series
    >>> df2 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/StudentStatistics.csv', sep=';', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> ex1 = df2['Gen_Age']
    >>> ts_z_os(ex1)
         mu  sample mean  statistic  p-value     test used
    0  68.5    24.454545 -19.291196      0.0  one-sample z
    >>> ts_z_os(ex1, mu=22, sigma=12.1)
       mu  sample mean  statistic   p-value     test used
    0  22    24.454545   1.345588  0.178435  one-sample z
    
    Example 2: Numeric list
    >>> ex2 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    >>> ts_z_os(ex2)
        mu  sample mean  statistic   p-value     test used
    0  3.0     3.444444    1.19335  0.232732  one-sample z

    '''
    if type(data) is list:
        data = pd.Series(data)
        
    data = data.dropna()
    
    if (mu is None):
        mu = (min(data) + max(data))/2
    
    n = len(data)
    m = data.mean()
    if (sigma is None):
        s = data.std()
    else:
        s = sigma
        
    se = s/n**0.5
    z = (m - mu)/se
    pValue = 2 * (1 - NormalDist().cdf(abs(z))) 
    
    testUsed = "one-sample z"
    testResults = pd.DataFrame([[mu, m, z, pValue, testUsed]], columns=["mu", "sample mean", "statistic", "p-value", "test used"])
    
    return (testResults)