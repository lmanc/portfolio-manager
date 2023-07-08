import pandas as pd


class Portfolio:
    def __init__(
        self,
        portfolio_file: str = 'portfolio.csv',
        allocation_file: str = 'allocation.csv',
        currency: str = 'EUR',
    ):
        self._pf = self.__class__._read_portfolio(portfolio_file)
        self._al = self.__class__._read_allocation(allocation_file)
        self._currency = currency

    @property
    def currency(self) -> str:
        return self._currency

    @staticmethod
    def _read_file(file: str) -> pd.DataFrame:
        try:
            return pd.read_csv(file)
        except FileNotFoundError as e:
            print(e)
            raise FileNotFoundError(e) from None

    @staticmethod
    def _replace_columns(df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError

    @staticmethod
    def _dropna_isin(df: pd.DataFrame) -> pd.DataFrame:
        return df.dropna(subset=['ISIN'])

    @staticmethod
    def _set_index_isin(df: pd.DataFrame) -> pd.DataFrame:
        return df.set_index('ISIN')

    @staticmethod
    def _convert_str_columns_to_float(df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError

    @staticmethod
    def _clean_portfolio(df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError

    @classmethod
    def _read_portfolio(cls, portfolio_file: str) -> pd.DataFrame:
        df = Portfolio._read_file(portfolio_file)
        df = cls._clean_portfolio(df)

        return df

    @staticmethod
    def _validate_allocation_percentage_sum(df: pd.DataFrame) -> bool:
        return df['Expected Percentage'].sum() == 100

    @staticmethod
    def _read_allocation(allocation_file: str) -> pd.DataFrame:
        df = Portfolio._read_file(allocation_file)

        if not Portfolio._validate_allocation_percentage_sum(df):
            raise ValueError(
                f'The total sum of percentages in the "Expected Percentage" column is not 100%'
            )

        df = Portfolio._set_index_isin(df)
        return df
