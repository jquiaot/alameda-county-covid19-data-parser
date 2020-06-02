# Alameda County COVID-19 Data Parser

Python scripts for parsing COVID-19 data made available through the Alameda 
County Open Data Hub.

## Disclaimer

I am not affiliated with Alameda County in any way. I'm just a resident 
looking at the data made available by the county on COVID-19 cases.

I made these scripts to process the available data for a personal spreadsheet
I'm maintaining. As such, the scripts may be severely limited in what they do.
You're more than welcome to take the code and do what you need with it. Perhaps
I'll have a future project to create a public dashboard based on the available
data, but I currently (as of 2020-06-02) have no plans to do so.

## References

Links (valid as of 2020-06-02):

* [Alameda County Open Data Hub][ac-odh]
* [Alameda County Public Health Department][ac-pub-health]
    * [Alameda County COVID-19 Info Home][ac-c19-home]
    * [Alameda County COVID-19 Dashboard][ac-c19-dash]

## Introduction

Alameda County has made county-wide COVID-19 statistics available through their
COVID-19 dashboard. However, as useful as the dashboard has been, it is (in my
opinion) pretty limited in that there is no historical data available for
the city/juristiction breakdown.

Fortunately, the county has published this data through their Open Data
initiative, providing a mechanism where historical city/juristiction cases
can be obtained.

## Open Data Endpoints

The Open Data that I'm processing with these scripts comes from two primary
sources:

* ["Alameda County COVID-19 Cases and Deaths Over Time"][ac-cases-api] - County/LHJ level case and death rates
* ["Alameda County Cumulative Cases By Place And Zip"][ac-place-cases-api] - Cumulative cases by place/zip in Alameda County

## Data Format

Ultimately, the data looks like the following JSON snippet:

```json
{
  // ... info not relevant to my use cases removed ...
  "features": [
    {
      "attributes": {
        "Date": 1582876800000,
        "AC_CumulCases": 2,
        "AC_CumulDeaths": 0,
        "ObjectId": 1
      }
    },
    {
      "attributes": {
        "Date": 1582963200000,
        "AC_CumulCases": 2,
        "AC_CumulDeaths": 0,
        "ObjectId": 2
      }
    },
    {
      "attributes": {
        "Date": 1583049600000,
        "AC_CumulCases": 2,
        "AC_CumulDeaths": 0,
        "ObjectId": 3
      }
    },
    // ...
  ]
}
```

That is, an array of `feature` objects, each with a single field `attributes`,
which is an object containing some date field (in milliseconds since Epoch)
and the data values.

For the County/LHJ-wide case rates, the date field is `Date`, and the relevant
data fields are in `AC_CumulCases` and `AC_CumulDeaths`.

For the place/zip case rates, the date field is `DtCreate`, and the relevant 
data fields are the actual place or zip names, e.g., `Fremont` for Fremont 
cases.

## `covid_json_to_csv.py` - JSON to CSV Parsing Script

Python script that parses the JSON output from the AC Open Data endpoints
and returns a CSV of the date and the appropriate case data.

[ac-odh]: https://data.acgov.org/
[ac-pub-health]: http://www.acphd.org/
[ac-c19-home]: http://www.acphd.org/2019-ncov.aspx
[ac-c19-dash]: https://ac-hcsa.maps.arcgis.com/apps/opsdashboard/index.html#/1e0ac4385cbe4cc1bffe2cf7f8e7f0d9
[ac-cases-api]: https://data.acgov.org/datasets/AC-HCSA::alameda-county-covid-19-cases-and-deaths-over-time-1
[ac-place-cases-api]: https://data.acgov.org/datasets/AC-HCSA::alameda-county-cumulative-cases-by-place-and-zip?orderBy=DtCreate
