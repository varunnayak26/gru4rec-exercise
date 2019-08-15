import preprocess
import pandas as pd
import numpy as np
from gru4rec.gru4rec import GRU4Rec
import util.data_utils
from Recommender import Recommender


def main():
    data = preprocess.get_data()
    print('Shape of dataframe is: {}'.format(data.shape))
    util.data_utils.print_dataset_info(data)

    gru = GRU4Rec(loss='bpr-max', final_act='elu-0.5', hidden_act='tanh', layers=[100], adapt='adagrad',
                  n_epochs=10, batch_size=2, dropout_p_embed=0, dropout_p_hidden=0, learning_rate=0.2,
                  momentum=0.3, n_sample=2048, sample_alpha=0, bpreg=1, constrained_embedding=False)
    gru.fit(data)


def main_using_interface():
    data = preprocess.get_data()
    print('Shape of dataframe is: {}'.format(data.shape))
    util.data_utils.print_dataset_info(data)

    recommender = Recommender(session_layers=[100],
                              batch_size=2,
                              learning_rate=0.01,
                              momentum=0.1,
                              dropout=0.1,
                              epochs=2,
                              personalized=False)
    recommender.fit(data)


if __name__ == "__main__":
    main()
