## How it words

The script checks title or arxiv articles on the specific subject and shows the most common and unique title. It can also rank provided title in terms of uniqueness 
```shell
python main.py --compared_article_title "Beam Search Splendor Game AI implementation" --topic "Reinforcement learning"
```

```shell
The least relevant article is Proximal Policy Optimization with Adaptive Exploration
Most common articles [
  {
    "id": "http://arxiv.org/pdf/1810.06339v1",
    "title": "Deep Reinforcement Learning"
  },
  {
    "id": "http://arxiv.org/pdf/2212.13980v1",
    "title": "Towards Learning Abstractions via Reinforcement Learning"
  },
  {
    "id": "http://arxiv.org/pdf/2004.07690v1",
    "title": "Data-Driven Robust Control Using Reinforcement Learning"
  },
  {
    "id": "http://arxiv.org/pdf/1702.05796v1",
    "title": "Collaborative Deep Reinforcement Learning"
  },
  {
    "id": "http://arxiv.org/pdf/2405.10369v1",
    "title": "Reinforcement learning"
  },
  {
    "id": "http://arxiv.org/pdf/1809.06064v1",
    "title": "Object-sensitive Deep Reinforcement Learning"
  },
  {
    "id": "http://arxiv.org/pdf/1906.10025v2",
    "title": "Modern Deep Reinforcement Learning Algorithms"
  },
  {
    "id": "http://arxiv.org/pdf/2302.01470v3",
    "title": "Learning to Optimize for Reinforcement Learning"
  },
  {
    "id": "http://arxiv.org/pdf/1806.04640v3",
    "title": "Unsupervised Meta-Learning for Reinforcement Learning"
  },
  {
    "id": "http://arxiv.org/pdf/1610.02707v1",
    "title": "Multi-Objective Deep Reinforcement Learning"
  }
]
Most unique articles [
  {
    "id": "http://arxiv.org/pdf/1812.04181v1",
    "title": "KF-LAX: Kronecker-factored curvature estimation for control variate optimization in reinforcement learning"
  },
  {
    "id": "http://arxiv.org/pdf/1705.06936v1",
    "title": "Atari games and Intel processors"
  },
  {
    "id": "http://arxiv.org/pdf/1806.01265v2",
    "title": "Equivalence Between Wasserstein and Value-Aware Loss for Model-based Reinforcement Learning"
  },
  {
    "id": "http://arxiv.org/pdf/2104.04893v1",
    "title": "The Atari Data Scraper"
  },
  {
    "id": "http://arxiv.org/pdf/1703.02658v1",
    "title": "What Would You Do? Acting by Learning to Predict"
  },
  {
    "id": "http://arxiv.org/pdf/2009.11403v2",
    "title": "CertRL: Formalizing Convergence Proofs for Value and Policy Iteration in Coq"
  },
  {
    "id": "http://arxiv.org/pdf/2406.17490v1",
    "title": "BricksRL: A Platform for Democratizing Robotics and Reinforcement Learning Research and Education with LEGO"
  },
  {
    "id": "http://arxiv.org/pdf/2003.03526v1",
    "title": "Convergence of Q-value in case of Gaussian rewards"
  },
  {
    "id": "http://arxiv.org/pdf/2108.10078v1",
    "title": "Distilling Neuron Spike with High Temperature in Reinforcement Learning Agents"
  },
  {
    "id": "http://arxiv.org/pdf/1908.09184v1",
    "title": "Universal Policies to Learn Them All"
  }
]
"Beam Search Splendor Game AI implementation" ranked as 3. The most similar articles are [
  {
    "id": "http://arxiv.org/pdf/2302.08969v1",
    "title": "Deep Reinforcement Learning for mmWave Initial Beam Alignment"
  },
  {
    "id": "http://arxiv.org/pdf/2202.12847v3",
    "title": "Building a 3-Player Mahjong AI using Deep Reinforcement Learning"
  },
  {
    "id": "http://arxiv.org/pdf/1602.04936v1",
    "title": "Reinforcement Learning approach for Real Time Strategy Games Battle city and S3"
  },
  {
    "id": "http://arxiv.org/pdf/1807.08217v1",
    "title": "Asynchronous Advantage Actor-Critic Agent for Starcraft II"
  },
  {
    "id": "http://arxiv.org/pdf/1712.06180v1",
    "title": "Towards a Deep Reinforcement Learning Approach for Tower Line Wars"
  }
]
```

## Running

You can run script with docker-compose or python

### Python
```shell
python main.py
```

### Docker compose

#### Linux
```shell
docker-compose run app /bin/sh
python main.py
```

#### Windows
```shell
docker compose run app /bin/sh
python main.py
```
