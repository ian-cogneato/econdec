jupyter nbconvert --execute notebooks/1.extract-beh-data.ipynb
jupyter nbconvert --execute notebooks/2.clean-all.ipynb
jupyter nbconvert --execute notebooks/3.extract-gaze-data.ipynb
jupyter nbconvert --execute notebooks/4.transform-znorm.ipynb
jupyter nbconvert --execute notebooks/5.transform-subject-level.ipynb

read -s -p Done