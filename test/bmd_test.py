from balancing_marketdocument.balancing import (
    BalancingMarketDocument,
    BMDTimePeriodTimeInteval,
    BMDTimeSeries,
    BMDTimeInterval,
    BMDPeriod,
    BMDPoint,
    BMDReason,
)
import json

reason_1 = BMDReason(
    code="A01",
    text="Accepted"
)

reason_2 = BMDReason(
    code="B02",
    text="Rejected"
)

point_1 = BMDPoint(
    position=1,
    quantity=100.0,
    secondaryQuantity=10.0,
    price_amount=45.50,
    financialPrice_amount=44.00,
    imbalance_Price_amount=46.00,
    procurement_Price_amount=43.50,
    settlement_amount_amount=100.0,
    quality="A01",
    reason=[reason_1]
)

point_2 = BMDPoint(
    position=2,
    quantity=120.0,
    secondaryQuantity=12.0,
    price_amount=46.00,
    financialPrice_amount=44.50,
    imbalance_Price_amount=47.00,
    procurement_Price_amount=44.00,
    settlement_amount_amount=120.0,
    quality="A01",
    reason=[reason_2]
)

point_3 = BMDPoint(
    position=3,
    quantity=110.0,
    secondaryQuantity=11.0,
    price_amount=45.75,
    financialPrice_amount=44.25,
    imbalance_Price_amount=46.50,
    procurement_Price_amount=43.75,
    settlement_amount_amount=110.0,
    quality="A02",
    reason=[]
)

period_time_interval_1 = BMDTimeInterval(
    start="2025-06-05T00:00Z",
    end="2025-06-05T01:00Z"
)

period_time_interval_2 = BMDTimeInterval(
    start="2025-06-05T01:00Z",
    end="2025-06-05T02:00Z"
)

period_1 = BMDPeriod(
    timeInterval=period_time_interval_1,
    resolution="PT15M",
    point=[point_1, point_2]
)

period_2 = BMDPeriod(
    timeInterval=period_time_interval_2,
    resolution="PT15M",
    point=[point_2, point_3]
)

time_series = BMDTimeSeries(
    mRID="BMD-TS-20250605-0001",
    businessType="A95",
    product="A01",
    objectAggregation="A01",
    in_Domain_mRID="10YHU-MAVIR----U",
    out_Domain_mRID="10YHU-MAVIR----U",
    marketEvaluationPoint_mRID="HU-MEP-001",
    auction_mRID="AUC-BAL-20250605-001",
    auction_category="A01",
    acquiring_Domain_mRID="10YHU-MAVIR----U",
    connecting_Domain_mRID="10YHU-MAVIR----U",
    registeredResource_mRID="HU-RESOURCE-001",
    resourceProvider_MarketParticipant_mRID="10XHU-BSP000001",
    resourceProvider_MarketParticipant_marketRole_type="A46",
    quantity_Measure_Unit_name="MAW",
    curveType="A01",
    flowDirection_direction="A01",
    direction="A01",
    settlementAmount_currency="EUR",
    price_Measure_Unit_name="MWH",
    Period=[period_1, period_2]
)

overall_time_period = BMDTimePeriodTimeInteval(
    start="2025-06-05T00:00Z",
    end="2025-06-05T02:00Z"
)

bmd = BalancingMarketDocument(
    mRID="BMD-DOC-20250604-0001",
    revisionNumber="1",
    _type="A25",
    process_processType="A51",
    sender_MarketParticipant_mRID="10XHU-BSP000001",
    sender_MarketParticipant_marketRole_type="A46",
    receiver_MarketParticipant_mRID="10X1001A1001A450",
    receiver_MarketParticipant_marketRole_type="A04",
    createdDateTime="2025-06-04T10:00:00Z",
    time_Period_timeInterval=overall_time_period,
    domain_mRID="10YHU-MAVIR----U",
    subject_MarketParticipant_mRID="10XHU-BSP000001",
    subject_MarketParticipant_marketRole_type="A46",
    businessType="A95",
    area_Domain_mRID="10YHU-MAVIR----U",
    currency_Unit_name="EUR",
    price_Measure_Unit_name="MWH",
    TimeSeries=[time_series]
)

bmd_data = bmd.to_dict()

with open("bmd_generated.json", "w") as f:
    json.dump(bmd_data, f, indent=4)
