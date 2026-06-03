from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Any

class BMDRoot(ABC):
    @abstractmethod
    def to_dict(self) -> dict[Any, Any]:
        pass

@dataclass
class BMDReason(BMDRoot):
    code: str | None
    text: str | None

    def to_dict(self):
        return {
            "code": self.code,
            "text": self.text
        }

@dataclass
class BMDPoint(BMDRoot):
    position: int | None
    quantity: float | None
    secondaryQuantity: float | None
    price_amount: float | None
    financialPrice_amount: float | None
    imbalance_Price_amount: float | None
    procurement_Price_amount: float | None
    settlement_amount_amount: float | None
    quality: str | None
    reason: list[BMDReason]

    def to_dict(self):
        return {
            "position": self.position,
            "quantity": self.quantity,
            "secondaryQuantity": self.secondaryQuantity,
            "price.amount": self.price_amount,
            "financialPrice.amount": self.financialPrice_amount,
            "imbalance_Price.amount": self.imbalance_Price_amount,
            "procurement_Price.amount": self.procurement_Price_amount,
            "settlement_Amount.amount": self.settlement_amount_amount,
            "quality": self.quality,
            "reason": [
                r.to_dict() for r in self.reason
            ]
        }

@dataclass
class BMDTimeInterval(BMDRoot):
    start: str | None
    end: str | None

    def to_dict(self):
        return {
            "start": self.start,
            "end": self.end
        }

@dataclass
class BMDPeriod(BMDRoot):
    timeInterval: BMDTimeInterval
    resolution: str | None
    point: list[BMDPoint]

    def to_dict(self):
        return {
            "timeInterval": self.timeInterval.to_dict(),
            "resolution": self.resolution,
            "Point": [
                p.to_dict() for p in self.point
            ]
        }

@dataclass
class BMDTimeSeries(BMDRoot):
    mRID: str | None
    businessType: str | None
    product: str | None
    objectAggregation: str | None
    in_Domain_mRID: str | None
    out_Domain_mRID: str | None
    marketEvaluationPoint_mRID: str | None
    auction_mRID: str | None
    auction_category: str | None
    acquiring_Domain_mRID: str | None
    connecting_Domain_mRID: str | None
    registeredResource_mRID: str | None
    resourceProvider_MarketParticipant_mRID: str | None
    resourceProvider_MarketParticipant_marketRole_type: str | None
    quantity_Measure_Unit_name: str | None
    curveType: str | None
    flowDirection_direction: str | None
    direction: str | None
    settlementAmount_currency: str | None
    price_Measure_Unit_name: str | None
    Period: list[BMDPeriod]

    def to_dict(self):
        return {
            "mRID": self.mRID,
            "businessType": self.businessType,
            "product": self.product,
            "objectAggregation": self.objectAggregation,
            "in_Domain.mRID": self.in_Domain_mRID,
            "out_Domain.mRID": self.out_Domain_mRID,
            "marketEvaluationPoint.mRID": self.marketEvaluationPoint_mRID,
            "auction.mRID": self.auction_mRID,
            "auction.category": self.auction_category,
            "acquiring_Domain.mRID": self.acquiring_Domain_mRID,
            "connecting_Domain.mRID": self.connecting_Domain_mRID,
            "registeredResource.mRID": self.registeredResource_mRID,
            "resourceProvider_MarketParticipant.mRID": self.resourceProvider_MarketParticipant_mRID,
            "resourceProvider_MarketParticipant.marketRole.type": self.resourceProvider_MarketParticipant_marketRole_type,
            "quantity_Measure_Unit.name": self.quantity_Measure_Unit_name,
            "curveType": self.curveType,
            "flowDirection.direction": self.flowDirection_direction,
            "direction": self.direction,
            "settlementAmount.currency": self.settlementAmount_currency,
            "price_Measure_Unit.name": self.price_Measure_Unit_name,
            "Period": [
                p.to_dict() for p in self.Period
            ]
        }

@dataclass
class BMDTimePeriodTimeInteval(BMDRoot):
    start: str | None
    end: str | None

    def to_dict(self):
        return {
            "start": self.start,
            "end": self.end
        }

@dataclass
class BalancingMarketDocument(BMDRoot):
    mRID: str | None
    revisionNumber: str | None
    _type: str | None
    process_processType: str | None
    sender_MarketParticipant_mRID: str | None
    sender_MarketParticipant_marketRole_type: str | None
    receiver_MarketParticipant_mRID: str
    receiver_MarketParticipant_marketRole_type: str | None
    createdDateTime: str | None
    time_Period_timeInterval: BMDTimePeriodTimeInteval
    domain_mRID: str | None
    subject_MarketParticipant_mRID: str | None
    subject_MarketParticipant_marketRole_type: str | None
    businessType: str | None
    area_Domain_mRID: str | None
    currency_Unit_name: str | None
    price_Measure_Unit_name: str | None
    TimeSeries: list[BMDTimeSeries]

    def to_dict(self):
        return {
            "mRID": self.mRID,
            "revisionNumber": self.revisionNumber,
            "type": self._type,
            "process.processType": self.process_processType,
            "sender_MarketParticipant.mRID": self.sender_MarketParticipant_mRID,
            "sender_MarketParticipant.marketRole.type": self.sender_MarketParticipant_marketRole_type,
            "receiver_MarketParticipant.mRID": self.receiver_MarketParticipant_mRID,
            "receiver_MarketParticipant.marketRole.type": self.receiver_MarketParticipant_marketRole_type,
            "createdDateTime": self.createdDateTime,
            "time_Period.timeInterval": self.time_Period_timeInterval.to_dict(),
            "domain.mRID": self.domain_mRID,
            "subject_MarketParticipant.mRID": self.subject_MarketParticipant_mRID,
            "subject_MarketParticipant.marketRole.type": self.subject_MarketParticipant_marketRole_type,
            "businessType": self.businessType,
            "currency_Unit.name": self.currency_Unit_name,
            "price_Measure_Unit.name": self.price_Measure_Unit_name,
            "TimeSeries": [
                t.to_dict() for t in self.TimeSeries
            ]
        }