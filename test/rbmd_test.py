from reservebid_marketdocument.reserve_bid import (
    ReserveBidMarketDocument,
    RBMDReserveBidPeriodInterval,
    RBMDBidTimeSeries,
    RBMDStatus,
    RBMDRegisteredResource,
    RBMDMeasurements,
    RBMDAnalogValue,
    RBMDValidityPeriodInterval,
    RBMDPeriodTimeInterval,
    RBMDPeriod,
    RBMDPoint,
    RBMDLinkedBidTimeSeries,
    RBMDReason,
    RBMDMridList,
)
import json

reserve_bid_period = RBMDReserveBidPeriodInterval(
    start="2025-06-05T00:00Z",
    end="2025-06-06T00:00Z"
)

status = RBMDStatus(value="A06")

analog_value = RBMDAnalogValue(value=25)
measurement = RBMDMeasurements(
    name="maximumAvailableCapacity",
    analogValue=analog_value
)

registered_resource = RBMDRegisteredResource(
    mRID="HU-RESOURCE-UNIT-001",
    measurements=[measurement]
)

validity_period = RBMDValidityPeriodInterval(
    start="2025-06-05T00:00Z",
    end="2025-06-05T04:00Z"
)

point1 = RBMDPoint(
    postion=1,
    quantity_quantity=100.0,
    quality="A01",
    minimum_Quantity_quantity=50.0,
    price_amount=45.50,
    energy_Price_amount=50.00
)

point2 = RBMDPoint(
    postion=2,
    quantity_quantity=120.0,
    quality="A01",
    minimum_Quantity_quantity=60.0,
    price_amount=46.00,
    energy_Price_amount=51.00
)

period_time_interval = RBMDPeriodTimeInterval(
    start="2025-06-05T00:00Z",
    end="2025-06-05T04:00Z"
)

period = RBMDPeriod(
    timeInterval=period_time_interval,
    resolution="PT15M",
    point=[point1, point2]
)

linked_bid = RBMDLinkedBidTimeSeries(
    mRID="RBID-LINKED-001",
    status=RBMDStatus(value="A06")
)

reason = RBMDReason(
    code="A01",
    text="Normal bid"
)

procured_participant = RBMDMridList(mRID="10XHU-BSP000002")
shared_participant = RBMDMridList(mRID="10XHU-BSP000003")

bid_time_series = RBMDBidTimeSeries(
    mRID="RBID-TS-20250605-0001",
    auction_mRID="AUC-FCR-20250605-001",
    businessType="A95",
    acquiring_Domain_mRID="10YHU-MAVIR----U",
    connecting_Domain_mRID="10YHU-MAVIR----U",
    biddingZone_Domain_mRID="10YHU-MAVIR----U",
    quantity_Measurement_Unit_name="MAW",
    currency_Unit_name="EUR",
    price_Measurement_Unit_name="MAW",
    divisible="A01",
    blockBid="A02",
    status=status,
    priority=1,
    registeredResource=registered_resource,
    flowDirection_direction="A01",
    stepIncrementQuantity="1.0",
    energyPrice_Measurement_Unit_name="MWH",
    marketAgreement_type="A01",
    marketAgreement_mRID="CAP-CONTRACT-2025-001",
    marketAgreement_createdDateTime="2025-06-01T08:00:00Z",
    activation_ConstraintDuration_duration="PT15M",
    resting_ConstraintDuration_duration="PT0M",
    minimum_ConstraintDuration_duration="PT15M",
    maximum_ConstraintDuration_duration="PT60M",
    standard_MarketProduct_marketProductType="A01",
    original_MarketProduct_marketProductType="A01",
    validity_Period_timeInterval=validity_period,
    inclusiveBidsIdentification="INC-001",
    linkedBidsIdentification="LNK-001",
    multipartBidIdentification="MULTI-001",
    exclusiveBidsIdentification="EXC-001",
    mktPSRType_psrType="A04",
    curveType="A01",
    original_MarketDocument_mRID="ORIG-DOC-001",
    original_MarketDocument_revisionNumber="1",
    period=[period],
    availableBiddingZone_Domain=[RBMDMridList(mRID="10YHU-MAVIR----U")],
    reason=[reason],
    linked_BidTimeSeries=[linked_bid],
    procuredFor_MarketParticipant=[procured_participant],
    sharedWith_MarketParticipant=[shared_participant],
    exchangedWith_MarketParticipant=[]
)

rbmd = ReserveBidMarketDocument(
    mRID="RBID-DOC-20250604-0001",
    revisionNumber="1",
    _type="A37",
    process_processType="A51",
    sender_MarketParticipant_mRID="10XHU-BSP000001",
    sender_MarketParticipant_marketRole_type="A46",
    receiver_MarketParticipant_mRID="10X1001A1001A450",
    receiver_MarketParticipant_marketRole_type="A04",
    createdDateTime="2025-06-04T10:00:00Z",
    reserveBid_Period_timeInterval=reserve_bid_period,
    domain_mRID="10YHU-MAVIR----U",
    subject_MarketParticipant_mRID="10XHU-BSP000001",
    subject_MarketParticipant_marketRole_type="A46",
    bid_TimeSeries=[bid_time_series]
)

rbmd_data = rbmd.to_dict()

with open("rbmd_generated.json", "w") as f:
    json.dump(rbmd_data, f, indent=4)
