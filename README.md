# laughing-waffle

Basic implementation of an OpenAI gym environment and solution using RLlib+Ray.

The environment (CorridorEnv) models a 1D hallway in which you can move left or
right.  The goal is to walk the length of the environment.

# Dev setup

Developed on OS X 10.15.2 with Python 3.7.6.

* `virtualenv -p /usr/local/bin/python3 laughing-waffle`
* `source laughing-waffle/bin/activate`
* `pip install -r requirements.txt`


Example command line rllib test: `rllib train --run=PPO --env=CartPole-v0`

Solve corridor: `python solve.py`

# Results

```
custom_metrics: {}
date: 2020-03-03_09-09-19
done: false
episode_len_mean: 20.0
episode_reward_max: -20.0
episode_reward_mean: -20.0
episode_reward_min: -20.0
episodes_this_iter: 200
episodes_total: 2211
experiment_id: 2c4b0be1c48e48a28bb618ff2652dcd8
hostname: roflmac
info:
  grad_time_ms: 6380.027
  learner:
    default_policy:
      cur_kl_coeff: 0.0035156249068677425
      cur_lr: 4.999999873689376e-05
      entropy: 0.260914146900177
      entropy_coeff: 0.0
      kl: 0.233213409781456
      policy_loss: -0.1097039207816124
      total_loss: -0.10883039981126785
      vf_explained_var: 0.9999980330467224
      vf_loss: 5.362247975426726e-05
  load_time_ms: 2.925
  num_steps_sampled: 60000
  num_steps_trained: 59520
  sample_time_ms: 4198.086
  update_time_ms: 11.373
iterations_since_restore: 15
node_ip: 192.168.1.143
num_healthy_workers: 2
off_policy_estimator: {}
perf:
  cpu_util_percent: 78.42857142857144
  ram_util_percent: 78.1857142857143
pid: 6885
policy_reward_max: {}
policy_reward_mean: {}
policy_reward_min: {}
sampler_perf:
  mean_env_wait_ms: 0.07089970211264157
  mean_inference_ms: 1.5481844698880929
  mean_processing_ms: 0.34513338729264853
time_since_restore: 161.8279185295105
time_this_iter_s: 10.09489917755127
time_total_s: 161.8279185295105
timestamp: 1583255359
timesteps_since_restore: 60000
timesteps_this_iter: 4000
timesteps_total: 60000
training_iteration: 15


CorridorEnv (length: 20) Training Iteration 15:
	Iteration episode mean length: 20.0
	Episodes total: 2211
	Time total: 161.8sec

Problem solved in 2211 training episodes
```
