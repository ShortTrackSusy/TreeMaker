import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/26CE7004-6F87-E911-952C-002590DE6DD4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/CCD16687-7487-E911-B2A0-00266CF3E130.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/F20A1B13-7B87-E911-A24D-0CC47AC33AB2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/B667A97B-8187-E911-AD27-00266CF94E34.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/C0CC7D97-9A87-E911-B01E-0CC47A7FC72C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/129EEC42-7088-E911-855A-3417EBE743C0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/806F40AE-9A87-E911-A4BD-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/C84BD5AE-9A87-E911-8E62-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/76EFD0EF-9887-E911-97F5-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/2C3B1CF5-9687-E911-B806-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/EC59229A-A887-E911-981E-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/207B38A4-2D88-E911-BD61-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/7E27DC5B-4088-E911-A123-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/CE2C0E84-4088-E911-820A-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/AAADEA70-098A-E911-A79E-002590FD5A78.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/50A97C6A-098A-E911-A3AC-0CC47AC17506.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/86CDFA15-128A-E911-B6F3-003048CBA444.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/246C7310-E98A-E911-B739-AC1F6BB17832.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/122DAD96-6388-E911-91ED-0026B9F8CB68.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/9A3607A1-5587-E911-854D-0CC47AF9739E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/5E95B4EF-6887-E911-8ED9-D48564447752.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/EE6B8201-6987-E911-93C9-00215A49197E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/22F2E422-7B87-E911-B08C-3C4A92F7BDB6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/1C114C25-7B87-E911-AEB9-8CDCD4A99E60.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/62A30E96-8887-E911-BD58-0CC47AF9739E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/34203198-8887-E911-A9DD-509A4C9EF8FF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/7E313970-8E87-E911-B7DA-AC162DA6E2F8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/4C24376F-9487-E911-97C7-002264069120.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/C6D7B7B0-9A87-E911-8EDD-441EA161CCEC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/9C611758-A787-E911-B3B0-509A4C9EF8FF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/4210A6AD-8188-E911-82F5-24BE05BDCEF1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/0A1E9DA9-8188-E911-9CF9-24BE05C6E7E1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/54720BA0-8888-E911-8E3F-B8CA3A709028.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/24BA7285-8888-E911-BDC1-24BE05C4D821.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/10A784AD-8988-E911-9D82-506B4BB16ADE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/44863D05-9388-E911-8E08-24BE05CE2EC1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/7219CE88-1289-E911-B83C-E0071B74AC30.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/5E12FACD-7E8A-E911-BECC-A0369FD0B196.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/C8426E3C-8A89-E911-9C39-001E673973C8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/AA47A67C-398A-E911-847B-A4BF0112BDCA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/14CFED3D-AB87-E911-BA2A-0CC47AFCC646.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/8AC973C7-2588-E911-A166-0CC47AFCC386.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/D0817306-5288-E911-B768-0CC47AFF0138.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/42B2453A-D688-E911-91DC-0CC47AFF02F8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/F4607F7E-548B-E911-B144-0242AC1C0500.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/B67EC255-328B-E911-831E-001E67E6F8F0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/EE6DE6B0-2588-E911-86FA-0090FAA578E0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/BE50BDEA-3988-E911-BD7D-48FD8E2824AD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/4263737C-5589-E911-9765-AC1F6B0DE4AE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/941CBCF8-7188-E911-91A3-00259073E42C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/8E01CF3C-9F89-E911-9432-002590E7E02E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/84DA0E7B-5D88-E911-8A27-FA163E0F2AD4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/508EBCFA-8689-E911-8009-FA163EBA2296.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/B2BB6D92-4188-E911-B1D2-A0369FC520EC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/2AA178E0-7188-E911-BFDD-20040FEABE68.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/6860FC3E-7488-E911-B2A5-842B2B1814E1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/32E1F734-5188-E911-8FC1-0242AC1C0502.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/CC7159B9-2689-E911-B7F6-0242AC1C0502.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/32C26788-668D-E911-9E69-FA163EF4DE66.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/28DA8E39-F487-E911-9AFB-001E67DDC2CC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/D45F70AC-D188-E911-9F4F-001E67A3FE66.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/3C01D8A9-4088-E911-9148-AC1F6B1AF002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/B446CF1B-5188-E911-B835-AC1F6B1AF194.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/3CD1FD27-5988-E911-954B-00266CFFCC54.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/545E93F2-7188-E911-9101-C4346BC84780.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/966D81EF-D88A-E911-9AFA-90E2BAC9B7A8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/204BFD19-A687-E911-9BAA-AC1F6BAC7C2A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/F2E3A654-7488-E911-8652-AC1F6BAC7EB0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/5C55B414-7B88-E911-82B2-0CC47A7C3458.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/BC43B31C-7B88-E911-AE30-AC1F6BAC7F24.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/A891DB28-7B88-E911-BC3D-0025905A611C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/FA15C428-7B88-E911-8905-0025905A60B0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/F893F5D3-8188-E911-B708-0CC47A74524E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/6A5A61E9-8188-E911-AE24-0025905B85B8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/E08E3DEF-8188-E911-A69C-0025905B8610.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/BE475E17-8988-E911-AA81-0025905A60A6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/C64CF80B-8988-E911-A372-AC1F6BAC8038.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/34A9BDD5-2E89-E911-A57F-AC1F6BAC7F24.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/68CB4BE2-8F87-E911-B63B-0CC47A5FBE21.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/DCC07DD1-2689-E911-8411-44A84225C4EB.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/66252574-A388-E911-8557-0CC47AD98B8E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/26CA4E2F-208B-E911-80CE-0025905C975C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/D87F2DDD-0688-E911-A824-008CFAC93CE4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/4E440177-0988-E911-B8C2-008CFAC941E4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/0201317C-0988-E911-A93A-8000002AFE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/C04484A4-D188-E911-BDA8-8000002AFE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/F08B5B8C-4188-E911-A4F0-C454449229EB.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/74F4F5EB-718A-E911-9EF4-B026283D96E0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/56450308-B88D-E911-8218-0242AC1C0504.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/AE105BDE-C38F-E911-8212-00259029ED22.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/5825DB32-BA8D-E911-9DF2-00259022516E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/E0D620AA-CC8E-E911-BE56-B499BAAC0A22.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/6AFE22CB-AD8D-E911-BE18-00259090836A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/9E06A46A-6B91-E911-8938-FA163EF898EA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/9615BFDB-CC8D-E911-9D16-28924A33B9AA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/1622496D-1D90-E911-80F7-C4346BC0F3E0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/24FC9BBE-7E8E-E911-A35D-002590D60028.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/2E7BFCAE-968D-E911-9E2A-0CC47AF9B13A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/98C71499-6B91-E911-A341-AC1F6B0DE348.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/10F60B70-D28D-E911-AA59-842B2B758AD8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/BCB390EC-C18D-E911-BEDB-008CFAE45320.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/DC9A6800-5B8E-E911-8C23-549F358EB748.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/76D20699-C291-E911-A1FE-14DDA9243247.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/30000/8253B65E-9C8D-E911-A93B-00238BAA1C4C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/260000/38954E63-70A7-E911-9879-3CFDFE6A2E60.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/260000/BCE45B43-69A7-E911-A227-FA163E61B118.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/260000/F4D01B6C-33A8-E911-B3E5-FA163E9D380D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/130000/8033A01E-67A4-E911-94D2-509A4C85402C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/260000/A0335352-34A8-E911-B006-48FD8E282979.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/260000/920A9EE3-5BA9-E911-80F3-001E67E713B3.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/260000/6C249400-4CA8-E911-9F6C-0CC47AA478BE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/260000/164F82EA-35A8-E911-B2EC-0CC47A6C1866.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/260000/C88D3F74-35A8-E911-BCD9-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-50_mLSP-400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_pilot_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/260000/F07FC17A-84A7-E911-9A14-B8CA3A70BAC8.root',
] )











