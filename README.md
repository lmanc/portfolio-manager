# TODO:
- Implement a mechanism using some public API to retrieve print names and daily closing values for assets.
- Improve logging by replacing print statements with appropriate logging functions.
- Enhance the "currency" property to support changes and ensure that changing the currency property affects the values inside the portfolio.
- Use Plotly to plot both Portfolio and PortfolioManager instances.

# FIXME:
- Write docstrings.
- Unit test everything with pytest.
- Address certain scenarios during rebalancing:
	- In the "no_sell" scenario, ensure that all assets in the portfolio are present in allocation.csv, while allowing assets in allocation.csv that are not in the portfolio.
	- In the "sell" scenario, fix the ".join()" operation in the build_working_dataframe function to avoid discarding rows that are not present in either of the two files.