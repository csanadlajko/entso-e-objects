from typing import Any
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

class RBMDRoot(ABC):
    @staticmethod
    def to_dict(self) -> dict[Any, Any]:
        pass

@dataclass
class RBMDReserveBidPeriodInterval(RBMDRoot):
    start: str = None
    end: str = None

    def to_dict(self):
        return {
            "start": self.start,
            "end": self.end
        }

@dataclass
class RBMDStatus(RBMDRoot):
    value: str = None
    
    def to_dict(self):
        return {
            "value": self.value
        }

@dataclass
class RBMDAnalogValue(RBMDRoot):
    value: int = None

    def to_dict(self):
        return {
            "value": self.value
        }

@dataclass
class RBMDMeasurements(RBMDRoot):
    name: str = None
    analogValue: RBMDAnalogValue = None

    def to_dict(self):
        return {
            "name": self.name,
            "AnalogValue" : self.analogValue.to_dict()
        }

@dataclass
class RBMDRegisteredResource(RBMDRoot):
    mRID: str = None
    measurements: list[RBMDMeasurements] = field(default_factory=list)

    def to_dict(self):
        return {
            "mRID": self.mRID,
            "Measurements": [
                m.to_dict() for m in self.measurements
            ]
        }
    
@dataclass
class RBMDValidityPeriodInterval(RBMDRoot):
    start: str = None
    end: str = None

    def to_dict(self):
        return {
            "start": self.start,
            "end": self.end
        }

@dataclass
class RBMDPeriodTimeInterval(RBMDRoot):
    start: str = None
    end: str = None

    def to_dict(self):
        return {
            "start": self.start,
            "end": self.end
        }

@dataclass
class RBMDLinkedBidTimeSeries(RBMDRoot):
    mRID: str = None
    status: RBMDStatus = None

    def to_dict(self):
        return {
            "mRID": self.mRID,
            "status": self.status.to_dict()
        }

@dataclass
class RBMDPoint(RBMDRoot):
    postion: int = None
    quantity_quantity: float = None
    quality: str = None
    minimum_Quantity_quantity: float = None
    price_amount: float = None
    energy_Price_amount: float = None

    def to_dict(self):
        return {
            "position": self.postion,
            "quantity.quantity": self.quantity_quantity,
            "quality": self.quality,
            "minimum_Quantity.quantity": self.minimum_Quantity_quantity,
            "price.amount": self.price_amount,
            "energy_Price.amount": self.energy_Price_amount
        }

@dataclass
class RBMDPeriod(RBMDRoot):
    timeInterval: RBMDPeriodTimeInterval = None
    resolution: str = None
    point: list[RBMDPoint] = field(default_factory=list)

    def to_dict(self):
        return {
            "timeInterval": self.timeInterval.to_dict(),
            "resolution": self.resolution,
            "Point": [p.to_dict() for p in self.point]
        }

@dataclass
class RBMDMridList(RBMDRoot):
    mRID: str = None

    def to_dict(self):
        return {
            "mRID": self.mRID
        }
    
@dataclass
class RBMDReason(RBMDRoot):
    code: str = None
    text: str = None

    def to_dict(self):
        return {
            "code": self.code,
            "text": self.text
        }

@dataclass
class RBMDBidTimeSeries(RBMDRoot):
    mRID: str = None
    auction_mRID: str = None
    businessType: str = None
    acquiring_Domain_mRID: str = None
    connecting_Domain_mRID: str = None
    biddingZone_Domain_mRID: str = None
    quantity_Measurement_Unit_name: str = None
    currency_Unit_name: str = None
    price_Measurement_Unit_name: str = None
    divisible: str = None
    blockBid: str = None
    status: RBMDStatus = None
    priority: int = None
    registeredResource: RBMDRegisteredResource = None
    flowDirection_direction: str = None
    stepIncrementQuantity: str = None
    energyPrice_Measurement_Unit_name: str = None
    marketAgreement_type: str = None
    marketAgreement_mRID: str = None
    marketAgreement_createdDateTime: str = None
    activation_ConstraintDuration_duration: str = None
    resting_ConstraintDuration_duration: str = None
    minimum_ConstraintDuration_duration: str = None
    maximum_ConstraintDuration_duration: str = None
    standard_MarketProduct_marketProductType: str = None
    original_MarketProduct_marketProductType: str = None
    validity_Period_timeInterval: RBMDValidityPeriodInterval = None
    inclusiveBidsIdentification: str = None
    linkedBidsIdentification: str = None
    multipartBidIdentification: str = None
    exclusiveBidsIdentification: str = None
    mktPSRType_psrType: str = None
    curveType: str = None
    original_MarketDocument_mRID: str = None
    original_MarketDocument_revisionNumber: str = None
    period: list[RBMDPeriod] = field(default_factory=list)
    availableBiddingZone_Domain: list[RBMDMridList] = field(default_factory=list)
    reason: list[RBMDReason] = field(default_factory=list)
    linked_BidTimeSeries: list[RBMDLinkedBidTimeSeries] = field(default_factory=list)
    procuredFor_MarketParticipant: list[RBMDMridList] = field(default_factory=list)
    sharedWith_MarketParticipant: list[RBMDMridList] = field(default_factory=list)
    exchangedWith_MarketParticipant: list[RBMDMridList] = field(default_factory=list)

    def to_dict(self):
        return {
            "mRID": self.mRID,
            "auction.mRID": self.auction_mRID,
            "businessType": self.businessType,
            "acquiring_Domain.mRID": self.acquiring_Domain_mRID,
            "connecting_Domain.mRID": self.connecting_Domain_mRID,
            "biddingZone_Domain.mRID": self.biddingZone_Domain_mRID,
            "quantity_Measurement_Unit.name": self.quantity_Measurement_Unit_name,
            "currency_Unit.name": self.currency_Unit_name,
            "price_Measurement_Unit.name": self.price_Measurement_Unit_name,
            "divisible": self.divisible,
            "blockBid": self.blockBid,
            "status": self.status.to_dict(),
            "priority": self.priority,
            "RegisteredResource": self.registeredResource.to_dict(),
            "flowDirection.direction": self.flowDirection_direction,
            "stepIncrementQuantity": self.stepIncrementQuantity,
            "energyPrice_Measurement_Unit.name": self.energyPrice_Measurement_Unit_name,
            "marketAgreement.type": self.marketAgreement_type,
            "marketAgreement.mRID": self.marketAgreement_mRID,
            "marketAgreement.createdDateTime": self.marketAgreement_createdDateTime,
            "activation_ConstraintDuration.duration": self.activation_ConstraintDuration_duration,
            "resting_ConstraintDuration.duration": self.resting_ConstraintDuration_duration,
            "minimum_ConstraintDuration.duration": self.maximum_ConstraintDuration_duration,
            "maximum_ConstraintDuration.duration": self.minimum_ConstraintDuration_duration,
            "standard_MarketProduct.marketProductType": self.standard_MarketProduct_marketProductType,
            "original_MarketProduct.marketProductType": self.original_MarketProduct_marketProductType,
            "validity_Period.timeInterval": self.validity_Period_timeInterval.to_dict(),
            "inclusiveBidsIdentification": self.inclusiveBidsIdentification,
            "linkedBidsIdentification": self.linkedBidsIdentification,
            "multipartBidIdentification": self.multipartBidIdentification,
            "exclusiveBidsIdentification": self.exclusiveBidsIdentification,
            "mktPSRType.psrType": self.mktPSRType_psrType,
            "curveType": self.curveType,
            "original_MarketDocument.mRID": self.original_MarketDocument_mRID,
            "original_MarketDocument.revisionNumber": self.original_MarketDocument_revisionNumber,
            "Period": [
                p.to_dict() for p in self.period
            ],
            "AvailableBiddingZone_Domain": [
                a.to_dict() for a in self.availableBiddingZone_Domain
            ],
            "Reason": [
                r.to_dict() for r in self.reason
            ],
            "Linked_BidTimeSeries": [
                l.to_dict() for l in self.linked_BidTimeSeries
            ],
            "ProcuredFor_MarketParticipant": [
                p.to_dict() for p in self.procuredFor_MarketParticipant
            ],
            "SharedWith_MarketParticipant": [
                s.to_dict() for s in self.sharedWith_MarketParticipant
            ],
            "ExchangedWith_MarketParticipant": [
                e.to_dict() for e in self.exchangedWith_MarketParticipant
            ]
        }
    
@dataclass
class ReserveBidMarketDocument(RBMDRoot):
    mRID: str = None
    revisionNumber: str = None
    _type: str = None
    process_processType: str = None
    sender_MarketParticipant_mRID: str = None
    sender_MarketParticipant_marketRole_type: str = None
    receiver_MarketParticipant_mRID: str = None
    receiver_MarketParticipant_marketRole_type: str = None
    createdDateTime: str = None
    reserveBid_Period_timeInterval: RBMDReserveBidPeriodInterval = None
    domain_mRID: str = None
    subject_MarketParticipant_mRID: str = None
    subject_MarketParticipant_marketRole_type: str = None
    bid_TimeSeries: list[RBMDBidTimeSeries] = field(default_factory=list)

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
            "reserveBid_Period.timeInterval": self.reserveBid_Period_timeInterval.to_dict(),
            "domain.mRID": self.domain_mRID,
            "subject_MarketParticipant.mRID": self.subject_MarketParticipant_mRID,
            "subject_MarketParticipant.marketRole.type": self.subject_MarketParticipant_marketRole_type,
            "Bid_TimeSeries": [
                ts.to_dict() for ts in self.bid_TimeSeries
            ]
        }