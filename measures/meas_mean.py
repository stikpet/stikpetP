import math
from numpy import log

def me_mean(data, version="arithmetic", trimProp=0.1, trimFrac="down"):
    '''
    Mean
    
    Different types of means can be determined using this function. 
    The mean is a measure of central tendency, to indicate the center.
    
    Parameters
    ----------
    data : pandas data series with numeric data
    version : string with mean to calculate. Either "arithmetic" (default), "winsorized", "trimmed", "windsor", "truncated", "winsorized", "olympic", "geometric", "harmonic", "midrange"
    trimProp : optional parameter to indicate the total proportion to trim. Default at 0.1 i.e. 0.05 from each side.
    trimFrac : optional parameter to indicate what to do if trimmed amount is non-integer. Either "down" (default), "prop" or "linear"
    
    Returns
    -------
    res : value of the mean
    
    Notes
    -----
    
    **Arithmetic Mean**
    
    One of the three Pythagorean means, and the mean most people would assume if you ask them to calculate the mean.
    It is the fulcrum of the distribution (Weinberg & Schumaker, 1962, p.19). One reference can for example be found 
    in Aristotle (384-322 BC) (1850, p. 43). 
    
    The formula:
    $$\\bar{x} = \\frac{\\sum_{i=1}^n x_i}{n}$$
    
    **Harmonic Mean**
    
    The second of the three Pythagorean means:
    $$H = \\frac{n}{\\sum_{i=1}^n \\frac{1}{x_i}}
    
    **Geometric Mean**
    
    The third of the three Pythagorean means:
    $$G = e^{\\frac{1}{n}\\times\\sum_{i=1}^n \\ln\\left(x_i\\right)}
    
    **Olympic Mean**
    
    Simply ignore the maximum and minimum (only once):
    $$OM = \\frac{\\sum_{i=2}^{n-1} x_i}{n - 2}$$
    
    **Mid Range**
    
    The average of the maximum and minimum:
    $$MR = \\frac{\\min x + \\max x}{2}
    
    **Trimmed**
    
    With a trimmed (Windsor/Truncated) mean we trim a fixed amount of scores from each side (Tukey, 1962, p. 17).
    Let \\(p_t\\) be the proportion to trim, we then need to trim \\(n_t = \\frac{p_t\\times n}{2}\\) 
    from each side.
    
    If this \\(n_t\\) is an integer there isn't a problem, but if it isn't we have options. The 
    first option is to simply round down, i.e. \\(n_l = \\lfloor n_t\\rfloor\\). The trimmed mean is then:
    
    $$\\bar{x}_t = \\frac{\\sum_{i=n_t+1}^{n - n_l + 1} x_i}{n - 2\\times n_l}$$
    This is used if *trimFrac = "down"* is set.
    
    We could also use linear interpolation based on the number of scores to trim. We missed out on:
    \\(f = n_t - n_l\\) on each side. So the first and last value we do include should 
    only count for \\(1 - f\\) each. The trimmed mean will then be:
    $$\\bar{x}_t = \\frac{\\left(x_{n_t + 1} + x_{n - n_l + 1}\\right)\\times\\left(1 - f\\right) + \\sum_{i=n_l+2}^{n - n_l} x_i}{n - 2\\times n_t}$$
    This is used if *trimFrac = "prop"* is set.

    Alternative, we could take the proportion itself and use linear interpolation on that. The found \\(n_l\\) 
    will be \\(p_1 = \\frac{n_l \\times 2}{n}\\) of the the total sample size. While if we had rounded up, we had 
    used \\(p_2 = \\frac{\\left(n_l + 1\\right)\\times 2}{n}\\) of the the total sample size. Using linear interpolation we 
    then get:
    $$\\bar{x}_t = \\frac{p_t - p_1}{p_2 - p_1}\\times\\left(\\bar{x}_{th}-\\bar{x}_{tl}\\right) + \\bar{x}_{tl}$$
    Where \\(\\bar{x}_{tl}\\) is the trimmed mean if \\(p_1\\) would be used as a trim proportion, and \\(\\bar{x}_{th}\\) is the 
    trimmed mean if \\(p_2\\) would be used.
    This is used if *trimFrac = "linear"* is set.
    
    **Winsorized Mean**
    
    Similar as with a trimmed mean, but now the data is not removed, but replaced by the value equal to the nearest 
    value that is still included (Winsor as cited in Dixon, 1960, p. 385).
    $$W = n_l \\times \\left(x_{n_l + 1} + x_{n - n_l}\\right)\\times\\frac{\\sum_{n_l + 1}^{n - n_l} x_i}{n - 2\\times n_l}$$
    
    References
    ----------
    Aristotle. (1850). *The nicomachean ethics of Aristotle* (R. W. Browne, Trans.). Henry G. Bohn.
    
    Dixon, W. J. (1960). Simplified estimation from censored normal samples. *The Annals of Mathematical Statistics, 31*(2), 385–391. https://doi.org/10.1214/aoms/1177705900
    
    Tukey, J. W. (1962). The future of data analysis. *The Annals of Mathematical Statistics, 33*(1), 1–67. https://doi.org/10.1214/aoms/1177704711
    
    Weinberg, G. H., & Schumaker, J. A. (1962). *Statistics An intuitive approach*. Wadsworth Publishing.
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    '''
    
    if version=="artithmetic":
        res = data.mean()
    elif version in ["winsorized", "trimmed", "windsor", "truncated"]:
        data = pd.to_numeric(data)
        data = data.sort_values()
        data = data.reset_index(drop=True)
        n = len(data)
        nt1 = n*trimProp/2
        nl = math.floor(nt1)
        
        if version=="winsorized":
            data[0:nl] = data[nl]
            data[n-nl:n] = data[n-nl-1]
            res = data.mean()
        
        else:
            if trimFrac=="down":
                res = data[nl:(n-nl)].mean()
            elif trimFrac=="prop":
                fr = nt1 - nl
                print(data[n-nl])
                res = (data[nl]*(1 - fr) + data[n-nl-1]*(1 - fr) + sum(data[nl+1:(n-nl-1)]))/(n - nt1*2)
            elif trimFrac=="linear":
                p1 = nl*2/n
                p2 = (nl + 1)*2/n
                m1 = data[nl:(n-nl)].mean()
                m2 = data[(nl+1):(n-nl-1)].mean()
                res = (trimProp - p1)/(p2 - p1)*(m2 - m1)+m1
    
    elif version=="olympic":
        res = (data.sum() - max(data) - min(data))/(len(data)-2)
        
    elif version=="geometric":
        res = math.exp(sum(log(data)))
        
    elif version=="harmonic":
        n = len(data)
        res = n/sum(1/data)
        
    elif version=="midrange":
        res = (max(data) + min(data))/2
    
    return res