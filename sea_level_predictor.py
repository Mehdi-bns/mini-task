import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df= read_csv("epa-sea-level.csv")

    # Create scatter plot
   plt.figure (figsize=(10,8))
   plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Data")
   plt.set_xlabel("Year")
   plt.set_ylabel("CSIRO Adjusted Sea Level")

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred = np.arange(df["Year"].min(), 2051)  
    y_pred = slope * x_pred + intercept 
    plt.plot(x_pred, y_pred, color="green", label="Best fit line (all data)")
    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
    df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"]
     )
    x_recent_pred = np.arange(2000, 2051)
    y_recent_pred = slope_recent * x_recent_pred + intercept_recent
    plt.plot(x_recent_pred, y_recent_pred, color="red", label="Best fit line")
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()