



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = np.array([221,227,280,261,264,238,250,236,240,230,246,283,253,273,516,256,271])
# print(sorted(data))
# df = pd.DataFrame(data)
# print(df.describe())
# df.plot.box(title="Box Chart")
# plt.grid(linestyle="--")
# plt.show()



plt.figure(figsize=(10, 6))
box = plt.boxplot(data,
                  labels=['A'],)
plt.show()