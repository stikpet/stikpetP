import pandas as pd
import math
from numpy import log

def me_qv(data, measure="vr", var1=2, var2=1):
    '''
    Measures of Qualitative Variation
    ---------------------------------
    
    Various methods exist that can be used to measure qualitative variation. This function has a few of them.
    
    Parameters
    ----------
    data : list or pandas series
    measure : string, optional
        to indicate which method to use. Either "vr" (default), "modvr", "ranvr", "avdev", "mndif", "varnc", "stdev", "hrel", "b", "m1", "m2", "m3", "m4", "m5", "m6", "d1", "d2", "d3", "d4", "bpi", "hd", "he", "swe", "re", "sw1", "sw2", "sw3", "hi", "si", "j", "b", "be", "bd"
    var1 : float, optional
        additional value for some measures
    var2 : float, optional
        additional value for some measures
        
    Returns
    -------
    results : pandas dataframe with
    
    * *value*, the value of the requested measure
    * *measure*, description of the measure calculated
    * *source*, source used for calculation
        
    Notes
    -----
    
    The following measures can be determined:
    
    * *"modvr"*, Wilcox MODVR
    * *"ranvr"*, Wilcox RANVR
    * *"avdev"*, Wilcox AVDEV
    * *"mndif"*, Wilcox MNDIF
    * *"varnc"*, Wilcox VARNC (equal to Gibbs-Poston M2 and Smith-Wilson E1)
    * *"stdev"*, Wilcox STDEV
    * *"hrel"*, Wilcox HREL (equal to Pielou J)
    * *"m1"*, Gibbs-Poston M1
    * *"m2"*, Gibbs-Poston M2 (equal to Wilcox VARNC and Smith-Wilson E1)
    * *"m3"*, Gibbs-Poston M3
    * *"m4"*, Gibbs-Poston M4
    * *"m5"*, Gibbs-Poston M5
    * *"m6"*, Gibbs-Poston M6
    * *"b"*, Kaiser b
    * *"bd"*, Bulla D
    * *"be"*, Bulla E
    * *"bpi"*, Berger-Parker index
    * *"d1"*, *"d2"*, *"d3"*, *"d4"*, Simpson D and variations
    * *"hd"*, Hill Diversity, requires a value for *var1*
    * *"he"*, Hill Eveness, requires a value for *var1* and *var2*
    * *"hi"*, Heip Index
    * *"j"*, Pielou J (equal to Wilcox HREL)
    * *"si"*, Sheldon Index
    * *"sw1"*, Smith & Wilson E1 (equal to Wilcox VARNC and Gibbs-Poston M2)
    * *"sw2"*, Smith-Wilson E2
    * *"sw3"*, Smith-Wilson E3
    * *"swe"*, Shannon-Weaver Entropy
    * *"re"*, Rényi entropy, requires a value for *var1*
    * *"vr"*, Freeman's variation ratio
    
    **MODE BASED MEASURES**
    
    **Freeman Variation Ratio** ("vr")
    
    Formula used from Freeman (1965, p. 41):
    $$v = 1 - \\frac{F_{mode}}{n}$$
    
    **Berger–Parker index** ("bpi")
    
    A very simplistic measure that just informs how much percentage the modal category is.
    
    The formula used is (Berger & Parker, 1970, p. 1345):
    $$BPI = \\frac{F_{mode}}{n}$$
    
    **Wilcox MODVR** ("modvr")
    
    This looks at the difference of the frequency for each category with the modal frequency. This then gets divided by \\(n\\times \\left(k -1\\right)\\) to standardize the results to 0 to 1.
    
    It is a modification of the Freeman Variation Ratio, hence the name MODVR. Wilcox noted that the Freeman VR can never reach the maximum value of 1.
    
    The formula used is (Wilcox, 1973, p. 7):
    $$\\text{MODVR} = \\frac{\\sum_{i=1}^k F_{mode} - F_i}{n\\times \\left(k - 1\\right)} = \\frac{k\\times F_{mode}-n}{n\\times \\left(k - 1\\right)}$$
    
    **Wilcox RANVR** ("ranvr")
    
    Short for 'range variation ratio' this measure is very similar to Freeman's VR. Instead of looking simply at the mode, it looks at the range.
    
    The formula used is (Wilcox, 1973, p. 8):
    $$\\text{RANVR} = 1 - \\frac{F_{mode} - F_{min}}{F_{mode}}$$
    
    **MEAN BASED MEASURES**
    
    The following measures use the average count to determine the variation. i.e.
    $$\\bar{F} = \\frac{\\sum_{i=1}^k F_i}{k} = \\frac{n}{k}$$
    
    **Wilcox AVDEV** ("avdev")
    
    This simply follows the mean absolute deviation analogue but then using frequencies.
    Again this is then standardized.
    
    The formula used is (Wilcox, 1973, p. 9):
    $$\\text{AVDEV} = 1-\\frac{\\sum_{i=1}^k \\left|F_i-\\bar{F}\\right|}{2\\times \\frac{n}{k}\\times \\left(k-1\\right)}= 1-\\frac{k\\times \\sum_{i=1}^k \\left|F_i-\\bar{F}\\right|}{2\\times n \\times \\left(k-1\\right)}$$ 
    
    **Wilcox VARNC** ("varnc"), **Gibbs-Poston M2** ("m2"), and **Smith & Wilson E1** ("sw1")
    
    This is similar as the variance for scale variables.
    
    The formula used is (Wilcox, 1973, p. 11):
    $$\\text{VARNC} = 1-\\frac{\\sum_{i=1}^{k}\\left(f_i-\\bar{F}\\right)^2}{\\frac{n^2\\times\\left(k-1\\right)}{k}} = \\frac{k\\times\\left(n^2-\\sum_{i=1}^k f_i^2\\right)}{n^2\\times\\left(k-1\\right)}$$
    
    This is the same as Gibbs and Poston's **M2** ("m2"). Their formula looks different but has the same result (Gibbs & Poston, 1975, p. 472)
    $$\\text{M2} = \\frac{1-\\sum_{i=1}^k p_i^2}{1-\\frac{1}{k}} = \\frac{\\text{M1}}{1-\\frac{1}{k}} = \\frac{k}{k-1}\\times\\text{M1}$$
    
    It is also the same as Smith and Wilson's first evenness measure ("sw1").

    The formula used (Smith & Wilson, 1996, p. 71):
    $$E_1 = \\frac{1 - D_s}{1 - \\frac{1}{k}}$$
    
    With \\(D_s\\) being Simpson's D, but defined as:
    $$D_s = \\sum_{i=1}^k\\left(\\frac{F_i}{n}\\right)^2$$

    **Wilcox STDEV** ("stdev")
    
    As with the variance for scale variables, we can take the square root to obtain the standard deviation.
    
    The formula used can be from the VARNC or the MNDIF (Wilcox, 1973, p. 14):
    $$\\text{STDEV} = 1-\\sqrt{\\frac{\\sum_{i=1}^k \\left(F_i-\\frac{n}{k}\\right)^2}{\\left(n-\\frac{n}{k}\\right)^2+\\left(k-1\\right)\\left(\\frac{n}{k}\\right)^2}}= 1-\\sqrt{\\frac{\\sum_{i=1}^{k-1}\\sum_{j=i+1}^k \\left(F_i-F_j\\right)^2}{n^2\\times\\left(k-1\\right)}}$$
    
    **Gibbs-Poston M4** ("m4")
    
    The formula used (Gibbs & Poston, 1975, p. 473):
    $$\\text{M4} = 1-\\frac{\\sum_{i=1}^k \\left|F_i-\\bar{F}\\right|}{2\\times n}$$
    
    **Gibbs-Poston M5** ("m5")
    
    The problem with M4 is that it can never be 0, so to adjust for this M5 could be used but is computationally then more difficult.
    
    The formula used (Gibbs & Poston, 1975, p. 474):
    $$\\text{M5} = 1-\\frac{\\sum_{i=1}^k \\left|F_i-\\bar{F}\\right|}{2\\times\\left(n-k+1-\\bar{F}\\right)}$$
    
    **Gibbs-Poston M6** ("m6")
    
    The formula used (Gibbs & Poston, 1975, p. 474):
    $$\\text{M6} = k\\times\\left(1-\\frac{\\sum_{i=1}^k \\left|F_i-\\bar{F}\\right|}{2\\times n}\\right) = k\\times\\text{M4}$$


    **ENTROPY and EVENNESS**
    
    **Shannon-Weaver Entropy** ("swe")
    
    The formula used (Shannon & Weaver, 1949, p. 20):
    $$H_{sw}=-\\sum_{i=1}^k p_i\\times\\ln\\left(p_i\\right)$$
    
    **Wilcox HREL** ("hrel") and **Pielou J** ("j")
    
    This uses Shannon's entropy but divides it over the maximum possible uncertainty.
    
    The formula used (Wilcox, 1973, p. 16):
    $$\\text{HREL} = \\frac{-\\sum_{i=1}^k p_i \\times \\text{log}_2 p_i}{\\text{log}_2 k}$$
    
    This is the same as Pielou J. ("j")
    
    The formula used (Pielou, 1966, p. 141):
    $$J=\\frac{H_{sw}}{\\ln\\left(k\\right)}$$
    
    **Sheldon Index** ("si")
    
    The formula used (Sheldon, 1969, p. 467):
    $$E = \\frac{e^{H_{sw}}}{k}$$
    
    **Rényi entropy** ("re")
    
    This is a generalisation for Shannon entropy.
    
    The formula used is (Rényi, 1961, p. 549):
    $$H_q = \\frac{1}{1 - q}\\times\\ln\\left(\\sum_{i=1}^k p_i^q\\right)$$
    
    **Heip Index** ("hi")
    
    The formula used is (Heip, 1974, p. 555):
    $$E_h = \\frac{e^{H_{sw}} - 1}{k - 1}$$ 
    
    **Hill Diversity** ("hd")
    
    The formula used is (Hill, 1973, p. 428):
    $$N_a = \\begin{cases}\\frac{1}{\\left(\\sum_{i=1}^k p_i^a\\right)^{1-a}} & \\text{ if } a\\neq 1 \\\\ e^{H_{sw}} & \\text{ if }  =1 \\end{cases}$$
    
    **Hill Eveness** ("he")
    
    The formula used is (Hill, 1973, p. 429):
    $$E_{a,b} = \frac{N_a}{N_b}$$
    
    Where \\(N_a\\) and \\(N_b\\) are Hill's diversity values for a and b.
    
    **Bulla E** ("be")
    
    Bulla's evenness measure.
    
    The formula used is (Bulla, 1994, pp. 168-169):
    $$E_b = \\frac{O - \\frac{1}{k} - \\frac{k - 1}{n}}{1 - \\frac{1}{k} - \\frac{k - 1}{n}}$$
    
    With:
    $$O = \\sum_{i=1}^k \\min\\left(p_i, \\frac{1}{k}\\right)$$
    
    **Bulla D** ("bd")
    
    Bulla's Evenness measure converted to a diversity measure.
    
    The formula used is (Bulla, 1994, p. 169):
    $$D_b = E_b\\times k$$
    
    Where \\(E_b\\) is Bulla E value.
    
    With:
    $$O = \\sum_{i=1}^k \\min\\left(p_i, \\frac{1}{k}\\right)$$
    
    **Smith & Wilson E2** ("sw2")

    The formula used (Smith & Wilson, 1996, p. 71):
    $$E_2 = \\frac{\\ln\\left(D_s\\right)}{\\ln\\left(k\\right)}$$
    
    With \\(D_s\\) being Simpson's D, but defined as:
    $$D_s = \\sum_{i=1}^k\\left(\\frac{F_i}{n}\\right)^2$$

    **Smith & Wilson E3** ("sw3")

    The formula used (Smith & Wilson, 1996, p. 71):
    $$E_3 = \\frac{1}{D_s \\times k}$$
    
    With \\(D_s\\) being Simpson's D, but defined as:
    $$D_s = \\sum_{i=1}^k\\left(\\frac{F_i}{n}\\right)^2$$
    
    **OTHER***
    
    **Wilcox MNDIF** ("mndif")
    
    Analog of the mean difference measure for scale variables.
    
    The formula used is (Wilcox, 1973, p. 9):
    $$\\text{MNDIF} = 1-\\frac{\\sum_{i=1}^{k-1}\\sum_{j=i+1}^k \\left|F_i-F_j\\right|}{n\\times\\left(k-1\\right)}$$
    
    **Gibbs-Poston M1** ("m1")
    
    The formula used (Gibbs & Poston, 1975, p. 471):
    $$\\text{M1} = 1 - \\sum_{i=1}^k p_i^2$$
    
    **Gibbs-Poston M3** ("m3")
    
    he formula used (Gibbs & Poston, 1975, p. 472):
    $$\\text{M3} = \\frac{1-\\sum_{i=1}^k p_i^2-p_{min}}{1-\\frac{1}{k}-p_{min}}$$
    
    With \\(p_{min}\\) the lowest proportion
    
    **Simpson D** ("d1", "d2", "d3", "d4")
    
    The formula used is based on Simpson (1949, p. 688):
    $$\\text{D_1} = \\frac{\\sum_{i=1}^k f_i\\times\\left(f_i-1\\right)}{n\\times\\left(n-1\\right)}$$
    
    Another alternative is:
    $$D_2 = \\sum_{i=1}^k\\left(\\frac{F_i}{n}\\right)^2$$
    
    Often the result is subtracted from 1 to reverse the scale. 
    $$\\text{D_3} = 1-\\frac{\\sum_{i=1}^k f_i\\times\\left(f_i-1\\right)}{n\\times\\left(n-1\\right)}$$
    
    and
    $$D_4 = \\sum_{i=1}^k\\left(\\frac{F_i}{n}\\right)^2$$
    
    
    **Kaiser b**
    
    The formula used (Kaiser, 1968, p. 211):
    $$B = 1 - \\sqrt{1 - \\left(\\sqrt[k]{\\prod_{i=1}^k\\frac{f_i\\times k}{n}}\\right)^2}$$
    
    References
    ----------
    Berger, W. H., & Parker, F. L. (1970). Diversity of planktonic foraminifera in deep-sea sediments. *Science, 168*(3937), 1345–1347. https://doi.org/10.1126/science.168.3937.1345
    
    Bulla, L. (1994). An index of evenness and its associated diversity measure. *Oikos, 70*(1), 167–171. https://doi.org/10.2307/3545713
    
    Fisher, R. A., Corbet, A. S., & Williams, C. B. (1943). The relation between the number of species and the number of individuals in a random sample of an animal population. *The Journal of Animal Ecology, 12*(1), 42–58. https://doi.org/10.2307/1411
    
    Freeman, L. C. (1965). *Elementary applied statistics: For students in behavioral science*. Wiley.
    
    Gibbs, J. P., & Poston, D. L. (1975). The division of labor: Conceptualization and related measures. *Social Forces, 53*(3), 468. https://doi.org/10.2307/2576589
    
    Heip, C. (1974). A new index measuring evenness. *Journal of the Marine Biological Association of the United Kingdom, 54*(3), 555–557. https://doi.org/10.1017/S0025315400022736
    
    Hill, M. O. (1973). Diversity and evenness: A unifying notation and its consequences. *Ecology, 54*(2), 427–432. https://doi.org/10.2307/1934352
    
    Kaiser, H. F. (1968). A measure of the population quality of legislative apportionment. *American Political Science Review, 62*(1), 208–215. https://doi.org/10.2307/1953335
    
    Pielou, E. C. (1966). The measurement of diversity in different types of biological collections. *Journal of Theoretical Biology, 13*, 131–144. https://doi.org/10.1016/0022-5193(66)90013-0
    
    Rényi, A. (1961). On measures of entropy and information. *Contributions to the Theory of Statistics, 1*, 547–562.
    
    Shannon, C. E., & Weaver, W. (1949). *The mathematical theory of communication*. The university of Illinois press.
    
    Sheldon, A. L. (1969). Equitability indices: Dependence on the species count. *Ecology, 50*(3), 466–467. https://doi.org/10.2307/1933900
    
    Simpson, E. H. (1949). Measurement of diversity. *Nature, 163*(4148), Article 4148. https://doi.org/10.1038/163688a0
    
    Smith, B., & Wilson, J. B. (1996). A consumer’s guide to evenness indices. *Oikos, 76*(1), 70–82. https://doi.org/10.2307/3545749
    
    Wilcox, A. R. (1973). Indices of qualitative variation and political measurement. *Political Research Quarterly, 26*(2), 325–343. https://doi.org/10.1177/106591297302600209
    
    Author
    ------
    Made by P. Stikker
    
    Companion website: https://PeterStatistics.com  
    YouTube channel: https://www.youtube.com/stikpet  
    Donations: https://www.patreon.com/bePatron?u=19398076
    
    Examples
    --------
    Example 1: pandas series
    >>> df1 = pd.read_csv('https://peterstatistics.com/Packages/ExampleData/GSS2012a.csv', sep=',', low_memory=False, storage_options={'User-Agent': 'Mozilla/5.0'})
    >>> ex1 = df1['mar1']
    >>> me_qv(ex1)
          value                  measure           source
    0  0.499227  Freeman Variation Ratio  (Freeman, 1965)
    
    Example 2: a list
    >>> ex2 = ["MARRIED", "DIVORCED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "NEVER MARRIED", "MARRIED", "MARRIED", "MARRIED", "SEPARATED", "DIVORCED", "NEVER MARRIED", "NEVER MARRIED", "DIVORCED", "DIVORCED", "MARRIED"]
    >>> me_qv(ex2, "swe")
          value                 measure                           source
    0  1.296892  Shannon-Weaver Entropy  (Shannon & Weaver, 1949, p. 20)
    
    
    '''
    if type(data) is list:
        data = pd.Series(data)
        
    freqs = data.value_counts().values
    
    k = len(freqs)
    n = sum(freqs)
    fm = max(freqs)
    props = freqs/n
    
    if measure=="modvr":
        #Modified Variation Ratio
        src = "(Wilcox, 1973, p. 7)"
        lbl = "Wilcox MODVR"
        qv = sum(fm - freqs)/(n*(k - 1))
    elif measure=="ranvr":
        #Range Variation Ratio
        src = "(Wilcox, 1973, p. 8)"
        lbl = "Wilcox RANVR"
        fl = min(freqs)
        qv = 1 - (fm - fl)/fm
    elif measure=="avdev":
        #Average Deviation
        src = "(Wilcox, 1973, p. 9)"
        lbl = "Wilcox AVDEV"
        qv = 1-sum(abs(freqs-n/k)) / (2*n/k*(k-1))
    elif measure=="mndif":
        #MNDif
        src = "(Wilcox, 1973, p. 9)"
        lbl = "Wilcox MNDIF"
        mndif = 0
        for i in range(0, k-1):
            for j in range(i+1,k):
                mndif = mndif + abs(freqs[i]-freqs[j])
        qv = 1 - mndif/(n*(k-1))
    elif measure=="varnc":
        #VarNC
        src = "(Wilcox, 1973, p. 11)"
        lbl = "Wilcox VARNC"
        qv = 1 - sum((freqs-n/k)**2)/(n**2*(k-1)/k)
    elif measure=="stdev":
        src = "(Wilcox, 1973, p. 14)"
        lbl = "Wilcox STDEV"
        qv = 1 - (sum((freqs-n/k)**2)/((n-n/k)**2+(k-1)*(n/k)**2))**0.5
    elif measure=="hrel":
        #HRel
        src = "(Wilcox, 1973, p. 16)"
        lbl = "Wilcox HREL"
        hrel = 0
        for i in range(k):
            hrel = hrel + props[i]*math.log2(props[i])
        qv = -hrel/math.log2(k)    
        
    elif measure=="m1":
        src = "(Gibbs & Poston, 1975, p. 471)"
        lbl = "Gibbs-Poston M1"
        qv = 1 - sum(props**2)
    elif measure=="m2":
        #equal to varnc
        src = "(Gibbs & Poston, 1975, p. 472)"
        lbl = "Gibbs-Poston M2"
        qv = (1 - sum(props**2)) / (1-1/k)
    elif measure=="m3":
        src = "(Gibbs & Poston, 1975, p. 472)"
        lbl = "Gibbs-Poston M3"
        pl = min(props)
        qv = (1 - sum(props**2) - pl) / (1-1/k - pl)
    elif measure=="m4":
        src = "(Gibbs & Poston, 1975, p. 473)"
        lbl = "Gibbs-Poston M4"
        fmean = n/k
        qv = 1 - sum(abs(freqs-fmean))/(2*n)
    elif measure=="m5":
        src = "(Gibbs & Poston, 1975, p. 474)"
        lbl = "Gibbs-Poston M5"
        fmean = n/k
        qv = 1 - sum(abs(freqs-fmean))/(2*(n-k+1-fmean))
    elif measure=="m6":
        src = "(Gibbs & Poston, 1975, p. 474)"
        lbl = "Gibbs-Poston M6"
        fmean = n/k
        qv = k*(1 - sum(abs(freqs-fmean))/(2*n))
    elif measure=="b":
        #Kaiser B index
        src = "(Kaiser, 1968, p. 211)"
        lbl = "Kaiser b"
        qv = 1 - (1 - ((math.prod(freqs*k/n))**(1/k))**2)**0.5        
    elif measure=="bd":
        #Bulla D
        src = "(Bulla, 1994, p. 169)"
        lbl = "Bulla D"
        o = 0
        for p in props:
            o = o + min(p, 1/k)
        qv = k*(o - 1/k + (k - 1)/n)/(1 - 1/k + (k-1)/n)
    elif measure=="be":
        #Bulla e
        src = "(Bulla, 1994, pp. 168-169)"
        lbl = "Bulla E"
        o = 0
        for p in props:
            o = o + min(p, 1/k)
        qv = (o - 1/k + (k - 1)/n)/(1 - 1/k + (k-1)/n)
    elif measure=="bpi":
        #Berger-Parker Index
        src = "(Berger & Parker, 1970, p. 1345)"
        lbl = "Berger-Parker D"
        qv = fm/n
    elif measure=="d1":
        #Simpson's D
        src = "(Simpson, 1949, p. 688)"
        lbl = "Simpson D"
        qv = sum(freqs*(freqs-1))/(n*(n-1))
    elif measure=="d2":
        #Simpson's D
        src = "(Smith & Wilson, 1996, p. 71)"
        lbl = "Simpson D biased"
        qv = sum((freqs/n)**2)
    elif measure=="d3":
        #Simpson's D
        src = "(Wikipedia, n.d.)"
        lbl = "Simpson D as diversity"
        qv = 1 - sum(freqs*(freqs-1))/(n*(n-1))
    elif measure=="d4":
        #Simpson's D
        src = "(Berger & Parker, 1970, p. 1345)"
        lbl = "Simpson D as diversity biased"
        qv = 1 - sum((freqs/n)**2)
    elif measure=="hd":
        #Hill's Diversity
        src = "(Hill, 1973, p. 428)"
        lbl = "Hill Diversity"
        if var1 == 1:
            qv = math.exp(-1*sum(props*log(props)))
        else:
            qv = 1/(sum(props**var1)**(var1 - 1))
    elif measure=="he":
        #Hill's Evenness
        src = "(Hill, 1973, p. 429)"
        lbl = "Hill Evenness"
        qv = me_qv(data, measure="hd", var1=var1)['value']/me_qv(data, measure="hd", var1=var2)['value'] 
    elif measure=="hi":
        #Heip Index
        src = "(Heip, 1974, p. 555)"
        lbl = "Heip Evenness"
        h = -1*sum(props*log(props))
        qv = (math.exp(h) - 1)/(k - 1)
    elif measure=="j":
        #Pielou J
        src = "(Pielou, 1966, p. 141)"
        lbl = "Pielou J"
        h = -1*sum(props*log(props))
        qv = h/log(k)
    elif measure=="si":
        #Sheldon Index
        src = "(Sheldon, 1969, p. 467)"
        lbl = "Sheldon Evenness"
        h = -1*sum(props*log(props))
        qv = math.exp(h)/k
    elif measure=="sw1":
        #Smith and Wilson Index 1
        src = "(Smith & Wilson, 1996, p. 71)"
        lbl = "Smith-Wilson Evenness Index 1"
        d = sum(props**2)
        qv = (1 - d)/(1 - 1/k)
    elif measure=="sw2":
        #Smith and Wilson Index 2
        src = "(Smith & Wilson, 1996, p. 71)"
        lbl = "Smith-Wilson Evenness Index 2"
        d = sum(props**2)
        qv = -log(d)/log(k)
    elif measure=="sw3":
        #Smith and Wilson Index 3
        src = "(Smith & Wilson, 1996, p. 71)"
        lbl = "Smith-Wilson Evenness Index 3"
        d = sum(props**2)
        qv = 1/(d*k)    
    
    elif measure=="swe":
        #Shannon-Weaver Entropy
        src = "(Shannon & Weaver, 1949, p. 20)"
        lbl = "Shannon-Weaver Entropy"
        qv = -1*sum(props*log(props))
    elif measure=="re":
        #Rényi Entropy
        src = "(Rényi, 1961, p. 549)"
        lbl = "Reneyi Entropy"
        qv = 1/(1 - var1)*math.log2(sum(props**var1))
    elif measure=="vr":
        #Variation Ratio
        src = "(Freeman, 1965)"
        lbl = "Freeman Variation Ratio"
        pm = fm/n
        qv = 1 - pm
    
    results = pd.DataFrame([[qv, lbl, src]], columns=["value", "measure", "source"])
    pd.set_option('display.max_colwidth', None)
    return (results)