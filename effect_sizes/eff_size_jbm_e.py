from math import log
import pandas as pd

def es_jbm_e(chi2, n, minExp, test='chi'):
    '''
    Johnston-Berry-Mielke E
     
    An effect size measure that could be used with a chi-square test or g-test. 
    
    Parameters
    ----------
    chi2 : the chi-square test statistic
    n : the sample size
    minExp: the minimum expected count
    test : either "chi" (default) for chi-square tests, or "g" for likelihood ratio
        
    Returns
    -------
    E : the value of JBM E
   
    Notes
    -----
    Two versions of this effect size. The formula for a chi-square test is:
    $$E_{\\chi^2}=\\frac{q}{1-q}\\times \\left(\\sum_{i=1}^{k}\\frac{p_{i}^{2}}{q_{i}}-1\\right) = \\frac{\\chi_{GoF}^2\\times E_{min}}{n\\times\\left(n - E_{min}\\right)}$$
    For a Likelihood Ratio (G) test:
    $$E_{L}=-\\frac{1}{\\textup{ln}(q)}\\times\\sum_{i=1}^{k}\\left(p_{i}\\times\\textup{ln}\\left(\\frac{p_{i}}{q_{i}}\\right)\\right) = -\\frac{1}{\\textup{ln}\\left(q\\right)\\times\\frac{\\chi_L^2}{2\\times n}}$$
    
    *Symbols used:*
    * \(q\) the minimum of all \(q_i\)
    * \(q_i\) the expected proportion in category i
    * \(p_i\) the observed proportion in category i
    * \(n\) the total sample size
    * \(E_min\) the minimum expected count
    * \(\\chi_{GoF}^2\) the chi-square test statistic of a Pearson chi-square test of goodness-of-fit
    * \(\\chi_L^2\) the chi-square test statistic of a likelihood ratio test of goodness-of-fit 
    
    Both formulas are from Johnston et al. (2006, p. 413)
    
    A qualification rule-of-thumb could be obtained by converting this to Cohen's w, using **es_convert(E, from=="jbme", to=="cohenw", ex1 = minExp/n)**
    
    The rule-of-thumb can then be obtained using **th_cohen_w(w)**
    
    References
    ----------
    Johnston, J. E., Berry, K. J., & Mielke, P. W. (2006). Measures of effect size for chi-squared and likelihood-ratio goodness-of-fit tests. *Perceptual and Motor Skills, 103*(2), 412–414. https://doi.org/10.2466/pms.103.2.412-414
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    Examples
    --------
    >>> chi2Value = 3.105263
    >>> n = 19
    >>> minExp = n/4
    >>> es_jbm_e(chi2Value, n, minExp)
    >>> es_jbm_e(chi2Value, n, minExp, test="likelihood")
    
    '''
    if test=='chi':
        E = chi2 * minExp / (n * (n - minExp))       
    else:
        E = -1/log(minExp/n) * chi2/(2*n)
    return E