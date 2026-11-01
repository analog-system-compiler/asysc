#!/usr/bin/bash

montage -resize "50%" images/*_ac.png     -mode Concatenate -tile 2x  images/ac_analysis.png
montage -resize "50%" images/*_trans.png  -mode Concatenate -tile 2x  images/trans_analysis.png