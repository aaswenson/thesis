import matplotlib.pyplot as plt

def load_data_therm(file):
    lines = open(file, 'r').readlines()
    

    data = {}

    for line in lines:
        res = [float(x) for x in line.split()]
        if len(res) == 1:
            power = res[0]
            data[power] = {'frac' : [],
                           'rad' : [],
                           'mass' : []
                          }
            continue
        data[power]['frac'].append(res[0])
        data[power]['mass'].append(res[1])

    return data


def load_data_crit(file):
    lines = open(file, 'r').readlines()
    
    data = {'frac' : [],
            'mass' : []
         }

    for line in lines:
        res = [float(x) for x in line.split()]
        data['frac'].append(res[0])
        data['mass'].append(res[2])

    return data

th_data = load_data_therm('th_mass.txt')
cr_data = load_data_crit('crit_mass.txt')


fig = plt.figure()
colors = ['c', 'g', 'b', 'r', 'k']

y1 = cr_data['mass']
for i, Q in enumerate(sorted(th_data.keys())[1:]):
    dat = th_data[Q]
    plt.scatter(dat['frac'], dat['mass'], label=str(int(Q)) + ' [kW]', s=8, c=colors[i])
    plt.plot(dat['frac'], dat['mass'], c=colors[i], linestyle='--')
    y2 = dat['mass']

plt.scatter(cr_data['frac'], cr_data['mass'], s=8, c='y', label='Critical Constraint')
plt.plot(cr_data['frac'], cr_data['mass'], c='y', linestyle='--')
plt.ylim((0, 2000))
plt.xlabel('fuel fraction [-]')
plt.ylabel('core mass [kg]')
plt.title('Limiting Core Mass')
plt.legend(title='Limiting Case')
plt.savefig('limiting_core_mass.png', dpi=700)
