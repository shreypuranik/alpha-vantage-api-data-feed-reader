from alpha_vantage_base import AlphaVantageBase
from companies import Companies

alpha_vantage_base_handler = AlphaVantageBase()
alpha_vantage_base_handler.execute(Companies.companies)