import textstat
from lexicalrichness import LexicalRichness
import statsmodels.api as sm
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
sns.set_theme(context="notebook", font_scale=1.05, 
              style='whitegrid')
BLUE = '#0077BB'
PURPLE = '#AA3377'


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


def its(row, base, x):
    """ Index time series so that first period is 0 and all subsequent values are percentage 
        changes from baseline/first period.
        
        base = baseline period value
        x = column to be turned into indexed time series
    """
    abs_change = 100 * (row[x] - base)/base
    if base > 0:
        return abs_change
    else:
        return -1 * abs_change

    
def plotline(x, y, title=None, yrange=None, xrange=range(0, 253, 36), xticklabels=None, color=BLUE, figsize=(12*.7, 8*.7), tickersize=13,
             markersize=80, labsize=15, titlesize=18, bw=0.4, savepath=None):
    
    # Get custom lowess
    lowess = sm.nonparametric.lowess(y, x, frac=bw)
    lowess_x = list(zip(*lowess))[0]
    lowess_y = list(zip(*lowess))[1]
    f = interp1d(lowess_x, lowess_y, bounds_error=False)
    ynew_line = f(x)

    # Init fig
    fig, ax = plt.subplots(figsize=figsize)

    # sns.regplot(x=x, y=y, 
    #             color=BLUE, 
    #             scatter_kws={'s': markersize, 'alpha': .3},
    #             line_kws={'linewidth':4, 'color': PURPLE, 'alpha': .9},
    #             lowess=True)

    sns.scatterplot(x=x, y=y, 
      s=markersize,
                    # scatter_kws={'s': markersize},
                    legend=False, 
                    color=color, 
                    alpha=0.3, 
                    ax=ax)

    sns.lineplot(x=x, y=ynew_line, 
                 linewidth=4, 
                 alpha=.85, color=PURPLE, 
                 ax=ax)    

    if xrange:
        plt.xticks(xrange)
    if xticklabels:
        ax.set_xticklabels(xticklabels, fontsize=tickersize)
    
    if yrange:
        plt.yticks(yrange, fontsize=tickersize)

    plt.xlabel('Publication year', fontweight='bold', loc='center', size=labsize)
    plt.ylabel('')
    if title:
        plt.title(title, fontweight='bold', loc='left', size=titlesize)
    
    ax.set_xlim(ax.set_xlim()[0]-3, ax.set_xlim()[1])
    ax.set_ylim(ax.set_ylim()[0], ax.set_ylim()[1]+.5)
    sns.despine(left=True, bottom=True)
    plt.tight_layout()        


    if savepath:
        plt.savefig(f'{savepath}.pdf', dpi=None, bbox_inches='tight', pad_inches=0)
        plt.savefig(f'{savepath}.png', dpi=120, bbox_inches='tight', pad_inches=0)

    return ax


def plot_dual_indices(y1,y2,x, title=None, yrange=None, xrange=None, color1=PURPLE, color2='darkslategray',
                      label1=None, label2=None, err_style='band', figsize=(12*.7, 8*.7), 
                      ylabel='Percentage change from 1987',
                      linewidth=3, tickersize=13, alpha=.6, labsize=15, titlesize=18, savepath=None):
    
    fig, ax = plt.subplots(figsize=figsize)

    sns.lineplot(x=x, y=y1, 
                 marker='o',
                 markersize=9,
                 linewidth=linewidth,
                 color=color1,
                 alpha=alpha,
                 label=label1,
                 ax=ax)

    sns.lineplot(x=x, y=y2, 
                 marker='o',
                 markersize=9,                 
                 linewidth=linewidth,
                 color=color2,
                 alpha=alpha,
                 label=label2,
                 ax=ax)

    ax.lines[1].set_linestyle("--")
    
    if xrange:
        plt.xticks(xrange)
    
    if yrange:
        plt.yticks(yrange, fontsize=tickersize)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))

    plt.xlabel('Publication year', fontweight='bold', loc='center', size=labsize)
    plt.ylabel(ylabel, fontweight='bold', loc='center', size=18)
    if title:
        plt.title(title, fontweight='bold', loc='left', size=titlesize)
        
    plt.legend(frameon=False, fontsize=16, loc='best')    
    
    sns.despine(left=True, bottom=True)
    plt.tight_layout()                

    if savepath:
        plt.savefig(f'{savepath}.pdf', dpi=None, bbox_inches='tight', pad_inches=0)
        plt.savefig(f'{savepath}.png', dpi=120, bbox_inches='tight', pad_inches=0)    

    
    return ax