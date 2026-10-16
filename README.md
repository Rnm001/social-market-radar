# Social Market Radar

**Social Market Radar** is a personal, non-commercial research project designed to analyze public discussions about publicly traded companies and identify changes in investor sentiment and market attention.

The project aims to investigate whether trends in online discussions have any measurable relationship with subsequent stock market movements.

## Project Objectives

* Measure the frequency of mentions of publicly traded companies.
* Analyze positive, negative, and neutral sentiment in financial discussions.
* Identify unusual increases in discussion activity.
* Monitor changes in investor attention and potential market euphoria.
* Compare historical sentiment indicators with subsequent market performance.
* Present aggregated results through a private dashboard.

## Initial Stock Coverage

The first version focuses on ten publicly traded companies:

| Ticker | Company                |
| ------ | ---------------------- |
| NVDA   | NVIDIA                 |
| TSLA   | Tesla                  |
| AAPL   | Apple                  |
| MSFT   | Microsoft              |
| AMD    | Advanced Micro Devices |
| GOOGL  | Alphabet               |
| AMZN   | Amazon                 |
| PLTR   | Palantir Technologies  |
| PBR    | Petrobras              |
| YPF    | YPF                    |

## Technology Stack

* **Python:** Data collection and statistical analysis.
* **MariaDB / MySQL:** Local database storage.
* **PHP:** Private dashboard and data visualization.
* **Reddit Data API:** Proposed source of public investment discussions, subject to authorization.

## How It Works

1. Retrieve a limited number of publicly available posts from authorized Reddit API endpoints.
2. Identify posts relevant to the selected companies.
3. Classify discussion sentiment using lightweight text analysis.
4. Calculate aggregated indicators, including mention volume, sentiment distribution, discussion acceleration, and unusual attention.
5. Store permitted data locally in MariaDB.
6. Display statistical results through a private PHP dashboard.
7. Evaluate historical relationships between discussion indicators and market performance.

## Reddit API Usage

Social Market Radar is designed as a **read-only application**.

The application will not:

* Publish posts or comments.
* Send private messages.
* Vote on content.
* Moderate communities.
* Contact Reddit users.
* Sell or redistribute Reddit content.
* Use Reddit data to train artificial intelligence models.

The project will respect applicable Reddit API terms, rate limits, privacy requirements, content deletion obligations, and data retention policies.

Reddit API access will only be implemented after obtaining the necessary authorization.

## Intended Communities

Subject to API permissions, the project may analyze public discussions from:

* r/stocks
* r/investing
* r/wallstreetbets
* r/StockMarket
* r/ValueInvesting

## Project Status

**Early development / Proof of Concept**

Currently implemented:

* Local MariaDB database.
* Database tables for tracked assets, publications, and indicators.
* Initial configuration for ten tracked stocks.
* Python-to-MariaDB connection.

Planned development:

* Authorized Reddit API integration.
* Sentiment classification.
* Aggregated trend indicators.
* Historical statistical analysis.
* Private PHP dashboard.
* Automated scheduled data collection.

## Privacy and Responsible Data Use

This project is intended for personal research and statistical analysis.

Its primary output consists of aggregated indicators rather than individual user profiles. It is not designed to identify, track, or profile individual Reddit users.

Any collection, storage, or processing of Reddit content will be subject to the permissions granted and Reddit's applicable developer policies.

## Disclaimer

Social Market Radar is an experimental research tool.

It does not provide financial advice, investment recommendations, or automated trading services.

All findings are exploratory and should not be interpreted as reliable predictions of future market performance.

## License

No license has been selected at this stage. All rights reserved.
