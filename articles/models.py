from django.db import models
#from django.db.models import JSONField
from jsonfield import JSONField
from django.contrib.auth.models import User

class FinalCSVTable(models.Model):
    table=JSONField(null=True)

# Create your models here.
class FinalCSV(models.Model):
    key = models.FloatField(null=True)
    buy_value=JSONField(null=True)
    correl = models.FloatField(null=True)	
    debt_to_equity	=models.FloatField(null=True)
    dividend_yield	=models.FloatField(null=True)
    earnings_yield=models.FloatField(null=True)
    fair_value_ddm	=models.FloatField(null=True)
    fair_value_fcf	=models.FloatField(null=True)
    free_cash_flow	=models.FloatField(null=True)
    industry	=models.CharField(max_length=100)
    industry_rank	=models.FloatField(null=True)
    market_share_growth	=models.FloatField(null=True)
    max_drawdown	=models.FloatField(null=True)
    name	=models.CharField(max_length=100)
    net_holding	=models.FloatField(null=True)
    net_inst_by_date	=JSONField( null=True)
    net_inst_value	=JSONField(null=True)
    net_value_executed	=models.FloatField(null=True)
    payout_ratio	=models.FloatField(null=True)
    price	=models.FloatField(null=True)
    profit_margin	=models.FloatField(null=True)
    profitability_rank	=models.CharField(max_length=100)
    quality_rank	=models.CharField(max_length=100)
    return_on_invested_capital	= models.FloatField()
    rev_growth =models.FloatField(null=True)	
    rev_uncertainty	=models.FloatField(null=True)
    roe_growth	=models.FloatField(null=True)
    roe_uncertainty	=models.FloatField(null=True)
    sector	=models.CharField(max_length=100)
    sell_value	=JSONField(null=True)
    top10_buys	=JSONField(null=True)
    top10_inst	=JSONField(null=True)
    top10_sells	=JSONField(null=True)
    value_rank	= models.CharField(max_length=100)
    vol	= models.FloatField(null=True)
    equity_to_debt	=models.FloatField(null=True)
    inv_rev_uncertainty	=models.FloatField(null=True)
    inv_roe_uncertainty	=models.FloatField(null=True)
    inv_correl	=models.FloatField(null=True)
    inv_max_drawdown	=models.FloatField(null=True)
    inv_vol	=models.FloatField(null=True)
    fcf_value	=models.FloatField(null=True)
    ddm_value	=models.FloatField(null=True)
    fair_value_score	=models.FloatField(null=True)
    risk_score	=models.FloatField(null=True)
    net_holding_pct=models.FloatField(null=True)
    net_value_executed_pct	=models.FloatField(null=True)
    company_health	=models.FloatField(null=True)
    company_yield	=models.FloatField(null=True)
    company_quality	=models.FloatField(null=True)
    ticker	= models.CharField(max_length=100, primary_key=True)
    ticker_name= models.CharField(max_length=100)
    wealth_graph = JSONField( null=True)
    def __str__(self):
        return self.ticker_name

class Portfolio(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    portfolio_name = models.CharField(primary_key=True ,max_length=100)
    date_created = models.DateField(auto_now=False, auto_now_add=False)
    execute_code = models.IntegerField(default=0)
    min_health = models.FloatField()
    min_yield = models.FloatField()
    min_quality = models.FloatField()
    min_fair_value = models.FloatField()
    max_industry_rank = models.FloatField()
    min_risk = models.FloatField()
    min_insider_rating = models.FloatField()
    min_inst_rating = models.FloatField()
    allocation = models.FloatField()
    def __str__(self):
        return (self.portfolio_name)

class TDState(models.Model):
    user = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)
    td_state = JSONField( null=True)

class PortfolioStats(models.Model):
    name = models.OneToOneField(Portfolio, related_name='name', on_delete=models.CASCADE)
    portfolio_constituents = JSONField( null=True)
    portfolio_wealth_graph = JSONField( null=True)
    portfolio_health = models.FloatField(null=True)
    portfolio_yield = models.FloatField(null=True)
    portfolio_quality = models.FloatField(null=True)
    portfolio_insider_rating = models.FloatField(null=True)
    portfolio_inst_rating = models.FloatField(null=True)
    portfolio_industry_rank = models.FloatField(null=True)
    portfolio_fair_value = models.FloatField(null=True)
    portfolio_risk = models.FloatField(null=True)
    portfolio_change = models.FloatField(null=True)
    portfolio_allocation= models.FloatField(null=True)
    portfolio_historical_return = models.FloatField(null=True)
    portfolio_historical_risk = models.FloatField(null=True)
    portfolio_historical_sharpe =models.FloatField(null=True)
    execute_portfolio = JSONField( null=True)
    