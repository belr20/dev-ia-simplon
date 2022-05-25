# [Crypto Trading Bot]()
***by [BelR](https://github.com/belr20) with*** [![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3104/)

![Bot](./assets/bot.png)

FOR EDUCATIONAL PURPOSE ONLY, this is a Reinforcement Learning Trading Bot to beat the Bitcoin market through different Neural Network architectures.  
Many thanks to [@pythonlessons](https://github.com/pythonlessons) for his [clear & powerfull tutorial](https://pylessons.com/RL-BTC-BOT-backbone) :pray:  
  
## Resources

* [Technical Analysis Python Library | GitHub](https://github.com/bukosabino/ta#technical-analysis-library-in-python)
* [RL Bitcoin Trading Bot | pythonlessons | GitHub](https://github.com/pythonlessons/RL-Bitcoin-trading-bot)
* [Generalized Advantage Estimate | Towards Data Science](https://towardsdatascience.com/generalized-advantage-estimate-maths-and-code-b5d5bd3ce737)
* [RL PPO Proximal Policy Optimization Explained | Medium](https://jonathan-hui.medium.com/rl-proximal-policy-optimization-ppo-explained-77f014ec3f12)
* [MongoDB & mongo-express using Docker containers | Tutorials 24x7](https://devops.tutorials24x7.com/blog/containerize-mongodb-and-mongo-express-using-docker-containers)
* [Convolutional Neural Networks in TensorFlow | Adventures in Machine Learning](https://adventuresinmachinelearning.com/convolutional-neural-networks-tutorial-tensorflow/)
* [Recurrent Neural Networks & LSTM in Python & TensorFlow | Adventures in Machine Learning](https://adventuresinmachinelearning.com/recurrent-neural-networks-lstm-tutorial-tensorflow/)

## Bitcoin OHLCV historical data fetching
  
Simply run `./deploy.sh` or `.\deploy.bat` depending on your OS Linux / Windows OR follow next steps :  
  
### DB initialization

* [MongoDB is required](https://openclassrooms.com/fr/courses/4462426-maitrisez-les-bases-de-donnees-nosql/4474601-decouvrez-le-fonctionnement-de-mongodb)
* [ ] Set `DB_USER` & `DB_PASSWD` from `./data/etl_binance_to_db.py`

### Mongo server start

* Linux OS `docker start mongo`
* Windows OS [MongoDB](https://practicalprogramming.fr/mongodb-windows#lancez-linstance-mongodb) service must be launched at session start-up

### Bitcoin OHLCV data from [Binance Marketplace](https://www.binance.com/fr)

* [ ] Run `python manage.py fetch-data`

## HOW TO test Agents

### [Dense network](https://www.tensorflow.org/guide/keras/sequential_model)

* [ ] Run `python manage.py dense-agent`

### [CNN network](https://www.tensorflow.org/tutorials/images/cnn)

* [ ] Run `python manage.py cnn-agent`

### [LSTM network](https://www.tensorflow.org/tutorials/structured_data/time_series)

* [ ] Run `python manage.py lstm-agent`

## Data Visualization

* [ ] Set `show_reward=True` & `show_indicators=True` from `CryptoEnv` class in `manage.py` to display indicators
* [ ] Run `tensorboard --logdir runs` for [TensorBoard](https://www.tensorflow.org/tensorboard/get_started) metrics exploration from [@pythonlessons](https://github.com/pythonlessons) HARD WORK trainings
  
# Enjoy :wink:  
