#!/usr/bin/bash

montage -resize "50%" images/*_ac.png     -mode Concatenate -tile 2x  ac_analysis.png
montage -resize "50%" images/*_trans.png  -mode Concatenate -tile 2x  trans_analysis.png