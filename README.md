## High Performance Computational Infrastructure


### Due to size >25 MB all dataset could not be uploaded on github. The datasets can be found at,

 - https://drive.google.com/drive/folders/1f3Ui6UIpP8Tu4liml1QM08NPhuc1nbcb?usp=sharing


### Main dataset is collected from [The OPENSKY Network 2020](https://zenodo.org/record/4485741) dataset, secondatary dataset from [Open Flights](https://openflights.org/data.html)

### Steps

- Download the february data(large dataset) [direct downlaod](https://zenodo.org/record/4601479/files/flightlist_20210201_20210228.csv.gz?download=1)
- Clean air travel data can be done with data <strong>Data_Pre-processing_with_dask.ipynb file</strong>
- Do groupby operation with <strong>airport_mapper.py</strong> and <strong>airport_reducer.py</strong> to get count of flights occurs in each airport
- Do groupby operation with <strong>date_mapper.py</strong> and <strong>date_reducer.py</strong> to get count of flights occurs in each day
- Do clean airport dataset <strong>airport_data_slicing.ipynb</strong> file
- as airport data not include airport name, join clean airport dataset with mapreduce airports' flight count data using <strong>air_count.pig</strong>
- Use <strong>AirPlaneFebruary.twbx</strong> for visualize february data.
- And <strong>covid_air_compare.twbx</strong> for visualize covid data along with air travel data.

### February Data
![dashboard](https://user-images.githubusercontent.com/32392691/114286663-b9352700-9a58-11eb-9cfe-c56a87b644c4.JPG)


### Covid Infection vs Number of flights
![covair](https://user-images.githubusercontent.com/32392691/115795440-d7d7de00-a3c7-11eb-89fb-401d99674de1.JPG)

