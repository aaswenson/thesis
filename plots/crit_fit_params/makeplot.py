import matplotlib.pyplot as plt
import numpy as np


def load_data(file):
    lines = open(file, 'r').readlines()
    
    data = {'order' : [],
            'keff' : [],
            'std' : []
           }

    for line in lines:
        res = [float(x) for x in line.split()]
        data['order'].append(res[0])
        data['keff'].append(res[4])
        data['std'].append(res[5])

    return data

def plot(data):

    fig = plt.figure()
    for rxtr in data:
        X = data[rxtr]['order']
        Y = data[rxtr]['keff']
        E = data[rxtr]['std']
        plt.errorbar(X, Y, yerr=E, linestyle='None', marker='.', markersize=8,
                     label=rxtr)

    plt.title("Testing Order of Fit to Critical Radius Data")
    plt.xlabel("order of polynomial fit [-]")
    plt.ylabel("keff of validation test model [-]")
    plt.legend()
    plt.hlines(1.01, 2, 9, linestyle='dotted')
    plt.xlim((2,9))
    plt.savefig('poly_order_test.png')

data = {'UN CO2' : load_data('UN_CO2.txt'),
        'UO2 CO2' : load_data('UO2_CO2.txt')
       }

plot(data)
