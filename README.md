# House Prices

## Introduction
This is a learning project. We are using data from Kaggle's "House Prices - Advanced Regression Techniques". Here are a couple of key facts about the competition and the data:
- We are trying to predict house price given some 79 features
- Our work will be evaluated by the RMSE of the **log** of the price

Here is the link to the competition: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques

## Setup
- Make sure you have uv installed. Read: [uv's installation docs](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer).
- Once you figure out cloning down the repo, cd into it and run these to sync and activate uv:

```bash
uv sync
source .venv/bin/activate
```

## Getting data
Before starting the project, make sure you log in to Kaggle and join the competition and accept all their paperwork. After that, follow either of these two options:

### Option 1: Manual download
- Create `data/raw` in your project root. Make sure the name is exactly right: all the scripts depend on it, and `.gitignore` only ignores a folder named `data/`, so a typo could get the data committed
- Download the zip file from Kaggle to the subdirectory and extract it. Delete the zip leftover if you'd like

### Option 2: Programmatic download
- Head over to Kaggle -> Settings -> API Tokens and generate a token
- Make a `.kaggle` subdirectory in your home directory, create an `access_token` file in it and paste your token. Save and close
- From the project root, run:

```bash
python scripts/download_data.py
```
