<div align="center">

  <img src="assets/images/bot.png" alt="logo" />
  <h1>Crypto Trading BOT</h1>
  <p>
    by
    <a href="https://github.com/belr20">BelR</a>
    with
  </p>
  
<!-- Badges -->
<p>
  <a href="https://www.python.org/downloads/release/python-3915/">
    <img src="https://img.shields.io/badge/python-3.9-blue.svg" alt="python version" />
  </a>
  <a href="https://github.com/carloscuesta/gitmoji">
    <img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/belr20/5b5005f852683fab26bd0ef5738ad9d6/raw/selenium-pom-gitmoji-badge.json" alt="gitmoji badge" />
  </a>
  <a href="https://github.com/belr20/dev-ia-simplon/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/belr20/dev-ia-simplon" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/belr20/dev-ia-simplon" alt="last update" />
  </a>
  <a href="https://github.com/belr20/dev-ia-simplon/network/members">
    <img src="https://img.shields.io/github/forks/belr20/dev-ia-simplon" alt="forks" />
  </a>
  <a href="https://github.com/belr20/dev-ia-simplon/stargazers">
    <img src="https://img.shields.io/github/stars/belr20/dev-ia-simplon" alt="stars" />
  </a>
  <a href="https://github.com/belr20/dev-ia-simplon/issues/">
    <img src="https://img.shields.io/github/issues/belr20/dev-ia-simplon" alt="open issues" />
  </a>
  <a href="http://www.wtfpl.net/about/">
    <img src="https://img.shields.io/badge/License-WTFPL-brightgreen.svg" alt="license" />
  </a>
</p>
   
<h4>
    <a href="https://github.com/belr20/dev-ia-simplon/tree/main/RNCP34757E1/cryptobot#screenshots">View Demo</a>
  <span> · </span>
    <a href="https://github.com/belr20/dev-ia-simplon">Documentation</a>
  <span> · </span>
    <a href="https://github.com/belr20/dev-ia-simplon/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/belr20/dev-ia-simplon/issues/">Request Feature</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->
# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
  * [Screenshots](#camera-screenshots)
  * [Tech Stack](#space_invader-tech-stack)
  * [Features](#dart-features)
  * [Environment Variables](#key-environment-variables)
- [Getting Started](#toolbox-getting-started)
  * [Prerequisites](#bangbang-prerequisites)
  * [Run Locally](#running-run-locally)
  * [Running Tests](#test_tube-running-tests)
  * [Deployment](#triangular_flag_on_post-deployment)
- [Usage](#eyes-usage)
  * [Dataset Creation](#card_file_box-dataset-creation)
  * [Test Agents](#white_check_mark-test-agents)
  * [Data Visualization](#monocle_face-data-visualization)
- [Roadmap](#compass-roadmap)
- [Contributing](#wave-contributing)
- [License](#warning-license)
- [Contact](#handshake-contact)
- [Acknowledgements](#gem-acknowledgements)


<!-- About the Project -->
## :star2: About the Project

**FOR EDUCATIONAL PURPOSE ONLY**, this is a Reinforcement Learning Trading Bot to beat the Bitcoin market through different Neural Network architectures.  
Many thanks to [@pythonlessons](https://github.com/pythonlessons) for his [clear & powerfull tutorial](https://pylessons.com/RL-BTC-BOT-backbone) :pray:  

<!-- Screenshots -->
### :camera: Screenshots

<div align="center"> 
  <img src="assets/images/gameplay.gif" alt="screenshot" width="1200"/>
</div>


<!-- TechStack -->
### :space_invader: Tech Stack

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.mongodb.com/">MongoDB</a></li>
  </ul>
</details>

<details>
<summary>DevOps</summary>
  <ul>
    <li><a href="https://www.docker.com/">Docker</a></li>
  </ul>
</details>

<!-- Features -->
### :dart: Features

- Reinforcement Learning ([Recurrent Neural Networks & LSTM in Python & TensorFlow](https://adventuresinmachinelearning.com/recurrent-neural-networks-lstm-tutorial-tensorflow/), [RL PPO Proximal Policy Optimization](https://jonathan-hui.medium.com/rl-proximal-policy-optimization-ppo-explained-77f014ec3f12), [Convolutional Neural Networks in TensorFlow](https://adventuresinmachinelearning.com/convolutional-neural-networks-tutorial-tensorflow/))
- Data & Technical indicators rendering ([Technical Analysis Python Library](https://github.com/bukosabino/ta#technical-analysis-library-in-python))

<!-- Env Variables -->
### :key: Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file :

`DB_USER` `DB_PASSWD` `DB_HOST` `DB_PORT` `DB_NAME` `COLLECTION_NAME`

Copy/paste, rename & fill in `.env.example` file.

<!-- Getting Started -->
## 	:toolbox: Getting Started

<!-- Prerequisites -->
### :bangbang: Prerequisites

This project uses Python with Pip as package manager & MongoDB with Docker as DBMS

* [ ] [Downloading & installing Python](https://wiki.python.org/moin/BeginnersGuide/Download)
* [ ] [Containerize MongoDB & Mongo Express using Docker Containers](https://devops.tutorials24x7.com/blog/containerize-mongodb-and-mongo-express-using-docker-containers)

<!-- Run Locally -->
### :running: Run Locally

Clone the repository (help [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))

```bash
git clone https://github.com/belr20/dev-ia-simplon.git
```

Go to the project directory

```bash
cd dev-ia-simplon/RNCP34757E1/cryptobot
```

Install dependencies in a recommended [virtual environment](https://docs.python.org/3/library/venv.html)

```bash
python -m venv venv
. ./venv/bin/activate
python -m pip install --upgrade pip wheel setuptools
python -m pip install -r requirements.txt
```


To see available commands run

```bash
python main.py -h
```


<!-- Running Tests -->
### :test_tube: Running Tests

TBD


<!-- Deployment -->
### :triangular_flag_on_post: Deployment

To deploy this project run

```bash
. ./deploy.sh
```

It will :
- Start MongoDB server
- Activate & install all dependencies in `venv`
- Fetch Bitcoin OHLCV data
- Test random agent


<!-- usage -->
## :eyes: Usage


<!-- dataset -->
### :card_file_box: Dataset Creation

* [MongoDB is required](https://openclassrooms.com/fr/courses/4462426-maitrisez-les-bases-de-donnees-nosql/4474601-decouvrez-le-fonctionnement-de-mongodb)
* [ ] Set `DB_USER` & `DB_PASSWD` from `./data/etl_binance_to_db.py` or in `.env` file
* [ ] Start Mongo server
  * Linux OS
  ```bash
  docker start mongo
  ```
  * Windows OS [MongoDB](https://practicalprogramming.fr/mongodb-windows#lancez-linstance-mongodb) service must be launched at session start-up
* [ ] Fetch Bitcoin OHLCV data from [Binance Marketplace](https://www.binance.com/fr)
```bash
python main.py fetch-data
```

```
cryptobot
│   .env
│   .gitignore
│   deploy.sh
│   main.py
│   README.md
│
└───data
│   │   create_db.py
│   │
│   └───input
│       │
│       └───BTCUSDT_Binance_hourly.csv
│       │
│       └───pricedata.csv
│
└───crypto_trading_bot
    │   --init--.py
    │   indicators.py
    │   model.py
    │   rl_bitcoin_trading_bot.py
    │   utils.py
```

<!-- Test Agents -->
### :white_check_mark: Test Agents

#### [Dense network](https://www.tensorflow.org/guide/keras/sequential_model)

* [ ] Run `python main.py dense-agent`

#### [CNN network](https://www.tensorflow.org/tutorials/images/cnn)

* [ ] Run `python main.py cnn-agent`

#### [LSTM network](https://www.tensorflow.org/tutorials/structured_data/time_series)

* [ ] Run `python main.py lstm-agent`

<!-- Data Visualization -->
### :monocle_face: Data Visualization

* [ ] Add option `--visualize` to CLI command for rendering data

```bash
python main.py --visualize dense-agent
```

* [ ] Add option `--show-reward` to CLI command for rendering rewards

```bash
python main.py --show-reward --visualize random-agent
```

* [ ] Add option `--show-indicators` to CLI command with a list within these indicators : [SMA](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.SMAIndicator), [BB](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.volatility.BollingerBands), [PSAR](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.PSARIndicator), [MACD](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.trend.MACD), [RSI](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html#ta.momentum.rsi)

```bash
# With SMA, BB, PSAR, MACD & RSI indicators
python main.py --show-indicators 'sma' 'bb' 'psar' 'macd' 'rsi' --show-reward --visualize lstm-agent
# With only SMA indicators
python main.py --show-indicators 'sma' --show-reward --visualize lstm-agent
```

* [ ] Run `tensorboard --logdir runs` for [TensorBoard](https://www.tensorflow.org/tensorboard/get_started) metrics exploration from [@pythonlessons](https://github.com/pythonlessons) HARD WORK trainings


Enjoy :thumbsup:


<!-- Roadmap -->
## :compass: Roadmap

* [x] Fork [RL Bitcoin Trading Bot | @pythonlessons | GitHub](https://github.com/pythonlessons/RL-Bitcoin-trading-bot)
* [x] Store OHLCV data in a Mongo server
* [x] Add the capability to chose which indicators to render
* [ ] Develop web API
* [ ] Implement integrated tests
* [ ] Add YouTube & Twitter Bitcoin posts NLP analysis to improve prediction


<!-- Contributing -->
## :wave: Contributing

<a href="https://github.com/belr20/dev-ia-simplon/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=belr20/dev-ia-simplon" />
</a>

Contributions are always welcome!


<!-- Acknowledgments -->
## :gem: Acknowledgements

 - [Technical Analysis Python Library | GitHub](https://github.com/bukosabino/ta#technical-analysis-library-in-python)
 - [RL Bitcoin Trading Bot | @pythonlessons | GitHub](https://github.com/pythonlessons/RL-Bitcoin-trading-bot)
 - [Generalized Advantage Estimate | Towards Data Science](https://towardsdatascience.com/generalized-advantage-estimate-maths-and-code-b5d5bd3ce737)
 - [RL PPO Proximal Policy Optimization Explained | Medium](https://jonathan-hui.medium.com/rl-proximal-policy-optimization-ppo-explained-77f014ec3f12)
 - [Convolutional Neural Networks in TensorFlow | Adventures in Machine Learning](https://adventuresinmachinelearning.com/convolutional-neural-networks-tutorial-tensorflow/)
 - [Containerize MongoDB and Mongo Express using Docker Containers | Tutorials 24x7](https://devops.tutorials24x7.com/blog/containerize-mongodb-and-mongo-express-using-docker-containers)
 - [Recurrent Neural Networks & LSTM in Python & TensorFlow | Adventures in Machine Learning](https://adventuresinmachinelearning.com/recurrent-neural-networks-lstm-tutorial-tensorflow/)

<br>

 - [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
 - [Downloading & installing Python](https://wiki.python.org/moin/BeginnersGuide/Download)
 - [Creation of Python virtual environments](https://docs.python.org/3/library/venv.html)
 
 <br>

 - [gitmoji](https://github.com/carloscuesta/gitmoji)
 - [Shields.io](https://shields.io/)
 - [Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#travel--places)
 - [Awesome Readme Template](https://github.com/Louis3797/awesome-readme-template)


<!-- License -->
## :warning: License

Distributed under the WTFPL License.


<!-- Contact -->
## :handshake: Contact

[BelR](https://github.com/belr20)

Project Link: [https://github.com/belr20/dev-ia-simplon](https://github.com/belr20/dev-ia-simplon)
