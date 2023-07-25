from custom_gym import env
from stable_baselines3 import A2C, DQN
from stable_baselines3.common.env_checker import check_env

env = env(3,10)

model = A2C("MlpPolicy", env, verbose=0)
model.learn(total_timesteps=5_000,progress_bar=True)

model.save("testwy.h5")

# print(model.policy)

# vec_env = model.get_env()
# obs = vec_env.reset()
# env.render()

# for i in range(10):
#     action = model.predict(obs, deterministic=True)
#     obs, reward,done, info = vec_env.step(action)
#     # print(obs)
#     env.render()

env.manual_control()
