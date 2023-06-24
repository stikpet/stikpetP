from scipy.stats import t 
import pandas as pd

def ts_student_t_os(data, mu=None, sigma=None):
    '''
    One-Sample Student t-Test
    
    A test for a single (arithmetic) mean.
    
    The assumption about the population (null hypothesis) for this test is a pre-defined mean, i.e. the (arithmetic) mean that is expected in the population. If the p-value (significance) is then below a pre-defined threhold (usually 0.05), the assumption is rejected.
    
    Paramaters
    ----------
    data : a pandas data series with the data as numbers
    mu : optional hypothesized mean, otherwise the midrange will be used
    sigma : optional population standard deviation, if not set the sample results will be used
    
    Returns
    -------
    A dataframe with:
    
    * *mu*, the hypothesized mean
    * *sample mean*, the sample mean
    * *statistic*, the test statistic (t-value)
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
    $$\\bar{x} = \\frac{\\sum_{i=1}^nx_i}{n}$$
    
    *Symbols used:*
    
    * \(T\\left(\\dots, \\dots\\right)\) the cumulative distribution function of the t-distribution
    * \(\\bar{x}\) the sample mean
    * \(\\mu_{H_0}\) the hypothesized mean in the population
    * \(SE\) the standard error (i.e. the standard deviation of the sampling distribution)
    * \(n\) the sample size (i.e. the number of scores)
    * \(s\) the unbiased sample standard deviation
    * \(x_i\) the i-th score
    
    The Student t test (Student, 1908) was described by Gosset under the pseudo name Student.
    
    References
    ----------
    Student. (1908). The probable error of a mean. *Biometrika, 6*(1), 1–25. https://doi.org/10.1093/biomet/6.1.1
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    '''
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
    tValue = (m - mu)/se
    df = n - 1
    
    pValue = 2 * (1 - t.cdf(abs(tValue), df)) 
    
    testUsed = "one-sample Student t"
    testResults = pd.DataFrame([[mu, m, tValue, pValue, testUsed]], columns=["mu", "sample mean", "statistic", "p-value", "test used"])
    
    return (testResults)