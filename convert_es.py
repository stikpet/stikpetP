import math

def es_convert(es, fr, to, ex1=None, ex2=None):
    '''
    Convert Effect Sizes
    
    Function to convert various effect sizes to other effect sizes.
    
    Parameters
    -----------
    es : the effect size value to convert
    fr : name of the original effect size (see details)
    to : name of the effect size to convert to (see details)
    ex1 : extra for some conversions (see details)
    ex2 : extra for some conversions (see details)
    
    Returns
    -------
    res : the converted effect size value
    
    Notes
    -----
    **COHEN D**
    
    **Cohen d to Odds Ratio**
    
    fr="cohend", to="or", ex1="chinn"
    
    This uses (Chinn, 2000, p. 3129):
    $$OR = e^{d\\times 1.81}$$
    
    fr="cohend", to="or", ex1="borenstein"
    
    This uses (Borenstein et. al, 2009, p. 3):
    $$OR = e^{\\frac{d\\times\\pi}{\\sqrt{3}}}$$
    
    **COHEN D'**
    
    *Convert a Cohen d' to Cohen d*
    
    fr="cohendos" to="cohend"
    
    This uses (Cohen , 1988, p. 46):
    $$d = d'\\times\\sqrt{2}$$
    
    **COHEN F**
    
    *Cohen f to Eta-squared*
    
    fr="cohenf" to="etasq"
    
    This uses (Cohen, 1988, p. 284):
    $$\\eta^2 = \\frac{f^2}{1 + f^2}$$
    
    **COHEN H'**
    
    *Cohen h' to Cohen h*
    
    fr= "cohenhos", to = "cohenh"
    
    This uses (Cohen, 1988, p. 203):
    $$h = h'\times\sqrt{2}$$
    
    **COHEN w**
    
    *Cohen w to Contingency Coefficient*
    
    fr="cohenw", to="cc"
    
    **CRAMER V GoF**
    
    *Cramer's v for Goodness-of-Fit to Cohen w*
    
    fr="cramervgof", to = "cohenw", ex1 = df
    
    This uses (Cohen, 1988, p. 223):
    $$w = v\\times\\sqrt{df - 1}$$
    
    **EPSILON SQUARED**
    
    *Epsilon Squared to Eta Squared*
    
    fr="epsilonsq", to="etasq", ex1 = n, ex2 = k
    
    This uses:
    $$\\eta^2 = 1 - \\frac{\\left(1 - \\epsilon^2\\right)\\times\\left(n - k\\right)}{n - 1}$$
    
    *Epsilon Squared to Omega Squared*
    
    fr="epsilonsq", to="omegasq", ex1=MS_w, ex2 = SS_t
    
    This uses:
    $$\\hat{\\omega}^2 = \\epsilon^2\\times\\left(1 - \\frac{MS_w}{SS_t + MS_w}\\right)$$
    
    **ETA SQUARED**
    
    *Eta squared to Cohen f*
    
    fr="etasq", to="cohenf"
    
    This uses:
    
    $$f = \\sqrt{\\frac{\\eta^2}{1 - \\eta^2}}$$
    
    *Eta squared to Epsilon Squared*
    
    fr="etasq", to="epsilonsq", ex1=n, ex2=k
    
    This uses:
    $$\\epsilon^2 = \\frac{n\\times\\eta^2 - k + \\left(1 - \\eta^2\\right)}{n - l}$$
    
    **JOHNSTON-BERRY-MIELKE**
    
    *Johnston-Berry-Mielke E to Cohen w*
    
    fr="jbme", to="cohenw", ex1=minExp/n
    
    This uses (Johnston et al., 2006, p. 413):
    $$w = \\sqrt{\\frac{E\\times\\left(1 - \\right)}{q}}$$
    
    **ODDS RATIO**
    
    *Odds Ratio to Cohen d*
    
    fr="or", to="cohend", ex1="chinn"
    
    This uses (Chinn, 2000, p. 3129):
    $$d = \\frac{\\ln{\\left(OR\\right)}}{1.81}$$
    
    fr="or", to="cohend", ex1="borenstein"
    
    This uses (Borenstein et. al, 2009, p. 3):
    $$d = \\ln\\left(OR\\right)\\times\\frac{\\sqrt{3}}{\\pi}$$
    
    *Odds Ratio to Yule Q*
    
    fr="or", to="yuleq"
    
    This uses:
    $$Q = \\frac{OR - 1}{OR + 1}$$
    
    *Odds Ratio to Yule Y*
    
    This uses
    $$Y = \\frac{\\sqrt{OR} - 1}{\\sqrt{OR} + 1}$$
    
    **OMEGA SQUARED**
    
    *Omega Squared to Epsilon Squared*
    
    fr="omegasq", to="epsilonsq", ex1=MS_w, ex2 = SS_t
    
    This uses:
    $$\\epsilon^2 = \\frac{\\hat{\\omega}^2}{1 - \\frac{MS_w}{SS_t + MS_w}}$$
    
    **YULE Q**
    
    *Yule Q to Odds Ratio*
    
    fr="yuleq", to="or"
    
    This uses:
    
    $$OR = \\frac{1 + Q}{1 - Q}$$
    
    *Yule Q to Yule Y*
    
    fr="yuleq", to="yuley"
    
    This uses:
    $$Y = \\frac{1 - sqrt{1 - Q^2}}{Q}$$
    
    **YULE Y**
    
    *Yule Y to Yule Q*
    
    fr="yuley", to=="yuleq"
    
    This uses:
    $$Q = \\frac{2\\times Y}{1 + Y^2}$$
    
    *Yule Y to Odds Ratio*
    
    fr="yuley", to=="or"
    
    This uses
    $$OR = \\left(\\frac{1 + Y}{1 - Y}\\right)^2$$
    
    References
    ----------
    Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2009). Converting Among Effect Sizes. In *Introduction to Meta-Analysis*. John Wiley & Sons, Ltd. https://doi.org/10.1002/9780470743386
    
    Chinn, S. (2000). A simple method for converting an odds ratio to effect size for use in meta-analysis. *Statistics in Medicine, 19*(22), 3127–3131. https://doi.org/10.1002/1097-0258(20001130)19:22<3127::aid-sim784>3.0.co;2-m
    
    Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). L. Erlbaum Associates.
    
    Johnston, J. E., Berry, K. J., & Mielke, P. W. (2006). Measures of effect size for chi-squared and likelihood-ratio goodness-of-fit tests. *Perceptual and Motor Skills, 103*(2), 412–414. https://doi.org/10.2466/pms.103.2.412-414
    
    
    Author
    ------
    Made by P. Stikker
    
    Please visit: https://PeterStatistics.com
    
    YouTube channel: https://www.youtube.com/stikpet
    '''
    
    #"or", "cohend" , "yuleq", "yuley", "vda", "rb"
    #fr="cohenh2", to = "cohenh"
    #fr="cramervgof", to = "cohenw", ex1 = df


    #COHEN d
    #Cohen d one-sample to Cohen d
    if(fr=="cohendos" and to=="cohend"):
        res = es*sqrt(2)
      #Cohen d to Odds Ratio
    elif(fr=="cohend" and to=="or"):
        #Chinn (2000, p. 3129)
        if(ex1=="chinn"):
            res = math.exp(1.81*es)
        else:
            #Borenstein et. al (2009, p. 3)
            res = exp(es*pi/sqrt(3))
            
    #COHEN F
    #Cohen f to eta squared
    elif(fr=="cohenf" and to=="etasq"):
        res = es**2/(1 + es**2)
        
    #COHEN h'
    #Cohen h' to Cohen h
    elif(fr=="cohenhos" and to=="cohenh"):
        res = es*(2)**0.5
        
    #COHEN w
    #Cohen w to Contingency Coefficient
    elif(fr=="cohenw" and to=="cc"):
        res = sqrt(es**2 / (1 + es**2))
        
    #CONTINGENCY COEFFICIENT
    #Contingency Coefficient to Cohen w
    elif(fr=="cc" and to=="cohenw"):
        res = sqrt(es**2 / (1 - es**2))
        
    #CRAMÉR V
    #Cramer's v GoF to Cohen w
    elif(fr=="cramervgof" and to=="cohenw"):
        res = es*(ex1 - 1)**0.5
        
    #EPSILON SQUARED
    #Epsilon squared to Eta squared
    elif(fr=="epsilonsq" and to=="etasq"):
        res = 1 - (1 - es)*(ex1 - ex2)/(ex1 - 1)
        
    #Epsilon squared to Omega squared
    elif(fr=="epsilonsq" and to=="omegasq"):
        res = es*(1 - ex1/(ex2 + ex1))
        
        
    #ETA SQUARED
    #Eta squared to Cohen f
    elif(fr=="etasq" and to=="cohenf"):
        res = (es/(1-es))**0.5
        
    #Eta squared to Epsilon Squared
    elif(fr=="etasq" and to=="epsilonsq"):
        res = (ex1*es - ex2 + (1 - es))/(ex1 - ex2)
        
        
    #JOHNSTON-BERRY-MIELKE E
    #Johnston-Berry-Mielke E to Cohen w
    elif(fr=="jbme" and to=="cohenw"):
        res = (es*(1 - ex1)/(ex1))**0.5
 
    
    
    #ODDS RATIO
    #Odds Ratio to Cohen d (Chinn, 2000, p. 3129)
    elif(fr=="or" and to=="cohend"):
        if(ex1=="chinn"):
            res = math.log(es)/1.81
        else:
            #Borenstein et. al (2009, p. 3)
            res = math.log(es)*(3)**0.5/math.pi

    #Odds Ratio to Yule Q
    elif(fr=="or" and to=="yuleq"):
        res = (es - 1)/(es + 1)
        
    #Odds Ratio to Yule Y
    elif(fr=="or" and to=="yuley"):
        res = ((es)**0.5 - 1)/((es)**0.5 + 1)

        
    #OMEGA SQUARED
    #Omega squared to Epsilon squared
    elif(fr=="omegasq" and to=="epsilonsq"):
        res = es/(1 - ex1/(ex2 + ex1))
        
        
    #RANK BISERIAL
    #Rank Biserial to Vargha and Delaney A
    elif(fr=="rb" and to=="vda"):
        res = (es + 1)/2
        
    #VARGHA AND DELANEY A
    #Vargha and Delaney A to Rank Biserial
    
    elif(fr=="vda" and to=="rb"):
        res = 2*es - 1
        
        
    #YULE Q
    #Yule Q to Odds Ratio
    elif(fr=="yuleq" and to=="or"):
        res = (1 + es)/(1 - es)
        
    #Yule Q to Yule Y
    elif(fr=="yuleq" and to=="yuley"):
        res = (1 - (1 - es**2)**0.5)/es
        
        
    #YULE Y
    #Yule Y to Odds Ratio
    elif(fr=="yuley" and to=="or"):
        res = ((1 + es)/(1 - es))**2
        
    #Yule Y to Yule Q
    elif(fr=="yuley" and to=="yuleq"):
        res = (2*es)/(1 + es**2)
        
    return(res)