package bmd

type BMDReason struct {
	code string
	text string
}

func (bmdR BMDReason) _bmdReasonToDict() map[string]any {
	return map[string]any{
		"code":   bmdR.code,
		"reason": bmdR.text,
	}
}

type BMDPoint struct {
	position                 int
	quantity                 float32
	secondaryQuantity        float32
	price_amount             float32
	financialPrice_amount    float32
	imbalance_Price_amount   float32
	procurement_Price_amount float32
	settlement_amount_amount float32
	quality                  string
	reason                   []BMDReason
}

func (bmdP BMDPoint) _bmdPointToDict() map[string]any {
	var reasons []map[string]any

	for _, r := range bmdP.reason {
		reasons = append(reasons, r._bmdReasonToDict())
	}

	return map[string]any{
		"position":                 bmdP.position,
		"quantity":                 bmdP.quantity,
		"secondaryQuantity":        bmdP.secondaryQuantity,
		"price.amount":             bmdP.price_amount,
		"financialPrice.amount":    bmdP.financialPrice_amount,
		"imbalance_Price.amount":   bmdP.imbalance_Price_amount,
		"procurement_Price.amount": bmdP.procurement_Price_amount,
		"settlement_Amount.amount": bmdP.settlement_amount_amount,
		"quality":                  bmdP.quality,
		"reason":                   reasons,
	}
}

type BMDTimeInterval struct {
	start string
	end   string
}

func (bmdTI BMDTimeInterval) _bmdTimeIntervalToDict() map[string]any {
	return map[string]any{
		"start": bmdTI.start,
		"end":   bmdTI.end,
	}
}

type BMDPeriod struct {
	timeInterval BMDTimeInterval
	resolution   string
	point        []BMDPoint
}

func (bmdP BMDPeriod) _bmdPeriodToDict() map[string]any {
	var points []map[string]any

	for _, p := range bmdP.point {
		points = append(points, p._bmdPointToDict())
	}

	return map[string]any{
		"timeInterval": bmdP.timeInterval._bmdTimeIntervalToDict(),
		"resolution":   bmdP.resolution,
		"Point":        points,
	}
}

type BMDTimeSeries struct {
	mRID                                               string
	businessType                                       string
	product                                            string
	objectAggregation                                  string
	in_Domain_mRID                                     string
	out_Domain_mRID                                    string
	marketEvaluationPoint_mRID                         string
	auction_mRID                                       string
	auction_category                                   string
	acquiring_Domain_mRID                              string
	connecting_Domain_mRID                             string
	registeredResource_mRID                            string
	resourceProvider_MarketParticipant_mRID            string
	resourceProvider_MarketParticipant_marketRole_type string
	quantity_Measure_Unit_name                         string
	curveType                                          string
	flowDirection_direction                            string
	direction                                          string
	settlementAmount_currency                          string
	price_Measure_Unit_name                            string
	period                                             []BMDPeriod
}

func (bmdTS BMDTimeSeries) _bmdTimeSeriesToDict() map[string]any {
	var periods []map[string]any

	for _, p := range bmdTS.period {
		periods = append(periods, p._bmdPeriodToDict())
	}

	return map[string]any{
		"mRID":                                    bmdTS.mRID,
		"businessType":                            bmdTS.businessType,
		"product":                                 bmdTS.product,
		"objectAggregation":                       bmdTS.objectAggregation,
		"in_Domain.mRID":                          bmdTS.in_Domain_mRID,
		"out_Domain.mRID":                         bmdTS.out_Domain_mRID,
		"marketEvaluationPoint.mRID":              bmdTS.marketEvaluationPoint_mRID,
		"auction.mRID":                            bmdTS.auction_mRID,
		"auction.category":                        bmdTS.auction_category,
		"acquiring_Domain.mRID":                   bmdTS.acquiring_Domain_mRID,
		"connecting_Domain.mRID":                  bmdTS.connecting_Domain_mRID,
		"registeredResource.mRID":                 bmdTS.registeredResource_mRID,
		"resourceProvider_MarketParticipant.mRID": bmdTS.resourceProvider_MarketParticipant_mRID,
		"resourceProvider_MarketParticipant.marketRole.type": bmdTS.resourceProvider_MarketParticipant_marketRole_type,
		"quantity_Measure_Unit.name":                         bmdTS.quantity_Measure_Unit_name,
		"curveType":                                          bmdTS.curveType,
		"flowDirection.direction":                            bmdTS.flowDirection_direction,
		"direction":                                          bmdTS.direction,
		"settlementAmount.currency":                          bmdTS.settlementAmount_currency,
		"price_Measure_Unit.name":                            bmdTS.price_Measure_Unit_name,
		"Period":                                             periods,
	}
}

type BMDTimePeriodTimeInterval struct {
	start string
	end   string
}

func (bmdPTI BMDTimePeriodTimeInterval) _bmdPeriodTimeIntervalToDict() map[string]any {
	return map[string]any{
		"start": bmdPTI.start,
		"end":   bmdPTI.end,
	}
}

type BalancingMarketDocument struct {
	mRID                                       string
	revisionNumber                             string
	_type                                      string
	process_processType                        string
	sender_MarketParticipant_mRID              string
	sender_MarketParticipant_marketRole_type   string
	receiver_MarketParticipant_mRID            string
	receiver_MarketParticipant_marketRole_type string
	createdDateTime                            string
	time_Period_timeInterval                   BMDTimePeriodTimeInterval
	domain_mRID                                string
	subject_MarketParticipant_mRID             string
	subject_MarketParticipant_marketRole_type  string
	businessType                               string
	area_Domain_mRID                           string
	currency_Unit_name                         string
	price_Measure_Unit_name                    string
	timeSeries                                 []BMDTimeSeries
}

func (bmd BalancingMarketDocument) _balancingMarketDocumentToDict() map[string]any {
	var ts []map[string]any

	for _, t := range bmd.timeSeries {
		ts = append(ts, t._bmdTimeSeriesToDict())
	}

	return map[string]any{
		"mRID":                          bmd.mRID,
		"revisionNumber":                bmd.revisionNumber,
		"type":                          bmd._type,
		"process.processType":           bmd.process_processType,
		"sender_MarketParticipant.mRID": bmd.sender_MarketParticipant_mRID,
		"sender_MarketParticipant.marketRole.type":   bmd.sender_MarketParticipant_marketRole_type,
		"receiver_MarketParticipant.mRID":            bmd.receiver_MarketParticipant_mRID,
		"receiver_MarketParticipant.marketRole.type": bmd.receiver_MarketParticipant_marketRole_type,
		"createdDateTime":                            bmd.createdDateTime,
		"time_Period.timeInterval":                   bmd.time_Period_timeInterval._bmdPeriodTimeIntervalToDict(),
		"domain.mRID":                                bmd.domain_mRID,
		"subject_MarketParticipant.mRID":             bmd.subject_MarketParticipant_mRID,
		"subject_MarketParticipant.marketRole.type":  bmd.subject_MarketParticipant_marketRole_type,
		"businessType":                               bmd.businessType,
		"currency_Unit.name":                         bmd.currency_Unit_name,
		"price_Measure_Unit.name":                    bmd.price_Measure_Unit_name,
		"TimeSeries":                                 ts,
	}
}
