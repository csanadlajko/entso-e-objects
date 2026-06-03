from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Any

class BMDRoot(ABC):
    @abstractmethod
    def to_dict(self) -> dict[Any, Any]:
        pass

@dataclass
class BMDReason(BMDRoot):
    code: str | None = None
    text: str | None = None

    def to_dict(self):
        return {
            "code": self.code,
            "text": self.text
        }

@dataclass
class BMDPoint(BMDRoot):
    position: int | None = None
    quantity: float | None = None
    secondaryQuantity: float | None = None
    price_amount: float | None = None
    financialPrice_amount: float | None = None
    imbalance_Price_amount: float | None = None
    procurement_Price_amount: float | None = None
    settlement_amount_amount: float | None = None
    quality: str | None = None
    reason: list[BMDReason] = field(default_factory=list)

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
    start: str | None = None
    end: str | None = None

    def to_dict(self):
        return {
            "start": self.start,
            "end": self.end
        }

@dataclass
class BMDPeriod(BMDRoot):
    timeInterval: BMDTimeInterval | None = None
    resolution: str | None = None
    point: list[BMDPoint] = field(default_factory=list)

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
    mRID: str | None = None
    businessType: str | None = None
    product: str | None = None
    objectAggregation: str | None = None
    in_Domain_mRID: str | None = None
    out_Domain_mRID: str | None = None
    marketEvaluationPoint_mRID: str | None = None
    auction_mRID: str | None = None
    auction_category: str | None = None
    acquiring_Domain_mRID: str | None = None
    connecting_Domain_mRID: str | None = None
    registeredResource_mRID: str | None = None
    resourceProvider_MarketParticipant_mRID: str | None = None
    resourceProvider_MarketParticipant_marketRole_type: str | None = None
    quantity_Measure_Unit_name: str | None = None
    curveType: str | None = None
    flowDirection_direction: str | None = None
    direction: str | None = None
    settlementAmount_currency: str | None = None
    price_Measure_Unit_name: str | None = None
    Period: list[BMDPeriod] = field(default_factory=list)

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
    start: str | None = None
    end: str | None = None

    def to_dict(self):
        return {
            "start": self.start,
            "end": self.end
        }

@dataclass
class BalancingMarketDocument(BMDRoot):
    mRID: str | None = None
    revisionNumber: str | None = None
    _type: str | None = None
    process_processType: str | None = None
    sender_MarketParticipant_mRID: str | None = None
    sender_MarketParticipant_marketRole_type: str | None = None
    receiver_MarketParticipant_mRID: str | None = None
    receiver_MarketParticipant_marketRole_type: str | None = None
    createdDateTime: str | None = None
    time_Period_timeInterval: BMDTimePeriodTimeInteval | None = None
    domain_mRID: str | None = None
    subject_MarketParticipant_mRID: str | None = None
    subject_MarketParticipant_marketRole_type: str | None = None
    businessType: str | None = None
    area_Domain_mRID: str | None = None
    currency_Unit_name: str | None = None
    price_Measure_Unit_name: str | None = None
    TimeSeries: list[BMDTimeSeries] = field(default_factory=list)

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