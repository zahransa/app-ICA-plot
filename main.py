import os
import mne
import json
import matplotlib.pyplot as plt
# Load brainlife config.json
with open('config.json','r') as config_f:
    config = json.load(config_f)


fname = config['fif']
ica=mne.preprocessing.read_ica(fname, verbose=None)
ica.plot_components()


plt.figure(1)
ica.plot_components()
plt.savefig(os.path.join('out_figs','ica.png'))