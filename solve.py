# Runs PPO (via Ray) to solve the CorridorEnv
# Generally solves the env in < 3000 episodes
import ray
from ray.rllib.agents import ppo
from ray.tune.logger import pretty_print

from corridor import CorridorEnv


def solve():
    length = 20
    ray.init()
    trainer = ppo.PPOTrainer(
        env=CorridorEnv, config={"env_config": {"length": length}}
    )
    while True:
        results = trainer.train()
        training_iteration = results.get("training_iteration")
        episode_length_mean = results.get("episode_len_mean")
        episodes_total = results.get("episodes_total")
        total_time = results.get("time_total_s")
        print("\n============")
        print(pretty_print(results))
        print(
            f"\nCorridorEnv (length: {length}) "
            f"Training Iteration {training_iteration}:"
            f"\n\tIteration episode mean length: {episode_length_mean}"
            f"\n\tEpisodes total: {episodes_total}"
            f"\n\tTime total: {round(total_time, 1)}sec"
        )
        if episode_length_mean <= length:
            break
    print(f"\nProblem solved in {episodes_total} training episodes")


if __name__ == "__main__":
    solve()
