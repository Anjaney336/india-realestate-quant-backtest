# Input contracts and provenance

No proprietary Alvionx data are used. The public repository does not redistribute raw Yahoo prices. Download them locally subject to provider terms; request parameters, hashes and coverage are recorded with results.

## Prices and liquidity

`download_prices` caches Yahoo adjusted close and raw close x volume (INR traded value). Adjusted prices are a total-return proxy; REIT distributions include components a vendor may classify inconsistently. Reconcile corporate actions against issuer filings before relying on results. The backtest models fractional exposures, not an executable unit-level order book.

The current symbols are EMBASSY.NS, MINDSPACE.NS, BIRET.NS and NXST.NS. On this run, older `-RR.NS` symbols each yielded one row. The data audit records their replacement; do not splice the series without checking identifiers. Developers include DLF, Godrej, Prestige, Oberoi, Lodha, Phoenix, Brigade and Sobha. This fixed modern universe has survivorship and selection bias.

Missing observations are not interpolated. A pair needs a complete training window. A missing held-position quote stops execution with an error. The historical run ends at the earliest last observed date among adequately populated series, rather than carrying stale quotes forward. The requested Nifty Realty vendor series returned only three observations and is not used as a benchmark or traded instrument.

## Government bond yields

Supply an RBI/CCIL export normalized to:

```csv
observation_date,available_date,yield_pct
```

Dates are ISO YYYY-MM-DD. `yield_pct` is percentage points (7.2 means 7.2%). `available_date` must reflect publication availability. Same-day timing is assumed available by close; use the next date if it was released after close. `align_rates` performs a backward availability join and rejects values more than seven calendar days after observation. No backward fill. Archive the source URL, download timestamp, series definition and file hash with your run. The code does not pretend that an imported CSV is an authenticated original-vintage RBI series.

The published historical run does **not** include a verified RBI/CCIL history. Its regime filter is disabled, explicitly. The synthetic validation run exercises HMM and yield-spread integration independently. Do not describe its results as historical rate-regime performance.

## REIT distributions

Normalize issuer events to `ticker,ex_date,available_date,cash_per_unit`. Use the raw market price on a matching unit basis. The helper requires a full year of event-history span and sums only trailing events already known and ex-distribution by the signal date. Independently establish completeness: sparse or missing events can bias yield downward.

The CLI optionally accepts a precomputed point-in-time distribution-yield panel with date index and ticker columns, in decimal units. The caller must document its provenance and confirm publication timing. Do not use present-day trailing yields retrospectively.

Distribution yield minus 10-year G-sec yield is a **yield spread**, not an asset cap rate, NAV discount, or bond-equivalent spread. Distribution composition, tax treatment, duration and principal risk differ.

## Sources

- yfinance project documentation: https://ranaroussi.github.io/yfinance/
- RBI Database on Indian Economy: https://data.rbi.org.in/
- CCIL: https://www.ccilindia.com/
- Embassy REIT: https://www.embassyofficeparks.com/
- Mindspace REIT: https://www.mindspacereit.com/
- Brookfield India REIT: https://www.brookfieldindiareit.in/investors
- Nexus Select Trust filings: https://www.nexusselecttrust.com/disclosure-report

These source links identify verification locations. They do not imply every source has supplied data for this run. No property-listing website was scraped.
