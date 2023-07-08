from scipy.stats import t 
import pandas as pd

def ts_student_t_os(data, mu=None):
    '''
    One-Sample Student t-Test
    -------------------------
    
    A test for a single (arithmetic) mean.
    
    The assumption about the population (null hypothesis) for this test is a pre-defined mean, i.e. the (arithmetic) mean that is expected in the population. If the p-value (significance) is then below a pre-defined threhold (usually 0.05), the assumption is rejected.
    
    Parameters
    ----------
    data : list or pandas data series 
        the data as numbers
    mu : float, optional 
        hypothesized mean, otherwise the midrange will be used
    
    Returns
    -------
    A dataframe with:
    
    * *mu*, the hypothesized mean
    * *sample mean*, the sample mean
    * *statistic*, the test statistic (t-value)
    * *df*, the degrees of freedom
    * *p-value*, the significance (p-value)
    * *test used*, name of test used
    
    Notes
    -----
    The formula used is:
    $$t = \\frac{\\bar{x} - \\mu_{H_0}}{SE}$$
    $$sig = 2\\times\\left(1 - T\\left(\\left|t\\right|, df\\right)\\right)$$
    
    With:
    $$df = n - 1$$
    $$SE = \\frac{s}{\\sqrt{n}}$$
    $$s = \\sqrt{\\frac{\\sum_{i=1}^n\\left(x_i - \\bar{x}\\right)^2}{n - 1}}$$
    $$\\bar{x} = \\frac{\\sum_{i=1}^n x_i}{n}$$
    
    *Symbols used:*
    
    * \\(T\\left(\\dots, \\dots\\right)\\) the cumulative distribution function of the t-distribution
    * \\(\\bar{x}\\) the sample mean
    * \\(\\mu_{H_0}\\) the hypothesized mean in the population
    * \\(SE\\) the standard error (i.e. the standard deviation of the sampling distribution)
    * \\(n\\) the sample size (i.e. the number of scores)
    * \\(s\\) the unbiased sample standard deviation
    * \\(x_i\\) the i-th score
    
    The Student t test (Student, 1908) was described by Gosset under the pseudo name Student.
    
    References
    ----------
    Student. (1908). The probable error of a mean. *Biometrika, 6*(1), 1–25. https://doi.org/10.1093/biomet/6.1.1
    
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
    >>> ts_student_t_os(ex1)
         mu  sample mean  statistic  df  p-value             test used
    0  68.5    24.454545 -19.291196  43      0.0  one-sample Student t
    >>> ts_student_t_os(ex1, mu=22)
       mu  sample mean  statistic  df   p-value             test used
    0  22    24.454545   1.075051  43  0.288347  one-sample Student t
    
    Example 2: Numeric list
    >>> ex2 = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    >>> ts_student_t_os(ex2)
        mu  sample mean  statistic  df   p-value             test used
    0  3.0     3.444444    1.19335  17  0.249121  one-sample Student t
    
    '''
    if type(data) is list:
        data = pd.Series(data)
        
    data = data.dropna()
    
    if (mu is None):
        mu = (min(data) + max(data))/2
    
    n = len(data)
    m = data.mean()
    
    s = data.std()
        
    se = s/n**0.5
    tValue = (m - mu)/se
    df = n - 1
    
    pValue = 2 * (1 - t.cdf(abs(tValue), df)) 
    
    testUsed = "one-sample Student t"
    testResults = pd.DataFrame([[mu, m, tValue, df, pValue, testUsed]], columns=["mu", "sample mean", "statistic", "df", "p-value", "test used"])
    
    return (testResults)