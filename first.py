import matplotlib.pyplot as plt
x=[2,3,4,5]
y=[2,4,6,8]
c=["r","b","g","y"]
plt.xlabel("number",fontsize=43)
plt.ylabel("number",fontsize=54)
plt.title("random",fontsize=34)
plt.bar(x,y,color=c,width=0.2,edgecolor="y",align="edge",linewidth="4",linestyle=":",alpha=0.5,label="population")#align="center"#by default center
plt.legend()
plt.show()
