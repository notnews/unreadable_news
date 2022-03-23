import re
import sys
# import textstat
from lexicalrichness import LexicalRichness
# import pandas as pd
# import numpy as np
# import datetime
# import july
# from typing import Optional, List, Union, Tuple
# from matplotlib.pyplot import Axes
# from matplotlib.colors import ListedColormap, LinearSegmentedColormap
# import matplotlib as mpl
# import statsmodels.api as sm
# from scipy.interpolate import interp1d
# import matplotlib.pyplot as plt
# import matplotlib.ticker as mtick
# import seaborn as sns
# sns.set_theme(context="notebook", font_scale=1.05, 
#               style='whitegrid')
# BLUE = '#0077BB'
# PURPLE = '#AA3377'


def clean_transcripts(text):
    """ This function applies minimal normalisation to transcript texts:
    
        * Removes parentheses and texts in them (e.g. (END VIDEO CLIP))
        
        * Removes transcript breaks 
            (e.g. "CAROL COSTELLO, CNN ANCHOR: A new tactic in Fallujah..." --> "A new tactic in Fallujah..."

        * Removes digits
            
        * Removes '/' for ' 
            (e.g. "I\'m Carol Costello" --> "I'm Carol Costello")
        
        * Removes dashes
            (e.g. "... they are -- that they recognized the heightened security..." --> "... they are that they recognized the heightened security...")
        
        * Removes astericks
            (e.g. "*3*** COMPANY REPORTS ** *3*AAR CORP (NYSE)" --> "COMPANY REPORTS  AAR CORP (NYSE)")
            
        * Removes extra white spaces 
            (e.g. "...United States.        Now..." -->  "...United States. Now...")        
    """
    
    # Remove parentheses
    re_parenthesis = re.compile(r'\([^)]*\)')
    text = re_parenthesis.sub('', text).strip()

    # Remove transcript breaks
    re_transcriptbreaks = re.compile(r'[^\.]+:')
    text = re_transcriptbreaks.sub('', text).strip()
    
    # Remove digits
    re_digits = re.compile(r'[0-9]+')
    text = re_digits.sub('', text).strip()

    # Removes '/'
    text = text.replace('\\', '')

    # Replace dashes/hyphens
    if sys.version_info[0] == 3:
        text = text.replace('–', ' ')
        text = text.replace('—', ' ')
        text = text.replace('-', ' ')
    else:
        text = text.replace('-', ' ')
    
    # Removes Astericks
    re_astericks = re.compile(r'\*\S*\*+')
    text = re_astericks.sub(" ", text).strip()
    
    # Remove extra whitespaces 
    re_extra_whitespaces = re.compile(r"\s+")
    text = re_extra_whitespaces.sub(" ", text).strip()    
    
    return text.lower()


def uniqueterms(text):
    lex = LexicalRichness(text)
    return lex.terms

def ttr(text):
    lex = LexicalRichness(text)
    if lex.words>1:
        return lex.ttr
    else:
        return None

def mtld(text):
    lex = LexicalRichness(text)
    if lex.words>1:
        return lex.mtld(threshold=0.72)
    else:
        return None

def hdd(text):
    lex = LexicalRichness(text)
    if lex.words>42:
        return lex.hdd(draws=42)
    else:
        return None
