# Dissecting APKs from Google Play

In this repository, you can find the tools used to extend the original metadata from `AndroZoo`. Additionally, we included in this repository some extended results that we could not fit into the paper to provide some extra information about our results. Finally, we include a [CSV file](Data/dataset_distributed.csv) with the SHA256s (Android package kit -APK- identifiers) and their associated SDKs values of the distributed dataset used in the study.

## Tools

The [AndroZoo-Extender](Tools/AndroZoo-Extender/) collects information from the `AndroidManifest.XML` file about the APK's SDKs and permissions. Meanwhile, the [AndroZoo-Analyzer](Tools/AndroZoo-Analyzer/) analyzes the APK to collect information (encoding, MIME type, magic type, and extension) from the files inside it.

### Setup

#### AndroZoo

To use these tools, you need to [contact](https://androzoo.uni.lu/access) the AndroZoo team and request an AndroZoo API key. Additionally, you will have to download the AndroZoo metadata ([latest.csv](https://androzoo.uni.lu/static/lists/latest.csv.gz)).

#### Environment

The setup of the environment to use our tools is relatively simple. Since our tools are developed using `Python 3`, you must have it installed. Additionally, one of our [requirements](Tools/requirements.txt) (`python-magic`) depends on the `libmagic` library, which will have to be [installed](https://github.com/ahupp/python-magic#installation). Finally, from inside the [Tools](Tools/) directory, you can install the requirements using
```
pip install -r requirements.txt
```
and the environment will be ready to use the tools.

### Run

You should start by running the `AndroZoo-Extender` as the `AndroZoo-Analyzer` depends on its output. To learn how to run the tools, from inside the [Tools](Tools/) directory, run either
```
python AndroZoo-Extender -h
```
or
```
python AndroZoo-Analyzer -h
```

## Results

- [Magic types count distribution evolution](Plots/Magic_Type_Count_Distribution_Evolution.pdf) (each plot represents the magic type count distribution of an SDK for those magic types whose median value is above 0).
