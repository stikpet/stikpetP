import pandas as pd
import math
from ..helper.help_quartileIndex import he_quartileIndex

def me_quartiles(data, levels=None, method="own", indexMethod="sas1", q1Frac="linear", q1Int="int", q3Frac="linear", q3Int="int"):
    '''
    Quartiles / Hinges
    
    The quartiles are at quarters of the data (McAlister, 1879, p. 374; Galton, 1881, p. 245). The median is at 50%, and the quartiles at 25% and 75%. Note that there are five quartiles, the minimum value is the 0-quartile, at 25% the first (or lower) quartile, at 50% the median a.k.a. the second quartile, at 75% the third (or upper) quartile, and the maximum as the fourth quartile.
    
    Tukey (1977) also introduced the term Hinges and sorted the values in a W shape, where the bottom parts of the W are then the hinges.
    
    There are quite a few different methods to determine the quartiles. This function has 19 different ones. See the notes for a description.
    
    Parameters
    ----------
    data : pandas series with
    levels : optional dictionary with coding to use
    method : optional which method to use to calculate quartiles.
    indexMethod : optional to indicate which type of indexing to use
    q1Frac : optional to indicate what type of rounding to use for first quarter
    q1Int : optional to indicate the use of the integer or the midpoint method for first quarter
    q3Frac : optional to indicate what type of rounding to use for third quarter
    q3Int : optional to indicate the use of the integer or the midpoint method for third quarter
    
    method can be set to "own" and then provide the next parameters, or any of the methods listed in the notes.
    
    indexMethod can be set to "inclusive", "exclusive", "sas1", "sas4", "excel", "hl", "hf8", or "hf9".
    
    q1Frac and q3Frac can be set to: "linear", "down", "up", "bankers", "nearest", "halfdown", or "midpoint".
    
    q1Int and q3Int can be set to: "int" or "midpoint".
    
    Returns
    -------
    results : pandas dataframe with:
    * Q1, the numeric value of the first quarter
    * Q3, the numeric value of the third quarter
    * Q1 text, text version of first quarter (only if levels are used)
    * Q3 text, text version of third quarter (only if levels are used)
    
    Notes
    -----
    To determine the quartiles a specific indexing method can be used. See **he_quartileIndexing()** for details on the different methods to choose from.
    
    Then based on the indexes either linear interpolation or different rounding methods (bankers, nearest, down, up, half-down) can be used, or the midpoint between the two values. If the index is an integer either the integer or the mid point is used. 
    
    See the **he_quartilesIndex()** for details on this.
    
    Note that the rounding method can even vary per quartile, i.e. the one used for the first quartile being different than the one for the second.

    I've come across the following methods:

    |method|indexing|q1 integer|q1 fractional|q3 integer|q3 fractional|
    |------|--------|----------|-------------|----------|-------------|
    |sas1|sas1|use int|linear|use int|linear|
    |sas2|sas1|use int|bankers|use int|bankers|
    |sas3|sas1|use int|up|use int|up|
    |sas5|sas1|midpoint|up|midpoint|up|
    |hf3b|sas1|use int|nearest|use int|halfdown|
    |sas4|sas4|use int|linear|use int|linear|
    |ms|sas4|use int|nearest|use int|halfdown|
    |lohninger|sas4|use int|nearest|use int|nearest|
    |hl2|hl|use int|linear|use int|linear|
    |hl1|hl|use int|midpoint|use int|midpoint|
    |excel|excel|use int|linear|use int|linear|
    |pd2|excel|use int|down|use int|down|
    |pd3|excel|use int|up|use int|up|
    |pd4|excel|use int|halfdown|use int|nearest|
    |pd5|excel|use int|midpoint|use int|midpoint|
    |hf8|hf8|use int|linear|use int|linear|
    |hf9|hf9|use int|linear|use int|linear|

    The following values can be used for the *method* parameter:

    1. inclusive = tukey =hinges = vining. (Tukey, 1977, p. 32; Siegel & Morgan, 1996, p. 77; Vining, 1998, p. 44).
    1. exclusive = jf. (Moore & McCabe, 1989, p. 33; Joarder & Firozzaman, 2001, p. 88).
    1. sas1 = parzen = hf4 = interpolated_inverted_cdf = maple3 = r4. (Parzen, 1979, p. 108; SAS, 1990, p. 626; Hyndman & Fan, 1996, p. 363)
    1. sas2 = hf3 = r3. (SAS, 1990, p. 626; Hyndman & Fan, 1996, p. 362)
    1. sas3 = hf1 = inverted_cdf = maple1 = r1 (SAS, 1990, p. 626; Hyndman & Fan, 1996, p. 362)
    1. sas4 = hf6 = minitab = snedecor = weibull = maple5 = r6 (Hyndman & Fan, 1996, p. 363; Weibull, 1939, p. ?; Snedecor, 1940, p. 43; SAS, 1990, p. 626)
    1. sas5 = hf2 = CDF = averaged_inverted_cdf = r2 (SAS, 1990, p. 626; Hyndman & Fan, 1996, p. 362)
    1. hf3b = closest_observation 
    1. ms (Mendenhall & Sincich, 1992, p. 35)
    1. lohninger (Lohninger, n.d.)
    1. hl1 (Hogg & Ledolter, 1992, p. 21)
    1. hl2 = hf5 = Hazen = maple4 = r5 (Hogg & Ledolter, 1992, p. 21; Hazen, 1914, p. ?)
    1. maple2
    1. excel = hf7 = pd1 = linear = gumbel = maple6 = r7 (Hyndman & Fan, 1996, p. 363; Freund & Perles, 1987, p. 201; Gumbel, 1939, p. ?)
    1. pd2 = lower
    1. pd3 = higher
    1. pd4 = nearest
    1. pd5 = midpoint
    1. hf8 = median_unbiased = maple7 = r8 (Hyndman & Fan, 1996, p. 363)
    1. hf9 = normal_unbiased = maple8 = r9 (Hyndman & Fan, 1996, p. 363)

    *hf* is short for Hyndman and Fan who wrote an article showcasing many different methods, *hl* is short for Hog and Ledolter, *ms* is short for Mendenhall and Sincich, *jf* is short for Joarder and Firozzaman. *sas* refers to the software package SAS, *maple* to Maple, *pd* to Python's pandas library, and *r* to R.
    
    The names *linear*, *lower*, *higher*, *nearest* and *midpoint* are all used by pandas quantile function and numpy percentile function. Numpy also uses *inverted_cdf*, *averaged_inverted_cdf*, *closest_observation*, *interpolated_inverted_cdf*, *hazen*, *weibull*, *median_unbiased*, and *normal_unbiased*. 
    
    References
    ----------
    Freund, J. E., & Perles, B. M. (1987). A new look at quartiles of ungrouped data. *The American Statistician, 41*(3), 200–203. https://doi.org/10.1080/00031305.1987.10475479

    Galton, F. (1881). Report of the anthropometric committee. *Report of the British Association for the Advancement of Science, 51*, 225–272.

    Gumbel, E. J. (1939). La Probabilité des Hypothèses. *Compes Rendus de l’ Académie des Sciences, 209*, 645–647.

    Hazen, A. (1914). Storage to be provided in impounding municipal water supply. *Transactions of the American Society of Civil Engineers, 77*(1), 1539–1640. https://doi.org/10.1061/taceat.0002563

    Hogg, R. V., & Ledolter, J. (1992). *Applied statistics for engineers and physical scientists* (2nd int.). Macmillan.

    Hyndman, R. J., & Fan, Y. (1996). Sample quantiles in statistical packages. *The American Statistician, 50*(4), 361–365. https://doi.org/10.2307/2684934

    Joarder, A. H., & Firozzaman, M. (2001). Quartiles for discrete data. *Teaching Statistics, 23*(3), 86–89. https://doi.org/10.1111/1467-9639.00063

    Langford, E. (2006). Quartiles in elementary statistics. *Journal of Statistics Education, 14*(3), 1–17. https://doi.org/10.1080/10691898.2006.11910589

    Lohninger, H. (n.d.). Quartile. Fundamentals of Statistics. Retrieved April 7, 2023, from http://www.statistics4u.com/fundstat_eng/cc_quartile.html

    McAlister, D. (1879). The law of the geometric mean. *Proceedings of the Royal Society of London, 29*(196–199), 367–376. https://doi.org/10.1098/rspl.1879.0061

    Mendenhall, W., & Sincich, T. (1992). *Statistics for engineering and the sciences* (3rd ed.). Dellen Publishing Company.

    Moore, D. S., & McCabe, G. P. (1989). *Introduction to the practice of statistics*. W.H. Freeman.

    Parzen, E. (1979). Nonparametric statistical data modeling. *Journal of the American Statistical Association, 74*(365), 105–121. https://doi.org/10.1080/01621459.1979.10481621

    SAS. (1990). SAS procedures guide: Version 6 (3rd ed.). SAS Institute.

    Siegel, A. F., & Morgan, C. J. (1996). *Statistics and data analysis: An introduction* (2nd ed.). J. Wiley.

    Snedecor, G. W. (1940). *Statistical methods applied to experiments in agriculture and biology* (3rd ed.). The Iowa State College Press.

    Tukey, J. W. (1977). *Exploratory data analysis*. Addison-Wesley Pub. Co.

    Vining, G. G. (1998). *Statistical methods for engineers*. Duxbury Press.

    Weibull, W. (1939).* The phenomenon of rupture in solids*. Ingeniörs Vetenskaps Akademien, 153, 1–55.
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    '''
    
    data = data.dropna()
    if levels is not None:
        dataN = data.replace(levels)
        dataN = pd.to_numeric(dataN)
    else:
        dataN = pd.to_numeric(data)
    
    dataN = dataN.sort_values()
    dataN = list(dataN)
    
    #alternative namings
    if method in ["inclusive", "tukey", "vining", "hinges"]:
        method="inclusive"
    elif method in ["exclusive", "jf"]:
        method ="exclusive"
    elif method in ["cdf", "sas5", "hf2", "averaged_inverted_cdf", "r2"]:
        method = "sas5"
    elif method in ["sas4", "minitab", "hf6", "weibull", "maple5", "r6"]:
        method = "sas4"
    elif method in ["excel", "hf7", "pd1", "linear", "gumbel", "maple6", "r7"]:
        method = "excel"
    elif method in ["sas1", "parzen", "hf4", "interpolated_inverted_cdf", "maple3", "r4"]:
        method = "sas1"
    elif method in ["sas2", "hf3", "r3"]:
        method = "sas2"
    elif method in ["sas3", "hf1", "inverted_cdf", "maple1", "r1"]:
        method = "sas3"
    elif method in ["hf3b", "closest_observation"]:
        method = "hf3b"
    elif method in ["hl2", "hazen", "hf5", "maple4"]:
        method = "hl2"
    elif method in ["np", "midpoint", "pd5"]:
        method = "pd5"
    elif method in ["hf8", "median_unbiased", "maple7", "r8"]:
        method = "hf8"
    elif method in ["hf9", "normal_unbiased", "maple8", "r9"]:
        method = "hf9"
    elif method in ["pd2", "lower"]:
        method = "pd2"
    elif method in ["pd3", "higher"]:
        method = "pd3"
    elif method in ["pd4", "nearest"]:
        method = "pd4"
    
    #settings
    settings = [indexMethod, q1Frac, q1Int, q3Frac, q3Int]
    if method=="inclusive":
        settings = ["inclusive", "linear","int","linear","int"]
    elif method=="exclusive":
        settings = ["exclusive", "linear","int","linear","int"]
    elif method=="sas1":
        settings = ["sas1","linear","int","linear","int"]
    elif method=="sas2":
        settings = ["sas1","bankers","int","bankers" ,"int"]
    elif method=="sas3":
        settings = ["sas1","up","int","up","int"]
    elif method=="sas5":
        settings = ["sas1","up","midpoint","up","midpoint"]
    elif method=="sas4":    
        settings = ["sas4","linear", "int","linear","int"]
    elif method=="ms": 
        settings = ["sas4", "nearest","int", "halfdown","int"]
    elif method=="lohninger":
        settings = ["sas4", "nearest", "int","nearest","int"]
    elif method=="hl2":
        settings = ["hl", "linear", "int","linear","int"]
    elif method=="hl1":
        settings = ["hl", "midpoint","int", "midpoint","int"]
    elif method=="excel":
        settings = ["excel", "linear","int","linear", "int"]
    elif method=="pd2":
        settings = ["excel", "down", "int", "down","int"]
    elif method=="pd3":
        settings = ["excel", "up","int","up","int"]
    elif method=="pd4":
        settings = ["excel", "halfdown",  "int","nearest", "int"]
    elif method=="hf3b":
        settings = ["sas1", "nearest","int","halfdown","int"]
    elif method=="pd5":
        settings = ["excel", "midpoint","int","midpoint","int"]
    elif method=="hf8":
        settings = ["hf8", "linear","int","linear", "int"]
    elif method=="hf9":
        settings = ["hf9", "linear","int","linear", "int"]
    elif method=="maple2":
        settings = ["hl", "down","int","down", "int"]
    
    q1, q3 = he_quartileIndex(dataN, settings[0], settings[1], settings[2], settings[3], settings[4])
    
    #find the text representatives
    
    if levels is not None:
        if q1 == round(q1):
            q1T = list(levels.keys())[list(levels.values()).index(q1)]

        else:
            q1T = "between " + list(levels.keys())[list(levels.values()).index(dataN.iloc[math.floor(q1)])] + " and " + list(levels.keys())[list(levels.values()).index(dataN.iloc[math.ceil(q1)])]

        if q3 == round(q3):
            q3T = list(levels.keys())[list(levels.values()).index(q3)]

        else:
            q3T = "between " + list(levels.keys())[list(levels.values()).index(dataN.iloc[math.floor(q3)])] + " and " + list(levels.keys())[list(levels.values()).index(dataN.iloc[math.ceil(q3)])]
        
        
        results = pd.DataFrame([[q1, q3, q1T, q3T]], columns=["Q1", "Q3", "Q1 text", "Q3 text"])
    else:
        results = pd.DataFrame([[q1, q3]], columns=["Q1", "Q3"])
        
    pd.set_option('display.max_colwidth', None)
    
    return results

