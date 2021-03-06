import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/324A7D30-59A5-E911-90A2-008CFAFFEA48.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/2E629016-56A5-E911-9E2B-509A4C74808D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/F2C2B866-2BA6-E911-BC14-7CD30AD091F0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3CA81D7F-70A5-E911-9BA8-008CFA197A28.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/D25A9015-F1A5-E911-9BD1-EC0D9A8221E6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/0426746C-87A5-E911-95CD-A0369FE2C19A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/10813E08-36A7-E911-9686-98039B3AFB12.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/30960E1F-47A7-E911-9EE6-008CFAFBFA98.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/2620A5DF-47A7-E911-95A9-8CDCD4A9A484.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/988F0703-60A5-E911-9F98-0242AC1C0507.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/2285D5D1-8EA5-E911-B855-0242AC1C0504.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/B6C13507-6EA6-E911-A97F-0242AC1C0502.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/6C204431-3EA7-E911-8DE4-002590908466.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/7EACFDFE-4FA7-E911-B40D-00259095305A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3C6CEE3A-7FA5-E911-915F-0CC47A7034D2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/6A9E9B99-03A6-E911-B9E7-0CC47AA98F92.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/F4FF0F18-6CA5-E911-99A1-1866DAEB5C78.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/1ED54C1D-6CA5-E911-BE5B-D4AE526DF5F9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/D6E68FD6-5AA5-E911-AE9F-AC1F6BAC8158.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/82F7810E-5BA5-E911-BE3C-0025905B85D2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3067381F-5DA5-E911-91C5-0025905A6122.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/50E9E056-62A5-E911-BB60-AC1F6BAC7D18.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/38400410-60A5-E911-8443-0025905A6122.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3C7CEC0A-60A5-E911-9C25-0025905B8580.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/2CEDE0D6-66A5-E911-9AFF-0CC47A4D75EC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/ACC1760D-69A5-E911-8193-0CC47A4C8EB6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/98B128E5-34A6-E911-90F9-0CC47A78A456.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/B82B83F0-5DA5-E911-8B13-0022640691C8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/48B5C70D-56A5-E911-9F7D-A0369FF88214.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/72680A6E-58A5-E911-AE52-B496910A80F0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/7C1D8513-56A5-E911-8151-008CFA197BBC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/94BB0A25-59A5-E911-9BBB-B496910A90E4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/ECB2767C-5AA5-E911-836E-A0369FF88246.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/0C560679-60A5-E911-9ECC-A0369FF88246.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/5E654C48-9EA5-E911-B6FC-008CFA056400.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/902D751C-57A5-E911-BC9D-A4BF01287CF8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/9C73FDD0-59A5-E911-BE05-002590DE6DD4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/664928E1-5BA5-E911-92DE-0025904B11CC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/D2E7466E-64A5-E911-9B83-0CC47A7FC74A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/02AAED37-38A6-E911-B522-98039B3B0036.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/109853F8-1FA6-E911-AE4A-0023AEEEB79C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3C94EE17-57A5-E911-AB56-405CFDFF481B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/464A8853-2AA6-E911-B80D-3417EBE34E8B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/4C27EB41-56A5-E911-8406-0025905C542E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/EA27C834-56A5-E911-B882-0CC47AFB8104.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/28502C6D-58A5-E911-B3C1-0CC47AFB8104.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/E4E02D46-59A5-E911-B97A-0CC47AFF0244.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/608D3A00-5BA5-E911-984B-0CC47AF9B2D2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/ACE11EC7-55A5-E911-82B5-20CF305B0629.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/96DCC7F0-5CA5-E911-B94C-AC1F6B0DE362.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/4096B435-3EA7-E911-B453-A0369FC5E9A4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/78C8ABF5-EBA5-E911-A614-002590D600E6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/2C27377E-32A7-E911-8995-44A84225C851.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/FED52D87-21A6-E911-984A-D4AE526A0DAE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/A89F8A99-4CA7-E911-9EFA-B496913C0C3C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/50402A1C-57A5-E911-ADDE-0017A4770444.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/F8E23389-21A6-E911-A391-0025B3E015D2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/B27B0B77-5AA5-E911-A3C6-C0BFC0E56826.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/321F478F-51A5-E911-B850-44A842CFCA00.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/9A202A24-57A5-E911-993C-6C3BE5B5A038.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/D22B4095-5AA5-E911-8822-B499BAAC068A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/C4F1FA89-2EA6-E911-90C6-6C3BE5B59218.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/AA63898F-66A5-E911-920D-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/9AE58ECD-7EA5-E911-8465-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/92B520D4-4FA6-E911-B5F0-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/2CC14DBF-36A7-E911-81E6-008CFAE45264.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/A45BC899-58A5-E911-8E40-FA163E093354.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/BA3D75A5-5CA5-E911-9BCC-FA163E6EDE73.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/FC980ECD-58A5-E911-8FAA-FA163E81F288.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/8C4AD0A1-5DA5-E911-A594-FA163E4E0EEC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/C0AE8BE7-69A5-E911-A1EE-FA163ECC4702.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/820ADF66-7EA5-E911-81A9-FA163EA4D40A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/0268D6DA-4DA6-E911-8A3B-FA163E21CC38.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/1CA7B307-F9A6-E911-80DE-002590FD5E3E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/7E2316D4-E0A7-E911-A4FB-AC1F6B4E0178.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/20DAF930-3EA7-E911-B598-0CC47A5FA3BD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/86BB0229-0EA8-E911-9F46-0025905A6070.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/F2FDADE1-83A7-E911-B995-AC1F6B0DE0C4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/6EA54762-D7A7-E911-B6D3-F4E9D4AF72D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/04CE8FF6-27A8-E911-9FD2-00259073E42C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/06D062B3-9EA7-E911-8A8B-AC1F6B1AEFEC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/72712862-9FA7-E911-B6D1-AC1F6B1E3070.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/30BA82E3-9EA7-E911-87CA-AC1F6B1B2364.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/BA99C71B-9FA7-E911-8318-AC1F6B1B2364.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/D2BCBE92-AAA7-E911-B8D2-00266CFFBC38.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/96093671-25A8-E911-A45D-0CC47AD98D6C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/145FD4E7-D3A7-E911-A411-AC1F6B0DE4A8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/54E8978E-D7A7-E911-9EFB-0CC47AC08BC8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/AA24FEE4-23A8-E911-B667-E0071B7A8570.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/6038C204-D6A7-E911-8BFB-001EC94CB3A4.root',
] )


















