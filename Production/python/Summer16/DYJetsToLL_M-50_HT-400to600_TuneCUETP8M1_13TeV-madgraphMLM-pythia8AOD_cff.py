import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7A72881C-DDD0-E611-A36F-ECF4BBE1BE70.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CABFFDD3-E0D0-E611-AA6C-0CC47A546E5E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3045ADF1-E6D0-E611-8BF4-001E67456F68.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/EAF27BC3-DED0-E611-AB2C-ECF4BBE16468.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0C2B0C4B-E0D0-E611-BDE3-001E674DA347.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0642BEB1-E3D0-E611-96DF-001E674FCAE9.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/385BEB7B-E2D0-E611-B5C8-001E67586A2F.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/60429277-3BD0-E611-A39C-001E6745764D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/74CECAAE-3FD0-E611-932A-ECF4BBE1C820.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/EA0CF568-38D0-E611-985E-001E67348055.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/40EA45BC-38D0-E611-A4B1-001E67456EBE.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/806067C5-11D0-E611-806E-0CC47A546E5E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/0483F875-15D0-E611-BEA3-001E67444EAC.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/E84AE5A8-17D0-E611-A8D0-001E674DA1AD.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/9E987A84-1BD0-E611-8BEA-0CC47A546E5E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/8AE781E1-17D0-E611-A069-ECF4BBE1C820.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/56FF7478-13D0-E611-B0BA-001E67444EAC.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/C41B13E5-19D0-E611-9213-001E674FB24D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/42BE3B0D-1CD0-E611-A328-001E674FB2D4.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/20CB1376-22D0-E611-817F-0CC47A537688.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/AA4AFCEF-24D0-E611-AAD4-0CC47A546E5E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/526149D6-23D0-E611-9381-0CC47A546E5E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/4C2862D4-1ED0-E611-85BE-001E674440E2.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/D4D07C4B-16D0-E611-AE15-001E673476AA.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/DE95E75A-18D0-E611-A037-001E67348055.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/32F09DA6-21D0-E611-B3E0-001E67456EBE.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/08DBC8A1-2BD0-E611-AA14-ECF4BBE16610.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/187A9925-28D0-E611-BE4C-001E67457A5D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/2E68C0DC-2CD0-E611-A31B-ECF4BBE16390.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/F88BCF10-29D0-E611-B9CB-001E67397DF5.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/A0DFEB31-27D0-E611-BC94-001E67346BA1.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/A670CB45-2ED0-E611-906E-001E674FB24D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/D8F8AF12-31D0-E611-B01B-001E674FB2D4.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/148B132F-2ED0-E611-9299-001E67348055.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/6EF6680D-30D0-E611-A29C-0CC47A546E5E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/F8B9F9C1-33D0-E611-B453-ECF4BBE16390.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/36D5C044-36D0-E611-B51E-001E674FBA1D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5436D12E-F5CE-E611-8628-001E674FB207.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1E3273E1-F8CE-E611-BB88-D067E5F91B8A.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/56B0E404-F9CE-E611-9739-D067E5F92064.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/00C91B98-7ACF-E611-B331-001E67346BA1.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/700AC971-EDCE-E611-950A-0242AC130006.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A699C0D4-EBCE-E611-9E79-0242AC130005.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C2C71B0C-F1CE-E611-B2B2-0242AC130005.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D237A483-F3CE-E611-913B-0242AC130002.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/78FDE97C-F3CE-E611-9DD7-0242AC130005.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F03B75AE-F3CE-E611-B428-0242AC130002.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F4B5524A-F2CE-E611-B425-D067E5F9145E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A628C969-F6CE-E611-ABF4-D067E5F91CCE.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E4A8F352-F2CE-E611-8E93-D067E5F91F71.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A2625B07-FACE-E611-A0BA-0242AC130005.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2EB8CE3D-ECCE-E611-8756-D067E5F910F5.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B4394868-F0CE-E611-A07D-001E674FBFC2.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3E69A594-EECE-E611-8FAC-001E67457A5D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/026E2D2E-F5CE-E611-A5CD-0CC47A537688.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4637BC63-FBCE-E611-A767-0242AC130002.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/745E7973-F2CE-E611-91A3-001E674FB063.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/627A1253-F2CE-E611-98C4-001E67457E7C.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/00FCD869-F0CE-E611-B764-001E674FB207.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1224650B-F7CE-E611-A348-D067E5FB77E0.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A0063309-F7CE-E611-8925-D067E5F90FDE.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AA25B063-F1CE-E611-B5F1-001E674FAF23.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AC994018-F5CE-E611-9F60-001E674FB063.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C2BAFE09-FACE-E611-9192-0CC47A546E5E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B2370F19-F5CE-E611-92AD-001E674440E2.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/42EF608F-FECE-E611-92CB-001E674DA1AD.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A26A86C5-F9CE-E611-919F-001E6745764D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/66CE80E9-F9CE-E611-A577-001E674FCAE9.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4C1DC4F5-F7CE-E611-B757-D067E5F921CC.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FE0E04F4-F7CE-E611-AB4F-001E674DA83D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6CB8E712-6ED0-E611-B952-001E67457107.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/26165FDC-6AD0-E611-B642-001E674FB24D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/60C5F78C-6FD0-E611-AEE2-001E67348055.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/68E47912-6ED0-E611-8FC9-001E674FCAE9.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7A07E74B-6FD0-E611-89B2-001E67457A5D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C430AB94-71D0-E611-A041-001E674FCAE9.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/96D17D50-70D0-E611-A79B-001E67348055.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DE2BF8FB-70D0-E611-A0A5-001E67586A2F.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/388E8C9B-71D0-E611-BB89-001E674FC800.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CC333E13-73D0-E611-A134-001E67397DF5.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A6463214-73D0-E611-80A6-001E674FAF23.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/926C5C3C-6ED0-E611-8271-001E673475A6.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0ABD2044-7AD0-E611-BB00-0CC47A537688.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C28ADA37-74D0-E611-B0BE-001E67348055.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1E25A5A1-71D0-E611-AA7E-001E674FC800.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/54A4C195-6FD0-E611-AC3D-001E673475A6.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/788966F5-75D0-E611-8D74-0CC47A546E5E.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/062A8F3F-7AD0-E611-801F-0CC47A546E5E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/82B730FD-75D0-E611-8BE5-001E674FBFC2.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/102E842F-6ED0-E611-8D22-001E67457A5D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/84162643-7AD0-E611-BB49-001E674FC800.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E459B67A-78D0-E611-8161-001E67456F68.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/60A6BCAD-71D0-E611-82E0-001E67456F68.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/744BFBD8-85D0-E611-BE54-D067E5F91B81.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/804F7442-7AD0-E611-B696-001E674FBA1D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/467C3804-7AD0-E611-85C2-D067E5F914D3.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2630C97C-7DD0-E611-B574-D067E5F917B5.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/04DC2D55-7AD0-E611-83D0-001E67457A5D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BE5EBDD4-74D0-E611-9113-001E67457E36.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0271A45A-7AD0-E611-9396-001E67346BA1.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/760BC962-6CD0-E611-989B-001E674FB24D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3CB66A51-7AD0-E611-B673-001E673475A6.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DA2E3750-7AD0-E611-A2F5-001E67444EAC.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7C4AF957-7AD0-E611-9011-001E674FB24D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/64BEBDC6-86D0-E611-B7DB-D067E5F914D3.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F2C7ECD5-83D0-E611-9DFC-0CC47A546E5E.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C8CDC3EA-7FD0-E611-B0E6-001E67456EBE.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/74CA8C55-8AD0-E611-80BC-D067E5F917B5.root',
] )




































