import streamlit as st
from page2 import filterer


def user_comparisons(data):
    # first subset
    first = filterer(data)

    # second subset
    second = filterer(data)
