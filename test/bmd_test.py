from balancing_marketdocument.balancing import *
import json

point_1 = BMDPoint()
point_2 = BMDPoint()

inter_1 = BMDTimePeriodTimeInteval()
inter_2 = BMDTimeInterval()

period_1 = BMDPeriod(point=[point_1], timeInterval=inter_2)
period_2 = BMDPeriod(point=[point_1, point_2], timeInterval=inter_2)

ts = BMDTimeSeries(Period=[period_1, period_2])

bmd = BalancingMarketDocument(TimeSeries=[ts], time_Period_timeInterval=inter_1)

bmd_data = bmd.to_dict()

with open("generated.json", "w") as f:
    json.dump(bmd_data, f)