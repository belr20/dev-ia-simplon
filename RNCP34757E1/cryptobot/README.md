# [Crypto Trading Bot]()
***by [BelR](https://github.com/belr20) with*** [![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3106/)

![Bot](./assets/images/bot.png)

**FOR EDUCATIONAL PURPOSE ONLY**, this is a Reinforcement Learning Trading Bot to beat the Bitcoin market through different Neural Network architectures.  
Many thanks to [@pythonlessons](https://github.com/pythonlessons) for his [clear & powerfull tutorial](https://pylessons.com/RL-BTC-BOT-backbone) :pray:  
  
## Resources

* [Technical Analysis Python Library | GitHub](https://github.com/bukosabino/ta#technical-analysis-library-in-python)
* [RL Bitcoin Trading Bot | @pythonlessons | GitHub](https://github.com/pythonlessons/RL-Bitcoin-trading-bot)
* [Generalized Advantage Estimate | Towards Data Science](https://towardsdatascience.com/generalized-advantage-estimate-maths-and-code-b5d5bd3ce737)
* [RL PPO Proximal Policy Optimization Explained | Medium](https://jonathan-hui.medium.com/rl-proximal-policy-optimization-ppo-explained-77f014ec3f12)
* [MongoDB & mongo-express using Docker containers | Tutorials 24x7](https://devops.tutorials24x7.com/blog/containerize-mongodb-and-mongo-express-using-docker-containers)
* [Convolutional Neural Networks in TensorFlow | Adventures in Machine Learning](https://adventuresinmachinelearning.com/convolutional-neural-networks-tutorial-tensorflow/)
* [Recurrent Neural Networks & LSTM in Python & TensorFlow | Adventures in Machine Learning](https://adventuresinmachinelearning.com/recurrent-neural-networks-lstm-tutorial-tensorflow/)

## Bitcoin OHLCV historical data fetching
  
After creating & activating your environment with [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#managing-environments) or [pip](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#installing-packages-using-pip-and-virtual-environments), you can run `./deploy.sh` or `.\deploy.bat` depending on your OS Linux / Windows and/or follow next steps.  
  
### OHLCV database initialization

* [MongoDB is required](https://openclassrooms.com/fr/courses/4462426-maitrisez-les-bases-de-donnees-nosql/4474601-decouvrez-le-fonctionnement-de-mongodb)
* [ ] Set `DB_USER` & `DB_PASSWD` from `./data/etl_binance_to_db.py` or in `.env` file

### Mongo server start

* Linux OS `docker start mongo`
* Windows OS [MongoDB](https://practicalprogramming.fr/mongodb-windows#lancez-linstance-mongodb) service must be launched at session start-up

### Bitcoin OHLCV data from [Binance Marketplace](https://www.binance.com/fr)

* [ ] Run `python main.py fetch-data`

## HOW TO test Agents
  
For HELP you can run `python main.py -h`  
  
### [Dense network](https://www.tensorflow.org/guide/keras/sequential_model)

* [ ] Run `python main.py dense-agent`

### [CNN network](https://www.tensorflow.org/tutorials/images/cnn)

* [ ] Run `python main.py cnn-agent`

### [LSTM network](https://www.tensorflow.org/tutorials/structured_data/time_series)

* [ ] Run `python main.py lstm-agent`

## Data Visualization

* [ ] Add option `--visualize` to CLI command for rendering data

```python
python main.py --visualize dense-agent
```

* [ ] Add option `--show-reward` to CLI command for rendering rewards

```python
python main.py --visualize --show-reward random-agent
```

* [ ] Add option `--show-indicators` to CLI command for rendering indicators : [SMA](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.SMAIndicator), [BB](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.BollingerBands), [PSAR](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.PSARIndicator), [MACD](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.MACD), [RSI](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.rsi)

```python
python main.py --visualize --show-reward --show-indicators lstm-agent
```

* [ ] Run `tensorboard --logdir runs` for [TensorBoard](https://www.tensorflow.org/tensorboard/get_started) metrics exploration from [@pythonlessons](https://github.com/pythonlessons) HARD WORK trainings
  
## Enjoy :wink:  
