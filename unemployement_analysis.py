import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
df = pd.read_csv("data/Unemployment in india.csv")
print(df['Region'].head())
print(df['Region'].tail())
print(df['Region'].unique())
print(df.loc[5:10,['Region',' Date','Area']])
print(df.describe())
df.columns = df.columns.str.strip()
print("after:", df.columns)


#to check datatype of all columns
print("datatype",df.dtypes)
#convert date from string into datetime
df['Date'] = df['Date'].str.strip()
df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y")

#check and drop all null values 
print("null values:\n",df.isnull().sum())
print(df[df.isnull().all(axis=1)])
df = df.dropna(how="all")

#check count and drop duplicate rows
print("dupicate values:\n",df.duplicated().sum()) 
df = df.drop_duplicates()

#renaming the columns
df = df.rename(
    columns={
    "Estimated Unemployment Rate (%)":"Unemployement_rate(%)",
    "Estimated Labour Participation Rate (%)" : "Labour_participation(%)"
    }
    
)

df["Region"] = df["Region"].str.strip()
df["Frequency"] = df["Frequency"].str.strip()
df["Area"] = df["Area"].str.strip()


df = df.reset_index(drop=True)



#overall average Unemployement_rate(%) by region from 2019 to 2020
top10 = df.groupby("Region")["Unemployement_rate(%)"].mean().sort_values(ascending=False).head(10)
plt.bar(
    top10.index,
    top10.values,
    color="#4C78A8",
    edgecolor="#263238",
    linewidth=1.2
)
plt.title("overall average Unemployement_rate(%) by region from 2019 to 2020",
          fontsize=16,
          fontweight="bold",
          pad=15)
plt.xlabel("Region",fontsize=12,fontweight="bold")
plt.ylabel("Unemployement_rate(%)",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.grid(axis="x",visible=False)
plt.show() 

#Distribution  of Unemployement_rate(%) by histogram
plt.hist(df["Unemployement_rate(%)"],bins=12,
         edgecolor = "#283618",
         color="#6A994E",
         linewidth=1.2)

plt.title("Distribution  of Unemployement_rate(%)",
          fontsize=16,
          fontweight="bold")
plt.xlabel("Unemployement_rate(%)",fontsize=12,fontweight="bold")
plt.ylabel("Frequency",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.grid(axis="x",visible=False)
plt.tight_layout()
plt.show()  
#Distribution  of Unemployement_rate(%) by area
plt.figure(figsize=(15,10))
sns.boxplot(x="Area",y="Unemployement_rate(%)",data=df,
            palette=["#6A4C93","#F4A261"],
            linewidth=1.5,
            width=0.55,
            fliersize=5,
            saturation=0.9,
            boxprops=dict(edgecolor="#252525",linewidth=1.5),
            whiskerprops=dict(color="#252525",linewidth=1.5),
            capprops=dict(color="#252525",linewidth=1.5),
            medianprops=dict(color="#FFFFFF",linewidth=2),
            flierprops=dict(
                marker="o",
                markerfacecolor="#E63946",
                markeredgecolor="#252525",
                markersize=5,
                alpha=0.7
            ))
plt.title("Distribution  of Unemployement_rate(%) by area",
          fontsize=16,
          fontweight="bold",
          pad=15)
plt.xlabel("Area",fontsize=12,fontweight="bold")
plt.ylabel("Unemployement_rate(%)",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.grid(axis="x",visible=False)
plt.tight_layout()
plt.show() 

#Scatterplot of Unemployement_rate(%) and Estimated Employed
plt.figure(figsize=(8,5))
plt.scatter(df["Unemployement_rate(%)"],
            df["Estimated Employed"],
            color="#7B2CBF",
            edgecolor="#252525",
            linewidth=0.8,
            s=70,
            alpha=0.75
)
plt.title("Relationship between Unemployement_rate(%) and Estimated Employed",
          fontsize=16,
          fontweight="bold")
plt.xlabel("Unemployement_rate(%",fontsize=12,fontweight="bold")
plt.ylabel("Estimated Employed",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.grid(axis="x",visible=False)
plt.tight_layout()
plt.show()

#correlation of all numerical columns
correlation = df[
    [
        "Unemployement_rate(%)",
        "Labour_participation(%)",
        "Estimated Employed"
    ]
].corr()
plt.figure(figsize=(6,6))
sns.heatmap(correlation,
            annot=True,
            cmap="RdBu_r",
            fmt=".2f",
            linewidths=3,
            linecolor="white",
            center=0,
            cbar_kws={"label":"Correlation"},
            #vmin=1,
            #vmax=1
            )
plt.title("correlation between all numerical columns",fontsize=16,fontweight="bold")
plt.tight_layout()
plt.show()
 

#Data visualisation starts here
trend = df.groupby("Date")["Unemployement_rate(%)"].mean()
plt.figure(figsize=(8,5))
plt.plot(trend.index,trend.values,
         color="blue",
         marker = "o",
         linewidth = 2,
         linestyle = "-",
         markersize = 5
         )
plt.title("unemployement changing with the time",fontsize=16,fontweight="bold")
plt.xlabel("Dates",fontsize=12,fontweight="bold")
plt.ylabel("Unemployement_rate(%)",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.grid(axis="x",visible=False)
plt.show()
#boxplot for distribution of unemployement(%)
plt.figure(figsize=(8,5))
plt.boxplot(df["Unemployement_rate(%)"],
              patch_artist=True,
              boxprops = dict(facecolor="blue"),
              medianprops=dict(color="red",linewidth=2),
              whiskerprops=dict(color="black"),
              capprops=dict(color="black"),
              flierprops=dict(marker="o",markerfacecolor="red",markersize=5),
              )
plt.title("unemployement_rate distribution through boxplot",fontsize=16,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.tight_layout()
plt.show()
#scatterplot of unemployement_rate(%) and Labour_participation
plt.figure(figsize=(8,5))
plt.scatter(df["Unemployement_rate(%)"],
            df["Labour_participation(%)"],
            color = "skyblue",
            marker="o",
            linewidth=5)
plt.title("releation between unemployement and labour_participation",fontsize=16,fontweight="bold")
plt.xlabel("Unemployement_rate(%)",fontsize=12,fontweight="bold")
plt.ylabel("Labour_participation(%)",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7
         )
plt.show() 
#Average Unemployement by region
observation = df.groupby("Region")["Unemployement_rate(%)"].mean().sort_values()
plt.figure(figsize=(8,5))
plt.bar(observation.index,
        observation.values,
        color="#5B8E7D",
        linewidth=2,
        edgecolor="#3B3B3B",
        )
plt.title("Average Unemployement rate by region",fontsize=16,fontweight="bold")
plt.xticks(rotation=90)
plt.xlabel("Region",fontsize=12,fontweight="bold")
plt.ylabel("Avg unemployement rate",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.tight_layout()
plt.show()

#Unemployement rate by area
observation = df.groupby("Area")["Unemployement_rate(%)"].mean()
plt.figure(figsize=(8,5))
plt.bar(observation.index,
        observation.values,
        color=["#4C78A8","#F28E2B"],
        linewidth=1.2,
        edgecolor="#2F2F2F",
        )
plt.title("highest Unemployement rate by Area",fontsize=16,fontweight="bold")
plt.xticks(rotation=90)
plt.xlabel("Area",fontsize=12,fontweight="bold")
plt.ylabel("unemployement_rate(%)",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linewidth=0.7,
         linestyle="--",
         alpha=0.35)
plt.show() 
#piechart of Area
"""count = df["Area"].value_counts()
plt.pie(count.values,
        labels=count.index,
        autopct="%1.1f%%",       #DISPLAYS the one digit after the decimal
        startangle=90,
        colors=["#4C78A8","#F28E2B"],
        explode=(0.03,0.03),      #Slightly seperate both slices
        shadow=True,
        wedgeprops={                   #control the appearance of pie slices
            "edgecolor":"#2F2F2F",
            "linewidth":1.5
        },
        textprops={                  #controls the appearance of labels and percentage text
            "fontsize":11,
            "fontweight":"bold",
            "color":"#2F2F2F"
        })
plt.title("records distribution of Area",fontsize=16,fontweight="bold",pad=18)
plt.axis("equal")
plt.tight_layout()
plt.show()"""


#unemployement rate trend in the covid time
think = df[(df["Date"] >= "2020-02") & (df["Date"] <= "2020-05")]
covid = think.groupby("Date")["Unemployement_rate(%)"].mean()
plt.figure(figsize=(6,6))
plt.plot(covid.index,
         covid.values,
         linewidth=2.5,
         marker ="o",
         color = "#2F6690",
         markeredgecolor="#1F1F1F"
         
         )
plt.title("unemployemnt trend in covid19 time",fontsize=16,fontweight="bold")
plt.xlabel("Dates of covid19",fontsize=12,fontweight="bold")
plt.ylabel("unemployement_rate(%)",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linewidth=0.7,
         linestyle="--",
         alpha=0.35)
plt.tight_layout()
plt.show()

#top 10 regions in covid most affected by unemployement
think = df[(df["Date"] >= "2020-02") & (df["Date"] <= "2020-05")]
covid = think.groupby("Region")["Unemployement_rate(%)"].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(6,6))
plt.bar(covid.index,
         covid.values,
         linewidth=1.2,
         edgecolor ="black",
         color = "steelblue")
plt.title("Top 10 region most affected in covid19",fontsize=16,fontweight="bold")
plt.xlabel("Regions",fontsize=12,fontweight="bold",)
plt.ylabel("unemployement_rate(%)",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linewidth=0.7,
         linestyle="--",
         alpha=0.35)
plt.tight_layout()
plt.show()

#2months before covid impact on unemployement
think = df[(df["Date"] >= "2019-12-01") & (df["Date"]<="2020-02-01")]
covid = think.groupby("Region")["Unemployement_rate(%)"].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(6,6))
plt.bar(covid.index,
         covid.values,
         linewidth=1.2,
         edgecolor="black",
         color = "steelblue")
plt.title("top 10 region affected before covid19",fontsize=16,fontweight="bold")
plt.xlabel("Regions",fontsize=12,fontweight="bold")
plt.ylabel("unemployement_rate(%)",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linewidth=0.7,
         linestyle="--",
         alpha=0.35)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
#after covid unemployement rate of top10 regions
think = df[(df["Date"] >= "2020-05") & (df["Date"]<="2020-07")]
covid = think.groupby("Region")["Unemployement_rate(%)"].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(6,6))
plt.bar(covid.index,
         covid.values,
         linewidth=1.2,
         color = "steelblue",
         edgecolor="black")
plt.title("top 10 region with highest unemployement after covid19",fontsize=16,fontweight="bold")
plt.xlabel("Regions",fontsize=12,fontweight="bold")
plt.ylabel("unemployement_rate(%)",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linewidth=0.7,
         linestyle="--",
         alpha=0.35)
plt.tight_layout()
plt.show()
#labour participation rate  during covid 
think = df[(df["Date"] >= "2020-05") & (df["Date"]<="2020-07")]
covid = think.groupby("Region")["Labour_participation(%)"].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(6,6))
plt.bar(covid.index,
         covid.values,
         linewidth=1.2,
         edgecolor="#2D3047",
         color = "#5B5F97")
plt.title("top 10 region with highest Labour_participation(%) after covid19",fontsize=16,fontweight="bold")
plt.xlabel("Regions",fontsize=12,fontweight="bold")
plt.ylabel("Labour_participation rate(%)",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linewidth=0.7,
         linestyle="--",
         alpha=0.35)
plt.tight_layout()
plt.show()  
#Estimated employed during covid
think = df[(df["Date"] >= "2020-05") & (df["Date"]<="2020-06")]
covid = think.groupby("Region")["Estimated Employed"].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(6,6))
plt.bar(covid.index,
         covid.values,
         linewidth=1.2,
         edgecolor="#2F2F2F",
         color = "#2E8B57")
plt.title("top 10 region with highest Estimated Employed after covid19",fontsize=16,fontweight="bold")
plt.xlabel("Regions",fontsize=12,fontweight="bold")
plt.ylabel("Estimated Employed",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linewidth=0.7,
         linestyle="--",
         alpha=0.35)
plt.show()  
#top 10regions in time of covid which affected most unemployement are they rural or urban
think = df[(df["Date"] >= "2020-03-01") & (df["Date"] <= "2020-04-29")]
covid = (think.groupby(["Region","Area"])["Unemployement_rate(%)"].mean().reset_index())
top_10= (covid.groupby("Region")["Unemployement_rate(%)"].mean().sort_values(ascending=False).head(10).index)
final_df=covid[covid["Region"].isin(top_10)].sort_values(by="Unemployement_rate(%)",ascending=False)
plt.figure(figsize=(8,6))
sns.barplot(
    data=final_df,
    x="Region",
    y="Unemployement_rate(%)",
    hue="Area",
    linewidth = 1.2,
    palette=["#2F6690","#F4A261"],
    edgecolor="#404040"
)
plt.title("Top10 regions in covid with highest unemployement in Rural and Urban Area",fontsize="15",fontweight="bold")
plt.xlabel("Regions",fontsize=12)
plt.ylabel("Unemployement_rate(%)",fontsize=12)
plt.grid(axis="y",linestyle="--",alpha=0.4)
plt.legend(title="Area",frameon=True)
plt.tight_layout()
plt.show() 

#top 10regions after the time of covid which affected most unemployement are they rural or urban
think = df[(df["Date"] >= "2020-04") & (df["Date"] <= "2020-06")]
covid = (think.groupby(["Region","Area"])["Unemployement_rate(%)"].mean().reset_index())
top_10=(covid.groupby("Region")["Unemployement_rate(%)"].mean().sort_values(ascending=False).head(10).index)
final_df=covid[covid["Region"].isin(top_10)].sort_values(by="Unemployement_rate(%)",ascending=False)
plt.figure(figsize=(8,6))
sns.barplot(
    data=final_df,
    x="Region",
    y="Unemployement_rate(%)",
    hue="Area",
    linewidth = 1.2,
    palette="deep",
    edgecolor="black"
)
plt.title("Top10 regions after covid with highest unemployement in Rural and Urban Area",fontsize="15",fontweight="bold")
plt.xlabel("Regions",fontsize=12)
plt.ylabel("Unemployement_rate(%)",fontsize=12)
plt.grid(axis="y",linestyle="--",alpha=0.4)
plt.legend(title="Area",frameon=True)
plt.tight_layout()
plt.show()  
