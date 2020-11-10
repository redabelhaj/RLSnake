import numpy as np
import matplotlib.pyplot as plt


def load_data(path):
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        rew, batch = [], []
        for i, l in enumerate(lines):
            r = float(l)
            batch.append(1+i)
            rew.append(r)
    return batch, rew

def running_mean(batch, rew, N=1):
    m = len(batch)
    cumsum = np.cumsum(np.insert(rew, 0, 0))
    running_mean = (cumsum[N:] - cumsum[:-N]) / float(N)
    s = len(running_mean)
    batch2 = np.linspace(0, m, num = s)
    return batch2, running_mean

def plot(path, label, N=20):
    b,r = load_data(path)
    b, r = running_mean(b,r, N=N)
    plt.plot(b,r, label = label)



# plot("ep_lengths", label = 'episode lengths')
# plt.xlabel("# episode")
# plt.ylabel("length")
# plt.legend()
# plt.title("episode length")
# plt.savefig("episode_lengths")
# plt.clf()

# plot("ep_rewards", label = 'episode rewards')
# plt.ylabel("rewards")
# plt.xlabel("# episode")
# plt.title("sum of rewards during the episode")
# plt.legend()
# plt.savefig("episode_rewards")
# plt.clf()

# plot("ep_lengths_ppo_img.txt", label = 'ppo - raw image')
# plot("ep_lengths_ppo.txt", label = 'ppo - few features')
# plot("ep_lengths_ppo_img_hunger30.txt", label = 'ppo - raw image - hunger = 30')
plot("ep_lengths_ppo_img_hunger30_newrew.txt", label = 'ppo - raw image NEW reward')
plot("ep_lengths_ppo_img_hunger30_bignet.txt", label = 'ppo - raw image - hunger = 30 - bigger net')
# plot("ep_lengths_ppo_img_hunger30_bignet_relu.txt", label = 'ppo - raw image - hunger = 30 - bigger net - relu')

plt.xlabel("# episode")
plt.ylabel("length")
plt.legend()
plt.title("episode length")
plt.savefig("episode_lengths_ppo_img")
plt.clf()

plot("ep_rewards_ppo_img.txt", label = 'ppo - raw image')
plot("ep_rewards_ppo.txt", label = 'ppo - few features')
plot("ep_rewards_ppo_img_hunger30.txt", label = 'ppo - raw image - hunger = 30')
plot("ep_rewards_ppo_img_hunger30_bignet.txt", label = 'ppo - raw image - hunger = 30 - bigger net')
plot("ep_rewards_ppo_img_hunger30_bignet_relu.txt", label = 'ppo - raw image - hunger = 30 - bigger net - relu')

plt.ylabel("rewards")
plt.xlabel("# episode")
plt.title("sum of rewards during the episode")
plt.legend()
plt.savefig("episode_rewards_ppo_img")
plt.clf()