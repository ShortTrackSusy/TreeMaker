import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/C04F5132-59A5-E911-B690-008CFA1983E0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/70350769-76A6-E911-86D7-B496910A01F0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/E437AB00-3EA5-E911-95C9-14187734413C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3073D914-56A5-E911-BBC3-0CC47AFF0454.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/245E7A7E-58A5-E911-BD91-0CC47AF9B2D2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/FCBA8EDC-A1A5-E911-A16B-0CC47AFCC69E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/0A027DEF-81A6-E911-9AE7-002590D9D8BC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/143A9BC1-55A5-E911-8C6B-FA163E83CFD7.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/DCCD5D20-56A5-E911-955D-FA163EA7059D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/74BBF1C0-55A5-E911-8D4F-FA163E3A3209.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/C8F94D87-5AA5-E911-A941-FA163EC0A9F4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/0C485188-5AA5-E911-BDF6-FA163E356580.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/A6A45CBD-5AA5-E911-812F-FA163EB4B8BD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/E4AB878B-58A5-E911-9B55-FA163E97883C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/F6379C9C-5DA5-E911-B567-FA163E74F827.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/001648A7-5FA5-E911-898E-FA163ED61884.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/981784BD-64A5-E911-B217-FA163EA7E5D8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/880265FF-6BA5-E911-91BC-FA163E15B395.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/A43A66CB-B3A5-E911-B7C8-FA163E25113F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/0EEA39E3-12A6-E911-9993-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/B6DE6849-35A7-E911-83D0-509A4C74D08C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/2616C7D1-47A7-E911-9159-509A4C9EF8FF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/2C18892D-56A5-E911-8E7C-0025905A6136.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/1ED78F02-60A5-E911-BD20-0CC47A4D764C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/9C8D3514-60A5-E911-A78F-0025905A60DE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/B0D5650F-60A5-E911-81FD-0025905A60A8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/E0249BC9-64A5-E911-B35B-0025905B8590.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/68CD8EA2-62A5-E911-BC47-0025905A606A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/FE2FD79D-62A5-E911-9063-0025905A48F0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/36A5B0C9-64A5-E911-8FB0-0025905B8590.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/8A1EAACB-64A5-E911-A76B-0025905B8562.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/7CF1D6B4-6BA5-E911-93F9-0CC47A4D7634.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/30ECCF3B-37A6-E911-B299-0CC47A4D7630.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/4AB65EE5-1FA6-E911-9C25-00269E95B1AC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/90F4A9FE-B8A6-E911-8BC4-002590D60056.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/00A6E000-D6A7-E911-BE6C-20CF307C98DC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/F602C4DF-54A5-E911-AC76-002590DE6DD4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/462A6A1A-57A5-E911-BCC7-0025904B11CC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/9C5F3082-61A5-E911-BF58-A4BF01287CF8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/0044592B-ABA5-E911-8737-A4BF01287D43.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3C198E8B-5AA5-E911-994D-008CFA0087C4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/70197A1B-69A5-E911-843E-D4AE526A03AD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/E8C8137A-2AA6-E911-8FE0-1866DA890622.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/F23D1937-B7A5-E911-A913-0242AC1C0500.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/18F22F83-1EA7-E911-BEA3-0242AC1C0503.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/7ACCE6C1-A0A7-E911-B514-AC1F6B1AEFEC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/B8F6F486-B0A7-E911-96A7-00266CFEFDE0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/FE5BED58-DBA7-E911-8483-EC0D9A0B3360.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/6CC3C544-91A8-E911-9AE5-001EC94BA144.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/3E64B1AF-95A8-E911-90F1-003048F7CC8A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/060DCE54-82A7-E911-9791-AC1F6B0DE296.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/4804D6A5-90A7-E911-9EEA-AC1F6B0DE3EE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/0A2E952A-97A8-E911-B4B3-F4E9D4A36760.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/5EA0FB3B-90A8-E911-9BB3-002590DBE1B2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/F68236B3-63A8-E911-A764-0025905C542C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/AE494FF4-94A8-E911-956A-0CC47AFCC3CE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/20CD7C82-93A8-E911-BBE5-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2bt-LLChipm_ctau-200_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/130000/5E3CA30C-95A8-E911-A6BF-0242AC1C0505.root',
] )


















