## Tim Deckers Python function collection
## last updated: March 3rd 2018

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


## handling files

def txt2str(filename):
	"""Reads the plain text of a .txt file and returns a string"""
	with open(filename, 'r') as myfile:
		data=myfile.read().replace('\n', '')
		myfile.close()
		return data
	
def txt2lst(filename):
    """Reads a .txt file line by line and returns a list"""
    with open(filename) as file:
        lines = [line.strip("\n") for line in file]
        return lines
	
	
	
## matplotlib/seaborn plotting

def kdeplot(d, labels, savefig=False, title="", xlabel="", ylabel=""):
    ismulti = False
    if isinstance(d, pd.Series):
        lst_d = d.tolist()
    elif isinstance(d, list):
        lst_d = d[:]
        
    if isinstance(lst_d[0], pd.Series):
        lst_d_multi = [x.tolist() for x in lst_d[:]]
        ismulti = True
    elif isinstance(lst_d[0], list):
        lst_d_multi = lst_d[:]
        ismulti = True
    
    sns.set_context("talk")
    
    if ismulti:
        for i, x in enumerate(lst_d_multi):
            sns.kdeplot(x, shade=True, label=labels[i])
    else:
        sns.kdeplot(lst_d, shade=True, label=labels)
        
    plt.title(title)      
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)       
    plt.tight_layout()
    
    if savefig:
        plt.savefig("kdeplot.pdf")
    else:
        plt.show()
        
    plt.clf()
