# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 08:04:27 2024

@author: erwan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#==============================================================================
# affichage des courbes ghi et dhi
#==============================================================================

def courbe_ghi_dhi(name, df_station):
    """
    Plot the irradiance curves (DHI and GHI) for a given station.

    Args:
        name (str): Name of the station.
        df_station (DataFrame): DataFrame containing irradiance data.
        
    Returns:
        None
    """
    i=0
    # Convert the index to datetime
    df_station.index = pd.to_datetime(df_station.index)
    
    # Create the figure
    plt.figure(f'DHI and GHI for station {name}',figsize=(10, 5))
    #plt.clf() #remove the hashtag if you only want to display one window at a time
    
    
    # Plot the curves for each column
    for col in df_station.columns:
        i=i+1
        print(f'Colonne : {i}') 
        plt.plot(df_station.index, df_station[col], label=col, linewidth=0.5)
    
    # Add title and labels
    plt.title(f'DHI and GHI for station {name}')
    plt.xlabel('Time [UTC+4]')
    plt.ylabel('Irradiance [$W/m^2$]')
    plt.legend(loc='best')
    
    # Show the plot
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    
def affiche_courbe(name,df):
    """
    Plot the irradiance curves (DHI and GHI) for a given station.

    Args:
        name (str): Name of the station.
        df (DataFrame): DataFrame containing irradiance valuable data.
        
    Returns:
        None
        
    Use this fonction after use the function "one_column_ghi_dhi(df_station)".
    """
    # Convert the index to datetime
    df.index = pd.to_datetime(df.index)
    # Create the figure
    plt.figure(f'DHI and GHI for station {name}',figsize=(10, 5))

    GHI=df['ghi']
    DHI=df['dhi']
    plt.plot(GHI, linestyle='-', linewidth=0.5, color='r', label='GHI')
    plt.plot(DHI, linestyle='-', linewidth=0.5, color='b', label='DHI')
    plt.xlabel('Time [UTC+4]')
    plt.ylabel('Irradiance [$W/m^2$]')
    plt.title(f'GHI and DHI in {name}')
    plt.legend(loc='best')
    
    # Show the plot
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return 
    
    
#==============================================================================
# Deletes data above the physical limit
#==============================================================================
    
def physic_limit(name_station, df_stations, df_geo):
    """
    Filter of data with physicals limits

    Args:
        name_station (str): Name of the station.
        df_station (DataFrame): DataFrame containing irradiance data.
        df_geo (DataFrame): DataFrame containing geographique data.
        
    Returns:
        df_filter (DataFrame): DataFrame containing data valid with BSRN criteria.
    """
    df_filter=df_stations.copy()
    return




#==============================================================================
# show only one column of ghi and one column of dhi
#==============================================================================


def one_column_ghi_dhi(df_station):
    """
    Show only one column of ghi and one column of dhi.

    Args:
        df_station (DataFrame): DataFrame containing irradiance data.
        
    Returns:
        df (DataFrame): DataFrame containing irradiance data with only 2 columns.
    """
    df=df_station.copy()
    # Filtrer les colonnes contenant 'GHI' et sommer les valeurs
    df['ghi'] = df.filter(like='GHI').sum(axis=1)
    
    # Filtrer les colonnes contenant 'DHI' et sommer les valeurs
    df['dhi'] = df.filter(like='DHI').sum(axis=1)
    
    # Suppression des colonnes individuelles GHI et DHI
    df = df.drop(columns=df.filter(like='GHI').columns)
    df = df.drop(columns=df.filter(like='DHI').columns)
    return df
