import pandas as pd
import math
from .help_quartileIndexing import he_quartileIndexing

def he_quartileIndex(data, indexMethod, q1Frac="linear", q1Int="int", q3Frac="linear", q3Int="int"):
    '''
    Quartile Numeric Based on Index
    
    Helper function for **me_quartiles()** to return the quartile as a number of the first and third quartile with different methods of rounding.
    
    Parameters
    ----------
    data : pandas series with numeric values
    indexMethod : optional to indicate which type of indexing to use
    q1Frac : optional to indicate what type of rounding to use for first quarter
    q1Int : optional to indicate the use of the integer or the midpoint method for first quarter
    q3Frac : optional to indicate what type of rounding to use for third quarter
    q3Int : optional to indicate the use of the integer or the midpoint method for third quarter
    
    q1Frac and q3Frac can be set to: "linear", "down", "up", "bankers", "nearest", "halfdown", or "midpoint".
    
    q1Int and q3Int can be set to: "int" or "midpoint".
    
    Returns
    -------
    q1 : the first (lower) quartile as a number
    13 : the third (upper/higher) quartile as a number
    
    Notes
    -----
    If **the index is an integer** often that integer will be used to find the corresponding value in the sorted data. This can be used by setting *q1Int* and/or *q3Int* to **int**.   
    However, in some rare methods they argue to take the midpoint between the found index and the next one, i.e. to use:

    $$iQ_i = iQ_i + \\frac{1}{2}$$
    This can be done by setting *q1Int* and/or *q3Int* to **midpoint**.
    
    If the index has a fractional part, we could use linear interpolation. It can be written as:

    $$X\\left[\\lfloor iQ_i \\rfloor\\right] + \\frac{iQ_i - \\lfloor iQ_i \\rfloor}{\\lceil iQ_i \\rceil - \\lfloor iQ_i \\rfloor} \\times \\left(X\\left[\\lceil iQ_i \\rceil\\right] - X\\left[\\lfloor iQ_i \\rfloor\\right]\\right)$$

    Where:
    * \\(X\\left[x\\right]\\) is the x-th score of the sorted scores 
    * \\(\\lfloor\\dots\\rfloor\\) is the function to always round down
    * \\(\\lceil\\dots\\rceil\\) is the function to always round up

    Or we can use 'rounding'. But there are different versions of rounding. Besides the already mentioned round down (use *q1Frac* and/or *q3Frac* as **down**) and round up versions (use *q1Frac* and/or *q3Frac* as **up**):

    * \\(\\lfloor\\dots\\rceil\\) to indicate rounding to the nearest even integer. A value of 2.5 gets rounded to 2, while 1.5 also gets rounded to 2. This is also referred to as *bankers* method. Use *q1Frac* and/or *q3Frac* as **bankers**.
    * \\(\\left[\\dots\\right]\\) to indicate rounding to the nearest integer. A value that ends with .5 is then always rounded up. Use *q1Frac* and/or *q3Frac* as **nearest**.
    * \\(\\left< \\dots\\right>\\) to indicate to round a value ending with .5 always down. Use *q1Frac* and/or *q3Frac* as **halfdown**.

    or even use the midpoint again i.e.:

    $$\\frac{\\lfloor iQ_i \\rfloor + \\lceil iQ_i \\rceil}{2}$$
    
    Use *q1Frac* and/or *q3Frac* as **midpoint**.
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    
    '''
    n = len(data)
    iq1, iq3 = he_quartileIndexing(data, indexMethod)

    if round(iq1) == iq1:
        # index is integer
        if q1Int == "int":
            q1 = iq1
        elif q1Int == "midpoint":
            q1 = iq1 + 1/2
    else:
        # index has fraction
        if q1Frac == "linear":
            q1 = iq1
        elif q1Frac == "down":
            q1 = math.floor(iq1)
        elif q1Frac == "up":
            q1 = math.ceil(iq1)
        elif q1Frac == "bankers":
            q1 = round(iq1)
        elif q1Frac == "nearest":
            q1 = int(iq1 + 0.5)
        elif q1Frac == "halfdown":
            if iq1 + 0.5 == round(iq1 + 0.5):
                q1 = math.floor(iq1)
            else:
                q1 = round(iq1)
        elif q1Frac == "midpoint":
            q1 = (math.floor(iq1) + math.ceil(iq1)) / 2
    
    q1i = q1
    q1iLow = math.floor(q1i)
    q1iHigh = math.ceil(q1i)

    if q1iLow==q1iHigh:
        q1 = data[int(q1iLow-1)]
    else:
        #Linear interpolation:
        q1 = data[int(q1iLow-1)] + (q1i - q1iLow)/(q1iHigh - q1iLow)*(data[int(q1iHigh-1)] - data[int(q1iLow-1)])
        
    if round(iq3) == iq3:
        # index is integer
        if q3Int == "int":
            q3 = iq3
        elif q3Int == "midpoint":
            q3 = iq3 + 1/2
    else:
        # index has fraction
        if q3Frac == "linear":
            q3 = iq3
        elif q3Frac == "down":
            q3 = math.floor(iq3)
        elif q3Frac == "up":
            q3 = math.ceil(iq3)
        elif q3Frac == "bankers":
            q3 = round(iq3)
        elif q3Frac == "nearest":
            q3 = int(iq3 + 0.5)
        elif q3Frac == "halfdown":
            if iq3 + 0.5 == round(iq3 + 0.5):
                q3 = math.floor(iq3)
            else:
                q3 = round(iq3)
        elif q3Frac == "midpoint":
            q3 = (math.floor(iq3) + math.ceil(iq3)) / 2
                
    q3i = q3
    q3iLow = math.floor(q3i)
    q3iHigh = math.ceil(q3i)

    if q3iLow==q3iHigh:
        q3 = data[int(q3iLow-1)]
    else:
        #Linear interpolation:
        q3 = data[int(q3iLow-1)] + (q3i - q3iLow)/(q3iHigh - q3iLow)*(data[int(q3iHigh-1)] - data[int(q3iLow-1)])
        
    return q1, q3