package bmd

import (
	"encoding/json"
	"os"
	"testing"
)

func TestGenerateDummyBMD(t *testing.T) {
	reason1 := BMDReason{code: "A01", text: "Accepted"}
	reason2 := BMDReason{code: "B02", text: "Rejected"}

	point1 := BMDPoint{
		position:                 1,
		quantity:                 float32(100.0),
		secondaryQuantity:        float32(10.0),
		price_amount:             float32(45.5),
		financialPrice_amount:    float32(44.0),
		imbalance_Price_amount:   float32(46.0),
		procurement_Price_amount: float32(43.5),
		settlement_amount_amount: float32(100.0),
		quality:                  "A01",
		reason:                   []BMDReason{reason1},
	}

	point2 := BMDPoint{
		position:                 2,
		quantity:                 float32(120.0),
		secondaryQuantity:        float32(12.0),
		price_amount:             float32(46.0),
		financialPrice_amount:    float32(44.5),
		imbalance_Price_amount:   float32(47.0),
		procurement_Price_amount: float32(44.0),
		settlement_amount_amount: float32(120.0),
		quality:                  "A01",
		reason:                   []BMDReason{reason2},
	}

	point3 := BMDPoint{
		position:                 3,
		quantity:                 float32(110.0),
		secondaryQuantity:        float32(11.0),
		price_amount:             float32(45.75),
		financialPrice_amount:    float32(44.25),
		imbalance_Price_amount:   float32(46.5),
		procurement_Price_amount: float32(43.75),
		settlement_amount_amount: float32(110.0),
		quality:                  "A02",
		reason:                   []BMDReason{},
	}

	period1 := BMDPeriod{
		timeInterval: BMDTimeInterval{start: "2025-06-05T00:00Z", end: "2025-06-05T01:00Z"},
		resolution:   "PT15M",
		point:        []BMDPoint{point1, point2},
	}

	period2 := BMDPeriod{
		timeInterval: BMDTimeInterval{start: "2025-06-05T01:00Z", end: "2025-06-05T02:00Z"},
		resolution:   "PT15M",
		point:        []BMDPoint{point2, point3},
	}

	ts := BMDTimeSeries{
		mRID:                                    "BMD-TS-20250605-0001",
		businessType:                            "A95",
		product:                                 "A01",
		objectAggregation:                       "A01",
		in_Domain_mRID:                          "10YHU-MAVIR----U",
		out_Domain_mRID:                         "10YHU-MAVIR----U",
		marketEvaluationPoint_mRID:              "HU-MEP-001",
		auction_mRID:                            "AUC-BAL-20250605-001",
		auction_category:                        "A01",
		acquiring_Domain_mRID:                   "10YHU-MAVIR----U",
		connecting_Domain_mRID:                  "10YHU-MAVIR----U",
		registeredResource_mRID:                 "HU-RESOURCE-001",
		resourceProvider_MarketParticipant_mRID: "10XHU-BSP000001",
		resourceProvider_MarketParticipant_marketRole_type: "A46",
		quantity_Measure_Unit_name:                         "MAW",
		curveType:                                          "A01",
		flowDirection_direction:                            "A01",
		direction:                                          "A01",
		settlementAmount_currency:                          "EUR",
		price_Measure_Unit_name:                            "MWH",
		period:                                             []BMDPeriod{period1, period2},
	}

	overall := BalancingMarketDocument{
		mRID:                                     "BMD-DOC-20250604-0001",
		revisionNumber:                           "1",
		_type:                                    "A25",
		process_processType:                      "A51",
		sender_MarketParticipant_mRID:            "10XHU-BSP000001",
		sender_MarketParticipant_marketRole_type: "A46",
		receiver_MarketParticipant_mRID:          "10X1001A1001A450",
		receiver_MarketParticipant_marketRole_type: "A04",
		createdDateTime:                           "2025-06-04T10:00:00Z",
		time_Period_timeInterval:                  BMDTimePeriodTimeInterval{start: "2025-06-05T00:00Z", end: "2025-06-05T02:00Z"},
		domain_mRID:                               "10YHU-MAVIR----U",
		subject_MarketParticipant_mRID:            "10XHU-BSP000001",
		subject_MarketParticipant_marketRole_type: "A46",
		businessType:                              "A95",
		area_Domain_mRID:                          "10YHU-MAVIR----U",
		currency_Unit_name:                        "EUR",
		price_Measure_Unit_name:                   "MWH",
		timeSeries:                                []BMDTimeSeries{ts},
	}

	data := overall._balancingMarketDocumentToDict()

	out, err := json.MarshalIndent(data, "", "    ")
	if err != nil {
		t.Fatalf("failed to marshal json: %v", err)
	}

	if err := os.WriteFile("../bmd_generated.json", out, 0644); err != nil {
		t.Fatalf("failed to write file: %v", err)
	}
}
