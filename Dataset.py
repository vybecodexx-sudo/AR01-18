import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('dataset_sinalizacao_ferroviaria.csv')

df_copy = df.copy()