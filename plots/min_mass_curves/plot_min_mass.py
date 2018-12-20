import matplotlib.pyplot as plt

def load_data(file):
    lines = open(file, 'r').readlines()
    
    data = {'frac' : [],
            'rad' : [],
            'mass' : []
           }

    for line in lines:
        res = [float(x) for x in line.split()]
        data['frac'].append(res[0])
        data['rad'].append(res[1])
        data['mass'].append(res[2])

    return data

th_data = load_data('th_mass.txt')
cr_data = load_data('crit_mass.txt')


fig = plt.figure()
plt.scatter(th_data['frac'], th_data['mass'], label='minimum coolable')
plt.scatter(cr_data['frac'], cr_data['mass'], label='minimum critical')
plt.xlabel('fuel fraction [-]')
plt.ylabel('core mass [kg]')
plt.title('Limiting Core Mass')
plt.legend()
plt.savefig('limiting_core_mass.png')
