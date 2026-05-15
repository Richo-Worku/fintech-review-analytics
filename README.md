## Data Collection Methodology

### Overview
User review data was collected from the Google Play Store using the `google-play-scraper` library. The objective was to gather user feedback for selected Ethiopian banking applications to support sentiment analysis and user experience evaluation.

### Target Applications
The following mobile banking applications were analyzed:

- CBE Mobile Banking (`com.combanketh.mobilebanking`)
- Dashen Bank (`com.dashen.dashensuperapp`)
- BOA Mobile Banking (`com.boa.boaMobileBanking`)

### Data Extraction Process
- Reviews were retrieved programmatically using the `reviews()` function from the `google-play-scraper` library.


### Data Fields Collected
The following attributes were extracted for each review:

- **review**: User-written review text
- **rating**: Numerical rating (1–5)
- **date**: Review timestamp (normalized to YYYY-MM-DD format)
- **bank**: Name of the banking application
- **source**: Data source ("Google Play")

### Data Volume
A target of at least 400 reviews per application (1,200 total) was set. Multiple requests were made to reach this threshold.

### Limitations
- The number of available reviews depends on Google Play Store visibility and regional availability.
- In cases where fewer than 400 reviews were accessible, all available reviews were collected.
- Language and regional filters may affect the completeness of the dataset.

### Data Storage
The cleaned dataset was stored as a CSV file(data/bank_reviews).
