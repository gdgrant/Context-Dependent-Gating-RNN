import numpy as np
from parameters import *
import model
import sys
import pickle


def try_model(save_fn):
    # To use a GPU, from command line do: python model.py <gpu_integer_id>
    # To use CPU, just don't put a gpu id: python model.py
    try:
        if len(sys.argv) > 1:
            model.main(save_fn, sys.argv[1])
        else:
            model.main(save_fn)
    except KeyboardInterrupt:
        print('Quit by KeyboardInterrupt.')

###############################################################################
###############################################################################
###############################################################################

def LSTM_RL_XdG():

    update_parameters({
        'omega_c': 0.1, 'gating_type': 'XdG', 'architecture': 'LSTM', \
        'training_method': 'RL', 'n_train_batches': 50000, 'learning_rate': 5e-4, \
        'val_cost': 0.01, 'entropy_cost': 0.001, 'omega_xi': 0.01})
    save_fn = 'LSTM_RL_XdG.pkl'
    print('Running {}'.format(save_fn))
    try_model(save_fn)



if __name__ == '__main__':
    # By default, do small LSTM RL XdG sweep
    LSTM_RL_XdG()
