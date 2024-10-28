#!/usr/bin/env python3

import pandas, os
import plotly.express as px
from science_match_quiz import science_quiz
from categorical_similarity import similarity_calc
from euclid_grapher_science import similarity_grapher

science_quiz()
similarity_calc()
similarity_grapher()